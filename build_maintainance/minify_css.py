import requests
from config import DIR_BASE, DIR_APP, APP_GIT_REPO, DIR_APP_ROOT

url = 'https://cssminifier.com/raw'
data = {'input': open(str(DIR_APP) + 'static/css/modern-business2.css', 'rb').read()}
response = requests.post(url, data=data)

print(response.text)
