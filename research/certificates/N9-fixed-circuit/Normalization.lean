import Mathlib.Algebra.Group.Int.Units
import Mathlib.Tactic
import Lean.Util.CollectAxioms

/- The integer normalization step only. No group or DPRM theorem is imported. -/
namespace N9

theorem integral_normalization (n p d x w t : ℤ)
    (ht : t = 3*n+1) (hx : x = 3*p)
    (hpf : d*w = x*x) (haff : t*d-x = 1) : d = 1 ∧ p = n := by
  have hxx : x = t*d-1 := by linarith
  have hu : d*(w-t^2*d+2*t) = 1 := by
    rw [hxx] at hpf
    nlinarith [hpf]
  rcases Int.eq_one_or_neg_one_of_mul_eq_one hu with hd | hd
  · subst d
    constructor
    · rfl
    · nlinarith [ht, hx, haff]
  · subst d
    omega

theorem normalization_iff (n p : ℤ) :
    (∃ d w : ℤ, d*w = (3*p)^2 ∧ (3*n+1)*d-3*p = 1) ↔ p = n := by
  constructor
  · rintro ⟨d, w, hp, ha⟩
    exact (integral_normalization n p d (3*p) w (3*n+1)
      rfl rfl (by nlinarith [hp]) ha).2
  · intro h
    subst p
    refine ⟨1, (3*n)^2, ?_, ?_⟩ <;> ring

theorem wedge_pfaffian (a b c d e f g h : ℤ) :
    (a*d-b*c)*(e*h-f*g) - (a*f-b*e)*(c*h-d*g)
      + (a*h-b*g)*(c*f-d*e) = 0 := by ring

theorem rank_chart_product (muv x y z : ℤ)
    (hpf : 1*muv-0*0+y*(-x) = 0) (hgate : muv = z) : z = x*y := by
  nlinarith [hpf, hgate]

end N9

#print axioms N9.integral_normalization
#print axioms N9.normalization_iff
#print axioms N9.wedge_pfaffian
#print axioms N9.rank_chart_product

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N9.integral_normalization, ``N9.normalization_iff,
      ``N9.wedge_pfaffian, ``N9.rank_chart_product] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N9 universal integer normalization and axiom audit"
