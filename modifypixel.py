import cv2
imagem = cv2.imread('ponte.jpg')
for y in range(0, imagem.shape[0]):
 for x in range(0, imagem.shape[1]):
 	imagem[y, x] = (255,0,0)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)