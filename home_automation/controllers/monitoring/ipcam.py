from home_automation.devices.ipcamdevice import IpCamDevice
from home_automation.private_config import ipcam_conf


def get_configured_ip_cams():
    ipcam = []
    ipcam.append(IpCamDevice("Car Port", "under the carport", ip="192.168.1.55", capture_path="snapshot.cgi",
                             payload=ipcam_conf["payload"], device_id="1"))
    ipcam.append(
        IpCamDevice("Room1", "room at the floor", ip="192.168.1.50", cam_user=ipcam_conf["payload"].get("user"),
                    capture_path="tmpfs/auto.jpg", cam_password=ipcam_conf["payload"].get("pwd"), device_id="2",
                    authentication="BASIC"))

    return [ipcam]
