
# Simple enough, just import everything from tkinter.
from tkinter import *

from PIL import Image, ImageTk

import cv2

import numpy as np



# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. 
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master
        
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
        #show image in window
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
        self.autenticar["width"] = 8
        self.autenticar["command"] = self.filterGray
        self.autenticar.pack(side = RIGHT)
        #Button green filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Green"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 8
        self.autenticar["command"] = self.filterGreen
        self.autenticar.pack(side = "left")
        #Button  filter Blur
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Blur"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 8
        self.autenticar["command"] = self.filterBlur
        self.autenticar.pack(side = TOP)
        #Button Gaussian filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "FiltroGaussian"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 8
        self.autenticar["command"] = self.filterGaussianBlur
        self.autenticar.pack(side = RIGHT)
        #Button Bilateral filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Bilateral"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 8
        self.autenticar["command"] = self.filterBilateral
        self.autenticar.pack(side ="left")
        #Button Blue filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Blue"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 8
        self.autenticar["command"] = self.filterBlue
        self.autenticar.pack(side = "bottom")
        #Button Red filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Red"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 8
        self.autenticar["command"] = self.filterRed
        self.autenticar.pack(side = "bottom")
        #Button Negative filter
        self.autenticar = Button(self.master)
        self.autenticar["text"] = "Filtro Negativo"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 8
        self.autenticar["command"] = self.filterNegative
        self.autenticar.pack(side = "bottom")

    #Creating the function showImg
    def showImg(self, image):
        load = Image.open(image)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=10)
    
    def filterGray(self):
        img = cv2.imread('Kanban-menor.png')
        #Applying Grayscale filter to image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Saving filtered image to new file
        cv2.imwrite('graytest.png',gray)
        ImgSave = gray
        #showing the new image 
        self.showImg("graytest.png")

    def filterBlur(self):
        image = cv2.imread('Kanban-menor.png')
        #Applying Blur filter to image
        filterBlur = cv2.blur(image,(5,5))
        #Saving filtered image to new file
        cv2.imwrite('filterBlur.png',filterBlur)
        #showing the new image 
        self.showImg("filterBlur.png")
    #filtro de suavização através da média
    def filterGaussianBlur(self):
        image = cv2.imread('Kanban-menor.png')
        #Applying Gaussian Blur filter to image
        gaussianBlur = cv2.GaussianBlur(image,(3,3),0)
        #Saving filtered image to new file
        cv2.imwrite('gaussianBl.png',gaussianBlur)
        #showing the new image 
        self.showImg("gaussianBlur.png")

    def filterBilateral(self):
        image = cv2.imread('Kanban-menor.png')
        #Applying Bilateral filter to image
        bilateralFilter = cv2.bilateralFilter(image,9,75,75)
        #Saving filtered image to new file
        cv2.imwrite('bilateralFilter.png',bilateralFilter)
        #showing the new image 
        self.showImg("bilateralFilter.png")

    def filterGreen(self):
        imagem = cv2.imread('Kanban-menor.png')
        #Reading the lines of image
        for linha in range(0, imagem.shape[0], 1):
        #Reading the collumns 
         for coluna in range(0, imagem.shape[1], 1):
            #Reading each pixel and add to variables the colors
            (b, g, r) = imagem[linha,coluna]
            #Add just the color blue in the picture  
            imagem[linha,coluna] = (b%1,g%256,r%1)
        #save the modify picture 
        cv2.imwrite("filterGreen.png", imagem)
        #showing the new image 
        self.showImg("filterGreen.png")

    def filterBlue(self):
        imagem = cv2.imread('Kanban-menor.png')
        #Reading the lines
        for linha in range(0, imagem.shape[0], 1):
        #Reading the collumns 
         for coluna in range(0, imagem.shape[1], 1):
            #Reading each pixel and add to variables the colors
            (b, g, r) = imagem[linha,coluna]
            #Add just the color blue in the picture  
            imagem[linha,coluna] = (b%256,g%1,r%1)
        #save the modify picture
        cv2.imwrite("filterBlue.png", imagem)
        #showing the new image 
        self.showImg("filterBlue.png")

    def filterRed(self):
        imagem = cv2.imread('Kanban-menor.png')
        #Reading the lines
        for linha in range(0, imagem.shape[0], 1):
        #Reading the collumns 
         for coluna in range(0, imagem.shape[1], 1):
            #Reading each pixel and add to variables the colors
            (b, g, r) = imagem[linha,coluna]
            #Add just the color blue in the picture  
            imagem[linha,coluna] = (b%1,g%1,r%256)
        #save the modify picture
        cv2.imwrite("filterRed.png", imagem)
        #showing the new image 
        self.showImg("filterRed.png")

    def filterNegative(self):
        imagem = cv2.imread('Kanban-menor.png')
             
        #Reading the lines
        for linha in range(0, imagem.shape[0], 1):
        #Reading the collumns 
         for coluna in range(0, imagem.shape[1], 1):
            #Reading each pixel and add to variables the colors
            (b, g, r) = imagem[linha,coluna]
            #Add just the color blue in the picture  
            imagem[linha,coluna] = (255 - b,255 - g,255 - r)
        #save the modify picture
        cv2.imwrite("filterNegative.png", imagem)
        #showing the new image 
        self.showImg("filterNegative.png")
        
    
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("500x500")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()