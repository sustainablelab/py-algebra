import solve
x = solve.solve_ax_plus_b_eq_0([5,3])
print(f"x = {x}")
print()

roots = solve.solve_second_order([2,2,1])
print("Roots:")
for root in roots:
    print(root.as_factor())
print()
