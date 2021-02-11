import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return np.sin(2*math.pi*.002*x)

def analytic_deriv(x):
    return (2*math.pi*.002)*np.cos(2*math.pi*.002*x)

def forward_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the forward
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x)
    denominator = h
    return numerator/denominator

def central_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the central
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x-h)
    denominator = 2*h
    return numerator/denominator

if __name__ == "__main__":
    #path_to_data = "/Users/mbottom/Desktop/teaching/computational_physics/assignments/2_derivatives/sinedata/sensor_position_data.txt" #obvsiouly change this to your directory
    oscillator_data = np.loadtxt('sensor_position_data.txt', skiprows=1, delimiter=',')
    #pulls out the first column (remember things start at 0 in python)
    oscillator_time = oscillator_data[:,0]
    oscillator_pos  = oscillator_data[:,1]
    timeList = oscillator_time.tolist()
    
    h = 0.01
    analytic = []
    forward = []
    central = []
    for time in timeList:
        analytic.append(analytic_deriv(time))
        forward.append(forward_difference(time, h, f))
        central.append(central_difference(time, h, f))

    plt.scatter(timeList, analytic, marker='.',color='red',label='Analytic')
    plt.scatter(timeList,forward,marker='.',color='blue',label='Forward')
    plt.scatter(timeList,central,marker='.',color='orange',label='Central')
    plt.title('Simple Harmonic Oscillator')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.show()



    
    
    
