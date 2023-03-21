import customtkinter as ctk
import json as js
import modules.images as img

list_images = []

# for i in range(5):
#     list_images.append("images/" + i + ".jpg")
#     i += 1

class Frame(ctk.CTkFrame):
    def __init__(self, master, text, width, height, **kwargs):
            super().__init__(master = master, width = width, height = height, **kwargs)
            # self.IMAGE = self.create_image(image=img.image_random)
            # self.IMAGE.place(x=0, y=0)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.app_height = 500
        self.app_width = 500
        
        self.title("Image App")
        self.geometry(f"{self.app_width}x{self.app_height}+{100}+{100}")

        self.FRAME = Frame(master = self, text = "", width = self.app_width, height = self.app_height)
        self.FRAME.grid(row = 0, column = 0, padx = 0, pady = 0)
        self.FRAME2 = Frame(master = self, text = "", width = self.app_width, height = self.app_height)
        self.LABEL = ctk.CTkLabel(
            master= self.FRAME,
            text= "",
            image= img.image_random
            )
        # self.LABEL.place(x = 0, y = 0)




    
def create_button(master,width,height,corner_radius, border_color, text, border_width,command):
    button = ctk.CTkButton(master = master,
                           width = width ,     
                           height = height,
                           border_width= border_width,
                           corner_radius= corner_radius,
                           border_color= border_color,
                           text = text,
                           command= command)

    
    return button

main_app = App()

# main_app_2 = App2()
def change_window():
    # global main_app
    # print(1111)
    new_window = ctk.CTkToplevel()
    new_window.title("Image App")
    new_window.geometry(f"{500}x{400}+{100}+{100}")
    new_window.FRAME_REGESTRATION = Frame(master = new_window, text = "", width = 500, height = 400)
    new_window.INPUT_LOGIN = ctk.CTkEntry(master= new_window.FRAME_REGESTRATION, width= 250, height = 10, corner_radius= 2, border_width=2, bg_color="yellow", )
    new_window.INPUT_PASSWORD = ctk.CTkEntry(master= new_window.FRAME_REGESTRATION, width= 250, height = 10, corner_radius= 2, border_width=2, bg_color="yellow", )
    new_window.INPUT_PASSWORD2 = ctk.CTkEntry(master= new_window.FRAME_REGESTRATION, width= 250, height = 10, corner_radius= 2, border_width=2, bg_color="yellow", )
    new_window.FRAME_REGESTRATION.place(x = 0, y = 0)
    new_window.INPUT_LOGIN.place(relx =0.4, rely = 0.3)
    new_window.INPUT_PASSWORD.place(relx =0.4, rely = 0.5)
    new_window.INPUT_PASSWORD2.place(relx =0.4, rely = 0.7)
    # return new_window

but1 = create_button(master=main_app.FRAME, text = "Реєстрація", height = 60, width = 150, corner_radius=3, border_width = 3, border_color ="green", command = change_window)

but2 = create_button(master= main_app.FRAME, text = "Авторизація", height = 60, width = 150, corner_radius = 3, border_width = 3 , border_color ="green", command = change_window)

but1.place(relx = 0.4, rely= 0.3)
but2.place(relx = 0.4, rely = 0.5)        













    



#with open("new_file.json", "w") as f:
