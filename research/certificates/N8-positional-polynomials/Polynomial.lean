import Mathlib.Algebra.MvPolynomial.Funext
import Mathlib.Topology.Algebra.MvPolynomial
import Mathlib.Data.Real.Basic
import Lean.Util.CollectAxioms

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
