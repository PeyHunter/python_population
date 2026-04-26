import streamlit as st
import pandas as pd
import numpy as np
from utils.countries import select_countries
from utils.api_client import get_population
selected_countries = select_countries()
st.title("Data Analysis")
if not selected_countries:
    st.write("Please select at least one country in the sidebar.")
else:
    for country in selected_countries:
        st.subheader(country)
        data = get_population(country)
        if "historical_population" in data:
            historical_data = data["historical_population"]
            df = pd.DataFrame(historical_data)
            df = df[
                [
                    "year",
                    "population",
                    "yearly_change",
                    "yearly_change_percentage",
                    "median_age",
                    "fertility_rate",
                    "density",
                ]
            ]
            populations = np.array(df["population"])
            average_population = np.mean(populations)
            highest_population = np.max(populations)
            lowest_population = np.min(populations)
            total_change = populations[0] - populations[-1]
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Average Population", f"{average_population:,.0f}")
            col2.metric("Highest Population", f"{highest_population:,.0f}")
            col3.metric("Lowest Population", f"{lowest_population:,.0f}")
            col4.metric("Total Change", f"{total_change:,.0f}")
            st.write("Historical Population Data")
            st.dataframe(df, use_container_width=True)
        else:
            st.write("No historical population data found.")