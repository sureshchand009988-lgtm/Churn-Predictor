import streamlit as st

st.set_page_config(page_title="Home", layout="wide")
import streamlit as st
# Main heading
st.title("Customer Churn Predictor")

# Banner image
st.image(
  r"C:\Users\chato\Downloads\churn_models_blend.png",
    width=15,use_container_width = True
)

st.subheader("Welcome to Customer Churn Analytics!")
st.markdown('Explore customer data, evaluate machine learning models, and predict customer churn to gain valuable insights into customer retention and business performance.')
st.subheader("Explore the Dashboard")
col1,col2,col3 = st.columns(3)
with col1:
    st.subheader("Churn Predictor   :material/query_stats:")
    st.caption("Explore →")
    st.page_link("predictor.py",label = 'open predictor')
with col2:
     st.subheader("About            :material/info:")
     st.caption("Explore →")
     st.page_link("about.py",label = 'about the model')
with col3:
     st.subheader("Model performance :material/analytics:")
     st.caption("Explore →")
     st.page_link("model_performance.py",label = 'check the performance')