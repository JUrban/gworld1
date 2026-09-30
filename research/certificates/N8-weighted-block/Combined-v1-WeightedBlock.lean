import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.Algebra.MvPolynomial.Eval
import Lean.Util.CollectAxioms

/- Concrete weighted ordered-word instantiation. The original free-Lie
   projection and nilpotent-group production of the hypotheses remain outside. -/
noncomputable section
namespace N8WeightedBlock

open scoped BigOperators
open N8Words N8Lie MvPolynomial

def tupleWeight {m : ℕ} (p u : ℕ) (v : Fin m → ℕ) : ℕ :=
  ∑ i, (u + p * v i)

def homogeneous {m : ℕ} (p u q : ℕ) (D : Words m) : Prop :=
  ∀ v, D v ≠ 0 → tupleWeight p u v = q

def restrictWords (m : ℕ) : Words (m+2) →ₗ[ℚ] MvPolynomial (Fin m) ℚ :=
  (aeval (N8Polynomial.diagonalVars m)).toLinearMap.comp (encode (m+2)).toLinearMap

theorem restrictWords_eq {m : ℕ} (F : Words (m+2)) :
    restrictWords m F = N8Polynomial.restriction (encode (m+2) F) := by
  rfl

def diagonalScalar (m : ℕ) : MvPolynomial (Fin m) ℚ :=
  C (-1/2) * ∑ i, X i

def multiplier (m : ℕ) (c : ℚ) (n : ℕ) :
    MvPolynomial (Fin m) ℚ →ₗ[ℚ] MvPolynomial (Fin m) ℚ :=
  c • LinearMap.mulLeft ℚ (diagonalScalar m ^ n)

theorem multiplier_apply (m : ℕ) (c : ℚ) (n : ℕ) (P : MvPolynomial (Fin m) ℚ) :
    multiplier m c n P = c • (diagonalScalar m ^ n * P) := by
  rfl

theorem restrict_deriv {m : ℕ} (F : Words (m+2)) :
    restrictWords m (deriv (m+2) F) = 0 :=
  restriction_delta_zero F

theorem restrict_bracket {m : ℕ} (j : ℕ) (F : Words (m+1)) :
    restrictWords m (bracket j F) =
      diagonalScalar m ^ j * restrictWords m (bracket 0 F) :=
  restriction_bracket j F

theorem weighted_diagonal_nonzero {m : ℕ} (p u q : ℕ) (huq : u < q)
    (D : Words m) (V : Words (m+1)) (hD : D ≠ 0)
    (hhom : homogeneous p u q D) (hLie : realize m D ∈ generatedLie)
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0) :
    restrictWords m (bracket 0 V) ≠ 0 := by
  intro hdiag
  obtain ⟨⟨c, hc⟩, _⟩ := ambient_positional_separation D V hdelta hdiag
  have hcnz : c ≠ 0 := by
    intro hz
    apply hD
    simp [hc, hz]
  have hl : c • E 0 ^ m ∈ generatedLie := by
    rw [← realize_zero_word, ← hc]
    exact hLie
  have hm : m = 1 := ((scalar_power_mem_iff m c).mp hl).resolve_left hcnz
  have hv : D (fun _ => 0) ≠ 0 := by simpa [hc] using hcnz
  have hw := hhom (fun _ => 0) hv
  simp [tupleWeight, hm] at hw
  omega

theorem earlier_restrictions_vanish {m : ℕ} (t : ℕ) (b : ℚ) (hb : b ≠ 0)
    (F : ℕ → Words (m+1)) (G : ℕ → Words (m+2))
    (c : ℕ → ℕ → ℚ) (n : ℕ → ℕ → ℕ)
    (heq : ∀ j < t, b • bracket 0 (F j) +
      ∑ k ∈ Finset.range j, c j k • bracket (n j k) (F k) = deriv (m+2) (G j)) :
    ∀ j < t, restrictWords m (bracket 0 (F j)) = 0 := by
  apply N8Block.triangular_vanishes t b hb
    (fun j => restrictWords m (bracket 0 (F j)))
    (fun j k => multiplier m (c j k) (n j k))
  intro j hj
  have h := congrArg (restrictWords m) (heq j hj)
  simpa only [map_add, map_smul, map_sum, restrict_deriv, restrict_bracket,
    multiplier_apply] using h

