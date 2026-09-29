import Kourovka.Paper
import Lean.Util.CollectAxioms

/- Independent scope check for GroupWorld A5. All mathematics proving
   enumeration belongs to Achyuth Jayadevan's prior development. -/
open Kourovka.MetabelianEnumeration

theorem gworld_A5_enumeration : REPred (fun m : ℕ =>
    let p := decodePresentation m
    (∀ w ∈ p.2, ∀ letter ∈ w, letter.1 < p.1) ∧
    ∀ a b c d : PresentedGroup {r | r ∈ p.2.map (interpretWord p.1)},
      (a * b * a⁻¹ * b⁻¹) * (c * d * c⁻¹ * d⁻¹) =
      (c * d * c⁻¹ * d⁻¹) * (a * b * a⁻¹ * b⁻¹)) :=
  Paper.metabelian_presentations_re

theorem gworld_A5_certificates : ∃ V : ℕ → ℕ → Bool,
    Primrec₂ V ∧ ∀ p : ℕ × List (List (ℕ × Bool)),
      ((∀ w ∈ p.2, ∀ letter ∈ w, letter.1 < p.1) ∧
        ∀ a b c d : PresentedGroup {r | r ∈ p.2.map (interpretWord p.1)},
          (a * b * a⁻¹ * b⁻¹) * (c * d * c⁻¹ * d⁻¹) =
          (c * d * c⁻¹ * d⁻¹) * (a * b * a⁻¹ * b⁻¹)) ↔
      ∃ c : ℕ, V (Encodable.encode p) c = true := by
  refine ⟨Paper.certificateCheck, Paper.certificateCheck_primrec, ?_⟩
  intro p
  simpa only [DefinesMetabelian, decode_encode_presentation] using
    Paper.metabelian_iff_certificate (Encodable.encode p)

#print gworld_A5_enumeration
#print gworld_A5_certificates
#print axioms gworld_A5_enumeration
#print axioms gworld_A5_certificates

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for name in #[``gworld_A5_enumeration, ``gworld_A5_certificates] do
    for axiomName in ← collectAxioms name do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName} in independent A5 restatement"
  logInfo "PASS: independent A5 statements and transitive axiom check"
