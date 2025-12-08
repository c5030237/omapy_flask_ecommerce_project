# This code imports the Flask library and some functions from it.
from flask import Flask,render_template

# Create a Flask application instance
app = Flask(__name__)

# Global variable for site name: Used in templates to display the site name
siteName = "Omapy"
# Set the site name in the app context
@app.context_processor
def inject_site_name():
    return dict(siteName=siteName)


# Routes
#===================
# These define which template is loaded, or action is taken, depending on the URL requested
#===================
# Home Page Route
@app.route('/')
def index():
    # This defines a variable 'studentName' that will be passed to the output HTML
 studentName = "SHU Student"
    
    # Render the 'index.html' template and a title to set the page title dynamically
 return render_template('index.html', title="Welcome to Omapy")

# About Page Route
@app.route('/about/')
def about():
   # Render the 'about.html' template and a title to set the page title dynamically
 return render_template('about.html', title="About Omapy")

# Shop Page Route
@app.route('/shop/')
def shop():
    # Render the 'shop.html' template and a title to set the page title dynamically
 return render_template('shop.html', title="Shop on Omapy")

@app.route('/contact/')
def contact():
   # Render the 'contact.html' template and a title to set the page title dynamically
 return render_template('contact.html', title="Contact Omapy")

@app.route('/create/')
def create():
   # Render the 'contact.html' template and a title to set the page title dynamically
 return render_template('create.html', title="Create your products on Omapy")

@app.route('/update/')
def update():
   # Render the 'contact.html' template and a title to set the page title dynamically
 return render_template('update.html', title="Update your products on Omapy")

# Run application
#=========================================================
# This code executes when the script is run directly.
if __name__ == '__main__':
    print("Starting Flask application...")
    print("Open Your Application in Your Browser: http://localhost:81")
    # The app will run on port 81, accessible from any local IP address
    app.run(host='0.0.0.0', port=81, debug=True)
