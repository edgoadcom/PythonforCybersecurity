#!/usr/bin/env python3
# Flask example that tells us how many people there are in space
# By Ed Goad

# Import Python modules
from flask import Flask, render_template
from models import get_people_in_space

# Create main Flask object
app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return render_template('index.html')  # Calls the View

# get_count route
@app.route('/get_count')
def get_count():
    number = get_people_in_space()  # Calls the Model
    return render_template('result.html', number=number)  # Calls the View

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
