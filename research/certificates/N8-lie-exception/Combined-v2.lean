import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.Tuple.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Lean.Util.CollectAxioms
import Mathlib.Topology.Order.Compact
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Topology.Instances.ENNReal.Lemmas
import Mathlib.Logic.Equiv.Fin.Rotate
import Mathlib.Algebra.MvPolynomial.Funext
import Mathlib.Topology.Algebra.MvPolynomial
import Mathlib.Algebra.FreeAlgebra
import Mathlib.LinearAlgebra.Finsupp.LSum
import Mathlib.Data.List.OfFn
import Mathlib.Data.Finsupp.Fin
import Mathlib.Algebra.MvPolynomial.Rename
import Mathlib.Algebra.Lie.Subalgebra
import Mathlib.Algebra.Lie.OfAssociative
import Mathlib.Algebra.Polynomial.Coeff


/- Universal finite-tuple bridge only. The positional encoding of free Lie
   elements and the full N8 algorithm are not formalized here. -/
namespace N8Bridge

open scoped BigOperators

def DeltaEquation {m : ℕ} (P : (Fin m → ℝ) → ℝ)
    (V : (Fin (m + 1) → ℝ) → ℝ) : Prop :=
  ∀ w, (∑ i, w i) * V w = P (Fin.tail w) - P (Fin.init w)

def DiagonalZero {m : ℕ} (V : (Fin (m + 1) → ℝ) → ℝ) : Prop :=
  ∀ w : Fin (m + 2) → ℝ, (∑ i, w i) = 0 →
    w 0 = w (Fin.last (m + 1)) → V (Fin.tail w) = V (Fin.init w)

theorem cyclic_boundary {m : ℕ} (P : (Fin m → ℝ) → ℝ)
    (V : (Fin (m + 1) → ℝ) → ℝ) (hdelta : DeltaEquation P V)
    (w : Fin (m + 1) → ℝ) (hzero : (∑ i, w i) = 0) :
    P (Fin.tail w) = P (Fin.init w) := by
  have h := hdelta w
  rw [hzero, zero_mul] at h
  linarith

