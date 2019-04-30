import cv2
imagem = cv2.imread('ponte.jpg')#abrir a imagem e colocar na varialvel imagem
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB
print('O pixel (0, 0) tem as seguintes cores:')#pixel superior mais a esquerda é o (0,0)
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)#exibindo o pixel 0,0