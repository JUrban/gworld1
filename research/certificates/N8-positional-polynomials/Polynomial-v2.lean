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

end N8Polynomial

#print axioms N8Polynomial.rational_polynomial_constant

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Polynomial.eval_delta, ``N8Polynomial.eval_bracket0,
      ``N8Polynomial.delta_equation, ``N8Polynomial.diagonal_equation,
      ``N8Polynomial.real_polynomial_constant, ``N8Polynomial.map_delta,
      ``N8Polynomial.map_bracket0, ``N8Polynomial.rational_polynomial_constant] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 rational positional polynomial constancy"
