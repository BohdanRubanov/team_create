import os
import customtkinter as ctk
from PIL import Image as I
import modules.screen_app as m_app

def find_path(filename):
    path_file = __file__
    path_file = path_file.split("/")
    for i in range(1):
        del path_file[-1]
    path_file = "/".join(path_file)
    path_file = os.path.join(path_file, filename)
    return path_file

image_width = 250
image_height = 250

image_random = ctk.CTkImage(
    light_image=I.open(find_path(filename="images/1.jpg")), 
    size=(image_width, image_height))

# image_random.place(x=0,y=0)