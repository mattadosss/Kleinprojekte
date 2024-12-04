from tkinter import *
from tkinter import ttk
from test import spawn_label
root = Tk()
frm = ttk.Frame(root, )
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

label_count = 1

cords_col = ttk.Entry(root)
cords_col.insert(0,0)
cords_col.grid()
def create_test():
    global label_count
    col_pos = cords_col.get()
    int(col_pos)
    label1 = ttk.Label(root, text='value')
    label1.grid(column=col_pos, row=label_count, pady=5)
    print('created label')
    label_count += 1


ttk.Button(frm, text='create', command=spawn_label()).grid(column=1, row=1)


def update_title(event):
    # Get the current window width and height
    width = root.winfo_width()
    height = root.winfo_height()
    root.title(f"current window size:({width}x{height}) last mouse click pos: {(event.x, event.y)}")


root.bind('<Configure>', update_title)
root.bind('<Button-1>', update_title)
root.geometry("1444x640")
root.title('teset')

root.mainloop()