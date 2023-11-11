from datetime import datetime

import re
import base64
import json
from random import randint

import requests


def send_sms(phone_number, text):
    """ Сервис отправки сообщений """

    pas_code = "wellnor:f1DZ#KymW"
    pas_code64 = "Basic " + str(base64.urlsafe_b64encode(pas_code.encode("utf-8")), "utf-8")
    url = "http://91.204.239.44/broker-api/send"
    headers = {
        'Authorization': pas_code64,
        'Content-Type': 'application/json'
    }

    message_id = phone_number + "_" + f'{datetime.now():%Y%m%d_%H%M%S}'

    payload = json.dumps(
        {
            "messages": [
                {
                    "recipient": re.sub(r'[()\s+-]', '', phone_number),
                    "message-id": message_id,
                    "sms": {
                        "originator": "3700",
                        "content": {"text": text}
                    }
                }
            ]
        }
    )
    response = requests.post(url, headers=headers, data=payload)
    return bool(response.ok)


def get_substation_load(code):
    """ Получение нагрузки подстанции """
    try:
        pas_code = "electron:f1DZ#KymW"
        pas_code64 = "Basic " + str(base64.urlsafe_b64encode(pas_code.encode("utf-8")), "utf-8")
        url = f"https://api.electro-net.uz/substation/{code}/"
        headers = {
            'Authorization': pas_code64,
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        return response.json().get("load")

    except Exception:
        # TEST TEMP
        hard_data = dict({"time": datetime.now(), "load": randint(5000, 10000)})
        return hard_data.get("load")
