import cv2
imagem = cv2.imread('ponte.jpg')#Cria um retangulo azul por toda a largura da imagem
imagem[30:50, :] = (255, 0, 0)#Cria um quadrado vermelho
imagem[100:150, 50:100] = (0, 0, 255)#Cria um retangulo amarelo por toda a altura da imagem
imagem[:, 200:220] = (0, 255, 255)#Cria um retangulo verde da linha 150 a 300 nas colunas 250 a 350
imagem[150:300, 250:350] = (0, 255, 0)#Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a 350
imagem[300:400, 50:150] = (255, 255, 0) #Cria um quadrado branco
imagem[250:350, 300:400] = (255, 255, 255) #Cria um quadrado preto
imagem[70:100, 300: 450] = (0, 0, 0) 
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0) # Espera pressionar qualquer tecla
cv2.imwrite("saida5.jpg", imagem)#salva a imagem modificada na pasta