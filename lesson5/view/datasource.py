import requests

def get_youbike_data()->list:
    url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(url)
    if response.ok:
        print('下載成功')
        data = response.json()
        return data