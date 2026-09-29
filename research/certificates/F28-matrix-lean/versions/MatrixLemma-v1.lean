import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic
import Lean.Util.CollectAxioms

/- An all-exponent lemma for the F28 candidate. No S5 theorem is imported. -/
namespace F28

abbrev Mat := Matrix (Fin 2) (Fin 2) ℤ

def Q : Mat := !![0, -1; 2, 1]

def coeff : ℕ → ℤ × ℤ
  | 0 => (0, 1)
  | n + 1 => ((coeff n).1 + (coeff n).2, -2 * (coeff n).1)

theorem power_formula (n : ℕ) :
    Q ^ n = !![(coeff n).2, -(coeff n).1;
      2 * (coeff n).1, (coeff n).1 + (coeff n).2] := by
  induction n with
  | zero =>
    ext i j
    fin_cases i <;> fin_cases j <;> norm_num [coeff]
  | succ n ih =>
    rw [pow_succ, ih]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Q, coeff, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

theorem coeff_parity (n : ℕ) :
    (coeff (n + 1)).1 % 2 = 1 ∧ (coeff (n + 1)).2 % 2 = 0 := by
  induction n with
  | zero => norm_num [coeff]
  | succ n ih =>
    simp only [coeff, Prod.fst, Prod.snd] at *
    omega

theorem coeff_nonzero (n : ℕ) : (coeff (n + 1)).1 ≠ 0 := by
  intro h
  have hp := (coeff_parity n).1
  rw [h] at hp
  norm_num at hp

theorem centralizer_shape (M : Mat) (n : ℕ)
    (h : M * Q ^ (n + 1) = Q ^ (n + 1) * M) :
    M 1 0 = -2 * M 0 1 ∧ M 1 1 = M 0 0 - M 0 1 := by
  have h00 := congrArg (fun X : Mat => X 0 0) h
  have h01 := congrArg (fun X : Mat => X 0 1) h
  rw [power_formula] at h00 h01
  simp [Matrix.mul_apply, Fin.sum_univ_two] at h00 h01
  have hleft : (coeff (n + 1)).1 * (2 * M 0 1 + M 1 0) = 0 := by
    nlinarith [h00]
  have hright : (coeff (n + 1)).1 * (-M 0 0 + M 0 1 + M 1 1) = 0 := by
    nlinarith [h01]
  have hl := (mul_eq_zero.mp hleft).resolve_left (coeff_nonzero n)
  have hr := (mul_eq_zero.mp hright).resolve_left (coeff_nonzero n)
  constructor <;> linarith

theorem determinant_one_periodic_is_scalar (M : Mat) (n : ℕ)
    (hdet : M.det = 1)
    (hcomm : M * Q ^ (n + 1) = Q ^ (n + 1) * M) :
    M = 1 ∨ M = -1 := by
  obtain ⟨hc, hd⟩ := centralizer_shape M n hcomm
  have heq : M 0 0 * M 1 1 - M 0 1 * M 1 0 = 1 := by
    simpa [Matrix.det_fin_two] using hdet
  rw [hc, hd] at heq
  have hnorm : (2 * M 0 0 - M 0 1)^2 + 7 * (M 0 1)^2 = 4 := by
    nlinarith [heq]
  have hb : M 0 1 = 0 := by
    by_contra hn
    have hpos : 0 < (M 0 1)^2 := sq_pos_of_ne_zero hn
    nlinarith [sq_nonneg (2 * M 0 0 - M 0 1)]
  have ha : (M 0 0 - 1) * (M 0 0 + 1) = 0 := by
    rw [hb] at heq
    nlinarith [heq]
  have hc0 : M 1 0 = 0 := by simpa [hb] using hc
  have hd0 : M 1 1 = M 0 0 := by simpa [hb] using hd
  rcases mul_eq_zero.mp ha with hpos | hneg
  · have ha1 : M 0 0 = 1 := by linarith
    left
    ext i j
    fin_cases i <;> fin_cases j <;> simp [ha1, hb, hc0, hd0]
  · have ha1 : M 0 0 = -1 := by linarith
    right
    ext i j
    fin_cases i <;> fin_cases j <;> simp [ha1, hb, hc0, hd0]

end F28

#print axioms F28.determinant_one_periodic_is_scalar

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for axiomName in ← collectAxioms ``F28.determinant_one_periodic_is_scalar do
    unless allowed.contains axiomName do
      throwError "Unexpected axiom {axiomName}"
  logInfo "PASS F28 all-exponent integer matrix lemma and axiom audit"
