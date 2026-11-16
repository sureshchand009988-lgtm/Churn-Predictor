import streamlit as st

home = st.Page('home.py')
predictor = st.Page('predictor.py')
model = st.Page('model_performance.py')
about = st.Page('about.py')
app = st.navigation([home,predictor,model,about],position = 'top')
app.run()