import requests

API_KEY = '0e9cbd2b7dfc4a248226aa67ae7e82b0'

def get_news(query: str = "petrobras"):
    url = (
        'https://newsapi.org/v2/everything?'
        f'q={query}&sortBy=relevancy&domains=globo.com&'
        f'apiKey={API_KEY}'
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Erro ao buscar notícias"}

    data = response.json()

    # Você pode filtrar os dados aqui se quiser
    articles = data.get("articles", [])

    simplified = [
        {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        }
        for article in articles
    ]

    return simplified