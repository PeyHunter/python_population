from fastapi import FastAPI, Query
from pydantic import BaseModel
from openai import OpenAI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class LLMAnalysisRequest(BaseModel):
    countries: list[str]

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
     
     
     
        
@app.post("/llm-analysis")
def get_llm_analysis(request: LLMAnalysisRequest):
    
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    population_data = []
    
    for country in request.countries:
        base_url = "https://api.api-ninjas.com/v1/population"
        url = f"{base_url}?country={country}"
        headers = {"X-Api-Key": os.getenv("API_KEY")}
        response = requests.get(url, headers=headers)
        data = response.json()
        population_data.append(data)
    
    prompt = f"""
You are analyzing population statistics.
Only use the data provided below.
Write exactly 2 or 3 short paragraphs.
Keep the response concise and easy to understand.

In your analysis:
1. Compare the countries directly.
2. Point out which country is growing, stable, or declining.
3. Explain what the differences may indicate demographically.
4. Mention the most important contrast between the countries.
Do not invent facts that are not supported by the data.
Population data:
{population_data}
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful data analyst."},
            {"role": "user", "content": prompt},
        ],
    )
    
    analysis = response.choices[0].message.content
    
    return {"analysis": analysis}   
        


