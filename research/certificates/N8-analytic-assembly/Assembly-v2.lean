import Mathlib.Logic.Equiv.Fin.Rotate

/- Concatenated with the exact prior Bridge.lean and Energy.lean sources by
   the checker. This file closes their cyclic-coordinate interface. -/
namespace N8Assembly
open scoped BigOperators
open Fin.NatCast
variable {n : ℕ}

def shift (k : Fin (n+2)) (y : Fin (n+2) → ℝ) : Fin (n+2) → ℝ :=
  fun i => y (i+k)

theorem sum_shift (k : Fin (n+2)) (y : Fin (n+2) → ℝ) :
    (∑ i, shift k y i) = ∑ i, y i := Equiv.sum_comp (Equiv.addRight k) y

theorem rotate_eq_shift (y : Fin (n+2) → ℝ) : N8Bridge.rotate y = shift 1 y := by
  unfold N8Bridge.rotate
  rw [Fin.snoc_eq_cons_rotate]
  simp only [Fin.cons_self_tail, finRotate_succ_apply]
  rfl

theorem shift_add (k l : Fin (n+2)) (y : Fin (n+2) → ℝ) :
    shift (k+l) y = shift l (shift k y) := by
  funext i
  simp only [shift]
  congr 1
  abel

theorem shift_invariance (f : (Fin (n+2) → ℝ) → ℝ)
    (hrot : ∀ y, (∑ i, y i) = 0 → f (N8Bridge.rotate y) = f y)
    (k : Fin (n+2)) (y : Fin (n+2) → ℝ) (hy : (∑ i, y i) = 0) :
    f (shift k y) = f y := by
  have hn (m : ℕ) : f (shift (m : Fin (n+2)) y) = f y := by
    induction m with
    | zero => simpa [shift]
    | succ m ih =>
      rw [Nat.cast_add, Nat.cast_one, shift_add, ← rotate_eq_shift]
      rw [hrot _ (by rw [sum_shift, hy]), ih]
  simpa only [Fin.cast_val_eq_self] using hn k.val

theorem shift_half (k i j : Fin (n+2)) (y : Fin (n+2) → ℝ) :
    shift k (N8Energy.half i j y) =
      N8Energy.half (i-k) (j-k) (shift k y) := by
  change (Function.update (Function.update y i (y i/2)) j (y j+y i/2)) ∘
    (Equiv.addRight k) = _
  rw [Function.update_comp_equiv, Function.update_comp_equiv]
  simp only [Equiv.addRight_symm_apply, ← sub_eq_add_neg]
  change Function.update (Function.update (shift k y) (i-k) (y i/2))
    (j-k) (y j+y i/2) = _
  simp only [N8Energy.half, shift, sub_add_cancel]

theorem one_ne_zero : (1 : Fin (n+2)) ≠ 0 := by
  intro h
  have hv := congrArg Fin.val h
  norm_num [Fin.val_one, Nat.mod_eq_of_lt (show 1 < n+2 by omega)] at hv

theorem successor_ne (i : Fin (n+2)) : i ≠ i+1 := by
  intro h
  have hz : (1 : Fin (n+2)) = 0 := add_left_cancel (h.symm.trans (add_zero i).symm)
  exact one_ne_zero hz

theorem predecessor_ne (i : Fin (n+2)) : i ≠ i-1 := by
  intro h
  have hz : (1 : Fin (n+2)) = 0 := (sub_eq_self.mp h.symm)
  exact one_ne_zero hz

theorem successor_cycle (i j : Fin (n+2)) :
    ∃ k : ℕ, (fun x : Fin (n+2) => x+1)^[k] i = j := by
  refine ⟨(j-i).val, ?_⟩
  rw [add_right_iterate_apply]
  change i + ((j-i).val : Fin (n+2)) = j
  rw [Fin.cast_val_eq_self]
  abel

theorem last_eq_neg_one : (Fin.last (n+1) : Fin (n+2)) = -1 :=
  eq_neg_of_add_eq_zero_left (Fin.last_add_one (n+1))

theorem clockwise_eq_half (y : Fin (n+2) → ℝ) :
    N8Bridge.clockwise y = N8Energy.half 0 1 y := by
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · simp [N8Bridge.clockwise, N8Energy.half, one_ne_zero.symm]
  · refine Fin.cases ?_ (fun k => ?_) j
    · simp [N8Bridge.clockwise, N8Bridge.shiftFirst, N8Energy.half, Fin.tail]
    · have h0 : k.succ.succ ≠ (0 : Fin (n+2)) := Fin.succ_ne_zero _
      have h1 : k.succ.succ ≠ (1 : Fin (n+2)) := by
        intro h
        have hv := congrArg Fin.val h
        simp only [Fin.val_succ, Fin.val_one] at hv
        omega
      simp [N8Bridge.clockwise, N8Bridge.shiftFirst, N8Energy.half,
        Function.update_of_ne h1, Fin.tail]

