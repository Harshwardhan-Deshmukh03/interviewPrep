from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "MYAPP"

from flask import Flask, render_template

app = Flask(__name__)

# Define route for the home page
@app.route('/')
def index():
    # Define variables for the content
    pageTitle = 'Welcome to My Website'
    paragraph1 = 'This is the first paragraph of the content.'
    paragraph2 = 'This is the second paragraph of the content.'
    btnLink = '#'
    btnText = 'Click Here'

    # Render the template with the variables
    return render_template('index.html', pageTitle=pageTitle, paragraph1=paragraph1, paragraph2=paragraph2, btnLink=btnLink, btnText=btnText)

if __name__ == '__main__':
    app.run(debug=True)
