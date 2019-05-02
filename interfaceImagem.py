
# Simple enough, just import everything from tkinter.
from tkinter import *

from PIL import Image, ImageTk

import cv2

import numpy as np


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
        self.showImg("Kanban-menor.png")

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #Button gray filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Gray"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filterGray
        self.autenticar.pack(side=RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Green"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filterGreen
        self.autenticar.pack(side=RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro 2d"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filter2D
        self.autenticar.pack(side=RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Blur"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filterBlur
        self.autenticar.pack(side=RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "FiltroGaussian"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filterGaussianBlur
        self.autenticar.pack(side=RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Menian"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filterMedian
        self.autenticar.pack(side=RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Bilateral"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filterBilateral
        self.autenticar.pack(side=RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Blue"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filterBlue
        self.autenticar.pack(side=RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Red"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.filterRed
        self.autenticar.pack(side=RIGHT)

    def showImg(self, image):
        load = Image.open(image)
        render = ImageTk.PhotoImage(load)
        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def filterGray(self):
        img = cv2.imread('Kanban-menor.png')
        #Applying Grayscale filter to image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Saving filtered image to new file
        cv2.imwrite('graytest.png',gray)
        #showing the new image in gray scale
        self.showImg("graytest.png")

    def filter2D(self):
        image = cv2.imread('Kanban-menor.png')
        #Applying Grayscale filter to image
        kernel = np.ones((6,6),np.float32)/25
        filter2D = cv2.filter2D(image,-1,kernel)
        #Saving filtered image to new file
        cv2.imwrite('filter2D.png',filter2D)
        #showing the new image in gray scale
        self.showImg("filter2D.png")

    def filterBlur(self):
        image = cv2.imread('Kanban-menor.png')
        #Applying Grayscale filter to image
        filterBlur = cv2.blur(image,(5,5))
        #Saving filtered image to new file
        cv2.imwrite('filterBlur.png',filterBlur)
        #showing the new image in gray scale
        self.showImg("filterBlur.png")

    def filterGaussianBlur(self):
        image = cv2.imread('Kanban-menor.png')
        #Applying Grayscale filter to image
        gaussianBlur = cv2.GaussianBlur(image,(5,5),0)
        #Saving filtered image to new file
        cv2.imwrite('gaussianBlur.png',gaussianBlur)
        #showing the new image in gray scale
        self.showImg("gaussianBlur.png")

    def filterMedian(self):
        image = cv2.imread('Kanban-menor.png')
        #Applying Grayscale filter to image
        median = cv2.medianBlur(image,5)
        #Saving filtered image to new file
        cv2.imwrite('median.png',median)
        #showing the new image in gray scale
        self.showImg("filterblur.png")

    def filterBilateral(self):
        image = cv2.imread('Kanban-menor.png')
        #Applying Grayscale filter to image
        bilateralFilter = cv2.bilateralFilter(image,9,75,75)
        #Saving filtered image to new file
        cv2.imwrite('bilateralFilter.png',bilateralFilter)
        #showing the new image in gray scale
        self.showImg("bilateralFilter.png")

    def filterGreen(self):
        imagem = cv2.imread('Kanban-menor.png')
        #percorre as linhas
        for y in range(0, imagem.shape[0], 1):
        #percorre as colunas 
         for x in range(0, imagem.shape[1], 1):
            #Lê cada pixel de imagem e adiciona as cores nas variáveis 
            (b, g, r) = imagem[y, x]
            #Adiciona a imagem apenas o pixel de cor verde 
            imagem[y, x] = (b%1,g%256,r%1)
        #salva a imagem modificada na pasta 
        cv2.imwrite("filterGreen.png", imagem)
        #showing the new image in gray scale
        self.showImg("filterGreen.png")

    def filterBlue(self):
        imagem = cv2.imread('Kanban-menor.png')
        #percorre as linhas
        for y in range(0, imagem.shape[0], 1):
        #percorre as colunas 
         for x in range(0, imagem.shape[1], 1):
            #Lê cada pixel de imagem e adiciona as cores nas variáveis 
            (b, g, r) = imagem[y, x]
            #Adiciona a imagem apenas o pixel de cor verde 
            imagem[y, x] = (b%1,g%256,r%1)
        #salva a imagem modificada na pasta 
        cv2.imwrite("filterBlue.png", imagem)
        #showing the new image in gray scale
        self.showImg("filterBlue.png")

    def filterRed(self):
        imagem = cv2.imread('Kanban-menor.png')
        #percorre as linhas
        for y in range(0, imagem.shape[0], 1):
        #percorre as colunas 
         for x in range(0, imagem.shape[1], 1):
            #Lê cada pixel de imagem e adiciona as cores nas variáveis 
            (b, g, r) = imagem[y, x]
            #Adiciona a imagem apenas o pixel de cor verde 
            imagem[y, x] = (b%1,g%256,r%1)
        #salva a imagem modificada na pasta 
        cv2.imwrite("filterRed.png", imagem)
        #showing the new image in gray scale
        self.showImg("filterRed.png")
        

    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("500x500")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()