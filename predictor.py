import streamlit as st
import pandas as pd
import numpy as np
import pickle
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import os
st.set_page_config(
    page_title = 'Predictor',
    layout = 'wide'
)
model_path = os.path.join(os.path.dirname(__file__),'..',r"C:\Users\chato\Downloads\customer_churn_predict.zip")
with open (model_path,'rb') as file:
    model = pickle.load(file)

col7,col8 = st.columns(2)
with col7:
    st.title("Prediction")
    st.markdown("""
### 🔍 Customer Churn Prediction

Enter customer details to evaluate their likelihood of leaving the platform.
Our machine learning model analyzes **account information, usage patterns, and subscription details** to estimate churn probability and classify the customer's risk level.
""")
with col8:
    st.image(r"C:\Users\chato\Downloads\Customer Churn Analytics Icon.png")
with st.expander("About the different parameter in the prediction"):
    st.markdown('''### Customer Usage & Account Details

- **Tenure Month:** Number of months the customer has been using the service.
- **Monthly Charges:** Amount charged to the customer every month.
- **Usage Minutes:** Total minutes of service usage by the customer.
- **Support Calls:** Number of times the customer contacted customer support.
- **Payment Delay Days:** Number of days the customer delayed their payment.

### Subscription & Customer Feedback

- **Contract Type:** Type of subscription agreement, such as month-to-month, one-year, or two-year.
- **Autopay Option:** Indicates whether the customer has enabled automatic monthly payments.
- **Num Services:** Total number of services currently used by the customer.
- **Satisfaction Score:** Customer satisfaction rating based on their experience with the service.

### Customer Preferences & Marketing Details

- **Signup Channel:** Source through which the customer registered, such as referral, advertisements, organic search, or partner.
- **Marketing Segment:** Category assigned to the customer for marketing and analysis purposes.
- **Favorite Color:** Customer's preferred color, included as a categorical feature in the prediction model.
- **Lucky Number:** Customer's selected number, included as a numerical feature in the prediction model.''')
conn = mysql.connector.connect(host = 'localhost',user = 'root',password = 'password',database = 'customer_churn')
cursor = conn.cursor()
col4,col5,col6 = st.columns([1,2,1])
with col5:
    if(st.button("Customer Information",use_container_width = True)):
        query = 'select * from prediction order by id desc'
        cursor.execute(query)
        history = cursor.fetchall()
          
        df = pd.DataFrame(history,columns = ['Id','Tenure_month','Monthly_charges','Contract','Probablity','Prediction'])
        st.dataframe(df)
st.subheader("Enter The Details")
col1,col2,col3 = st.columns(3)
with col1:
    tenure_month = st.number_input("Tenure Month ")
    monthly_charges = st.number_input("Monthly Charges ")
    usage_minutes = st.number_input("Usage minutes ")
    support_calls = st.number_input("Support Calls ")
    payment_delay_days = st.number_input("Payment Delay Days ")

with col2:
    contract_type = st.selectbox("Contract type ",
['two-year', 'month-to-month', 'one-year']
)
    autopay = st.selectbox("Autopay option",['Yes','No'])
    f = 0
    if(autopay == 'Yes'):
        f = 1
    num_services = st.radio("Num services ",[1,2,3,4,5,6])
    satisfaction_score = st.slider("Rating ",10.0,1.0,0.1)


with col3:
    signup_channel = st.selectbox("Signup Channel type ",['referral', 'ads', 'organic', 'partner'])
    marketing_segment = st.selectbox("Marketing Segment ",['B', 'C', 'A'])
    favorite_color = st.selectbox("favorite color ",['yellow', 'red', 'green', 'black', 'white', 'blue'])
    lucky_number = st.number_input("Lucky Number ")

l = [tenure_month,monthly_charges,usage_minutes,support_calls,payment_delay_days,contract_type,f,num_services,satisfaction_score,signup_channel
     ,marketing_segment,favorite_color,lucky_number]
data = pd.DataFrame([l],columns = ['tenure_months','monthly_charges','usage_minutes','support_calls',
'payment_delay_days','contract_type','autopay','num_services','satisfaction_score',
'signup_channel','marketing_segment','favorite_color','lucky_number'])
button = st.button("🔍Predict")
prediction = ""
probablity = 0
if(button):
    y_pred = model.predict(data)
    prob = model.predict_proba(data)
    threshold = prob[0][1]*100
    probablity = threshold
    col7,col8 = st.columns(2)
    with col7:
        if(y_pred == 1):
                st.error("Customer can leave the platform!")
                prediction = "customer churn"
        else:
                st.success("Customer not leave the platform!")
                st.subheader("The Probablity of Customer Leaving")
                prediction = "customer not churn"
                st.write(f"Probablity : {threshold : .1f}%")
        st.write(f"Probablity : {threshold : .1f}%")
        if(threshold <= 35):
                st.markdown("Customer Leaving Chance : low 🟢")
                st.markdown("Likely to Stay on the platform")
        elif(threshold <= 50):
                st.markdown("Customer Leaving Chance : Moderate 🟡")
                st.markdown("Likely to Stay on the platform")
        elif(threshold <= 70):
                  st.markdown("Customer Leaving Chance : High 🔴")
                  st.mardown("Likely to Churn")
    with col8:
         plt.pie(prob[0],autopct = '%0.1f%%',labels = ['Probablity of not churn','Probablity of churn'])
         st.pyplot(plt.gcf(),width = 400)
    query = 'insert into prediction (tenure_month,monthly_charges,contract,probablity,prediction) value (%s,%s,%s,%s,%s)'
    values = (tenure_month,monthly_charges,contract_type,probablity,prediction)
    cursor.execute(query,values)
    conn.commit()
