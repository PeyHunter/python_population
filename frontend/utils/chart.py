import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from utils.api_client import get_population


def show_chart(selected_countries):
    plt.figure(figsize=(12, 7))
    
    for country in selected_countries:
        data = get_population(country)
        
        if 'historical_population' in data:
           pop_data = data['historical_population']
           
           years = [record['year'] for record in pop_data]
           populations = [record['population'] for record in pop_data]
            
           plt.plot(years, populations, marker="o", label=country, linewidth=2)
    
    # Styling (after all lines)
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
    