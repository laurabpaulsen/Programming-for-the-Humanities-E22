import json
from urllib.request import urlopen


def getTodaysHoroscope(url_to_api):
    response = urlopen(url_to_api)
    data_json = json.loads(response.read())
    
    return data_json


def main():

    sign = "libra"
    url = f"https://any.ge/horoscope/api/?sign={sign}&type=daily&day=today"
    receivedJSONdata = getTodaysHoroscope(url)
    print(receivedJSONdata)
    print()
    print(receivedJSONdata[0]['text'])
    
    
if __name__ == '__main__':
    main()