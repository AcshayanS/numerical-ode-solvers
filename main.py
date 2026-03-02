from convergence import run_convergence
import math
import matplotlib.pyplot as plt
import numpy as np
import os

def f(t,y):
    return y

def exact_solution(t):
    return math.exp(t)

script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, "convergence.png")

t0 = 0
y0 = 1
T = 1
hs = [0.2, 0.1, 0.05, 0.025, 0.0125]

# Will not execute unless it is main.py
if __name__ == "__main__":
    fe_errors, rk4_errors = run_convergence(f, exact_solution, t0, y0, T, hs)

    print(fe_errors)
    print(rk4_errors)

    h_ref = hs[-1]

    # Calculating the coefficient for Forward Euler
    error_ref_fe = fe_errors[-1]
    p_fe = 1
    C_fe = error_ref_fe/ (h_ref**p_fe)

    # Calculating the coefficient for RK4
    error_ref_rk4 = rk4_errors[-1]
    p_rk4 = 4
    C_rk4 = error_ref_rk4/ (h_ref**p_rk4)

    # Reference lines
    fe_reference = [C_fe*i**p_fe for i in hs]
    rk4_reference = [C_rk4*j**p_rk4 for j in hs]

    # -- Plotting --
    plt.loglog(hs, fe_errors, "o-", label="Forward Euler")
    plt.loglog(hs, rk4_errors, "s-", label="RK4")
    plt.loglog(hs, fe_reference, "--", label="Convergence Order 1")
    plt.loglog(hs, rk4_reference, "--", label="Convergence Order 4")

    plt.xlabel("Step size h")
    plt.ylabel("Error at T")
    plt.title("Convergence Plot")
    plt.legend()
    plt.grid(True, which="major")

    plt.savefig(save_path, dpi=300)
    plt.show()

