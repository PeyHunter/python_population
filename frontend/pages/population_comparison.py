import streamlit as st
from utils.countries import select_countries
from utils.chart import show_chart

selected_countries = select_countries()

st.title("Population Comparison")
if selected_countries:
    show_chart(selected_countries)
else:
    st.write("Please select at least one country in the sidebar.")
    
    
    