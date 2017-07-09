from home_automation.devices.device import Device
import uuid
import requests



class IpCamDevice(Device) :
    def __init__(self, name, location, device_id=uuid.uuid4(), ip=None, cam_user=None, cam_password=None,
                 capture_path=None, payload=None):
        """
        Driver for IpCam type devices.
        :param name: name of the device
        :param location: physical location
        :param device_id: unique identifier for the device
        :param ip: ip on the network
        :param cam_user: user name for accessing the monitoring
        :param cam_password: password for accessing the monitoring
        :param capture_path: address to call for getting a snapshot
        :payload parameters to pass to the capture url
        """
        Device.__init__(self, name, "ipcam", location, device_id)
        self.ip = ip
        self.cam_user = cam_user
        self.cam_password = cam_password
        self.capture_path = capture_path
        self.payload = payload

    def run(self):
        capture_url = "http://" + self.ip + "/" + self.capture_path + "/" + self.capture_path
        req = requests.get(capture_url, params=self.payload)
        content = req.content
        raw = req.raw
        return content