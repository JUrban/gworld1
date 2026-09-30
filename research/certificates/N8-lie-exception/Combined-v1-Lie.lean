import Mathlib.Algebra.Lie.Subalgebra
import Mathlib.Algebra.Lie.OfAssociative
import Mathlib.Algebra.Polynomial.Coeff
import Lean.Util.CollectAxioms

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
  simpa [hm, Ne.symm hm] using hcoeff

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

end N8Lie

#print axioms N8Lie.lie_separation
#print axioms N8Lie.lie_separation_ne_one

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Lie.image_generator, ``N8Lie.generator_mem,
      ``N8Lie.image_lie_linear, ``N8Lie.scalar_power_exclusion,
      ``N8Lie.lie_separation, ``N8Lie.lie_separation_ne_one] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 generated Lie subalgebra exception"
