import requests

response = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

json = response.json()

list = json['RealtimeCityAir']['row']

for target in list:
    if target['IDEX_MVL'] < 70:
        print(target['MSRSTE_NM'], target['IDEX_MVL'])