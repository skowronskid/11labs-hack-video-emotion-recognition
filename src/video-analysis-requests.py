# %%
import requests
import yaml

with open("../env.yaml") as stream:
    API_KEYS = yaml.safe_load(stream)


CALLBACK_URL = "https://silly-doctor-72.webhook.cool" 
URL_PREFIX = "https://api.imentiv.ai/v1/videos"


# %%
# UPLOADING A VIDEO
headers = {
    "accept": "application/json",
    "X-API-Key": API_KEYS["IMENTIV_API_KEY"]
}

data = {
    "title": "test3",
    "description": "test3",
    "video_url": "",
    "start_millis": "",
    "end_millis": "",
    "callback_url": ""
}

files = {
    "video": ("WIN_20250222_15_37_05_Pro.mp4", open("../WIN_20250222_15_37_05_Pro.mp4", "rb"), "video/mp4")
}

response = requests.post(URL_PREFIX, headers=headers, data=data, files=files)

print(response.status_code, ": ", response.json())
video_id = response.json()["id"]

# %%
# GENERATE PERSONALITY REPORT
url = f"{URL_PREFIX}/{video_id}/personality/request"

headers = {
    "accept": "application/json",
    "X-API-Key": API_KEYS["IMENTIV_API_KEY"],
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "callback_url": CALLBACK_URL
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code, ": ", response.json())

# %%
video_id = "e8a7897c-05dc-4806-a100-9fe1706fa170"

# %%
# GET PERSONALITY REPORT
url = f"{URL_PREFIX}/{video_id}/personality/"

# Headers
headers = {
    "accept": "application/json",
    "X-API-Key": API_KEYS["IMENTIV_API_KEY"],
}
response = requests.get(url, headers=headers)
print(response.status_code, ": ", response.json())

# %%
with open("personality_report.json", "w") as f:
    f.write(response.text)

# %%
# GENERATE REPORT FILE
url = f"{URL_PREFIX}/{video_id}/report/"

headers = {
    "accept": "application/json",
    "X-API-Key": API_KEYS["IMENTIV_API_KEY"],
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "callback_url": CALLBACK_URL
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code, ": ", response.json())


# %%
# GET REPORT FILE
url = "https://api.imentiv.ai/v1/videos/408bef4d-0f92-4dae-aa5b-f556acaa037f/report"

headers = {
    "accept": "application/json",
    "X-API-Key": API_KEYS["IMENTIV_API_KEY"]
}

response = requests.get(url, headers=headers)
print(response.status_code)#, ": ", response.json())

# %%
import zipfile
import io

if response.status_code == 200 and 'application/zip' in response.headers.get('Content-Type', ''):
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        zip_ref.extractall('../data/video_id')  


