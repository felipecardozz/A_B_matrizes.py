import numpy as np
from fractions import Fraction

T = np.array([
    [1, 0, 0, 0, 0, 0, 0],
    [0.5, 0, 0.5, 0, 0, 0, 0],
    [0, 0.5, 0, 0.5, 0, 0, 0],
    [0, 0, 0.5, 0, 0.5, 0, 0],
    [0, 0, 0, 0.5, 0, 0.5, 0],
    [0, 0, 0, 0, 0.5, 0, 0.5],
    [0, 0, 0, 0, 0, 0, 1]
])

D = np.array([0, 0, 0, 0, 1, 0, 0]) #valor inicial, A = +1, B = 0 

for _ in range(100): #loop de 100 rodadas
    D = np.dot(D, T)

chance_A_vencer = Fraction(D[6]).limit_denominator(
    max_denominator=3)

print("A Chance de A vencer é", chance_A_vencer) # chance_A_vencer = D[6] onde probabilidade de próxima rodada é 0
print("Já a chance de B vencer é ", D[0])        # a indexação em python tem origem em 0, ou seja D[0] = estado - 3
