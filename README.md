# numerical-ode-solvers

Numerical ODE Solvers & Error Convergence Analysis 

This project implements and analyzes numerical methods for solving ordinary differential equations of the form y' = f(t, y). The global error at the final time is computed for Forward Euler and RK4, and a log-log convergence plot is generated. The slopes correspond to first-order behavior for Forward Euler and fourth-order behavior for RK4, consistent with theoretical expectations.  
The implementation is validated using the test problem y’=y, with the exact solution exp(t). 
To run the program, install matplotlib and numpy. Then run main.py. The program generates and saves the convergence plot for both methods. 
    
