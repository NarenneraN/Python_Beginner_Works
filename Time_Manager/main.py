from tkinter import *
from PIL import Image, ImageTk
print("Simple time manger!")
def start_it():
    timer(5*60)
def timer(time_sec):
    convert_min = str(int(time_sec/60))
    convert_sec = str(time_sec%60)
    # print("Naren")
    if time_sec>=0:
        canvas.itemconfig(dyn_text,text=f"{convert_min.zfill(2)}:{convert_sec.zfill(2)}")
        window.after(1000,timer,time_sec-1)
window =Tk()
window.title("Time Manager")
window.config(padx=200,pady=120,bg="#181818")
canvas = Canvas(width=300,height=300,bg="#181818",highlightthickness=0)
image = Image.open("timer.png")
timer_image_r= image.resize((300,300))
timer_image = ImageTk.PhotoImage(timer_image_r)
canvas.create_image(150,150,image=timer_image)
dyn_text = canvas.create_text(150,270,text="00:00:00",fill="white",font=("Arial",25,"bold"))
canvas.grid(row=1,column=1,padx=50)


start = Button(text="Start",font=("Arial",15,"bold"),command=start_it)
stop = Button(text="Stop",font=("Arial",15,"bold"))
start.grid(row=1,column=0,padx=50)
stop.grid(row=1,column=2,padx=50)

check_marks = Label(text="✔",font=("Arial",10,"bold"))
check_marks.grid(row=2,column=1,pady=50)
# Footer
window.mainloop()