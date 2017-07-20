from home_automation.devices.ipcamdevice import IpCamDevice
from home_automation.private_config import ipcam_conf


def get_configured_ip_cams():

    ipcam = []
    ipcam2 = []
    for conf in ipcam_conf:
        ipcam2.append(IpCamDevice(**conf))

    ipcam.append(IpCamDevice("Car Port", "under the carport", ip="192.168.1.55", capture_path="snapshot.cgi",
                                 payload=ipcam_conf[0]["payload"], device_id="3"))
    ipcam.append(
    IpCamDevice("Room1", "room at the floor", ip="192.168.1.50", cam_user=ipcam_conf[0]["payload"].get("user"),
                    capture_path="tmpfs/auto.jpg", cam_password=ipcam_conf[0]["payload"].get("pwd"), device_id="4",
                    authentication="BASIC"))

    return [ipcam2, ipcam]


def get_cam(cam_id):
    cam = filter(lambda c: c.device_id == cam_id, reduce(lambda c1, c2: c1 + c2, cams, []))
    return cam

cams = get_configured_ip_cams()
