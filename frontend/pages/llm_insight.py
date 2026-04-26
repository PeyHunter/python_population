import streamlit as st
from utils.countries import select_countries
from utils.api_client import get_llm_analysis

selected_countries = select_countries()

st.title("LLM Insight")

if not selected_countries:
    st.write("Please select at least one country in the sidebar.")
else:
    st.write("Generate an AI analysis of the selected population data.")
    if st.button("Generate Analysis"):
        with st.spinner("Generating analysis..."):
            result = get_llm_analysis(selected_countries)
        st.subheader("Analysis")
        st.write(result["analysis"])