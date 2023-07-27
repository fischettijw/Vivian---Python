# establish imports (GUI and Images)
from tkinter import *
from PIL import ImageTk, Image

# counter integer
image_counter = 0

# setup image function and return image_list
def setup_images():
    image1 = ImageTk.PhotoImage(Image.open("images/01.jpg").resize((600, 350)))
    image2 = ImageTk.PhotoImage(Image.open("images/02.jpg").resize((600, 350)))
    image3 = ImageTk.PhotoImage(Image.open("images/03.jpg").resize((600, 350)))
    image4 = ImageTk.PhotoImage(Image.open("images/04.jpg").resize((600, 350)))
    image5 = ImageTk.PhotoImage(Image.open("images/05.jpg").resize((600, 350)))
    image6 = ImageTk.PhotoImage(Image.open("images/06.jpg").resize((250, 350)))
    return [image1, image2, image3, image4, image5, image6]

# set up the widgets
def setup_widgets(win, init_image, image_list):
    image = Label(win, image=init_image)
    label = Label(win, text=f"Image 1 of {len(image_list)}", font="Helvetica, 20")
    button = Button(win, text="Change", width=20, height=2, bg="purple", fg="white",
                    command=lambda: change_image(init_image, image_list))
    return (image,label,button)

# change image function
def change_image(image_list, image_label):
    global image_counter
    if image_counter < len(image_list) - 1:
        image_counter += 1
    else:
        image_counter = 0
    image_label.config(image=image_list[image_counter])
    image_label.config(text="Image " + str(image_counter + 1) + " of " + str(len(image_list)))
    
# display the widgets
def display_widgets(image,label,button):
    image.pack()
    label.pack()
    button.pack(side="bottom", pady=3)