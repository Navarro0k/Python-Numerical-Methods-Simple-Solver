def f(x):
     return x**3 - x - 2

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

biseccion(f,1,2,0.0001)

