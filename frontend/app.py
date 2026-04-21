import streamlit as st
from utils.countries import select_countries

selected_countries = select_countries()


st.title("Population Statistics")
st.write("This application compares population data across countries.")
st.write("Use the navigation menu to open the different pages.")