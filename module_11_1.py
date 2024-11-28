import requests


response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

for post in data[:5]:
    print(f"Title: {post['title']}, Body: {post['body']}")

