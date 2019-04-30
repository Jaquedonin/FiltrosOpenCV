import numpy as np
import cv2
imagem = cv2.imread('ponte.jpg')
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'OpenCV',(550,40), fonte, 1,(100,159,200),2,cv2.LINE_AA)
cv2.imshow("Ponte", imagem)
cv2.waitKey(0) # Espera pressionar qualquer tecla
cv2.imwrite("saida5.jpg", imagem)#salva a imagem modificada na pasta