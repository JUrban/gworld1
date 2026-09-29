import Mathlib.LinearAlgebra.Matrix.Defs
import Mathlib.Topology.Order.Compact
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Tactic
import Lean.Util.CollectAxioms

/- Analytic ingredients only: the N8 Lie encoding and transfer-word
   construction are not formalized by this file. -/
namespace N8

open scoped BigOperators
open Filter Topology

def l1 {I : Type*} [Fintype I] (v : I → ℝ) : ℝ := ∑ i, |v i|

theorem stochastic_contraction {I : Type*} [Fintype I]
    (A : Matrix I I ℝ) (e : ℝ) (v : I → ℝ)
    (hentry : ∀ i j, e ≤ A i j)
    (hcol : ∀ j, ∑ i, A i j = 1)
    (hzero : ∑ j, v j = 0) :
    l1 (A.mulVec v) ≤ (1 - (Fintype.card I : ℝ) * e) * l1 v := by
  have hrow (i : I) : (A.mulVec v) i = ∑ j, (A i j - e) * v j := by
    simp only [Matrix.mulVec, dotProduct, sub_mul, Finset.sum_sub_distrib]
    rw [← Finset.mul_sum, hzero, mul_zero, sub_zero]
  unfold l1
  calc
    ∑ i, |(A.mulVec v) i| ≤ ∑ i, ∑ j, (A i j - e) * |v j| := by
      apply Finset.sum_le_sum
      intro i hi
      rw [hrow i]
      calc
        |∑ j, (A i j - e) * v j| ≤ ∑ j, |(A i j - e) * v j| :=
          Finset.abs_sum_le_sum_abs _ _
        _ = ∑ j, (A i j - e) * |v j| := by
          apply Finset.sum_congr rfl
          intro j hj
          rw [abs_mul, abs_of_nonneg (sub_nonneg.mpr (hentry i j))]
    _ = (1 - (Fintype.card I : ℝ) * e) * ∑ j, |v j| := by
      rw [Finset.sum_comm]
      simp_rw [← Finset.sum_mul, Finset.sum_sub_distrib, hcol]
      simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      rw [Finset.mul_sum]

inductive Reach {X I : Type*} (A B : I → X → X) (x : X) : X → Prop
  | refl : Reach A B x x
  | left {y : X} (h : Reach A B x y) (i : I) : Reach A B x (A i y)
  | right {y : X} (h : Reach A B x y) (i : I) : Reach A B x (B i y)

theorem reach_preserves_max {X I : Type*} (S : Set X)
    (f : X → ℝ) (A B : I → X → X)
    (hA : ∀ i x, x ∈ S → A i x ∈ S)
    (hB : ∀ i x, x ∈ S → B i x ∈ S)
    (hmean : ∀ i x, x ∈ S → 2 * f x = f (A i x) + f (B i x))
    {x y : X} (hx : x ∈ S) (hmax : IsMaxOn f S x)
    (hreach : Reach A B x y) : y ∈ S ∧ f y = f x := by
  induction hreach with
  | refl => exact ⟨hx, rfl⟩
  | @left y h i ih =>
    have ha := hA i y ih.1
    have hb := hB i y ih.1
    have hma : f (A i y) ≤ f x := hmax ha
    have hmb : f (B i y) ≤ f x := hmax hb
    have hm := hmean i y ih.1
    exact ⟨ha, by linarith [ih.2]⟩
  | @right y h i ih =>
    have ha := hA i y ih.1
    have hb := hB i y ih.1
    have hma : f (A i y) ≤ f x := hmax ha
    have hmb : f (B i y) ≤ f x := hmax hb
    have hm := hmean i y ih.1
    exact ⟨hb, by linarith [ih.2]⟩

theorem harmonic_le_base {X I : Type*} [TopologicalSpace X]
    (S : Set X) (hcompact : IsCompact S) (base : X) (hbase : base ∈ S)
    (f : X → ℝ) (hf : Continuous f) (A B : I → X → X)
    (hA : ∀ i x, x ∈ S → A i x ∈ S)
    (hB : ∀ i x, x ∈ S → B i x ∈ S)
    (hmean : ∀ i x, x ∈ S → 2 * f x = f (A i x) + f (B i x))
    (happroach : ∀ x ∈ S, ∃ seq : ℕ → X,
      (∀ n, Reach A B x (seq n)) ∧ Tendsto seq atTop (𝓝 base)) :
    ∀ z ∈ S, f z ≤ f base := by
  obtain ⟨x, hx, hm⟩ := hcompact.exists_isMaxOn ⟨base, hbase⟩ hf.continuousOn
  obtain ⟨seq, hs, ht⟩ := happroach x hx
  have heq : (fun n => f (seq n)) = fun _ : ℕ => f x := by
    funext n
    exact (reach_preserves_max S f A B hA hB hmean hx hm (hs n)).2
  have hlim : Tendsto (fun n => f (seq n)) atTop (𝓝 (f base)) :=
    (hf.tendsto base).comp ht
  rw [heq] at hlim
  have hvalue : f x = f base := tendsto_nhds_unique tendsto_const_nhds hlim
  intro z hz
  simpa only [hvalue] using hm hz

theorem harmonic_constant {X I : Type*} [TopologicalSpace X]
    (S : Set X) (hcompact : IsCompact S) (base : X) (hbase : base ∈ S)
    (f : X → ℝ) (hf : Continuous f) (A B : I → X → X)
    (hA : ∀ i x, x ∈ S → A i x ∈ S)
    (hB : ∀ i x, x ∈ S → B i x ∈ S)
    (hmean : ∀ i x, x ∈ S → 2 * f x = f (A i x) + f (B i x))
    (happroach : ∀ x ∈ S, ∃ seq : ℕ → X,
      (∀ n, Reach A B x (seq n)) ∧ Tendsto seq atTop (𝓝 base)) :
    ∀ z ∈ S, f z = f base := by
  have hupper := harmonic_le_base S hcompact base hbase f hf A B hA hB hmean happroach
  have hnegmean : ∀ i x, x ∈ S →
      2 * (-f x) = (-f (A i x)) + (-f (B i x)) := by
    intro i x hx
    linarith [hmean i x hx]
  have hlower := harmonic_le_base S hcompact base hbase (fun x => -f x)
    hf.neg A B hA hB hnegmean happroach
  intro z hz
  linarith [hupper z hz, hlower z hz]

end N8

#print axioms N8.stochastic_contraction
#print axioms N8.harmonic_constant

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8.stochastic_contraction, ``N8.reach_preserves_max,
      ``N8.harmonic_le_base, ``N8.harmonic_constant] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 stochastic contraction and harmonic maximum principle"
