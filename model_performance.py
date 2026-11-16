from sklearn.metrics import classification_report,f1_score,recall_score,precision_score,confusion_matrix,accuracy_score,roc_auc_score,roc_curve
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pickle
import os
import zipfile
st.title(":material/analytics: Model Performance")
st.set_page_config(
    page_title="Model Performance",
    layout="wide"
)
#model
model_path = os.path.join(
    os.path.dirname(__file__),
    'customer_churn_predict.zip'
)

with zipfile.ZipFile(model_path, 'r') as z:
    pkl_file = [f for f in z.namelist() if f.endswith('.pkl')][0]

    with z.open(pkl_file, 'r') as file:
        model = pickle.load(file)

#model performance
df = pd.read_csv(os.path.join(os.path.dirname(__file__),'cutstomer_churn.csv'))
df = df.drop(columns = ['customer_id'])

x = df.drop(columns = ['churn'])
y = df[['churn']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state = 42)
                                                 
y_pred = model.predict(x_test)
prob = model.predict_proba(x_test)
p = precision_score(y_test,y_pred)*100
f1 = f1_score(y_test,y_pred)*100
r = recall_score(y_test,y_pred)*100
accuracy = accuracy_score(y_test,y_pred)*100
col1,col2,col3,col4 = st.columns(4)
with col1: 
    st.metric("Accuracy",f"{accuracy : .2f}%")
with col2:
    st.metric("Precision score",f"{p : .2f}%")
with col3:
     st.metric("Recall score",f"{r : .2f}%")
with col4:
    st.metric("F1 Score",f"{f1 : .2f}%")

report = classification_report(y_test,y_pred,output_dict = True)
rep = pd.DataFrame(report).T
st.subheader("Classification Report")
st.dataframe(rep)

#here is ai use for this curve
fpr,tpr,threshold = roc_curve(y_test,y_pred)
plt.plot(fpr,tpr)
plt.xlabel('false Positive')
plt.ylabel('True Positive')
plt.legend()
plt.grid()
col5,col6 = st.columns(2)
#here is ai use for this line
with col5:
    st.subheader("ROC-AUC Curve")
    st.pyplot(plt.gcf())
    plt.close()

with col6:
    st.subheader("Confusion Matrix")
    fig = sns.heatmap(
    confusion_matrix(y_test, y_pred),
    annot=True,
    fmt='d',
    xticklabels=['TP', 'FP'],
    yticklabels=['TN', 'FN']
)
    st.pyplot(plt.gcf())
    plt.close()
st.subheader('Feature Importance')
rf = model.named_steps['randomforestclassifier']
features = model.named_steps['columntransformer'].get_feature_names_out()
data = pd.DataFrame({
    'Feature': features,
    'Importance': rf.feature_importances_
})
plt.figure(figsize = (30,30))
plt.barh(data['Feature'],data['Importance'])
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
st.pyplot(plt.gcf())










