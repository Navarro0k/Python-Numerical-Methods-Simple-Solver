import math


def f(x):
    e = math.e
    return e**(-x) - x

def df(x):
    e = math.e
    return -e**(-x) - 1

def biseccion(f, a: float, b: float, tol: float, max_iter: int = 50):
    c_act = (a + b) / 2
    iteraciones = 0

    while True:
        if iteraciones >= max_iter:
            print("Se alcanzó el número máximo de iteraciones.")
            return

        iteraciones += 1

        if f(a) * f(c_act) < 0:
            b = c_act
        else:
            a = c_act

        c_ant = c_act
        c_act = (a + b) / 2

        ea = abs((c_act - c_ant) / c_act) * 100 if c_act != 0 else 0.0

        print(f"Iteración {iteraciones}: c = {c_act:.5f}, error aproximado = {ea:.4f}%")

        if ea <= tol:
            break

    return

def newton_raphson(f, df, x0: float, tol: float, max_iter: int = 50):
    x_act = x0
    iteraciones = 0

    while True:
        if iteraciones >= max_iter:
            print("Se alcanzó el número máximo de iteraciones.")
            return

        iteraciones += 1
        x_ant = x_act
        x_act = x_ant - f(x_ant) / df(x_ant)

        if x_act != 0:
            ea = abs((x_act - x_ant) / x_act) * 100
        else:
            ea = 0.0

        print(f"Iteración {iteraciones}: x = {x_act:.5f}, error aproximado = {ea:.4f}%")

        if ea <= tol:
            break

    return

print("\nMétodo de Bisección: \n")
biseccion(f, 0, 1, 0.0001)

print("\nMétodo de Newton-Raphson: \n")
newton_raphson(f, df, 0.5, 0.0001)
