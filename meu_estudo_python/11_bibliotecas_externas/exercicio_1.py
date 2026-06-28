import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

dados = response.json()

#print(dados)

filtrar = [todo for todo in dados if todo['completed']]

#print(filtrar)

exibir = [{"id": todo['id'], "title": todo['title']} for todo in filtrar]

print(exibir)