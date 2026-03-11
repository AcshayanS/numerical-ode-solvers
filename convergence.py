# Imports forward_euler and rk4 from solvers.py
from solvers import forward_euler, rk4, rk2, backward_euler_linear
import numpy as np

def run_convergence(f, exact_solution, t0, y0, T, hs, A):
    # List of convergence errors for different solvers

    fe_errors = []
    rk4_errors = []
    rk2_errors = []
    be_errors = []

    for h in hs:
        _, ys_fe = forward_euler(f, t0, y0, h, T)
        _, ys_rk4 = rk4(f, t0, y0, h, T)
        _, ys_rk2 = rk2(f, t0, y0, h, T)
        _, ys_be = backward_euler_linear(t0, y0, h, T, A)

        fe_errors.append(np.linalg.norm(ys_fe[-1] - exact_solution(T)))
        rk4_errors.append(np.linalg.norm(ys_rk4[-1] - exact_solution(T)))
        rk2_errors.append(np.linalg.norm(ys_rk2[-1] - exact_solution(T)))
        be_errors.append(np.linalg.norm(ys_be[-1] - exact_solution(T)))

    return fe_errors, rk4_errors, rk2_errors, be_errors