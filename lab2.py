

from tkinter import *
from tkinter import ttk


def set_result_label():

    try:
        n1 = int(enter_1_entry.get())
        n2 = int(enter_2_entry.get())
    except ValueError:
        print("error: wrong values in entry blocks")
        return

    if n1 > n2:
        label_res["text"] = str(n1)
    else:
        label_res["text"] = str(n2)


root = Tk(screenName="Find max value")
root.geometry("120x120")

frame_find_max = ttk.Frame(root)
frame_find_max.grid()

label_1 = ttk.Label(frame_find_max, text="Enter numbers")
label_1.grid(row=0, column=0)

enter_1_entry = ttk.Entry(frame_find_max)
enter_1_entry.grid(row=1, column=0)

enter_2_entry = ttk.Entry(frame_find_max)
enter_2_entry.grid(row=2, column=0)

btn_res = ttk.Button(frame_find_max, text="Result", command=set_result_label)
btn_res.grid(row=3, column=0)

label_res = ttk.Label(frame_find_max, text="")
label_res.grid(row=4, column=0)

root.mainloop()
