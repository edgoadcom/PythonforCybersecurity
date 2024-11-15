# third tkinter script
# Get people in space
# Create by Ed 12/29

# Import tkinter
import tkinter
from tkinter.font import Font
import requests

# Functions
def get_dadjoke():
    request_uri = "https://icanhazdadjoke.com/"
    headers = { "Accept": "application/json" }
    r = requests.get(request_uri, headers = headers)
    items = r.json()
    joke = items["joke"]
    my_label.configure(text = joke)

# Create the GUI main window
my_window = tkinter.Tk()

# Create font object
my_font = Font(family="Arial", weight="bold", size=50)
# Set wraplength to 25 characters
char_width = my_font.measure("A")
wrap_length = char_width * 25

# Add widgets
my_label = tkinter.Label(my_window,
                         text = "Get Dad Joke",
                         font = my_font,
                         wraplength=wrap_length)
my_label.pack()
my_button = tkinter.Button(my_window,
                           text = "Click here to update",
                           command = get_dadjoke)
my_button.pack()

# Enter the main event loop
my_window.mainloop()