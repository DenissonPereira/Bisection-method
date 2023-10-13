from sympy import Symbol, sympify
import matplotlib.pyplot as plt
import numpy as np

funcao_x = input("Digite uma função: ")

x = Symbol('x')

funcao_simbolica = sympify(funcao_x)

a = float(input("DIgite o valor de a: "))
b = float(input("Digite o valor de b: "))
tol = float(input("Digite a tolerância: "))

def funcao(valor):
    return funcao_simbolica.subs(x, valor)

interacao = 1
while abs(b - a) / 2 > tol:
    m = (a + b) / 2
    f_m = funcao(m)
    if f_m == 0:
        break
    if funcao(a) * f_m < 0:
        b = m
    else:
        a = m
    interacao += 1

raiz = (a + b) / 2
print(raiz)

val_x = np.linspace(-1, 1, 100)
val_y = [funcao(valor) for valor in val_x]

plt.plot(val_x, val_y)
plt.xlabel("x")
plt.ylabel("f(X)")
plt.legend(["legenda"])
plt.grid(True)
plt.title("Título do gráfico", color='green' )
plt.show()