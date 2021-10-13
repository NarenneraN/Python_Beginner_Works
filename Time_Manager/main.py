from tkinter import *
from PIL import Image, ImageTk
print("Simple time manger!")
window =Tk()
window.title("Time Manager")
window.config(padx=200,pady=120)

canvas = Canvas(width=300,height=300)
image = Image.open("timer.png")
timer_image_r= image.resize((300,300))
timer_image = ImageTk.PhotoImage(timer_image_r)
canvas.create_image(150,150,image=timer_image)
canvas.pack()
# Footer
window.mainloop()