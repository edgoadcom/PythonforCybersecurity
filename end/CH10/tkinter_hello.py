# First tkinter script
# Create by Ed 11/14

# Import modules
import tkinter

# Create the GUI main window
my_window = tkinter.Tk()

# Add widgets
my_label = tkinter.Label(my_window, text = "Hello World",
                         font = ("Arial Bold", 50))
my_label.pack()

# Enter the main event loop
my_window.mainloop()