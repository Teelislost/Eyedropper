from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from ctk_colorpicker_plus import CTkColorPicker
import os

Photo_Image= None

def showimage():
    global Photo_Image
    Photos = filedialog.askopenfilename(initialdir= os.getcwd(), filetypes= (("JPG file", "*.jpg"),
                                        ("PNGFile", "*.png") ,("All Files", "*.*")))
    Photo_Image = Image.open(Photos)
    Photo_Image.thumbnail((300,300))
    More_Photo = ImageTk.PhotoImage(Photo_Image)
    Photo = ImageTk.PhotoImage(Photo_Image)
    Eyedropper_Label.config (image=More_Photo)
    Eyedropper_Label.image= More_Photo

def rgb_to_hex(rgb):
   return "#"+"%02X%02X%02X" % rgb


def pickingcolor(event):
    global Photo_Image
    x = event.x
    y = event.y

    Photo = Photo_Image.convert("RGB")
    Pixel = Photo_Image.getpixel((x,y))
    Color = rgb_to_hex (Pixel)
    Colors = Color
   # print(Color)
    Colorpicker.entry.delete(0, tk.END)
    Colorpicker.entry.insert(0, Colors)
    Colorpicker.apply_hex_input()

    

def pressbutton(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

     
Eyedropper = Tk()
Eyedropper.title("Eyedropper")
Eyedropper.state("zoomed")
Eyedropper.iconbitmap("Let_me_go.ico")
Eyedropper.rowconfigure(0, weight=1)
Eyedropper.columnconfigure(0, weight=1)



Colorpicker = CTkColorPicker(
             Eyedropper,
             width= 200,
             height=300,
             bg_color= "#333333",
             fg_color= "#333333")
Colorpicker.place(x=1050,y=0)


Frame_1 = Frame(Eyedropper)
Frame_1.pack(side= BOTTOM, padx=15, pady=15)


Eyedropper_Label = Label(Eyedropper,)
Eyedropper_Label.place(x=500, y=150)

Image_Button = Button(Eyedropper,
               font= ("Pileup", "40"),
               text= ("Add Image."),
               bg = "#D3D3D3",
               fg = "Black",
               command= showimage,
               bd=0,
               )
Image_Button.pack()
Image_Button.place(x=0,y=0)

Eyedropper.bind("<Button-1>",pickingcolor)
Eyedropper.mainloop()








