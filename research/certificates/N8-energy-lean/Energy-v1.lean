import Mathlib.Topology.Order.Compact
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Topology.Instances.ENNReal.Lemmas
import Mathlib.Tactic
import Lean.Util.CollectAxioms

/- A concrete half-transfer maximum principle. No reachable-sequence or
   contraction hypothesis is assumed. The positional/Lie bridge is separate. -/
namespace N8Energy
open scoped BigOperators

variable {I : Type*} [Fintype I] [DecidableEq I]

def energy (y : I → ℝ) : ℝ := ∑ i, (y i)^2
def l1 (y : I → ℝ) : ℝ := ∑ i, |y i|

noncomputable def half (i j : I) (y : I → ℝ) : I → ℝ :=
  Function.update (Function.update y i (y i / 2)) j (y j + y i / 2)

theorem sum_transform_update (g : ℝ → ℝ) (y : I → ℝ) (i : I) (a : ℝ) :
    (∑ k, g (Function.update y i a k)) = (∑ k, g (y k)) - g (y i) + g a := by
  have hm : (fun k => g (Function.update y i a k)) =
      Function.update (fun k => g (y k)) i (g a) := by
    funext k
    by_cases hk : k = i <;> simp [hk]
  rw [hm, Finset.sum_update_of_mem (Finset.mem_univ i)]
  have h := Finset.sum_eq_add_sum_diff_singleton (Finset.mem_univ i) (fun k => g (y k))
  linarith

theorem half_sum (i j : I) (hij : i ≠ j) (y : I → ℝ) :
    (∑ k, half i j y k) = ∑ k, y k := by
  unfold half
  rw [sum_transform_update (fun x => x), sum_transform_update (fun x => x)]
  simp only [Function.update_of_ne hij.symm]
  ring

theorem half_energy (i j : I) (hij : i ≠ j) (y : I → ℝ) :
    energy (half i j y) = energy y - (y i)^2/2 + y i*y j := by
  unfold energy half
  rw [sum_transform_update (fun x => x^2), sum_transform_update (fun x => x^2)]
  simp only [Function.update_of_ne hij.symm]
  ring

theorem half_l1 (i j : I) (hij : i ≠ j) (y : I → ℝ) :
    l1 (half i j y) ≤ l1 y := by
  unfold l1 half
  rw [sum_transform_update abs, sum_transform_update abs]
  simp only [Function.update_of_ne hij.symm]
  have h := abs_add_le (y j) (y i / 2)
  have hd : |y i / 2| = |y i| / 2 := by norm_num [abs_div]
  rw [hd] at h ⊢
  linarith

