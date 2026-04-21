import requests

def get_population(country):
    response = requests.get(f"http://backend:8000/population?country={country}")
    return response.json()