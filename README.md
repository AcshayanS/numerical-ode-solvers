# Numerical ODE Solvers in Python
The project implements four numerical methods for solving ordinary differential equations and analyzes their behavior through numerical experiments on the harmonic oscillator. 

## Methods Implemented
- Forward Euler
- Backward Euler for linear systems
- Second-order Runge-Kutta (RK2)
- Forth-order Runge-Kutta (RK4)
## Experiments
### Convergence Study
The numerical convergence order was confirmed by computing the error at the final time for each numerical method while decreasing the step size. 
The following orders were observed:
- Forward Euler ≈ 1
- Backward Euler ≈ 1
- RK2 ≈ 2
- RK4 ≈ 4
### Phase Portraits
The phase portrait was plotted by graphing y1 against y2 instead of plotting the variables against time. For harmonic oscillators the exact solution traces a circle. The following behavior was observed from the numerical methods:
- Forward Euler’s trajectory spirals outwards
- Backward Euler’s trajectory spirals inwards
- RK4’s trajectory remains very close to a circle
### Energy Behavior
The numerical methods were applied to the harmonic oscillator and the energy drift over time was examined. 
- Forward Euler showed energy growth
- Backward Euler showed energy decay
- RK4 showed approximately stable energy for moderate time intervals
## Project Structure
```
main.py            - runs convergence study and experiments
solvers.py         - numerical ordinary equation solvers
convergence.py     - neccessity for convergence study
experiments.py     - phase portraits and energy experiments
```
## Run the code
Run the main script
```
python main.py
```
This generates:
- Convergence plots
- Phase portraits
- Energy plots
