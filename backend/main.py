from fastapi import FastAPI, Query
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# ---- ENDPOINTS ----
@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/population")
def get_population(
    country: str = Query(None),
    min_population: int = Query(None),
    max_population: int = Query(None)
):
    # Build the URL
    base_url = "https://api.api-ninjas.com/v1/population"
    params = []
    
    if country: 
        params.append(f"country={country}")
    if min_population:
        params.append(f"min_population={min_population}")
    if max_population:
        params.append(f"max_population={max_population}") 
        
    if params:
        url = f"{base_url}?{'&'.join(params)}"
    else:
        url = base_url
        
    #---- GET REQUEST
    api_key = os.getenv("API_KEY")  
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    
    return response.json()        
        
   
        
