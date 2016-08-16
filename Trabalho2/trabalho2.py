# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
from collections import deque

def rotula(img):
	contador = 0
	minX = []
	minY = []
	maxX = []
	maxY = []
	visitado = img < 255
	for x in range(0, img.shape[1]):
		for y in range(0, img.shape[0]):
			if not visitado[x, y]:
				contador += 1
				q = deque()
				q.append([x, y])
				aX, aY, bX, bY = vizinhos(img, q, contador, visitado)
				minX.append(aX)
				minY.append(aY)
				maxX.append(bX)
				maxY.append(bY)
	print "Há " + str(contador) + " elementos na imagem."
	return contador, minX, minY, maxX, maxY

def vizinhos(img, fila, contador, visitado):
	minX = float('Inf')
	minY = float('Inf')
	maxX = -1
	maxY = -1
	while fila:
		px = fila.popleft()
		x = px[0]
		y = px[1]
		if (x > 0 and x < img.shape[1] and y > 0 and y < img.shape[0]):
			if not visitado[x, y]:
				img[x, y] = 255 - contador * 10
				visitado[x, y] = True
				fila.append([x+1, y])
				fila.append([x-1, y])
				fila.append([x, y+1])
				fila.append([x, y-1])
				if x < minX: minX = x
				if y < minY: minY = y
				if x > maxX: maxX = x
				if y > maxY: maxY = y
	return minX, minY, maxX, maxY

def corte(img, minX, minY, maxX, maxY, i):
	return img[minX[i]:maxX[i], minY[i]:maxY[i]]	

#Abre Imagem
img = Image.open('entrada.png')

#Converte para tons de cinza
img = img.convert('L')
img = np.asarray(img, dtype="int32")

#Threshold para limitar a imagem em 2 tons de cinza
img[img > 127] = 255
img[img <= 127] = 0

cont, minX, minY, maxX, maxY = rotula(img)

#Pergunta ao usuário qual elemento cortar
a = input("Qual elemento deseja recortar? (Índices 0 a " + str(cont - 1) + ") ")
elemento = corte(img, minX, minY, maxX, maxY, a)

#Exporta a imagem do corte de acordo com o elemento escolhido
imgElemento = elemento.astype(np.uint8)
imgElementoOut = Image.fromarray(imgElemento)
imgElementoOut.save('corte'+str(a)+'.png')

#Exporta a imagem onde cada elemento tem um tom de cinza do mais claro para escuro de acordo com o momento de descobrimento
imgSaida = img.astype(np.uint8)
imgSaidaOut = Image.fromarray(imgSaida)
imgSaidaOut.save('rotulada.png')
