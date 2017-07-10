from flask import Blueprint, Response, request
from home_automation.controllers.monitoring.ipcam import get_configured_ip_cams

monitoring = Blueprint("monitoring", __name__)


def stream(camera):
    while True:
        frame = camera.run()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@monitoring.route("/video_feed")
def video_feed():
    cam_id = request.args.get("id")
    cam = get_configured_ip_cams().get(cam_id)
    try :
        return Response(stream(cam),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        pass