theorem tail_snoc {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    Fin.tail (α := fun _ : Fin (n + 2) => ℝ) (Fin.snoc z a) =
      Fin.snoc (Fin.tail z) a := by
  have h := congrArg (Fin.tail (α := fun _ : Fin (n + 2) => ℝ))
    (Fin.cons_snoc_eq_snoc_cons (z 0) (Fin.tail z) a)
  simpa only [Fin.tail_cons, Fin.cons_self_tail] using h.symm

theorem init_cons {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    Fin.init (α := fun _ : Fin (n + 2) => ℝ) (Fin.cons a z) =
      Fin.cons a (Fin.init z) := by
  have h := congrArg (Fin.init (α := fun _ : Fin (n + 2) => ℝ))
    (Fin.cons_snoc_eq_snoc_cons a (Fin.init z) (z (Fin.last n)))
  simpa only [Fin.init_snoc, Fin.snoc_init_self] using h

theorem diagonal_midpoint {m : ℕ} (V : (Fin (m + 1) → ℝ) → ℝ)
    (hdiag : DiagonalZero V) (z : Fin m → ℝ) (a : ℝ)
    (ha : 2 * a + ∑ i, z i = 0) :
    V (Fin.snoc z a) = V (Fin.cons a z) := by
  have hz : (∑ i, (Fin.cons a (Fin.snoc z a)) i) = 0 := by
    rw [Fin.sum_cons, Fin.sum_snoc]
    linarith
  have hend : (Fin.cons (α := fun _ : Fin (m + 2) => ℝ) a (Fin.snoc z a)) 0 =
      (Fin.cons (α := fun _ : Fin (m + 2) => ℝ) a (Fin.snoc z a))
        (Fin.last (m + 1)) := by simp
  have h := hdiag (Fin.cons a (Fin.snoc z a)) hz hend
  rw [Fin.tail_cons, Fin.cons_snoc_eq_snoc_cons, Fin.init_snoc] at h
  exact h

theorem boundary_average {n : ℕ} (P : (Fin (n + 1) → ℝ) → ℝ)
    (V : (Fin (n + 2) → ℝ) → ℝ)
    (hdelta : DeltaEquation P V) (hdiag : DiagonalZero V)
    (z : Fin (n + 1) → ℝ) (a : ℝ) (ha : 2 * a + ∑ i, z i = 0) :
    2 * P z = P (Fin.snoc (Fin.tail z) a) + P (Fin.cons a (Fin.init z)) := by
  have hv := diagonal_midpoint V hdiag z a ha
  have hr := hdelta (Fin.snoc z a)
  have hl := hdelta (Fin.cons a z)
  simp only [Fin.sum_snoc, Fin.init_snoc, tail_snoc] at hr
  simp only [Fin.sum_cons, Fin.tail_cons, init_cons] at hl
  rw [← hv] at hl
  nlinarith

def shiftFirst {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) : Fin (n + 1) → ℝ :=
  Fin.cons (z 0 + a) (Fin.tail z)

def shiftLast {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) : Fin (n + 1) → ℝ :=
  Fin.snoc (Fin.init z) (z (Fin.last n) + a)

theorem sum_shiftFirst {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    (∑ i, shiftFirst z a i) = (∑ i, z i) + a := by
  simp only [shiftFirst, Fin.sum_cons]
  rw [Fin.sum_univ_succ]
  simp only [Fin.tail]
  ring

theorem sum_shiftLast {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    (∑ i, shiftLast z a i) = (∑ i, z i) + a := by
  simp only [shiftLast, Fin.sum_snoc]
  rw [Fin.sum_univ_castSucc]
  simp only [Fin.init]
  ring

theorem transfer_average {n : ℕ} (P : (Fin (n + 1) → ℝ) → ℝ)
    (V : (Fin (n + 2) → ℝ) → ℝ)
    (hdelta : DeltaEquation P V) (hdiag : DiagonalZero V)
    (z : Fin (n + 1) → ℝ) (a : ℝ) (ha : 2 * a + ∑ i, z i = 0) :
    2 * P z = P (shiftFirst z a) + P (shiftLast z a) := by
  have hrzero : (∑ i, (Fin.snoc (shiftFirst z a) a) i) = 0 := by
    rw [Fin.sum_snoc, sum_shiftFirst]
    linarith
  have hlzero : (∑ i, (Fin.cons a (shiftLast z a)) i) = 0 := by
    rw [Fin.sum_cons, sum_shiftLast]
    linarith
  have hr := cyclic_boundary P V hdelta (Fin.snoc (shiftFirst z a) a) hrzero
  have hl := cyclic_boundary P V hdelta (Fin.cons a (shiftLast z a)) hlzero
  simp only [Fin.init_snoc, tail_snoc, shiftFirst, Fin.tail_cons] at hr
  simp only [Fin.tail_cons, init_cons, shiftLast, Fin.init_snoc] at hl
  change P (Fin.snoc (Fin.tail z) a) = P (shiftFirst z a) at hr
  change P (shiftLast z a) = P (Fin.cons a (Fin.init z)) at hl
  rw [← hr, hl]
  exact boundary_average P V hdelta hdiag z a ha

theorem transfer_average_half {n : ℕ} (P : (Fin (n + 1) → ℝ) → ℝ)
    (V : (Fin (n + 2) → ℝ) → ℝ)
    (hdelta : DeltaEquation P V) (hdiag : DiagonalZero V)
    (z : Fin (n + 1) → ℝ) :
    2 * P z = P (shiftFirst z (-(∑ i, z i) / 2)) +
      P (shiftLast z (-(∑ i, z i) / 2)) := by
  apply transfer_average P V hdelta hdiag
  ring

def rotate {m : ℕ} (w : Fin (m + 1) → ℝ) : Fin (m + 1) → ℝ :=
  Fin.snoc (Fin.tail w) (w 0)

theorem sum_rotate {m : ℕ} (w : Fin (m + 1) → ℝ) :
    (∑ i, rotate w i) = ∑ i, w i := by
  simp only [rotate, Fin.sum_snoc]
  rw [Fin.sum_univ_succ]
  simp only [Fin.tail]
  ring

theorem cyclic_invariance {m : ℕ} (P : (Fin m → ℝ) → ℝ)
    (V : (Fin (m + 1) → ℝ) → ℝ) (hdelta : DeltaEquation P V)
    (w : Fin (m + 1) → ℝ) (hzero : (∑ i, w i) = 0) :
    P (Fin.tail (rotate w)) = P (Fin.tail w) := by
  have hrzero : (∑ i, rotate w i) = 0 := by rw [sum_rotate, hzero]
  have h := cyclic_boundary P V hdelta (rotate w) hrzero
  simpa only [rotate, Fin.init_snoc] using h

noncomputable def clockwise {n : ℕ} (w : Fin (n + 2) → ℝ) : Fin (n + 2) → ℝ :=
  Fin.cons (w 0 / 2) (shiftFirst (Fin.tail w) (w 0 / 2))

noncomputable def counterclockwise {n : ℕ} (w : Fin (n + 2) → ℝ) : Fin (n + 2) → ℝ :=
  Fin.cons (w 0 / 2) (shiftLast (Fin.tail w) (w 0 / 2))

theorem sum_clockwise {n : ℕ} (w : Fin (n + 2) → ℝ) :
    (∑ i, clockwise w i) = ∑ i, w i := by
  simp only [clockwise, Fin.sum_cons, sum_shiftFirst]
  conv_rhs => rw [Fin.sum_univ_succ]
  simp only [Fin.tail]
  ring

theorem sum_counterclockwise {n : ℕ} (w : Fin (n + 2) → ℝ) :
    (∑ i, counterclockwise w i) = ∑ i, w i := by
  simp only [counterclockwise, Fin.sum_cons, sum_shiftLast]
  conv_rhs => rw [Fin.sum_univ_succ]
  simp only [Fin.tail]
  ring

theorem origin_average {n : ℕ} (P : (Fin (n + 1) → ℝ) → ℝ)
    (V : (Fin (n + 2) → ℝ) → ℝ)
    (hdelta : DeltaEquation P V) (hdiag : DiagonalZero V)
    (w : Fin (n + 2) → ℝ) (hzero : (∑ i, w i) = 0) :
    2 * P (Fin.tail w) = P (Fin.tail (clockwise w)) +
      P (Fin.tail (counterclockwise w)) := by
  have ha : 2 * (w 0 / 2) + ∑ i, (Fin.tail w) i = 0 := by
    rw [Fin.sum_univ_succ] at hzero
    simp only [Fin.tail]
    linarith
  simpa only [clockwise, counterclockwise, Fin.tail_cons] using
    transfer_average P V hdelta hdiag (Fin.tail w) (w 0 / 2) ha

def l1 {m : ℕ} (z : Fin m → ℝ) : ℝ := ∑ i, |z i|

theorem l1_cons {m : ℕ} (a : ℝ) (z : Fin m → ℝ) :
    l1 (Fin.cons a z) = |a| + l1 z := by
  unfold l1
  rw [Fin.sum_univ_succ]
  simp only [Fin.cons_zero, Fin.cons_succ]

theorem l1_snoc {m : ℕ} (z : Fin m → ℝ) (a : ℝ) :
    l1 (Fin.snoc z a) = l1 z + |a| := by
  unfold l1
  rw [Fin.sum_univ_castSucc]
  simp only [Fin.snoc_last, Fin.snoc_castSucc]

theorem l1_shiftFirst {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    l1 (shiftFirst z a) ≤ l1 z + |a| := by
  have hz : l1 z = |z 0| + l1 (Fin.tail z) := by
    rw [← l1_cons, Fin.cons_self_tail]
  rw [shiftFirst, l1_cons, hz]
  linarith [abs_add_le (z 0) a]

theorem l1_shiftLast {n : ℕ} (z : Fin (n + 1) → ℝ) (a : ℝ) :
    l1 (shiftLast z a) ≤ l1 z + |a| := by
  have hz : l1 z = l1 (Fin.init z) + |z (Fin.last n)| := by
    rw [← l1_snoc, Fin.snoc_init_self]
  rw [shiftLast, l1_snoc, hz]
  linarith [abs_add_le (z (Fin.last n)) a]

theorem l1_clockwise {n : ℕ} (w : Fin (n + 2) → ℝ) :
    l1 (clockwise w) ≤ l1 w := by
  have hw : l1 w = |w 0| + l1 (Fin.tail w) := by
    rw [← l1_cons, Fin.cons_self_tail]
  have habs : |w 0 / 2| = |w 0| / 2 := by norm_num [abs_div]
  have hb := l1_shiftFirst (Fin.tail w) (w 0 / 2)
  rw [clockwise, l1_cons, hw, habs]
  rw [habs] at hb
  linarith

theorem l1_counterclockwise {n : ℕ} (w : Fin (n + 2) → ℝ) :
    l1 (counterclockwise w) ≤ l1 w := by
  have hw : l1 w = |w 0| + l1 (Fin.tail w) := by
    rw [← l1_cons, Fin.cons_self_tail]
  have habs : |w 0 / 2| = |w 0| / 2 := by norm_num [abs_div]
  have hb := l1_shiftLast (Fin.tail w) (w 0 / 2)
  rw [counterclockwise, l1_cons, hw, habs]
  rw [habs] at hb
  linarith

end N8Bridge

#print axioms N8Bridge.transfer_average_half

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Bridge.cyclic_boundary, ``N8Bridge.tail_snoc,
      ``N8Bridge.init_cons, ``N8Bridge.diagonal_midpoint,
      ``N8Bridge.boundary_average, ``N8Bridge.sum_shiftFirst,
      ``N8Bridge.sum_shiftLast, ``N8Bridge.transfer_average,
      ``N8Bridge.transfer_average_half, ``N8Bridge.sum_rotate,
      ``N8Bridge.cyclic_invariance, ``N8Bridge.sum_clockwise,
      ``N8Bridge.sum_counterclockwise, ``N8Bridge.origin_average,
      ``N8Bridge.l1_cons, ``N8Bridge.l1_snoc, ``N8Bridge.l1_shiftFirst,
      ``N8Bridge.l1_shiftLast, ``N8Bridge.l1_clockwise,
      ``N8Bridge.l1_counterclockwise] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 division-free positional averaging bridge"


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
    by_cases hk : k = i
    · subst k; simp
    · simp only [Function.update_of_ne hk]
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
    have hma : f (half i (sigma i) y) ≤ f x := hmax ha'
    have hmb : f (B i y) ≤ f x := hmax hb'
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

omit [DecidableEq I] in
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


/- Concatenated with the exact prior Bridge.lean and Energy.lean sources by
   the checker. This file closes their cyclic-coordinate interface. -/
namespace N8Assembly
open scoped BigOperators
open Fin.NatCast
variable {n : ℕ}

def shift (k : Fin (n+2)) (y : Fin (n+2) → ℝ) : Fin (n+2) → ℝ :=
  fun i => y (i+k)

theorem sum_shift (k : Fin (n+2)) (y : Fin (n+2) → ℝ) :
    (∑ i, shift k y i) = ∑ i, y i := Equiv.sum_comp (Equiv.addRight k) y

theorem rotate_eq_shift (y : Fin (n+2) → ℝ) : N8Bridge.rotate y = shift 1 y := by
  unfold N8Bridge.rotate
  rw [Fin.snoc_eq_cons_rotate]
  simp only [Fin.cons_self_tail, finRotate_succ_apply]
  rfl

theorem shift_add (k l : Fin (n+2)) (y : Fin (n+2) → ℝ) :
    shift (k+l) y = shift l (shift k y) := by
  funext i
  simp only [shift]
  congr 1
  abel

theorem shift_invariance (f : (Fin (n+2) → ℝ) → ℝ)
    (hrot : ∀ y, (∑ i, y i) = 0 → f (N8Bridge.rotate y) = f y)
    (k : Fin (n+2)) (y : Fin (n+2) → ℝ) (hy : (∑ i, y i) = 0) :
    f (shift k y) = f y := by
  have hn (m : ℕ) : f (shift (m : Fin (n+2)) y) = f y := by
    induction m with
    | zero =>
      congr 1
      funext i
      simp only [N8Assembly.shift, Nat.cast_zero, add_zero]
    | succ m ih =>
      rw [Nat.cast_add, Nat.cast_one, shift_add, ← rotate_eq_shift]
      rw [hrot _ (by rw [sum_shift, hy]), ih]
  simpa only [Fin.cast_val_eq_self] using hn k.val

theorem shift_half (k i j : Fin (n+2)) (y : Fin (n+2) → ℝ) :
    shift k (N8Energy.half i j y) =
      N8Energy.half (i-k) (j-k) (shift k y) := by
  change (Function.update (Function.update y i (y i/2)) j (y j+y i/2)) ∘
    (Equiv.addRight k) = _
  rw [Function.update_comp_equiv, Function.update_comp_equiv]
  simp only [Equiv.addRight_symm_apply, ← sub_eq_add_neg]
  change Function.update (Function.update (shift k y) (i-k) (y i/2))
    (j-k) (y j+y i/2) = _
  simp only [N8Energy.half, shift, sub_add_cancel]

theorem one_ne_zero : (1 : Fin (n+2)) ≠ 0 := by
  intro h
  have hv := congrArg Fin.val h
  norm_num [Fin.val_one, Nat.mod_eq_of_lt (show 1 < n+2 by omega)] at hv

theorem successor_ne (i : Fin (n+2)) : i ≠ i+1 := by
  intro h
  have hz : (1 : Fin (n+2)) = 0 := add_left_cancel (h.symm.trans (add_zero i).symm)
  exact one_ne_zero hz

theorem predecessor_ne (i : Fin (n+2)) : i ≠ i-1 := by
  intro h
  have hz : (1 : Fin (n+2)) = 0 := (sub_eq_self.mp h.symm)
  exact one_ne_zero hz

theorem successor_cycle (i j : Fin (n+2)) :
    ∃ k : ℕ, (fun x : Fin (n+2) => x+1)^[k] i = j := by
  refine ⟨(j-i).val, ?_⟩
  rw [add_right_iterate_apply]
  rw [nsmul_one, Fin.cast_val_eq_self]
  abel

theorem last_eq_neg_one : (Fin.last (n+1) : Fin (n+2)) = -1 :=
  eq_neg_of_add_eq_zero_left (Fin.last_add_one (n+1))

theorem clockwise_eq_half (y : Fin (n+2) → ℝ) :
    N8Bridge.clockwise y = N8Energy.half 0 1 y := by
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · simp [N8Bridge.clockwise, N8Energy.half, one_ne_zero.symm]
  · refine Fin.cases ?_ (fun k => ?_) j
    · simp [N8Bridge.clockwise, N8Bridge.shiftFirst, N8Energy.half, Fin.tail]
    · have h0 : k.succ.succ ≠ (0 : Fin (n+2)) := Fin.succ_ne_zero _
      have h1 : k.succ.succ ≠ (1 : Fin (n+2)) := by
        intro h
        have hv := congrArg Fin.val h
        simp only [Fin.val_succ, Fin.val_one] at hv
        omega
      simp [N8Bridge.clockwise, N8Bridge.shiftFirst, N8Energy.half,
        Function.update_of_ne h1, Fin.tail]

theorem counterclockwise_eq_half (y : Fin (n+2) → ℝ) :
    N8Bridge.counterclockwise y = N8Energy.half 0 (-1) y := by
  rw [← last_eq_neg_one]
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · have hlast : (0 : Fin (n+2)) ≠ Fin.last (n+1) := by
      intro h; have := congrArg Fin.val h; simp at this
    simp [N8Bridge.counterclockwise, N8Energy.half, hlast]
  · refine Fin.lastCases ?_ (fun k => ?_) j
    · simp [N8Bridge.counterclockwise, N8Bridge.shiftLast, N8Energy.half, Fin.tail]
    · have h0 : k.castSucc.succ ≠ (0 : Fin (n+2)) := Fin.succ_ne_zero _
      have hl : k.castSucc.succ ≠ (Fin.last (n+1) : Fin (n+2)) := by
        intro h; have hv := congrArg Fin.val h
        change k.val+1 = n+1 at hv
        omega
      simp [N8Bridge.counterclockwise, N8Bridge.shiftLast, N8Energy.half,
        Fin.tail, Fin.init]

theorem all_index_average (f : (Fin (n+2) → ℝ) → ℝ)
    (hrot : ∀ y, (∑ i, y i) = 0 → f (N8Bridge.rotate y) = f y)
    (hmean0 : ∀ y, (∑ i, y i) = 0 →
      2*f y = f (N8Energy.half 0 1 y) + f (N8Energy.half 0 (-1) y))
    (i : Fin (n+2)) (y : Fin (n+2) → ℝ) (hy : (∑ j, y j) = 0) :
    2*f y = f (N8Energy.half i (i+1) y) + f (N8Energy.half i (i-1) y) := by
  have hs := hmean0 (shift i y) (by rw [sum_shift, hy])
  have ha : shift i (N8Energy.half i (i+1) y) = N8Energy.half 0 1 (shift i y) := by
    rw [shift_half]; simp
  have hb : shift i (N8Energy.half i (i-1) y) = N8Energy.half 0 (-1) (shift i y) := by
    rw [shift_half]
    have he : (i-1)-i = (-1 : Fin (n+2)) := by abel
    rw [sub_self, he]
  have hza : (∑ j, N8Energy.half i (i+1) y j) = 0 := by
    rw [N8Energy.half_sum i (i+1) (successor_ne i), hy]
  have hzb : (∑ j, N8Energy.half i (i-1) y j) = 0 := by
    rw [N8Energy.half_sum i (i-1) (predecessor_ne i), hy]
  rw [shift_invariance f hrot i y hy, ← ha, ← hb,
    shift_invariance f hrot i _ hza, shift_invariance f hrot i _ hzb] at hs
  exact hs

theorem positive_dimension_positional_constant (P : (Fin (n+1) → ℝ) → ℝ)
    (V : (Fin (n+2) → ℝ) → ℝ) (hP : Continuous P)
    (hdelta : N8Bridge.DeltaEquation P V) (hdiag : N8Bridge.DiagonalZero V) :
    ∀ z, P z = P 0 := by
  let f : (Fin (n+2) → ℝ) → ℝ := fun y => P (Fin.tail y)
  have hf : Continuous f := hP.comp (by fun_prop)
  have hrot : ∀ y, (∑ i, y i) = 0 → f (N8Bridge.rotate y) = f y := by
    intro y hy
    exact N8Bridge.cyclic_invariance P V hdelta y hy
  have hm0 : ∀ y, (∑ i, y i) = 0 →
      2*f y = f (N8Energy.half 0 1 y) + f (N8Energy.half 0 (-1) y) := by
    intro y hy
    have h := N8Bridge.origin_average P V hdelta hdiag y hy
    rwa [clockwise_eq_half, counterclockwise_eq_half] at h
  have hc := N8Energy.hyperplane_harmonic_constant
    (fun i : Fin (n+2) => i+1) (fun i : Fin (n+2) => i-1)
    successor_ne predecessor_ne successor_cycle f hf (all_index_average f hrot hm0)
  intro z
  have hz : (∑ i, (Fin.cons (-(∑ j, z j)) z) i) = 0 := by rw [Fin.sum_cons]; ring
  have h := hc (Fin.cons (-(∑ j, z j)) z) hz
  simpa only [f, Fin.tail_cons] using h

theorem positional_constant {m : ℕ} (P : (Fin m → ℝ) → ℝ)
    (V : (Fin (m+1) → ℝ) → ℝ) (hP : Continuous P)
    (hdelta : N8Bridge.DeltaEquation P V) (hdiag : N8Bridge.DiagonalZero V) :
    ∀ z, P z = P 0 := by
  cases m with
  | zero => intro z; congr 1; exact Subsingleton.elim _ _
  | succ n => exact positive_dimension_positional_constant P V hP hdelta hdiag

end N8Assembly

#print axioms N8Assembly.positional_constant

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Assembly.sum_shift, ``N8Assembly.rotate_eq_shift,
      ``N8Assembly.shift_add, ``N8Assembly.shift_invariance, ``N8Assembly.shift_half,
      ``N8Assembly.one_ne_zero, ``N8Assembly.successor_ne, ``N8Assembly.predecessor_ne,
      ``N8Assembly.successor_cycle, ``N8Assembly.last_eq_neg_one,
      ``N8Assembly.clockwise_eq_half, ``N8Assembly.counterclockwise_eq_half,
      ``N8Assembly.all_index_average, ``N8Assembly.positive_dimension_positional_constant,
      ``N8Assembly.positional_constant] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 assembled positional identities imply constancy"


/- Polynomial interface for N8's positional lemma. The prior analytic
   assembly is included by the checker. No free-Lie/group theorem here. -/
namespace N8Polynomial

open scoped BigOperators
open MvPolynomial

noncomputable def delta {R : Type*} [CommRing R] {m : ℕ}
    (P : MvPolynomial (Fin m) R) : MvPolynomial (Fin m) R :=
  (∑ i, X i) * P

noncomputable def bracket0 {R : Type*} [CommRing R] {m : ℕ}
    (P : MvPolynomial (Fin m) R) : MvPolynomial (Fin (m+1)) R :=
  rename Fin.succ P - rename Fin.castSucc P

def diagonalZero {m : ℕ} (P : MvPolynomial (Fin (m+2)) ℝ) : Prop :=
  ∀ w : Fin (m+2) → ℝ, (∑ i, w i) = 0 →
    w 0 = w (Fin.last (m+1)) → eval w P = 0

theorem eval_delta {m : ℕ} (P : MvPolynomial (Fin m) ℝ) (w : Fin m → ℝ) :
    eval w (delta P) = (∑ i, w i) * eval w P := by
  simp [delta]

theorem eval_bracket0 {m : ℕ} (P : MvPolynomial (Fin m) ℝ)
    (w : Fin (m+1) → ℝ) :
    eval w (bracket0 P) = eval (Fin.tail w) P - eval (Fin.init w) P := by
  simp only [bracket0, map_sub, eval_rename]
  rfl

theorem delta_equation {m : ℕ} (P : MvPolynomial (Fin m) ℝ)
    (V : MvPolynomial (Fin (m+1)) ℝ) (h : delta V = bracket0 P) :
    N8Bridge.DeltaEquation (fun z => eval z P) (fun z => eval z V) := by
  intro w
  have hh := congrArg (eval w) h
  simpa only [eval_delta, eval_bracket0] using hh

theorem diagonal_equation {m : ℕ} (V : MvPolynomial (Fin (m+1)) ℝ)
    (h : diagonalZero (bracket0 V)) :
    N8Bridge.DiagonalZero (fun z => eval z V) := by
  intro w hsum hend
  have hh := h w hsum hend
  rw [eval_bracket0] at hh
  exact sub_eq_zero.mp hh

theorem real_polynomial_constant {m : ℕ} (P : MvPolynomial (Fin m) ℝ)
    (V : MvPolynomial (Fin (m+1)) ℝ) (hdelta : delta V = bracket0 P)
    (hdiag : diagonalZero (bracket0 V)) : P = C (constantCoeff P) := by
  have hc := N8Assembly.positional_constant
    (fun z => eval z P) (fun z => eval z V) P.continuous_eval
    (delta_equation P V hdelta) (diagonal_equation V hdiag)
  apply MvPolynomial.funext
  intro z
  simpa only [eval_C, eval_zero] using hc z

theorem map_delta {R S : Type*} [CommRing R] [CommRing S] {m : ℕ}
    (f : R →+* S) (P : MvPolynomial (Fin m) R) :
    map f (delta P) = delta (map f P) := by
  simp [delta]

theorem map_bracket0 {R S : Type*} [CommRing R] [CommRing S] {m : ℕ}
    (f : R →+* S) (P : MvPolynomial (Fin m) R) :
    map f (bracket0 P) = bracket0 (map f P) := by
  simp [bracket0, map_rename]

theorem rational_polynomial_constant {m : ℕ} (P : MvPolynomial (Fin m) ℚ)
    (V : MvPolynomial (Fin (m+1)) ℚ) (hdelta : delta V = bracket0 P)
    (hdiag : ∀ w : Fin (m+2) → ℝ, (∑ i, w i) = 0 →
      w 0 = w (Fin.last (m+1)) → eval₂ (algebraMap ℚ ℝ) w (bracket0 V) = 0) :
    P = C (constantCoeff P) := by
  let f : ℚ →+* ℝ := algebraMap ℚ ℝ
  have hd : delta (map f V) = bracket0 (map f P) := by
    simpa only [map_delta, map_bracket0] using congrArg (map f) hdelta
  have hr : diagonalZero (bracket0 (map f V)) := by
    intro w hsum hend
    rw [← map_bracket0, eval_map]
    exact hdiag w hsum hend
  have hc := real_polynomial_constant (map f P) (map f V) hd hr
  apply MvPolynomial.map_injective (f := f) (FaithfulSMul.algebraMap_injective ℚ ℝ)
  simpa only [map_C, constantCoeff_map] using hc

noncomputable def diagonalVars (m : ℕ) : Fin (m+2) → MvPolynomial (Fin m) ℚ :=
  let a : MvPolynomial (Fin m) ℚ := C (-1/2) * ∑ i, X i
  Fin.cons a (Fin.snoc X a)

noncomputable def restriction {m : ℕ} (P : MvPolynomial (Fin (m+2)) ℚ) :
    MvPolynomial (Fin m) ℚ := eval₂ C (diagonalVars m) P

theorem diagonalVars_eval {m : ℕ} (z : Fin m → ℝ) :
    (fun i => eval₂ (algebraMap ℚ ℝ) z (diagonalVars m i)) =
      Fin.cons (-(∑ i, z i)/2) (Fin.snoc z (-(∑ i, z i)/2)) := by
  have ha : eval₂ (algebraMap ℚ ℝ) z
      (C (-1/2) * ∑ i : Fin m, X i) = -(∑ i, z i)/2 := by
    simp only [eval₂_mul, eval₂_C, eval₂_sum, eval₂_X]
    norm_num
    ring
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · simpa only [diagonalVars, Fin.cons_zero] using ha
  · refine Fin.lastCases ?_ (fun k => ?_) j
    · simpa only [diagonalVars, Fin.cons_succ, Fin.snoc_last] using ha
    · simp only [diagonalVars, Fin.cons_succ, Fin.snoc_castSucc, eval₂_X]

theorem eval_restriction {m : ℕ} (P : MvPolynomial (Fin (m+2)) ℚ)
    (z : Fin m → ℝ) :
    eval₂ (algebraMap ℚ ℝ) z (restriction P) =
      eval₂ (algebraMap ℚ ℝ)
        (Fin.cons (-(∑ i, z i)/2) (Fin.snoc z (-(∑ i, z i)/2))) P := by
  unfold restriction
  rw [← eval₂_assoc, diagonalVars_eval]

theorem diagonal_tuple {m : ℕ} (w : Fin (m+2) → ℝ)
    (hsum : (∑ i, w i) = 0) (hend : w 0 = w (Fin.last (m+1))) :
    w = Fin.cons (-(∑ i, (Fin.init (Fin.tail w)) i)/2)
      (Fin.snoc (Fin.init (Fin.tail w)) (-(∑ i, (Fin.init (Fin.tail w)) i)/2)) := by
  let z := Fin.init (Fin.tail w)
  have hlast : (Fin.tail w) (Fin.last m) = w 0 := by
    simpa only [Fin.tail, Fin.succ_last] using hend.symm
  have hw : w = Fin.cons (w 0) (Fin.snoc z (w 0)) := by
    have hz : Fin.snoc z (w 0) = Fin.tail w := by
      rw [← hlast]
      exact Fin.snoc_init_self (Fin.tail w)
    rw [hz, Fin.cons_self_tail]
  have ha : w 0 = -(∑ i, z i)/2 := by
    rw [hw, Fin.sum_cons, Fin.sum_snoc] at hsum
    linarith
  simpa only [ha] using hw

theorem restriction_zero_evaluation {m : ℕ} (P : MvPolynomial (Fin (m+2)) ℚ)
    (h : restriction P = 0) (w : Fin (m+2) → ℝ)
    (hsum : (∑ i, w i) = 0) (hend : w 0 = w (Fin.last (m+1))) :
    eval₂ (algebraMap ℚ ℝ) w P = 0 := by
  rw [diagonal_tuple w hsum hend, ← eval_restriction, h, eval₂_zero]

theorem rational_diagonal_constant {m : ℕ} (P : MvPolynomial (Fin m) ℚ)
    (V : MvPolynomial (Fin (m+1)) ℚ) (hdelta : delta V = bracket0 P)
    (hdiag : restriction (bracket0 V) = 0) : P = C (constantCoeff P) := by
  apply rational_polynomial_constant P V hdelta
  intro w hsum hend
  exact restriction_zero_evaluation (bracket0 V) hdiag w hsum hend

end N8Polynomial

#print axioms N8Polynomial.rational_polynomial_constant
#print axioms N8Polynomial.rational_diagonal_constant

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Polynomial.eval_delta, ``N8Polynomial.eval_bracket0,
      ``N8Polynomial.delta_equation, ``N8Polynomial.diagonal_equation,
      ``N8Polynomial.real_polynomial_constant, ``N8Polynomial.map_delta,
      ``N8Polynomial.map_bracket0, ``N8Polynomial.rational_polynomial_constant,
      ``N8Polynomial.diagonalVars_eval, ``N8Polynomial.eval_restriction,
      ``N8Polynomial.diagonal_tuple, ``N8Polynomial.restriction_zero_evaluation,
      ``N8Polynomial.rational_diagonal_constant] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 rational positional polynomial constancy"


/- The homogeneous word component of a free associative algebra and its
   positional polynomial dictionary. Earlier polynomial/analytic components
   are included unchanged by the checker. No free-Lie/group theorem here. -/
noncomputable section
namespace N8Words

open scoped BigOperators
open MvPolynomial

abbrev Words (m : ℕ) := (Fin m → ℕ) →₀ ℚ
abbrev Assoc := MonoidAlgebra ℚ (FreeMonoid ℕ)

def exponents {m : ℕ} (v : Fin m → ℕ) : Fin m →₀ ℕ :=
  Finsupp.equivFunOnFinite.symm v

def encode (m : ℕ) : Words m ≃ₗ[ℚ] MvPolynomial (Fin m) ℚ :=
  Finsupp.mapDomain.linearEquiv ℚ ℚ Finsupp.equivFunOnFinite.symm

def word {m : ℕ} (v : Fin m → ℕ) : FreeMonoid ℕ :=
  FreeMonoid.ofList (List.ofFn v)

def realize (m : ℕ) : Words m →ₗ[ℚ] Assoc :=
  Finsupp.lmapDomain ℚ ℚ word

def E (j : ℕ) : Assoc := Finsupp.single (FreeMonoid.of j) 1

def prepend {m : ℕ} (j : ℕ) : Words m →ₗ[ℚ] Words (m+1) :=
  Finsupp.lmapDomain ℚ ℚ (fun v : Fin m → ℕ => Fin.cons j v)

def append {m : ℕ} (j : ℕ) : Words m →ₗ[ℚ] Words (m+1) :=
  Finsupp.lmapDomain ℚ ℚ (fun v => Fin.snoc v j)

def bracket {m : ℕ} (j : ℕ) : Words m →ₗ[ℚ] Words (m+1) :=
  prepend j - append j

def increment {m : ℕ} (i : Fin m) (v : Fin m → ℕ) : Fin m → ℕ :=
  fun k => v k + if k = i then 1 else 0

def deriv (m : ℕ) : Words m →ₗ[ℚ] Words m :=
  ∑ i : Fin m, Finsupp.lmapDomain ℚ ℚ (increment i)

@[simp] theorem encode_single {m : ℕ} (v : Fin m → ℕ) (c : ℚ) :
    encode m (Finsupp.single v c) = monomial (exponents v) c := by
  change Finsupp.mapDomain exponents (Finsupp.single v c) = Finsupp.single (exponents v) c
  exact Finsupp.mapDomain_single

@[simp] theorem realize_single {m : ℕ} (v : Fin m → ℕ) (c : ℚ) :
    realize m (Finsupp.single v c) = Finsupp.single (word v) c := by
  change Finsupp.mapDomain word (Finsupp.single v c) = Finsupp.single (word v) c
  exact Finsupp.mapDomain_single

theorem realize_injective (m : ℕ) : Function.Injective (realize m) := by
  apply Finsupp.mapDomain_injective
  intro v w h
  exact List.ofFn_injective (FreeMonoid.ofList.injective h)

theorem exponents_increment {m : ℕ} (i : Fin m) (v : Fin m → ℕ) :
    exponents (increment i v) = Finsupp.single i 1 + exponents v := by
  classical
  ext k
  by_cases h : k = i <;> simp [exponents, increment, h, add_comm]

theorem exponents_cons {m : ℕ} (j : ℕ) (v : Fin m → ℕ) :
    exponents (Fin.cons j v) =
      Finsupp.single 0 j + (exponents v).mapDomain Fin.succ := by
  classical
  ext k
  refine Fin.cases ?_ (fun i => ?_) k
  · rw [Finsupp.add_apply, Finsupp.single_eq_same,
      Finsupp.mapDomain_notin_range _ _ (by simp)]
    simp [exponents]
  · rw [Finsupp.add_apply, Finsupp.mapDomain_apply (Fin.succ_injective m)]
    simp [exponents]

theorem exponents_snoc {m : ℕ} (j : ℕ) (v : Fin m → ℕ) :
    exponents (Fin.snoc v j) =
      Finsupp.single (Fin.last m) j + (exponents v).mapDomain Fin.castSucc := by
  classical
  ext k
  refine Fin.lastCases ?_ (fun i => ?_) k
  · rw [Finsupp.add_apply, Finsupp.single_eq_same,
      Finsupp.mapDomain_notin_range _ _ (by simp)]
    simp [exponents]
  · rw [Finsupp.add_apply, Finsupp.mapDomain_apply (Fin.castSucc_injective m)]
    simp [exponents]

theorem encode_prepend {m : ℕ} (j : ℕ) (D : Words m) :
    encode (m+1) (prepend j D) = X 0 ^ j * rename Fin.succ (encode m D) := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf, mul_add]
  | single v c =>
    simp only [prepend, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, encode_single]
    rw [exponents_cons, monomial_single_add, rename_monomial]

theorem encode_append {m : ℕ} (j : ℕ) (D : Words m) :
    encode (m+1) (append j D) = X (Fin.last m) ^ j * rename Fin.castSucc (encode m D) := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf, mul_add]
  | single v c =>
    simp only [append, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, encode_single]
    rw [exponents_snoc, monomial_single_add, rename_monomial]

