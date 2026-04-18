import streamlit as st
import requests
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter

st.set_page_config(layout="centered")
st.title("Population Statestics")


def get_country_list():
    with open("countries.txt", "r") as f:
        countries = [line.strip() for line in f if line.strip()]
    return sorted(countries)




def show_chart(selected_countries):  
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'cyan', 'magenta', 'gray']
    
    plt.figure(figsize=(20, 12))
    
    # Loop: ALL countries plotted on SAME figure
    for i, country in enumerate(selected_countries):
        response = requests.get(f"http://backend:8000/population?country={country}")
        data = response.json()
        
        if 'historical_population' in data:
            years = [d['year'] for d in data['historical_population']]
            pops = [d['population'] for d in data['historical_population']]
            
            color = colors[i % len(colors)]
            plt.plot(years, pops, marker="o", label=country, linewidth=2, color=color)
    
    # OUTSIDE loop: styling (after all lines drawn)
    plt.title("Population Over Time: Country Comparison", fontsize=16, fontweight='bold', loc='left')
    plt.xlabel("Year", fontsize=16)
    plt.ylabel("Population", fontsize=16)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, p: f"{x/1e6:.0f}M"))
    plt.legend(fontsize=12, loc='upper left')
    plt.xticks(fontsize=10, rotation=45)
    plt.yticks(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    st.pyplot(plt)

countries = get_country_list()

# Multiple countries selection
selected_countries = st.multiselect(
    "Select countries to see population:",
    countries,
    default=["Japan"]
)

if selected_countries:
    show_chart(selected_countries)        