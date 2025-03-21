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

# Route for the items page
@app.route('/items')
def items():
    with open('items.json') as file:
        data = json.load(file)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