theorem encode_bracket_zero {m : ℕ} (D : Words m) :
    encode (m+1) (bracket 0 D) = N8Polynomial.bracket0 (encode m D) := by
  simp [bracket, encode_prepend, encode_append, N8Polynomial.bracket0]

theorem deriv_single {m : ℕ} (v : Fin m → ℕ) (c : ℚ) :
    deriv m (Finsupp.single v c) = ∑ i, Finsupp.single (increment i v) c := by
  classical
  simp [deriv, Finsupp.lmapDomain_apply]

theorem encode_deriv {m : ℕ} (D : Words m) :
    encode m (deriv m D) = N8Polynomial.delta (encode m D) := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp [N8Polynomial.delta]
  | add D F hd hf => simp [map_add, hd, hf, N8Polynomial.delta, mul_add]
  | single v c =>
    rw [deriv_single, map_sum]
    simp only [encode_single, exponents_increment, monomial_single_add, pow_one]
    simp [N8Polynomial.delta, Finset.sum_mul]

theorem realize_prepend {m : ℕ} (j : ℕ) (D : Words m) :
    realize (m+1) (prepend j D) = E j * realize m D := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf, mul_add]
  | single v c =>
    simp only [prepend, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, realize_single]
    change MonoidAlgebra.single (word (Fin.cons j v)) c =
      MonoidAlgebra.single (FreeMonoid.of j) 1 * MonoidAlgebra.single (word v) c
    rw [MonoidAlgebra.single_mul_single, one_mul]
    congr 1
    simp only [word, List.ofFn_cons, FreeMonoid.ofList_cons]

