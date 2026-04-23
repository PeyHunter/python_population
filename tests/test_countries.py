from frontend.utils.countries import save_selected_countries
import streamlit as st

def test_save_selected_countries():
    st.session_state._selected_countries = ["Denmark", "Japan"]
    save_selected_countries()
    assert st.session_state.selected_countries == ["Denmark", "Japan"]
    
    '''
    Why this one is optional
It tests your helper logic, which is good,
but Streamlit state can be a little more awkward in tests than 
the first two examples.'''