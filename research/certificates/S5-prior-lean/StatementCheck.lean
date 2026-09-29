import Kourovka.CentralHopfian
import Lean.Util.CollectAxioms

/- Independent restatement of the frozen GroupWorld S5 question.
   The proof is entirely Jayadevan's prior theorem, not a new result. -/
universe u v

theorem gworld_S5 (A : Type u) (B : Type v) [Group A] [Group B]
    [Group.FG A] [Group.FG B] [IsSolvable A] [IsSolvable B]
    (hA : ∀ f : A →* A, Function.Surjective f → Function.Injective f)
    (hB : ∀ f : B →* B, Function.Surjective f → Function.Injective f) :
    ∀ f : A × B →* A × B, Function.Surjective f → Function.Injective f :=
  Kourovka.directProduct_isHopfian hA hB

#print gworld_S5
#print Group.FG
#print IsSolvable
#print axioms gworld_S5

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for axiomName in ← collectAxioms ``gworld_S5 do
    unless allowed.contains axiomName do
      throwError "Unexpected axiom {axiomName} in independent S5 restatement"
  logInfo "PASS: independent S5 statement and transitive axiom check"
