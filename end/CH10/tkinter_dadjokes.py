# third tkinter script
# Get people in space
# Create by Ed 12/29

# Import tkinter
import tkinter
import requests

# Functions
def get_people_in_space():
    request_uri = "http://api.open-notify.org/astros.json"
    r = requests.get(request_uri)
    items = r.json()
    people_in_space = items["number"]
    tkinter.Label(my_window, text = people_in_space).pack()

def get_dadjoke():
    request_uri = "https://icanhazdadjoke.com/"
    headers = { "Accept": "application/json" }
    r = requests.get(request_uri, headers = headers)
    items = r.json()
    joke = items["joke"]
    #tkinter.Label(my_window, text = joke).pack()
    my_label.configure(text = joke)

# Create the GUI main window
my_window = tkinter.Tk()

# Add widgets
my_label = tkinter.Label(my_window, text = "Get Dad Joke", font = ("Arial Bold", 50))
my_label.pack()
my_button = tkinter.Button(my_window, text = "Click here to update", command = get_dadjoke)
my_button.pack()

# Enter the main event loop
my_window.mainloop()