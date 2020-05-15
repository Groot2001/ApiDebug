# coding=utf-8

import requests
import time
import hashlib
import json

header = {"Content-Type": "application/json"}


def _Sign():
    timestamp = time.time()
    srcSign = str(timestamp) + "#" + "panther5c4eb83b6c744c34bbad01368faddc9a"
    md5_object = hashlib.md5()
    md5_object.update(srcSign.encode("utf-8"))
    return md5_object.hexdigest(), timestamp


def PostRequest(url, params, body):
    r = requests.post(url=url, headers=header, params=params, data=body)
    print(r.text)


def preRecommendCst(mobileList, projectId):
    for m in mobileList:
        print(m)


if __name__ == "__main__":
    sign, t = _Sign()
    print(sign, t)
    for m in range(19805143960,19805144960):
        print(m)
        data = {
            "customer_name": "未知",
            "customer_gender": "",
            "customer_mobile": "{}".format(m),
            "project_id": "39db3a7d-4ec4-c4b4-fc9e-e698e81f627c",
            "member_uuid": "39e84f15-eea6-6caa-93d1-3775f3bd1f14",
            "relation_id": "500",
            "longitude": "116.394653",
            "latitude": "39.866534"
        }
        datajson = json.dumps(data)
        PostRequest("https://test-extapi.myscrm.cn/index.php",
                    "r=marketing/recommend/report&orgcode=hzzhongxadmin&appid=panther&t={}&sign={}".format(t, sign),
                    datajson)
