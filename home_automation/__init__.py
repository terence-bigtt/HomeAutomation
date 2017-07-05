from flask import Flask, render_template, session, g

app = Flask(__name__)

app.config.from_pyfile("websiteconfig.py")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from home_automation.views import general
app.register_blueprint(general.mod)