theorem energy_minimum_forces_zero (sigma : I → I)
    (hneq : ∀ i, i ≠ sigma i)
    (hcycle : ∀ i j, ∃ n : ℕ, sigma^[n] i = j)
    (y : I → ℝ) (hsum : (∑ i, y i) = 0)
    (hmin : ∀ i, energy y ≤ energy (half i (sigma i) y)) : y = 0 := by
  by_contra hy
  have hp : ∃ i, 0 < y i := by
    by_contra hn
    push_neg at hn
    have hz := (Finset.sum_eq_zero_iff_of_nonpos
      (fun i (_ : i ∈ Finset.univ) => hn i)).mp hsum
    exact hy (funext (fun i => hz i (Finset.mem_univ i)))
  obtain ⟨i, hi⟩ := hp
  have propagate (j : I) (hj : 0 < y j) : 0 < y (sigma j) := by
    have h := hmin j
    rw [half_energy j (sigma j) (hneq j)] at h
    by_contra hn
    have hn' : y (sigma j) ≤ 0 := le_of_not_gt hn
    have hm : y j * y (sigma j) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hj.le hn'
    nlinarith [sq_pos_of_pos hj]
  have iterate_pos (n : ℕ) : 0 < y (sigma^[n] i) := by
    induction n with
    | zero => simpa using hi
    | succ n ih => simpa only [Function.iterate_succ_apply'] using propagate _ ih
  have allpos (j : I) : 0 < y j := by
    obtain ⟨n, hn⟩ := hcycle i j
    rw [← hn]
    exact iterate_pos n
  have hs : 0 < ∑ j, y j := Finset.sum_pos'
    (fun j _ => (allpos j).le) ⟨i, Finset.mem_univ i, hi⟩
  linarith

theorem compact_harmonic_le_zero (S : Set (I → ℝ)) (hc : IsCompact S)
    (hzero : (0 : I → ℝ) ∈ S) (hsum : ∀ y ∈ S, (∑ i, y i) = 0)
    (sigma : I → I) (hneq : ∀ i, i ≠ sigma i)
    (hcycle : ∀ i j, ∃ n : ℕ, sigma^[n] i = j)
    (B : I → (I → ℝ) → (I → ℝ))
    (ha : ∀ i y, y ∈ S → half i (sigma i) y ∈ S)
    (hb : ∀ i y, y ∈ S → B i y ∈ S)
    (f : (I → ℝ) → ℝ) (hf : Continuous f)
    (hmean : ∀ i y, y ∈ S → 2*f y = f (half i (sigma i) y) + f (B i y)) :
    ∀ z ∈ S, f z ≤ f 0 := by
  obtain ⟨x, hx, hmax⟩ := hc.exists_isMaxOn ⟨0, hzero⟩ hf.continuousOn
  let K : Set (I → ℝ) := {y | y ∈ S ∧ f y = f x}
  have hk : IsCompact K := hc.inter_right (isClosed_eq hf continuous_const)
  have he : Continuous (energy : (I → ℝ) → ℝ) := by unfold energy; fun_prop
  obtain ⟨y, hy, hmin⟩ := hk.exists_isMinOn ⟨x, hx, rfl⟩ he.continuousOn
  have hstay (i : I) : half i (sigma i) y ∈ K := by
    have ha' := ha i y hy.1
    have hb' := hb i y hy.1
    have hma := hmax ha'
    have hmb := hmax hb'
    have hm := hmean i y hy.1
    exact ⟨ha', by linarith [hy.2]⟩
  have hey : y = 0 := energy_minimum_forces_zero sigma hneq hcycle y
    (hsum y hy.1) (fun i => hmin (hstay i))
  have hv : f x = f 0 := by simpa only [hey] using hy.2.symm
  intro z hz
  simpa only [hv] using hmax hz

theorem compact_harmonic_constant (S : Set (I → ℝ)) (hc : IsCompact S)
    (hzero : (0 : I → ℝ) ∈ S) (hsum : ∀ y ∈ S, (∑ i, y i) = 0)
    (sigma : I → I) (hneq : ∀ i, i ≠ sigma i)
    (hcycle : ∀ i j, ∃ n : ℕ, sigma^[n] i = j)
    (B : I → (I → ℝ) → (I → ℝ))
    (ha : ∀ i y, y ∈ S → half i (sigma i) y ∈ S)
    (hb : ∀ i y, y ∈ S → B i y ∈ S)
    (f : (I → ℝ) → ℝ) (hf : Continuous f)
    (hmean : ∀ i y, y ∈ S → 2*f y = f (half i (sigma i) y) + f (B i y)) :
    ∀ z ∈ S, f z = f 0 := by
  have hu := compact_harmonic_le_zero S hc hzero hsum sigma hneq hcycle B ha hb f hf hmean
  have hnmean : ∀ i y, y ∈ S →
      2*(-f y) = (-f (half i (sigma i) y)) + (-f (B i y)) := by
    intro i y hy
    linarith [hmean i y hy]
  have hl := compact_harmonic_le_zero S hc hzero hsum sigma hneq hcycle B ha hb
    (fun y => -f y) hf.neg hnmean
  intro z hz
  linarith [hu z hz, hl z hz]

def zeroBall (R : ℝ) : Set (I → ℝ) := {y | (∑ i, y i) = 0 ∧ l1 y ≤ R}

theorem compact_zeroBall (R : ℝ) : IsCompact (zeroBall (I := I) R) := by
  have hs : Continuous (fun y : I → ℝ => ∑ i, y i) := by fun_prop
  have hn : Continuous (l1 : (I → ℝ) → ℝ) := by unfold l1; fun_prop
  have hc : IsClosed (zeroBall (I := I) R) :=
    (isClosed_eq hs continuous_const).inter (isClosed_le hn continuous_const)
  apply (isCompact_Icc : IsCompact (Set.Icc (fun _ : I => -R) (fun _ => R))).of_isClosed_subset hc
  intro y hy
  have hb (i : I) : |y i| ≤ R := by
    exact (Finset.single_le_sum (fun j _ => abs_nonneg (y j)) (Finset.mem_univ i)).trans hy.2
  exact ⟨fun i => (abs_le.mp (hb i)).1, fun i => (abs_le.mp (hb i)).2⟩

theorem half_mem_zeroBall (R : ℝ) (i j : I) (hij : i ≠ j)
    {y : I → ℝ} (hy : y ∈ zeroBall R) : half i j y ∈ zeroBall R := by
  exact ⟨by rw [half_sum i j hij, hy.1], (half_l1 i j hij y).trans hy.2⟩

theorem hyperplane_harmonic_constant (sigma tau : I → I)
    (hsigma : ∀ i, i ≠ sigma i) (htau : ∀ i, i ≠ tau i)
    (hcycle : ∀ i j, ∃ n : ℕ, sigma^[n] i = j)
    (f : (I → ℝ) → ℝ) (hf : Continuous f)
    (hmean : ∀ i y, (∑ j, y j) = 0 →
      2*f y = f (half i (sigma i) y) + f (half i (tau i) y)) :
    ∀ y, (∑ i, y i) = 0 → f y = f 0 := by
  intro y hy
  have hn : 0 ≤ l1 y := Finset.sum_nonneg (fun i _ => abs_nonneg (y i))
  have hz : (0 : I → ℝ) ∈ zeroBall (l1 y) := by simp [zeroBall, l1]; exact hn
  exact compact_harmonic_constant (zeroBall (l1 y)) (compact_zeroBall (l1 y))
    hz (fun _ h => h.1) sigma hsigma hcycle (fun i => half i (tau i))
    (fun i _ h => half_mem_zeroBall _ i _ (hsigma i) h)
    (fun i _ h => half_mem_zeroBall _ i _ (htau i) h)
    f hf (fun i _ h => hmean i _ h.1) y ⟨hy, le_rfl⟩

end N8Energy

#print axioms N8Energy.hyperplane_harmonic_constant

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Energy.sum_transform_update,
      ``N8Energy.half_sum, ``N8Energy.half_energy, ``N8Energy.half_l1,
      ``N8Energy.energy_minimum_forces_zero, ``N8Energy.compact_harmonic_le_zero,
      ``N8Energy.compact_harmonic_constant, ``N8Energy.compact_zeroBall,
      ``N8Energy.half_mem_zeroBall, ``N8Energy.hyperplane_harmonic_constant] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 concrete half-transfer energy maximum principle"
