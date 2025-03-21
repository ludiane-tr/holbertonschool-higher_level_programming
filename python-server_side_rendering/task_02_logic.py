from flask import Flask, render_template
import json

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html template for the home page

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')  # Renders the about.html template for the about page

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Renders the contact.html template for the contact page

# Route for displaying a list of items from a JSON file
@app.route('/items')
def items():
    # Read the data from the items.json file
    with open('items.json') as f:
        data = json.load(f)  # Parse the JSON data into a Python dictionary

    # Pass the list of items to the items.html template
    return render_template('items.html', items=data['items'])  # Render the items.html template with items

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run the app in debug mode on port 5000
