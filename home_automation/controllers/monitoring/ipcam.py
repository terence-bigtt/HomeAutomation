from home_automation.devices.ipcamdevice import IpCamDevice
from home_automation.private_config import ipcam_conf


def get_configured_ip_cams():
    ipcam = IpCamDevice("Car Port", "under the carport", ip="192.168.1.55", capture_path="snapshot.cgi",
                        payload=ipcam_conf["payload"], device_id="1")
    return {ipcam.device_id:ipcam}


