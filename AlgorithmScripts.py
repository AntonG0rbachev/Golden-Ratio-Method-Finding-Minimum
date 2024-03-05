from math import sqrt
import numpy
import matplotlib.pyplot as plot


def goldenRatioMethod(interval, delta, function):
    print("step 1", interval, delta)
    x_min: float
    iterations = 0
    const = (3 - sqrt(5)) / 2
    y_k = interval[0] + const * (interval[1] - interval[0])
    z_k = sum(interval) - y_k
    print("step 2 k =", iterations, "\nstep 3 y_0 =", y_k, "z_0 = ", z_k)
    while abs(interval[0] - interval[1]) >= delta:
        iterations += 1
        if function(y_k) <= function(z_k):
            print("\nstep 4#", iterations, "f(y_k) =", function(y_k), "f(z_k) =", function(z_k))
            interval[1] = z_k
            z_k = y_k
            y_k = sum(interval) - y_k
            print("step 5.1#", iterations, " interval =", interval, "y_k+1 =", y_k, "z_k+1 =", z_k)
        elif function(y_k) > function(z_k):
            print("step 4#", iterations, " f(y_k) =", function(y_k), "f(z_k) =", function(z_k))
            interval[0] = y_k
            y_k = z_k
            z_k = sum(interval) - z_k
            print("step 5.2#", iterations, " interval =", interval, "y_k+1 =", y_k, "z_k+1 =", z_k)
        print("step 6#", iterations, "interval =", interval, "\n")
    else:
        x_min = (sum(interval)) / 2
    convergence = pow(0.618, iterations - 1)
    return ("x_min = " + str(x_min), "f(x_min) = " + str(function(x_min)), "interval = " + str(interval),
            "iterations = " + str(iterations), "convergence = " + str(convergence))


f = lambda argument: 2 * argument ** 2 - 2 * argument + 3 / 2
L = [-2, 8]
eps = 0.2
x = numpy.arange(L[0] - 1, L[1] + 1, 0.01)
plot.plot(x, f(x))
plot.show()
print(goldenRatioMethod(L, eps, f))
