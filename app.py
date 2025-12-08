# This code imports the Flask library and some functions from it.
from flask import Flask,render_template

# Create a Flask application instance
app = Flask(__name__)

# Global variable for site name: Used in templates to display the site name
siteName = "Omapy E-commerce Project"
# Set the site name in the app context
@app.context_processor
def inject_site_name():
    return dict(siteName=siteName)


# Routes
#===================
# These define which template is loaded, or action is taken, depending on the URL requested
#===================
# Home Page
@app.route('/')
def index():
    # This defines a variable 'studentName' that will be passed to the output HTML
 studentName = "SHU Student"
    # Render HTML with the name in a H1 tag
 return render_template('index.html', title="Welcome to Omapy")

@app.route('/about/')
def about():
   
 return render_template('about.html', title="About Omapy")

@app.route('/shop/')
def shop():
   
 return render_template('shop.html', title="Shop on Omapy")

@app.route('/contact/')
def contact():
   
 return render_template('contact.html', title="Contact Omapy")

# About Page
@app.route('/about_test/')
def about_test():
    # Render HTML with the name in a H1 tag
    return render_template('about_test.html', title="About Omapy Test")

# About Page
@app.route('/aboutcopy/')
def aboutcopy():
    # Render HTML with the name in a H1 tag
    return render_template('aboutcopy.html', title="About copy test Omapy Test")

# About Page
@app.route('/register/')
def register():
    # Render HTML with the name in a H1 tag
    return render_template('register.html', title="Register on Omapy")



# Run application
#=========================================================
# This code executes when the script is run directly.
if __name__ == '__main__':
    print("Starting Flask application...")
    print("Open Your Application in Your Browser: http://localhost:81")
    # The app will run on port 81, accessible from any local IP address
    app.run(host='0.0.0.0', port=81, debug=True)



