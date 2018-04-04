import requests

r = requests.get('http://152.10.10.162/sm101.xml')
print(r.text)

r = requests.get('https://api.enphaseenergy.com/api/v2/systems/664018/summary?key=67551e09a7f4aa3609816466b9c4a757&user_id=4e6a4d344d7a45790a')
print(r.text)
