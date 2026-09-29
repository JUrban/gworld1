import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Int.Interval
import Mathlib.Data.Fintype.Pigeonhole
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
    simp only [coeff] at *
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

/- The positive integral energy avoids spectral theory and real norm arguments. -/
def energy (M : Mat) : ℤ :=
  (8 * M 0 0 - 4 * M 0 1 + 2 * M 1 0 - M 1 1)^2 +
  7 * (4 * M 0 1 + M 1 1)^2 +
  7 * (2 * M 1 0 - M 1 1)^2 + 49 * (M 1 1)^2

theorem energy_nonneg (M : Mat) : 0 ≤ energy M := by
  unfold energy
  positivity

theorem energy_step (M N : Mat) (h : N * Q = Q * M) :
    energy N = energy M := by
  have h00 := congrArg (fun X : Mat => X 0 0) h
  have h01 := congrArg (fun X : Mat => X 0 1) h
  have h10 := congrArg (fun X : Mat => X 1 0) h
  have h11 := congrArg (fun X : Mat => X 1 1) h
  simp [Q, Matrix.mul_apply, Fin.sum_univ_two] at h00 h01 h10 h11
  have hc : M 1 0 = -2 * N 0 1 := by linarith
  have ha : M 0 0 = N 1 1 + N 0 1 := by linarith
  have hna : N 0 0 = N 0 1 + M 1 1 := by linarith
  have hnc : N 1 0 = N 1 1 - 2 * M 0 1 - M 1 1 := by linarith
  unfold energy
  rw [hc, ha, hna, hnc]
  ring

theorem integer_bound (x E : ℤ) (h : x^2 ≤ E) : -E ≤ x ∧ x ≤ E := by
  have hx := Int.le_self_sq x
  have hn := Int.le_self_sq (-x)
  constructor <;> nlinarith

theorem entry_bound (M : Mat) (i j : Fin 2) :
    -energy M ≤ M i j ∧ M i j ≤ energy M := by
  have hE := energy_nonneg M
  have hA : (8 * M 0 0 - 4 * M 0 1 + 2 * M 1 0 - M 1 1)^2 ≤ energy M := by
    unfold energy
    nlinarith [sq_nonneg (4 * M 0 1 + M 1 1),
      sq_nonneg (2 * M 1 0 - M 1 1), sq_nonneg (M 1 1)]
  have hB : (4 * M 0 1 + M 1 1)^2 ≤ energy M := by
    unfold energy
    nlinarith [sq_nonneg (8 * M 0 0 - 4 * M 0 1 + 2 * M 1 0 - M 1 1),
      sq_nonneg (4 * M 0 1 + M 1 1),
      sq_nonneg (2 * M 1 0 - M 1 1), sq_nonneg (M 1 1)]
  have hC : (2 * M 1 0 - M 1 1)^2 ≤ energy M := by
    unfold energy
    nlinarith [sq_nonneg (8 * M 0 0 - 4 * M 0 1 + 2 * M 1 0 - M 1 1),
      sq_nonneg (4 * M 0 1 + M 1 1),
      sq_nonneg (2 * M 1 0 - M 1 1), sq_nonneg (M 1 1)]
  have hD : (M 1 1)^2 ≤ energy M := by
    unfold energy
    nlinarith [sq_nonneg (8 * M 0 0 - 4 * M 0 1 + 2 * M 1 0 - M 1 1),
      sq_nonneg (4 * M 0 1 + M 1 1),
      sq_nonneg (2 * M 1 0 - M 1 1), sq_nonneg (M 1 1)]
  obtain ⟨hAl, hAu⟩ := integer_bound _ _ hA
  obtain ⟨hBl, hBu⟩ := integer_bound _ _ hB
  obtain ⟨hCl, hCu⟩ := integer_bound _ _ hC
  obtain ⟨hDl, hDu⟩ := integer_bound _ _ hD
  fin_cases i <;> fin_cases j <;> dsimp <;> constructor <;> linarith

