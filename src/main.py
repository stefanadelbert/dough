# A basic streamlit app which takes user input for pizza dough creation and spits out a recipe.

import streamlit as st

pages = [
    st.Page("pages/basic_dough.py", title="Basic Pizza Dough", default=True),
    st.Page("pages/poolish_dough.py", title="Poolish Pizza Dough"),
]


pg = st.navigation(pages)
pg.run()