theorem counterclockwise_eq_half (y : Fin (n+2) → ℝ) :
    N8Bridge.counterclockwise y = N8Energy.half 0 (-1) y := by
  rw [← last_eq_neg_one]
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · have hlast : (0 : Fin (n+2)) ≠ Fin.last (n+1) := by
      intro h; have := congrArg Fin.val h; simp at this
    simp [N8Bridge.counterclockwise, N8Energy.half, hlast]
  · refine Fin.lastCases ?_ (fun k => ?_) j
    · simp [N8Bridge.counterclockwise, N8Bridge.shiftLast, N8Energy.half, Fin.tail]
    · have h0 : k.castSucc.succ ≠ (0 : Fin (n+2)) := Fin.succ_ne_zero _
      have hl : k.castSucc.succ ≠ (Fin.last (n+1) : Fin (n+2)) := by
        intro h; have hv := congrArg Fin.val h
        change k.val+1 = n+1 at hv
        omega
      simp [N8Bridge.counterclockwise, N8Bridge.shiftLast, N8Energy.half,
        Fin.tail, Fin.init]

theorem all_index_average (f : (Fin (n+2) → ℝ) → ℝ)
    (hrot : ∀ y, (∑ i, y i) = 0 → f (N8Bridge.rotate y) = f y)
    (hmean0 : ∀ y, (∑ i, y i) = 0 →
      2*f y = f (N8Energy.half 0 1 y) + f (N8Energy.half 0 (-1) y))
    (i : Fin (n+2)) (y : Fin (n+2) → ℝ) (hy : (∑ j, y j) = 0) :
    2*f y = f (N8Energy.half i (i+1) y) + f (N8Energy.half i (i-1) y) := by
  have hs := hmean0 (shift i y) (by rw [sum_shift, hy])
  have ha : shift i (N8Energy.half i (i+1) y) = N8Energy.half 0 1 (shift i y) := by
    rw [shift_half]; simp
  have hb : shift i (N8Energy.half i (i-1) y) = N8Energy.half 0 (-1) (shift i y) := by
    rw [shift_half]
    have he : (i-1)-i = (-1 : Fin (n+2)) := by abel
    rw [sub_self, he]
  have hza : (∑ j, N8Energy.half i (i+1) y j) = 0 := by
    rw [N8Energy.half_sum i (i+1) (successor_ne i), hy]
  have hzb : (∑ j, N8Energy.half i (i-1) y j) = 0 := by
    rw [N8Energy.half_sum i (i-1) (predecessor_ne i), hy]
  rw [shift_invariance f hrot i y hy, ← ha, ← hb,
    shift_invariance f hrot i _ hza, shift_invariance f hrot i _ hzb] at hs
  exact hs

theorem positive_dimension_positional_constant (P : (Fin (n+1) → ℝ) → ℝ)
    (V : (Fin (n+2) → ℝ) → ℝ) (hP : Continuous P)
    (hdelta : N8Bridge.DeltaEquation P V) (hdiag : N8Bridge.DiagonalZero V) :
    ∀ z, P z = P 0 := by
  let f : (Fin (n+2) → ℝ) → ℝ := fun y => P (Fin.tail y)
  have hf : Continuous f := hP.comp (by fun_prop)
  have hrot : ∀ y, (∑ i, y i) = 0 → f (N8Bridge.rotate y) = f y := by
    intro y hy
    exact N8Bridge.cyclic_invariance P V hdelta y hy
  have hm0 : ∀ y, (∑ i, y i) = 0 →
      2*f y = f (N8Energy.half 0 1 y) + f (N8Energy.half 0 (-1) y) := by
    intro y hy
    have h := N8Bridge.origin_average P V hdelta hdiag y hy
    rwa [clockwise_eq_half, counterclockwise_eq_half] at h
  have hc := N8Energy.hyperplane_harmonic_constant
    (fun i : Fin (n+2) => i+1) (fun i : Fin (n+2) => i-1)
    successor_ne predecessor_ne successor_cycle f hf (all_index_average f hrot hm0)
  intro z
  have hz : (∑ i, (Fin.cons (-(∑ j, z j)) z) i) = 0 := by rw [Fin.sum_cons]; ring
  have h := hc (Fin.cons (-(∑ j, z j)) z) hz
  simpa only [f, Fin.tail_cons] using h

theorem positional_constant {m : ℕ} (P : (Fin m → ℝ) → ℝ)
    (V : (Fin (m+1) → ℝ) → ℝ) (hP : Continuous P)
    (hdelta : N8Bridge.DeltaEquation P V) (hdiag : N8Bridge.DiagonalZero V) :
    ∀ z, P z = P 0 := by
  cases m with
  | zero => intro z; congr 1; exact Subsingleton.elim _ _
  | succ n => exact positive_dimension_positional_constant P V hP hdelta hdiag

end N8Assembly

#print axioms N8Assembly.positional_constant

open Lean in
run_cmd do
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  for declarationName in #[``N8Assembly.sum_shift, ``N8Assembly.rotate_eq_shift,
      ``N8Assembly.shift_add, ``N8Assembly.shift_invariance, ``N8Assembly.shift_half,
      ``N8Assembly.one_ne_zero, ``N8Assembly.successor_ne, ``N8Assembly.predecessor_ne,
      ``N8Assembly.successor_cycle, ``N8Assembly.last_eq_neg_one,
      ``N8Assembly.clockwise_eq_half, ``N8Assembly.counterclockwise_eq_half,
      ``N8Assembly.all_index_average, ``N8Assembly.positive_dimension_positional_constant,
      ``N8Assembly.positional_constant] do
    for axiomName in ← collectAxioms declarationName do
      unless allowed.contains axiomName do
        throwError "Unexpected axiom {axiomName}"
  logInfo "PASS N8 assembled positional identities imply constancy"
