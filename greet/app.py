from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Return simple "Wellcome" Greeting."""
    return 'welcome'

@app.route('/welcome/home')
def say_welcome_home():
    """Return simple "Wellcome Home" Greeting."""
    return 'welcome Home'

@app.route('/welcome/back')
def say_welcome_back():
    """Return simple "Wellcome back" Greeting."""
    return 'welcome back'