from home_automation.devices.device import Device
import uuid
import requests
import base64


class IpCamDevice(Device) :
    def __init__(self, name, location, device_id=uuid.uuid4(), ip=None, cam_user=None, cam_password=None,
                 capture_path=None, payload=None, authentication = None):
        """
        Driver for IpCam type devices.
        :param name: name of the device
        :param location: physical location
        :param device_id: unique identifier for the device
        :param ip: ip on the network
        :param cam_user: user name for accessing the cam
        :param cam_password: password for accessing the cam
        :param capture_path: address to call for getting a snapshot
        :param payload parameters to pass to the capture url
        :param authentication : type of authentication
        """
        Device.__init__(self, name, "ipcam", location, device_id)
        self.ip = ip
        self.cam_user = cam_user
        self.cam_password = cam_password
        self.capture_path = capture_path
        self.payload = payload
        self.authentication = authentication

    def run(self):
        capture_url = "http://" + self.ip + "/" + self.capture_path + "/" + self.capture_path
        headers = None
        if self.authentication is not None:
            headers = self.header()
        params = {"headers": headers}
        params = {k: params.get(k) for k in params.keys() if params.get(k) is not None}
        req = requests.get(capture_url, params=self.payload, **params)
        content = req.content

        return content

    def header(self):
        if self.authentication == "BASIC":
            return {"Authorization": "BASIC " + base64.b16encode(self.cam_user + ":" + self.cam_password)}

