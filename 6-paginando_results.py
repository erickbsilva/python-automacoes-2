import requests
from collections import Counter

# import pandas as pd

token = str(open("token", "r").read())

# 1 - Utilizando Access Token
access_token = token  # token gerado pelo github
headers = {
    "Authorization": "Bearer " + access_token,
    "X-GitHub-Api-Version": "2022-11-28",
}

# 2 - Mapeando Informações
base_api = "https://api.github.com"
owner = "erickbsilva"
url = f"{base_api}/users/{owner}/repos"

# 3 - Organizando os Dados
repos_list = []
for page_num in range(1, 3):
    try:
        url_page = f"{url}?page={page_num}"
        response = requests.get(url_page, headers=headers)
        repos_list.append(response.json())
    except:
        repos_list.append(None)

# print(repos_list)
# print(len(repos_list)) # Primeira página
# print(len(repos_list[0])) # Na primeira página tem 30 projetos

# 4 - Filtrando Resultados
# print(repos_list[0][2]) # página - repositório
print(repos_list[0][2]["name"])  # página - repositório

# 5 - Pegando apenas o nome
name_repos = []
for page in repos_list:
    for repo in page:
        name_repos.append(repo["name"])

print(name_repos[:10])  # pega os 10 primeiros repositórios
print(len(name_repos))
