import tkinter
from tkinter import *
from PIL import Image, ImageTk

def spawn_picture():
    # Create a photoimage object of the image in the path
    image = Image.open("C:/BZZ/Python/pythonProject9/4007875831087_S01_210617.webp")
    image = image.resize((100, 100))
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = Label(root, image=photo)
    label.image = photo

    # Position the label
    label.place(x=150, y=150)

def spawn_picture3():

    # Create a photoimage object of the image in the path
    image = Image.open("C:\BZZ\Python\pythonProject9\ea8c71c293468f4e4421bb09cd3f691c695f348f.webp")
    image = image.resize((120, 160))
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = Label(root, image=photo)
    label.image = photo
    global lable
    # Position the label
    label.place(x=250, y=130)







def change_background():
    color = bg_e1.get()
    root.config(bg= color)
def sizeplus():
    y = '500x400'
    return y
def on_submit():
    user_input = e1.get()
    root.geometry(user_input)
def calc_submit():
    optator = calc_e3.get()
    calca1 = int(calc_e1.get())
    calca2= int(calc_e2.get())
    if optator == '+':
        a3 = calca2 + calca1
    if optator == '-':
        a3 = calca1 - calca2
    if optator == '*':
        a3 = calca2 * calca1
    if optator == ':':
        a3 = calca1 / calca2
    calc_lable4 = Label(root, text=a3, font=1)
    calc_lable4.place(x=100, y=175)
    if calca2 == 11 and calca1 == 9:
        spawn_picture3()
    if a3 == 911:
        spawn_picture3()

def deletelabel():
    l1.after(1000, l1.deletecommand())







# Create the main Tkinter window
root = Tk()
e1 = tkinter.Entry(root)
e1.insert(END, '400x300')


# Create a button that spawns a picture when pressed
button = Button(root, text="Spawn Picture", command=spawn_picture)
button.pack(pady=10)

exit_button = Button(root, text='Exit', command=lambda:root.quit())
exit_button.place(x=0, y=0)

color_button = Button(root, text='submit color', command=change_background)
color_button.place(x=10, y=70)

submit_button = Button(root, text="Submit", command=on_submit)

calc_lable1 = Label(root, text='Rechner:')
calc_lable1.place(x=0, y=150)

calc_e1 = tkinter.Entry(root, width=5)
calc_e1.place(x=3, y=180)

calc_e3 = Entry(root, width=1)
calc_e3.place(x=48, y=180)

calc_e2 = tkinter.Entry(root, width=5)
calc_e2.place(x=80, y=180)

calc_lable3 = Label(root, text='=', font=1)
calc_lable3.place(x=100, y=175)

calc_submit = Button(root, text='submit', command=calc_submit)
calc_submit.place(x=100, y=150)

bg_e1 = Entry(root, width=10)
bg_e1.place(x=10, y=50)

#calc_submit = Button(root, text='delete', command=deletelabel())
#calc_submit.place(x=100, y=350)

l1 = Label(root, text='bruh')
l1.place(x=200, y=350)







y='400x300'
root.title('v2')
# Set the size of the main window
root.geometry(y)
submit_button.pack(pady=5)
e1.pack(pady=5)
root.minsize(400,300)

# Start the Tkinter event loop
root.mainloop()

