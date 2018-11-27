import math

def newton(func, func_derivative, initial_guess, num_of_iterations):
    i = 0
    xi = initial_guess
    for i in range(0, num_of_iterations):
        xi_prev = xi
        xi = xi - (func(xi_prev) / func_derivative(xi_prev))

    return xi

f = lambda x : math.pow(math.e, x) - 2
f_der = lambda x: math.pow(math.e, x)

print(newton(f, f_der, 1, 10))
print(newton(f, f_der, 1, 100))
