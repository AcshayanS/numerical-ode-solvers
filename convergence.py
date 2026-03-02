# Imports forward_euler and rk4 from solvers.py
from solvers import forward_euler, rk4

def run_convergence(f, exact_solution, t0, y0, T, hs):
    
    fe_errors = []
    rk4_errors = []

    for h in hs:
        _, ys_fe = forward_euler(f, t0, y0, h, T)
        _, ys_rk4 = rk4(f, t0, y0, h, T)

        fe_errors.append(abs(ys_fe[-1] - exact_solution(T)))
        rk4_errors.append(abs(ys_rk4[-1] - exact_solution(T)))

    return fe_errors, rk4_errors