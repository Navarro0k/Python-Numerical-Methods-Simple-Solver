def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

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

newton_raphson(f, df, 1.5, 0.0001)