theorem realize_append {m : ℕ} (j : ℕ) (D : Words m) :
    realize (m+1) (append j D) = realize m D * E j := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf, add_mul]
  | single v c =>
    simp only [append, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, realize_single]
    have hs : List.ofFn (Fin.snoc v j) = List.ofFn v ++ [j] := by
      rw [List.ofFn_succ']
      simp
    change MonoidAlgebra.single (word (Fin.snoc v j)) c =
      MonoidAlgebra.single (word v) c * MonoidAlgebra.single (FreeMonoid.of j) 1
    rw [MonoidAlgebra.single_mul_single, mul_one]
    congr 1

theorem realize_bracket {m : ℕ} (j : ℕ) (D : Words m) :
    realize (m+1) (bracket j D) = E j * realize m D - realize m D * E j := by
  simp [bracket, realize_prepend, realize_append]

theorem exponents_zero (m : ℕ) : exponents (fun _ : Fin m => 0) = 0 := by
  ext i
  rfl

theorem encode_zero_word (m : ℕ) (c : ℚ) :
    encode m (Finsupp.single (fun _ => 0) c) = C c := by
  rw [encode_single, exponents_zero]
  rfl

theorem positional_word_constant {m : ℕ} (D : Words m) (V : Words (m+1))
    (hdelta : deriv (m+1) V = bracket 0 D)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    ∃ c : ℚ, D = Finsupp.single (fun _ => 0) c := by
  have hd := congrArg (encode (m+1)) hdelta
  rw [encode_deriv, encode_bracket_zero] at hd
  rw [encode_bracket_zero] at hdiag
  have hc := N8Polynomial.rational_diagonal_constant (encode m D) (encode (m+1) V) hd hdiag
  refine ⟨constantCoeff (encode m D), (encode m).injective ?_⟩
  rw [encode_zero_word]
  exact hc

theorem sum_variables_ne_zero {m : ℕ} (hm : 0 < m) :
    (∑ i : Fin m, X i : MvPolynomial (Fin m) ℚ) ≠ 0 := by
  intro h
  have hh := congrArg (eval (fun _ => (1 : ℚ))) h
  simp only [map_sum, eval_X, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul, mul_one, map_zero] at hh
  have hz : m = 0 := by exact_mod_cast hh
  omega

theorem deriv_injective {m : ℕ} (hm : 0 < m) : Function.Injective (deriv m) := by
  intro D F h
  apply (encode m).injective
  have hh := congrArg (encode m) h
  rw [encode_deriv, encode_deriv] at hh
  exact mul_left_cancel₀ (sum_variables_ne_zero hm) hh

theorem bracket_zero_word (m : ℕ) (c : ℚ) :
    bracket 0 (Finsupp.single (fun _ : Fin m => 0) c) = 0 := by
  apply (encode (m+1)).injective
  rw [encode_bracket_zero, encode_zero_word]
  simp [N8Polynomial.bracket0]

theorem positional_word_separation {m : ℕ} (D : Words m) (V : Words (m+1))
    (hdelta : deriv (m+1) V = bracket 0 D)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    (∃ c : ℚ, D = Finsupp.single (fun _ => 0) c) ∧ V = 0 := by
  obtain ⟨c, hc⟩ := positional_word_constant D V hdelta hdiag
  refine ⟨⟨c, hc⟩, deriv_injective (Nat.zero_lt_succ m) ?_⟩
  rw [hdelta, hc, bracket_zero_word, map_zero]

theorem deriv_prepend {m : ℕ} (j : ℕ) (D : Words m) :
    deriv (m+1) (prepend j D) = prepend (j+1) D + prepend j (deriv m D) := by
  apply (encode (m+1)).injective
  rw [encode_deriv, map_add, encode_prepend, encode_prepend, encode_prepend, encode_deriv]
  simp only [N8Polynomial.delta, map_mul, map_sum, rename_X, Fin.sum_univ_succ, pow_succ]
  ring

def basisWord (w : List ℕ) : Assoc := Finsupp.single (FreeMonoid.ofList w) 1

def derivWord : List ℕ → Assoc
  | [] => 0
  | i :: w => E (i+1) * basisWord w + E i * derivWord w

def assocDeriv : Assoc →ₗ[ℚ] Assoc :=
  Finsupp.linearCombination ℚ (fun w => derivWord (FreeMonoid.toList w))

theorem assocDeriv_single (w : FreeMonoid ℕ) (c : ℚ) :
    assocDeriv (Finsupp.single w c) = c • derivWord (FreeMonoid.toList w) := by
  exact Finsupp.linearCombination_single ℚ c w

theorem derivWord_ofFn (m : ℕ) (v : Fin m → ℕ) :
    derivWord (List.ofFn v) = realize m (deriv m (Finsupp.single v 1)) := by
  classical
  induction m with
  | zero => simp [derivWord, deriv]
  | succ m ih =>
    let a := v 0
    let u := Fin.tail v
    have hv : v = Fin.cons a u := (Fin.cons_self_tail v).symm
    have hs : Finsupp.single (Fin.cons a u) (1 : ℚ) = prepend a (Finsupp.single u 1) := by
      simp [prepend, Finsupp.lmapDomain_apply]
    rw [hv, List.ofFn_cons, derivWord, hs, deriv_prepend, map_add,
      realize_prepend, realize_prepend]
    rw [← ih u, realize_single]
    rfl

theorem assocDeriv_realize {m : ℕ} (D : Words m) :
    assocDeriv (realize m D) = realize m (deriv m D) := by
  classical
  induction D using Finsupp.induction_linear with
  | zero => simp
  | add D F hd hf => simp [map_add, hd, hf]
  | single v c =>
    rw [realize_single, assocDeriv_single]
    have hs : Finsupp.single v c = c • Finsupp.single v (1 : ℚ) := by simp
    rw [hs, map_smul, map_smul, ← derivWord_ofFn]
    rfl

theorem assocDeriv_generator (j : ℕ) : assocDeriv (E j) = E (j+1) := by
  rw [E, assocDeriv_single]
  simp only [FreeMonoid.toList_of, derivWord, basisWord, FreeMonoid.ofList_nil,
    ← MonoidAlgebra.one_def, mul_one, mul_zero, add_zero, one_smul]

theorem ambient_positional_separation {m : ℕ} (D : Words m) (V : Words (m+1))
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    (∃ c : ℚ, D = Finsupp.single (fun _ => 0) c) ∧ realize (m+1) V = 0 := by
  have hd : deriv (m+1) V = bracket 0 D := by
    apply realize_injective (m+1)
    simpa only [← assocDeriv_realize, realize_bracket] using hdelta
  obtain ⟨hc, hv⟩ := positional_word_separation D V hd hdiag
  exact ⟨hc, by rw [hv, map_zero]⟩

theorem basisWord_nil : basisWord [] = 1 := by
  rfl

theorem basisWord_cons (j : ℕ) (w : List ℕ) :
    basisWord (j :: w) = E j * basisWord w := by
  simp only [basisWord, E, MonoidAlgebra.single_mul_single, one_mul,
    FreeMonoid.ofList_cons]

theorem basisWord_append (u v : List ℕ) :
    basisWord (u ++ v) = basisWord u * basisWord v := by
  simp only [basisWord, MonoidAlgebra.single_mul_single, one_mul,
    FreeMonoid.ofList_append]

theorem derivWord_append (u v : List ℕ) :
    derivWord (u ++ v) = derivWord u * basisWord v + basisWord u * derivWord v := by
  induction u with
  | nil => simp [derivWord, basisWord_nil]
  | cons j u ih =>
    simp only [List.cons_append, derivWord, basisWord_append, basisWord_cons, ih]
    noncomm_ring

theorem single_eq_smul_basis (w : FreeMonoid ℕ) (c : ℚ) :
    (Finsupp.single w c : Assoc) = c • basisWord (FreeMonoid.toList w) := by
  simp [basisWord]

theorem assocDeriv_mul (F G : Assoc) :
    assocDeriv (F * G) = assocDeriv F * G + F * assocDeriv G := by
  classical
  induction F using Finsupp.induction_linear with
  | zero => simp
  | add F H hf hh => simp [add_mul, map_add, hf, hh, add_assoc, add_left_comm, add_comm]
  | single u c =>
    induction G using Finsupp.induction_linear with
    | zero => simp
    | add G H hg hh => simp [mul_add, map_add, hg, hh, add_assoc, add_left_comm, add_comm]
    | single v d =>
      rw [MonoidAlgebra.single_mul_single, assocDeriv_single, assocDeriv_single,
        assocDeriv_single, FreeMonoid.toList_mul, derivWord_append, smul_add,
        single_eq_smul_basis v d, single_eq_smul_basis u c]
      simp only [smul_mul_assoc, mul_smul_comm, smul_smul, mul_comm c d]

theorem basisWord_replicate (j m : ℕ) : basisWord (List.replicate m j) = E j ^ m := by
  induction m with
  | zero => simp [basisWord_nil]
  | succ m ih => simp only [List.replicate_succ, basisWord_cons, ih, pow_succ']

theorem realize_zero_word (m : ℕ) (c : ℚ) :
    realize m (Finsupp.single (fun _ : Fin m => 0) c) = c • E 0 ^ m := by
  rw [realize_single, single_eq_smul_basis]
  simp only [word, FreeMonoid.toList_ofList, List.ofFn_const, basisWord_replicate]

theorem associative_separation {m : ℕ} (D : Words m) (V : Words (m+1))
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    (∃ c : ℚ, realize m D = c • E 0 ^ m) ∧ realize (m+1) V = 0 := by
  obtain ⟨⟨c, hc⟩, hv⟩ := ambient_positional_separation D V hdelta hdiag
  exact ⟨⟨c, by rw [hc, realize_zero_word]⟩, hv⟩

theorem diagonalVars_sum (m : ℕ) : (∑ i, N8Polynomial.diagonalVars m i) = 0 := by
  simp only [N8Polynomial.diagonalVars, Fin.sum_cons, Fin.sum_snoc]
  have hc : (C (-1/2) : MvPolynomial (Fin m) ℚ) + C (-1/2) + 1 = 0 := by
    calc
      _ = C ((-1/2 : ℚ) + (-1/2) + 1) := by simp only [C_add, C_1]
      _ = 0 := by norm_num
  calc
    (C (-1/2 : ℚ) : MvPolynomial (Fin m) ℚ) * (∑ i : Fin m, X i) +
        ((∑ i : Fin m, X i) + C (-1/2 : ℚ) * (∑ i : Fin m, X i)) =
        (C (-1/2 : ℚ) + C (-1/2 : ℚ) + 1) * (∑ i : Fin m, X i) := by ring
    _ = 0 := by rw [hc, zero_mul]

theorem restriction_delta_zero {m : ℕ} (D : Words (m+2)) :
    N8Polynomial.restriction (encode (m+2) (deriv (m+2) D)) = 0 := by
  rw [encode_deriv]
  simp [N8Polynomial.restriction, N8Polynomial.delta, diagonalVars_sum]

theorem restriction_bracket {m : ℕ} (j : ℕ) (D : Words (m+1)) :
    N8Polynomial.restriction (encode (m+2) (bracket j D)) =
      (C (-1/2) * ∑ i : Fin m, X i) ^ j *
        N8Polynomial.restriction (encode (m+2) (bracket 0 D)) := by
  simp only [bracket, LinearMap.sub_apply, map_sub, encode_prepend, encode_append]
  simp [N8Polynomial.restriction, N8Polynomial.diagonalVars, mul_sub]

end N8Words

#print axioms N8Words.positional_word_constant
#print axioms N8Words.associative_separation

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Words.encode_single, ``N8Words.realize_single,
      ``N8Words.realize_injective, ``N8Words.exponents_increment,
      ``N8Words.exponents_cons, ``N8Words.exponents_snoc,
      ``N8Words.encode_prepend, ``N8Words.encode_append,
      ``N8Words.encode_bracket_zero, ``N8Words.deriv_single,
      ``N8Words.encode_deriv, ``N8Words.realize_prepend,
      ``N8Words.realize_append, ``N8Words.realize_bracket,
      ``N8Words.exponents_zero, ``N8Words.encode_zero_word,
      ``N8Words.positional_word_constant, ``N8Words.sum_variables_ne_zero,
      ``N8Words.deriv_injective, ``N8Words.bracket_zero_word,
      ``N8Words.positional_word_separation, ``N8Words.deriv_prepend,
      ``N8Words.assocDeriv_single, ``N8Words.derivWord_ofFn,
      ``N8Words.assocDeriv_realize, ``N8Words.assocDeriv_generator,
      ``N8Words.ambient_positional_separation, ``N8Words.basisWord_nil,
      ``N8Words.basisWord_cons, ``N8Words.basisWord_append,
      ``N8Words.derivWord_append, ``N8Words.single_eq_smul_basis,
      ``N8Words.assocDeriv_mul, ``N8Words.basisWord_replicate,
      ``N8Words.realize_zero_word, ``N8Words.associative_separation,
      ``N8Words.diagonalVars_sum, ``N8Words.restriction_delta_zero,
      ``N8Words.restriction_bracket] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 ordered-word positional dictionary"


/- The generated Lie subalgebra of the actual associative word algebra.
   All ordered-word and polynomial prerequisites are included unchanged. -/
noncomputable section
namespace N8Lie

open N8Words

def generatedLie : LieSubalgebra ℚ Assoc :=
  LieSubalgebra.lieSpan ℚ Assoc (Set.range E)

def abelianImage : Assoc →ₐ[ℚ] Polynomial ℚ :=
  MonoidAlgebra.lift ℚ (FreeMonoid ℕ) (Polynomial ℚ)
    (FreeMonoid.lift (fun j : ℕ => if j = 0 then Polynomial.X else 0))

@[simp] theorem image_generator (j : ℕ) :
    abelianImage (E j) = if j = 0 then Polynomial.X else 0 := by
  simp [abelianImage, E]

theorem generator_mem (j : ℕ) : E j ∈ generatedLie :=
  LieSubalgebra.subset_lieSpan ⟨j, rfl⟩

theorem image_lie_linear {D : Assoc} (hD : D ∈ generatedLie) :
    ∃ c : ℚ, abelianImage D = c • Polynomial.X := by
  change D ∈ LieSubalgebra.lieSpan ℚ Assoc (Set.range E) at hD
  induction hD using LieSubalgebra.lieSpan_induction with
  | mem x hx =>
    obtain ⟨j, rfl⟩ := hx
    by_cases hj : j = 0
    · exact ⟨1, by simp [hj]⟩
    · exact ⟨0, by simp [hj]⟩
  | zero => exact ⟨0, by simp⟩
  | add x y hx hy ix iy =>
    obtain ⟨a, ha⟩ := ix
    obtain ⟨b, hb⟩ := iy
    exact ⟨a+b, by simp [ha, hb, add_smul]⟩
  | smul a x hx ix =>
    obtain ⟨b, hb⟩ := ix
    exact ⟨a*b, by simp [hb, mul_smul]⟩
  | lie x y hx hy ix iy =>
    exact ⟨0, by simp [Ring.lie_def, mul_comm]⟩

theorem scalar_power_exclusion (m : ℕ) (c : ℚ)
    (hD : c • E 0 ^ m ∈ generatedLie) (hm : m ≠ 1) : c = 0 := by
  obtain ⟨a, ha⟩ := image_lie_linear hD
  have hcoeff := congrArg (fun P : Polynomial ℚ => P.coeff m) ha
  simpa [Polynomial.coeff_X_of_ne_one hm] using hcoeff

theorem scalar_power_mem_iff (m : ℕ) (c : ℚ) :
    c • E 0 ^ m ∈ generatedLie ↔ c = 0 ∨ m = 1 := by
  constructor
  · intro hD
    by_cases hm : m = 1
    · exact Or.inr hm
    · exact Or.inl (scalar_power_exclusion m c hD hm)
  · rintro (rfl | hm)
    · simpa only [zero_smul] using generatedLie.zero_mem
    · simpa [hm] using generatedLie.smul_mem c (generator_mem 0)

theorem deriv_bracket (F G : Assoc) :
    assocDeriv ⁅F, G⁆ = ⁅assocDeriv F, G⁆ + ⁅F, assocDeriv G⁆ := by
  simp only [Ring.lie_def, map_sub, assocDeriv_mul]
  noncomm_ring

theorem deriv_mem {D : Assoc} (hD : D ∈ generatedLie) :
    assocDeriv D ∈ generatedLie := by
  change D ∈ LieSubalgebra.lieSpan ℚ Assoc (Set.range E) at hD
  induction hD using LieSubalgebra.lieSpan_induction with
  | mem x hx =>
    obtain ⟨j, rfl⟩ := hx
    simpa only [assocDeriv_generator] using generator_mem (j+1)
  | zero => simpa only [map_zero] using generatedLie.zero_mem
  | add x y hx hy ix iy =>
    simpa only [map_add] using generatedLie.add_mem ix iy
  | smul a x hx ix =>
    simpa only [map_smul] using generatedLie.smul_mem a ix
  | lie x y hx hy ix iy =>
    rw [deriv_bracket]
    exact generatedLie.add_mem (generatedLie.lie_mem ix hy) (generatedLie.lie_mem hx iy)

theorem lie_separation {m : ℕ} (D : Words m) (V : Words (m+1))
    (hLie : realize m D ∈ generatedLie)
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    realize (m+1) V = 0 ∧
      ((m = 1 ∧ ∃ c : ℚ, realize m D = c • E 0) ∨ realize m D = 0) := by
  obtain ⟨⟨c, hc⟩, hv⟩ := associative_separation D V hdelta hdiag
  refine ⟨hv, ?_⟩
  by_cases hm : m = 1
  · exact Or.inl ⟨hm, c, by simpa [hm] using hc⟩
  · have hz : c = 0 := scalar_power_exclusion m c (hc ▸ hLie) hm
    exact Or.inr (by simpa [hz] using hc)

theorem lie_separation_ne_one {m : ℕ} (hm : m ≠ 1)
    (D : Words m) (V : Words (m+1))
    (hLie : realize m D ∈ generatedLie)
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0)
    (hdiag : N8Polynomial.restriction (encode (m+2) (bracket 0 V)) = 0) :
    D = 0 ∧ V = 0 := by
  obtain ⟨hv, hd⟩ := lie_separation D V hLie hdelta hdiag
  have hd0 : realize m D = 0 := hd.resolve_left (fun h => hm h.1)
  exact ⟨realize_injective m (by simpa using hd0),
    realize_injective (m+1) (by simpa using hv)⟩

theorem diagonal_nonzero {m : ℕ} (hm : m ≠ 1)
    (D : Words m) (V : Words (m+1)) (hD : D ≠ 0)
    (hLie : realize m D ∈ generatedLie)
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0) :
    N8Polynomial.restriction (encode (m+2) (bracket 0 V)) ≠ 0 := by
  intro hdiag
  exact hD (lie_separation_ne_one hm D V hLie hdelta hdiag).1

end N8Lie

#print axioms N8Lie.lie_separation
#print axioms N8Lie.lie_separation_ne_one

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Lie.image_generator, ``N8Lie.generator_mem,
      ``N8Lie.image_lie_linear, ``N8Lie.scalar_power_exclusion,
      ``N8Lie.scalar_power_mem_iff, ``N8Lie.deriv_bracket, ``N8Lie.deriv_mem,
      ``N8Lie.lie_separation, ``N8Lie.lie_separation_ne_one,
      ``N8Lie.diagonal_nonzero] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 generated Lie subalgebra exception"
