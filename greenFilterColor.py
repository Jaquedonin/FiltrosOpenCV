import cv2
imagem = cv2.imread('ponte.jpg')
for y in range(0, imagem.shape[0], 1): #percorre as linhas
 for x in range(0, imagem.shape[1], 1): #percorre as colunas
 	(b, g, r) = imagem[y, x] #Lê cada pixel de imagem e adiciona as cores nas variáveis
 	imagem[y, x] = (b%256,g%256,r%256) #Adiciona a imagem apenas o pixel de cor verde
cv2.imshow("Imagem modificada", imagem)
cv2.imwrite("saida7.jpg", imagem)#salva a imagem modificada na pasta
cv2.waitKey(0) # Espera pressionar qualquer tecla