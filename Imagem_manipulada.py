import cv2
import numpy as np

# Carregar imagem
imagem = cv2.imread("jogo_de_damas.png")

# Verifica se carregou corretamente
if imagem is None:
    raise ValueError("Erro ao carregar a imagem. Verifique o caminho do arquivo.")

#1 reduzir em 30%
altura, largura = imagem.shape[:2]
nova_largura = int(largura * 0.7)
nova_altura = int(altura * 0.7)
escala = cv2.resize(imagem, (nova_largura, nova_altura), interpolation=cv2.INTER_AREA)

#2 Translação50px esquerda, 80px cima
tx, ty = -50, -80
M_trans = np.float32([[1, 0, tx], [0, 1, ty]])
translacao = cv2.warpAffine(imagem, M_trans, (largura, altura))

#3 Rotação 90° em torno do centro
centro = (largura // 2, altura // 2)
M_rot = cv2.getRotationMatrix2D(centro, 90, 1.0)
rotacao = cv2.warpAffine(imagem, M_rot, (largura, altura))

# Salvar resultados
cv2.imwrite("jogo_de_damas.png", escala)
cv2.imwrite("jogo_de_damas.png", translacao)
cv2.imwrite("jogo_de_damas.png", rotacao)

print("Transformações concluídas. As imagens foram salvas no mesmo diretório.")
