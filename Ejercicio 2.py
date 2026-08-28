def g(x):
    base = x - 2
    if base < 0:
        return -((-base) ** (1/3))
    else:
        return base ** (1/3)

def puntoFijo(g, x0: float, tol: float, max_iter: int = 50):
    xi = x0
    iteraciones = 0

    while True:
        if iteraciones >= max_iter:
            print("Se alcanzó el número máximo de iteraciones.")
            return

        iteraciones += 1
        xu = xi
        xi = g(xu)
        
        if xi != 0:
            ea = abs((xi - xu) / xi) * 100
        else:
            ea = 0.0

        print(f"Iteración {iteraciones}: x = {xi:.5f}, error aproximado = {ea:.4f}%")

        if ea <= tol:
            break

    return

puntoFijo(g, 1.5, 0.0001)