theorem later_restrictions_vanish {m : ℕ} {I : Type*} (t : ℕ)
    (F : ℕ → Words (m+1)) (hF : ∀ j < t, restrictWords m (bracket 0 (F j)) = 0)
    (W : I → Words (m+2)) (d : I → ℕ → ℚ) (n : I → ℕ → ℕ)
    (B : I → Words (m+2))
    (hB : ∀ s, B s = deriv (m+2) (W s) +
      ∑ i ∈ Finset.Ioc t (2*t), d s i • bracket (n s i) (F (2*t-i))) :
    ∀ s, restrictWords m (B s) = 0 := by
  intro s
  rw [hB s, map_add, restrict_deriv, zero_add, map_sum]
  apply Finset.sum_eq_zero
  intro i hi
  have hij := Finset.mem_Ioc.mp hi
  have hj : 2*t-i < t := by omega
  rw [map_smul, restrict_bracket, hF _ hj]
  simp

theorem correction_span_killed {m : ℕ} {I : Type*} (t : ℕ)
    (F : ℕ → Words (m+1)) (hF : ∀ j < t, restrictWords m (bracket 0 (F j)) = 0)
    (W : I → Words (m+2)) (d : I → ℕ → ℚ) (n : I → ℕ → ℕ)
    (B : I → Words (m+2))
    (hB : ∀ s, B s = deriv (m+2) (W s) +
      ∑ i ∈ Finset.Ioc t (2*t), d s i • bracket (n s i) (F (2*t-i))) :
    LinearMap.range (deriv (m+2)) ⊔ Submodule.span ℚ (Set.range B) ≤
      LinearMap.ker (restrictWords m) := by
  refine sup_le ?_ (Submodule.span_le.mpr ?_)
  · rintro _ ⟨H, rfl⟩
    exact restrict_deriv H
  · rintro _ ⟨s, rfl⟩
    exact later_restrictions_vanish t F hF W d n B hB s

theorem weighted_block_separation {m : ℕ} {I : Type*}
    (p u q : ℕ) (huq : u < q)
    (D : Words m) (V : Words (m+1)) (hD : D ≠ 0)
    (hhom : homogeneous p u q D) (hLie : realize m D ∈ generatedLie)
    (hdelta : assocDeriv (realize (m+1) V) = E 0 * realize m D - realize m D * E 0)
    (t : ℕ) (b : ℚ) (hb : b ≠ 0)
    (F : ℕ → Words (m+1)) (G : ℕ → Words (m+2))
    (c : ℕ → ℕ → ℚ) (n : ℕ → ℕ → ℕ)
    (heq : ∀ j < t, b • bracket 0 (F j) +
      ∑ k ∈ Finset.range j, c j k • bracket (n j k) (F k) = deriv (m+2) (G j))
    (W : I → Words (m+2)) (d : I → ℕ → ℚ) (e : I → ℕ → ℕ)
    (B : I → Words (m+2))
    (hB : ∀ s, B s = deriv (m+2) (W s) +
      ∑ i ∈ Finset.Ioc t (2*t), d s i • bracket (e s i) (F (2*t-i))) :
    (b*b) • bracket 0 V ∉
      LinearMap.range (deriv (m+2)) ⊔ Submodule.span ℚ (Set.range B) := by
  have hF := earlier_restrictions_vanish t b hb F G c n heq
  have hS := correction_span_killed t F hF W d e B hB
  have hQ := weighted_diagonal_nonzero p u q huq D V hD hhom hLie hdelta
  intro hmem
  have hz := hS hmem
  rw [LinearMap.mem_ker, map_smul, smul_eq_zero] at hz
  exact hz.elim (mul_ne_zero hb hb) hQ

end N8WeightedBlock

#print axioms N8WeightedBlock.weighted_block_separation

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8WeightedBlock.restrictWords_eq,
      ``N8WeightedBlock.multiplier_apply, ``N8WeightedBlock.restrict_deriv,
      ``N8WeightedBlock.restrict_bracket, ``N8WeightedBlock.weighted_diagonal_nonzero,
      ``N8WeightedBlock.earlier_restrictions_vanish,
      ``N8WeightedBlock.later_restrictions_vanish,
      ``N8WeightedBlock.correction_span_killed,
      ``N8WeightedBlock.weighted_block_separation] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 weighted word block separation"
