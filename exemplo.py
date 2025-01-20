import requests

link = 'https://www.youtube.com/watch?v=TdWxS2ZBTCU'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
print(requisicao)
print(requisicao.status_code)
print(requisicao.text)