theorem Q_left_cancel (M N : Mat) (h : Q * M = Q * N) : M = N := by
  ext i j
  have h0 := congrArg (fun X : Mat => X 0 j) h
  have h1 := congrArg (fun X : Mat => X 1 j) h
  simp [Q, Matrix.mul_apply, Fin.sum_univ_two] at h0 h1
  fin_cases i <;> dsimp <;> linarith

/-- Every infinite integral forward orbit under conjugation by Q, starting
    at a determinant-one matrix, starts at I or -I. No boundedness hypothesis. -/
theorem integral_orbit_is_scalar (orbit : ℕ → Mat)
    (hdet : (orbit 0).det = 1)
    (step : ∀ n, orbit (n + 1) * Q = Q * orbit n) :
    orbit 0 = 1 ∨ orbit 0 = -1 := by
  have econst : ∀ n, energy (orbit n) = energy (orbit 0) := by
    intro n
    induction n with
    | zero => rfl
    | succ n ih => exact (energy_step _ _ (step n)).trans ih
  let E := energy (orbit 0)
  let enc : ℕ → (Fin 2 → Fin 2 → Set.Icc (-E) E) := fun n i j =>
    ⟨orbit n i j, by simpa only [econst n] using entry_bound (orbit n) i j⟩
  obtain ⟨i, j, hne, heq⟩ := Finite.exists_ne_map_eq_of_infinite enc
  have heq' : orbit i = orbit j := by
    ext a b
    exact congrArg Subtype.val (congrFun (congrFun heq a) b)
  have hrepeat : ∃ i k, 0 < k ∧ orbit i = orbit (i + k) := by
    rcases lt_or_gt_of_ne hne with hlt | hgt
    · refine ⟨i, j - i, by omega, ?_⟩
      simpa only [Nat.add_sub_of_le (Nat.le_of_lt hlt)] using heq'
    · refine ⟨j, i - j, by omega, ?_⟩
      simpa only [Nat.add_sub_of_le (Nat.le_of_lt hgt)] using heq'.symm
  have descend : ∀ i k, orbit i = orbit (i + k) → orbit 0 = orbit k := by
    intro i
    induction i with
    | zero => intro k h; simpa using h
    | succ i ih =>
      intro k h
      apply ih k
      apply Q_left_cancel
      rw [← step i, ← step (i + k)]
      simpa only [Nat.succ_eq_add_one, Nat.add_assoc, Nat.add_comm,
        Nat.add_left_comm] using congrArg (fun M : Mat => M * Q) h
  have intertwine : ∀ n, orbit n * Q^n = Q^n * orbit 0 := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
      calc
        orbit (n + 1) * Q^(n + 1) = (orbit (n + 1) * Q) * Q^n := by
          rw [pow_succ', mul_assoc]
        _ = (Q * orbit n) * Q^n := by rw [step n]
        _ = Q * (orbit n * Q^n) := mul_assoc _ _ _
        _ = Q * (Q^n * orbit 0) := by rw [ih]
        _ = Q^(n + 1) * orbit 0 := by rw [pow_succ', mul_assoc]
  obtain ⟨i, k, hk, hr⟩ := hrepeat
  have hreturn := descend i k hr
  have hcomm := intertwine k
  rw [← hreturn] at hcomm
  have hk1 : k = (k - 1) + 1 := by omega
  apply determinant_one_periodic_is_scalar (orbit 0) (k - 1) hdet
  simpa only [hk1] using hcomm

end F28

#print axioms F28.determinant_one_periodic_is_scalar
#print axioms F28.integral_orbit_is_scalar

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for axiomName in ← collectAxioms ``F28.integral_orbit_is_scalar do
    unless allowed.contains axiomName do
      throwError "Unexpected axiom {axiomName}"
  logInfo "PASS F28 all-exponent integer matrix lemma and axiom audit"
