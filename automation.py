import requests
country_code=input(" Enter Country Code : ")
pin_code=int(input(" Enter Pin Code : "))
response = requests.get(f'https://api.zippopotam.us/{country_code}/{pin_code}')
json_response = response.json()
repository = json_response['places'][0]
print(f'Country: {json_response["country"]}')
print(f'Place Name: {repository["place name"]}')
print(f'State: {repository["state"]}')
