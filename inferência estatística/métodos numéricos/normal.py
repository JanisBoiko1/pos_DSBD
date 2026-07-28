import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm  # para calcular a probabilidade exata

#media 2.0
media  = 2.0
#variancia 5.0
variancia = 5.0
#sigma pela raiz da variância
sigma = math.sqrt(variancia)

#limites do intervalo (P(1 < X < 5)) 
a , b = 1 , 5

#calcular (P(1 < X < 5)) usando a CDF (Função de Distribuição Acumulada)
probabilidade = norm.cdf(b, media, sigma) - norm.cdf(a, media, sigma)

print(f"Para X ~ N(μ={media}, σ²={variancia}):")
print(f"P({a} < X < {b}) = {probabilidade:.6f}")
print(f"ou aproximadamente {probabilidade:.4%}")


#gerar pontos espaçados linearmente
x = np.linspace(media - 4*sigma, media + 4*sigma, 1000)
f = norm.pdf(x, media, sigma)  # função densidade de probabilidade

# Preencher a área do intervalo
x_fill = np.linspace(a, b, 100)
f_fill = norm.pdf(x_fill, media, sigma)
plt.fill_between(x_fill, 0, f_fill, color='red', alpha=0.3, label=f'P({a}<X<{b}) = {probabilidade:.4f}')

plt.xlabel('x')
plt.ylabel('Densidade')
plt.title(f'Distribuição Normal: P({a} < X < {b})')
plt.axvline(media, color='black', linestyle='--', alpha=0.5, label=f'Média = {media}')
plt.axvline(a, color='red', linestyle=':', alpha=0.5)
plt.axvline(b, color='red', linestyle=':', alpha=0.5)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()