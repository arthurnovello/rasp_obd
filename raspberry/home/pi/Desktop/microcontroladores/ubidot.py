import requests
import time

TOKEN = "BBFF-Hz4QeNCQGT9aWJrTL5JKSYAi0BwaGk"  # Put your TOKEN here
DEVICE_LABEL = "raspberry"  # Put your device label here


def build_payload(umid, tempe, passa, alert):
    json = {"umid": umid,
                "tempe": tempe,
                "passa": passa,
                "alerta": alert}
    return json


def post_request(json):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=json)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True
