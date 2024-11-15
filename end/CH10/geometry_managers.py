# Various tkinter geometry managers
# View how pack, grid, place work together
# Created by Ed 11/15

# Import tkinter
import tkinter

# Create the GUI main window
my_window = tkinter.Tk()
my_window.geometry('250x250')

# Using pack in a separate frame
frame_pack = tkinter.Frame(my_window, bg="lightblue")
frame_pack.pack(side="top", fill="x")
label1 = tkinter.Label(frame_pack, text="Packed Label 1")
label1.pack(pady=10)
label2 = tkinter.Label(frame_pack, text="Packed Label 2")
label2.pack(pady=10)

# Using grid in another frame
frame_grid = tkinter.Frame(my_window, bg="lightgreen")
frame_grid.pack(side="top", fill="x")
label3 = tkinter.Label(frame_grid, text="Gridded Label 1")
label3.grid(row=0, column=0, padx=10, pady=10)
label4 = tkinter.Label(frame_grid, text="Gridded Label 2")
label4.grid(row=1, column=1, padx=10, pady=10)

# Using place in the root window
label5 = tkinter.Label(my_window, text="Placed Label 1", bg="pink")
label5.place(x=50, y=190)
label6 = tkinter.Label(my_window, text="Placed Label 2", bg="pink")
label6.place(relx=0.7, rely=0.92, anchor="center", width=100, height=30)

# Enter the main event loop
my_window.mainloop()
