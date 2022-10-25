import requests

url_template = 'http://wttr.in/{}'
url = url_template.format('London?mnqT&lang=ru')
response = requests.get(url)
print(response.text)

url = url_template.format('svo?mnqT&lang=ru')
response = requests.get(url)
print(response.text)

url = url_template.format('Череповец?MmnqT&lang=ru')
response = requests.get(url)
print(response.text)