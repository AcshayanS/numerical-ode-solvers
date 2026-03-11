from convergence import run_convergence
from solvers import forward_euler, rk4, backward_euler_linear
from experiments import phase_portraits, energy_plot
import math
import matplotlib.pyplot as plt
import numpy as np
import os

def f(t,y):
    # Matrix multiplication
    return A.dot(y)

def exact_solution(t):
    return np.array([math.cos(t), -math.sin(t)])

def convergence_study(fe_errors, rk4_errors, rk2_errors, be_errors):
    """Convergence Study"""
    p_fe = []
    p_rk4 = []
    p_rk2 = []
    p_be = []

    for i in range(len(fe_errors)-1):
        p_fe.append(np.log2(fe_errors[i]/fe_errors[i+1]))

    for i in range(len(rk4_errors)-1):
        p_rk4.append(np.log2(rk4_errors[i]/rk4_errors[i+1]))

    for i in range(len(rk2_errors)-1):
        p_rk2.append(np.log2(rk2_errors[i]/rk2_errors[i+1]))

    for i in range(len(be_errors)-1):
        p_be.append(np.log2(be_errors[i]/be_errors[i+1]))

    return p_fe, p_rk4, p_rk2, p_be

script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, "convergence.png")

t0 = 0
y0 = np.array([1.0, 0.0])
T = 1
hs = [0.2, 0.1, 0.05, 0.025, 0.0125]
A = np.array([[0, 1], [-1, 0]])

# Will not execute unless it is main.py
if __name__ == "__main__":
    
    fe_errors, rk4_errors, rk2_errors, be_errors = run_convergence(f, exact_solution, t0, y0, T, hs, A)

    # -- Plotting --
    plt.loglog(hs, fe_errors, "o-", label="Forward Euler, order ≈ 1")
    plt.loglog(hs, rk4_errors, "o-", label="RK4, order ≈ 4")
    plt.loglog(hs, rk2_errors, "o-", label="RK2, order ≈ 2")
    plt.loglog(hs, be_errors, "o--", label="Backward Euler, order ≈ 1")

    plt.xlabel("Step size h")
    plt.ylabel("Error at T")
    plt.title("Convergence Plot")
    plt.legend()
    plt.grid(True, which="major")

    plt.savefig(save_path, dpi=300)
    plt.show()

    p_fe, p_rk4, p_rk2, p_be = convergence_study(fe_errors, rk4_errors, rk2_errors, be_errors)

    print("forward euler", p_fe)
    print("rk4", p_rk4)
    print("rk2", p_rk2)
    print("backward euler", p_be)

    h = 0.1
    T = 100     # We want to check for higher values of time T

    fe_ts, fe_ys = forward_euler(f, t0, y0, h, T)
    rk4_ts, rk4_ys = rk4(f, t0, y0, h, T)
    be_ts, be_ys = backward_euler_linear(t0, y0, h, T, A)

    phase_portraits(fe_ys, rk4_ys, be_ys)
    energy_plot(fe_ts, fe_ys, rk4_ts, rk4_ys, be_ts, be_ys)
