from flask import Flask, render_template
from flask_socketio import SocketIO
from home_automation.views import general
from home_automation.views import monitoring

app = Flask(__name__)
app.config.from_pyfile("websiteconfig.py")
socketio = SocketIO(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


app.register_blueprint(general.mod)
app.register_blueprint(monitoring.monitoring)
