import requests 

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Berlin,DE&appid=ecd3e7093d6e140683678a7e3963e92c&lang=de&units=metric')

print(r.json())