import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm  # para calcular a probabilidade exata

#media 100
media  = 100.0
#variancia 100
variancia = 100.0
#sigma pela raiz da variância
sigma = math.sqrt(variancia)

#limites do intervalo (P(X < 95)) 
limite = 95

#calcular (P(1 < X < 5)) usando a CDF (Função de Distribuição Acumulada)
probabilidade = norm.cdf(limite, media, sigma)

print(f"Para X ~ N(μ={media}, σ²={variancia}):")
print(f"P( X < {limite}) = {probabilidade:.4f}")
print(f"ou aproximadamente {probabilidade:.2%}")
print(f"Resposta com duas casas decimais: {probabilidade:.4f} → {probabilidade:.2f}")


# Criar eixo x (de 60 a 140, cobre bem μ ± 4σ)
x = np.linspace(media - 4*sigma, media + 4*sigma, 1000)

# Calcular a densidade para cada x
f = (1.0/(sigma * np.sqrt(2.0 * math.pi))) * np.exp(-0.5 * ((x - media)/sigma)**2.0)

# Criar a figura
plt.figure(figsize=(12, 6))

# Plotar a curva inteira
plt.plot(x, f, 'b-', linewidth=2, label=f'N(μ={media}, σ={sigma:.1f})')

# Preencher a área à esquerda de 95 (P(X < 95))
x_fill = np.linspace(media - 4*sigma, limite, 500)
f_fill = (1.0/(sigma * np.sqrt(2.0 * math.pi))) * np.exp(-0.5 * ((x_fill - media)/sigma)**2.0)
plt.fill_between(x_fill, 0, f_fill, color='red', alpha=0.4, 
                 label=f'P(X < {limite}) = {probabilidade:.4f}')

# Linhas verticais de referência
plt.axvline(media, color='black', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Média = {media}')
plt.axvline(limite, color='red', linestyle='-', linewidth=2, alpha=0.8, label=f'Limite = {limite}')

# Configurações do gráfico
plt.xlabel('x', fontsize=12)
plt.ylabel('Densidade de Probabilidade', fontsize=12)
plt.title(f'Distribuição Normal: P(X < {limite}) = {probabilidade:.4f}', fontsize=14)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3)

# Adicionar texto com o valor da probabilidade
plt.text(limite - 15, 0.015, f'Área = {probabilidade:.4f}\n(ou {probabilidade:.2%})', 
         fontsize=11, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()