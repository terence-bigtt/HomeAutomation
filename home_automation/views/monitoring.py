from flask import Blueprint, Response, request, send_file, url_for
from home_automation.controllers.monitoring.ipcam import get_configured_ip_cams

monitoring = Blueprint("monitoring", __name__)


def stream(camera):
    while True:
        frame = camera.run()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def preview(camera):
    return camera.run()


@monitoring.route("/preview")
def video_preview():
    cam_id = request.args.get("id")
    cams = get_configured_ip_cams()
    cam = filter(lambda c: c.device_id == cam_id, reduce(lambda c1, c2: c1 + c2, cams, []))

    return send_file("static/image/noimage.jpg", mimetype='image/jpg')

    try:
        return Response(preview(cam[0]))
    except Exception as e:
        return send_file("static/image/noimage.jpg", mimetype='image/jpg')


@monitoring.route("/video_feed")
def video_feed():
    cam_id = request.args.get("id")
    cams = get_configured_ip_cams()
    cam = filter(lambda c: c.device_id == cam_id, reduce(lambda c1, c2: c1 + c2, cams, []))

    try:
        return Response(stream(cam[0]),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        return send_file("static/image/noimage.jpg", mimetype='image/jpg')
