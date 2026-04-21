import streamlit as st

def get_country_list():
    with open("./countries.txt", "r") as f:
        countries = [line.strip() for line in f if line.strip()]
    return sorted(countries)

def save_selected_countries():
    st.session_state.selected_countries = st.session_state._selected_countries

def select_countries():
    countries = get_country_list()
    if "selected_countries" not in st.session_state:
        st.session_state.selected_countries = ["Denmark"]
    if "_selected_countries" not in st.session_state:
        st.session_state._selected_countries = st.session_state.selected_countries
    st.sidebar.multiselect(
        "Select countries:",
        countries,
        key="_selected_countries",
        on_change=save_selected_countries
    )
    return st.session_state._selected_countries