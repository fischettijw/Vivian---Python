# establish imports (GUI and Images)
from tkinter import *
from PIL import ImageTk, Image
from image_viewer_helper import *

# counter integer
# image_counter = 0

# set up the tkinter window
window = Tk()
window.title("Dog Image Viewer")
window.geometry("610x430")
window.iconbitmap("images/icon.ico")

image_list = setup_images()
(image,label,button) = setup_widgets(window,image_list[0], image_list)
display_widgets(image,label,button)
change_image(image_list, label)

# run the main loop
window.mainloop()