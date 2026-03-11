import matplotlib.pyplot as plt
import numpy as np
import os

def phase_portraits(fe_ys, rk4_ys, be_ys):
    """ Phase Portraits """
    # y1 vs y2
    y1_fe = [y[0] for y in fe_ys]
    y2_fe = [y[1] for y in fe_ys]

    y1_rk4 = [y[0] for y in rk4_ys]
    y2_rk4 = [y[1] for y in rk4_ys]

    y1_be = [y[0] for y in be_ys]
    y2_be = [y[1] for y in be_ys]

    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.plot(y1_fe, y2_fe, label="Forward Euler")
    plt.axis("equal")
    plt.xlabel("y1")
    plt.ylabel("y2")
    plt.title("Phase Portrait FE")
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(y1_rk4, y2_rk4, label="RK4")
    plt.plot(y1_be, y2_be, label="Backward Euler")

    plt.axis("equal")
    plt.xlabel("y1")
    plt.ylabel("y2")
    plt.title("Phase Portrait RK4 vs BE")
    plt.legend()

    plt.savefig(save_path_phase_portraits, dpi=300)
    plt.show()

def energy_plot(fe_ts, fe_ys, rk4_ts, rk4_ys, be_ts, be_ys):
    """ Energy Plot """
    energy_fe = []
    energy_rk4 = []
    energy_be = []

    for y in fe_ys:
        E = y[0]**2 + y[1]**2
        energy_fe.append(E)

    for y in rk4_ys:
        E = y[0]**2 + y[1]**2
        energy_rk4.append(E)

    for y in be_ys:
        E = y[0]**2 + y[1]**2
        energy_be.append(E)

    plt.plot(fe_ts, energy_fe, label="Energy Forward Euler")
    plt.plot(rk4_ts, energy_rk4, label="Energy RK4")
    plt.plot(be_ts, energy_be, label="Energy Backward Euler")

    plt.yscale("log")
    plt.xlabel("time")
    plt.ylabel("Energy")
    plt.title("Energy Plot")
    plt.legend()

    plt.savefig(save_path_energy_plot, dpi=300)
    plt.show()

script_dir = os.path.dirname(os.path.abspath(__file__))
save_path_phase_portraits = os.path.join(script_dir, "phase_portraits.png")
save_path_energy_plot = os.path.join(script_dir, "energy_plot.png")



