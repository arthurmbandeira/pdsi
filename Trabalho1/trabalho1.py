# -*- coding: utf-8 -*-
"""
Created on Fri May 13 20:13:54 2016

@author: arthur
"""
from PIL import Image
import numpy as np

valMax = 255.0
#Abre Imagem
lenna = Image.open('lenna.png')

#Transforma imagem em matriz
lenna = np.asarray(lenna, dtype="int32")

#Deixa de ponta-cabeça e exporta
lennaUD = lenna[::-1,::-1]
lennaUD = lennaUD.astype(np.uint8)
lennaUDOut = Image.fromarray(lennaUD)
lennaUDOut.save('out-ud.png')

#Replica em 2 na altura e 3 no comprimento e exporta
lennaTile = np.tile(lennaUD, (2,3))
lennaUDTile = lennaTile.astype(np.uint8)
lennaUDTileOut = Image.fromarray(lennaUDTile)
lennaUDTileOut.save('out-ud-tile.png')

#Faz o gradiente e exporta
def gradiente(img, nivel):
	u = img.shape[0]
	for i in range(img.shape[0]):
		u -= nivel
		for j in range(img.shape[1]):
			img[i][j] *= (((i/2+j/2)/u/2))
	gradient = img.astype(np.uint8)
	gradientOut = Image.fromarray(gradient)
	gradientOut.save('out-ud-tile-grad.png')

#lennaUDTileContrast
def contraste(img, nivel):
	contrast = (valMax)*(img/(valMax))**nivel
	contrast = contrast.astype(np.uint8)
	contrastOut = Image.fromarray(contrast)
	contrastOut.save('out-ud-tile-contrast.png')

#Passar nível de contraste: menor para mais claro, maior para mais escuro
contraste(lennaTile, 0.5)
#Passar nível de gradiente (< 1): maior para mais claro, menor para mais escuro
gradiente(lennaTile, 0.5)