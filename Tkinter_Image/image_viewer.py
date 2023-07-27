# https://www.youtube.com/watch?v=olom5Ow7zbo
# https://www.youtube.com/watch?v=dN-5Q7DO9Ww
# https://www.youtube.com/watch?v=VnwDPa9biwc
# https://www.youtube.com/watch?v=ZbSncQYZ56U

from tkinter import *
from PIL import ImageTk, Image

# set up the tkinter window
window = Tk()
window.title("Dog Image Viewer")
window.geometry("625x450")
window.iconbitmap("images/icon.ico")

# set up the images
# image3 = ImageTk.PhotoImage(Image.open("images/03.jpg").resize((600, 350)))

image1 = ImageTk.PhotoImage(Image.open("images/01.jpg").resize((622, 350)))
image2 = ImageTk.PhotoImage(Image.open("images/02.jpg").resize((524, 350)))
image3 = ImageTk.PhotoImage(Image.open("images/03.jpg").resize((378, 350)))
image4 = ImageTk.PhotoImage(Image.open("images/04.jpg").resize((622, 350)))
image5 = ImageTk.PhotoImage(Image.open("images/05.jpg").resize((528, 350)))
image6 = ImageTk.PhotoImage(Image.open("images/06.jpg").resize((197, 350)))

# add them to the list
image_list = [image1, image2, image3, image4, image5, image6]

# counter integer
image_counter = 0

# change image function
def change_image():
    global image_counter
    if image_counter < len(image_list) - 1:
        image_counter += 1
    else:
        image_counter = 0
    image.config(image=image_list[image_counter])
    label.config(text="Image " + str(image_counter + 1) + " of " + str(len(image_list)))
    
# set up the widgets
image = Label(window, image=image1)
label = Label(window, text=f"Image 1 of {len(image_list)}", font="Helvetica, 20")
button = Button(window, text="Change", width=20, height=2, bg="purple", fg="white", 
                command=change_image)

# display the widgets
image.pack()
label.pack()
button.pack(side="bottom", pady=3)

# run the main loop
window.mainloop()