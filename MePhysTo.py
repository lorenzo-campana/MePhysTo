import streamlit as st
from multiapp import MultiApp
from apps import decay_calculator, constraint_calculator # import your app modules here
st.set_page_config(layout="wide")
app = MultiApp()

# Add all your application here
app.add_app("Decay Calculator", decay_calculator.app)
app.add_app("Constraint Calculator", constraint_calculator.app)

# The main app
app.run()