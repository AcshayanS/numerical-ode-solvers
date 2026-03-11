import numpy as np

def forward_euler(f, t0, y0, h, T):
    """
    Solves y' = f(t,y) using the Forward Euler method

    Parameters:
    f: function defining the ordinary differential equation
    t0: initial time
    y0: initial value
    h: stepsize
    T: final time

    Returns
    ts: list of time values
    ys: list of approximated solution values according to FE
    """

    ts = []
    ys = []
    t = t0
    y = y0

    N = int((T-t0)/h)   # number of steps based on time
    
    for n in range(N+1):    # include the final point T
        
        ts.append(t)
        ys.append(y.copy())

        if n < N:
            y = y + h*f(t,y)
            t = t + h

    return ts, ys

def rk4(f, t0, y0, h, T):
    """
    Solves y' = f(t,y) using the Runge-Kutta4 method

    Parameters:
    f: function defining the ordinary differential equation
    t0: initial time
    y0: initial value
    h: stepsize
    T: final time

    Returns
    ts: list of time values
    ys: list of approximated solution values according to RK4
    """

    ts = []
    ys = []
    t = t0
    y = y0

    N = int((T-t0)/h)

    for n in range(N+1):

        ts.append(t)
        ys.append(y.copy())

        if n < N:
            # Compute RK4 stage slopes
            k1 = f(t,y)
            k2 = f(t+h/2,y+h*k1/2)
            k3 = f(t+h/2,y+h*k2/2)
            k4 = f(t+h,y+h*k3)

            # Weighted average of slopes
            y = y + h/6*(k1+2*k2+2*k3+k4)
            t = t + h

    return ts, ys

def rk2(f, t0, y0, h, T):
    """
    Solves y' = f(t,y) using the Runge-Kutta2 method

    Parameters:
    f: function defining the ordinary differential equation
    t0: initial time
    y0: initial value
    h: stepsize
    T: final time

    Returns
    ts: list of time values
    ys: list of approximated solution values according to RK2
    """

    ts = []
    ys = []
    t = t0
    y = y0

    N = int((T-t0)/h)   # number of steps based on time
    
    for n in range(N+1):    # include the final point T
        
        ts.append(t)
        ys.append(y.copy())

        if n < N:
            k1 = f(t,y)
            k2 = f(t + h/2, y + h/2 * k1)
            y = y + h * k2
            t = t + h

    return ts, ys

def backward_euler_linear(t0, y0, h, T, A):
    """
    Solves y' = f(t,y) using the Backward Euler method, only works for linear functions

    Parameters:
    t0: initial time
    y0: initial value
    h: stepsize
    T: final time
    A: a constant matrix used in f(t,y)

    Returns
    ts: list of time values
    ys: list of approximated solution values according to Backward Euler
    """

    ts = []
    ys = []
    t = t0
    y = y0

    I = np.identity(len(y0))
    M = I - h*A        # constant matrix

    N = int((T-t0)/h)   # number of steps based on time
    
    for n in range(N+1):    # include the final point T
        
        ts.append(t)
        ys.append(y.copy())     

        if n < N:
            y = np.linalg.solve(M, y)
            t = t + h

    return ts, ys
