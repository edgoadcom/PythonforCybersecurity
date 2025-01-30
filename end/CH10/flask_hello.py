# First flask script
# Create by Ed 11/14
# Install Flask if not already installed
# pip install Flask

# Import modules
from flask import Flask, request, render_template_string

# Create main Flask object
app = Flask(__name__)

# Default route
@app.route('/')
def welcome():
    return render_template_string('''
        <html>
            <body>
                <h1>Welcome!</h1>
                <form action="/greet" method="post">
                    <label for="name">Enter your name:</label>
                    <input type="text" id="name" name="name">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    ''')

# Greet route
@app.route('/greet', methods=['POST'])
def greet():
    # Retrive name from browser data
    name = request.form['name']
    return f'<h1>Hello {name}!</h1>'

# Run the Flask app
app.run(debug=True)