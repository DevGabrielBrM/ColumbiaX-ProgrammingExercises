import numpy as np
from matplotlib import pyplot as plt 

# Carregar a chave e a imagem
key = np.load('key.npy')
img = plt.imread('secret.bmp')

# Configurar NumPy para exibir mais linhas e colunas
np.set_printoptions(threshold=np.inf)  # Exibir a matriz completa

# Exibir a matriz completa da imagem
print(img)
