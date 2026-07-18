from tkinter import *
import pyqrcode
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("QRx")
root.geometry("500x550")

def create_code():
    data = my_entry.get().strip()
    if not data:
        messagebox.showwarning("QRx", "Please enter some text or a URL first.")
        return

    input_path = filedialog.asksaveasfilename(
            title="Save Image",
            defaultextension=".png",
            filetypes=[("PNG File", "*.png")]
            )
    if not input_path:
        return

    if not input_path.endswith(".png"):
        input_path = f"{input_path}.png"

    try:
        get_code = pyqrcode.create(data)
        get_code.png(input_path, scale=5)

        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        new_label.config(image=get_image)

        my_entry.delete(0, END)
        my_entry.insert(0, "Finished!")
    except Exception as e:
        messagebox.showerror("QRx", f"Could not create QR code:\n{e}")

def clear_created():
    my_entry.delete(0, END)
    new_label.config(image="")

my_entry = Entry(root, font=("Helvetica", 16))
my_entry.pack(pady=20)

create_button = Button(root, text="Create QR Code", command=create_code)
create_button.pack(pady=20)

clear_button = Button(root, text="Clear", command=clear_created)
clear_button.pack()

new_label = Label(root, text="")
new_label.pack(pady=20)

root.mainloop()
