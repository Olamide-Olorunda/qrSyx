from tkinter import *
import png
import pyqrcode
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("QRx")
root.iconbitmap(" ၏  ")
root.geometry("500x550")

def create_code():
    input_path = filedialog.asksaveasfilename(
            title="Save Image", 
            filetypes=[("PNG File", "*.png" )]
            )
    if input_path:
        if input_path.endswith(".png"):
            get_code = pyqrcode.create(my_netry.get())
            
            get_code.png(input_path, scale=5)
        else:
            input_path = f"{input_path}.png"
            get_code = pyqrcode.create(my_netry.get())

            get_code.png(input_path, scale=5)

        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))

        new_label.config(image=get_image)

        my_netry.delete(0, END)                                      

        my_netry. insert(0, "Finished!")

def clear_created():
    my_netry.delete(0, END)
    new_label.config(image="")

my_netry = Entry(root, font=("Helvetica", 16))
my_netry.pack(pady=20)

netry_button = Button(root, text="Create QR Code", command=create_code)
netry_button.pack(pady=20)

clear_button = Button(root, text="Clear", command=clear_created)
clear_button.pack()

new_label = Label(root, text="")
new_label.pack(pady=20)

root.mainloop()

