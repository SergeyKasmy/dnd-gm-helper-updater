#!/usr/bin/env python3
import requests

api = requests.get("https://api.github.com/repos/SleeplessSloth/dnd-gm-helper/releases/latest").json()
link = api["assets"][0]["browser_download_url"]

with open("dnd-gm-helper.exe", "wb") as file:
    file.write(requests.get(link).content)
