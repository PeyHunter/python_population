import requests

def get_population(country):
    response = requests.get(f"http://backend:8000/population?country={country}")
    return response.json()

def get_llm_analysis(selected_countries):
    response = requests.post(
        "http://backend:8000/llm-analysis",
        json={"countries": selected_countries}
    )
    return response.json()