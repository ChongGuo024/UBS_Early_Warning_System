# -*- coding: utf-8 -*-
"""EA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1clE1MtsDREik-QvSZUsiRH1GFfJehOxz
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance
import warnings
import plotly
import plotly.express as px
import plotly.graph_objects as go

warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Title and Subheader
st.title("Early Warning System for Small Business Dataset EDA App")
st.subheader("EDA Web App with Streamlit ")

# EDA
my_dataset = "temp_11_14_version3.csv"


# To Improve speed and cache data
# @st.cache(persist=True)
def explore_data(dataset):
    df = pd.read_csv('temp_11_14_version3.csv')
    df = df[['target', 'Company Name', 'Address','County', 'Credit Score Alpha',
       'Employee_Change', 'Estimated Labor Cost', 'Google_Reviews',
       'Google_Scores', 'Grocery_within_Zip', 'NAICS', 
       'Sales_Change', 'Sales_per_employee', 'Square Footage',
       'Supermarket_within_5_miles', 'county_personal_income',
       'county_population','Year']]
    df.drop(['NAICS'],axis=1,inplace=True)
    return df 

# Show Dataset
if st.checkbox("Preview DataFrame"):
    data = explore_data(my_dataset)
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())
    else:
        st.write(data.head(2))
        
# Show Entire Dataframe
if st.checkbox("Show All DataFrame"):
    data = explore_data(my_dataset)
    st.dataframe(data)
    
# Show Description
if st.checkbox("Show All Column Name"):
    data = explore_data(my_dataset)
    st.text("Columns:")
    st.write(data.columns)
    
# Dimensions
data_dim = st.radio('What Dimension Do You Want to Show',('Rows','Columns'))
if data_dim == 'Rows':
    data = explore_data(my_dataset)
    st.text("Showing Length of Rows")
    st.write(len(data))
if data_dim == 'Columns':
    data = explore_data(my_dataset)
    st.text("Showing Length of Columns")
    st.write(data.shape[1])

# Summary of the Dataframe
if st.checkbox("Show Summary of Dataset"):
    data = explore_data(my_dataset)
    st.write(data.describe())
    
# Selection
species_option = st.selectbox('Select Columns',('Address','Company Name','County','Credit Score Alpha','Employee_Change','Estimated Labor Cost',
                                                'Google_Reviews','Google_Scores','Grocery_within_Zip','target','Sales_Change',
                                                'Sales_per_employee','Square Footage','Supermarket_within_5_miles','county_personal_income','county_population','Year'))
data = explore_data(my_dataset)
# Numerical Features
if species_option == 'Sales_Change':
    st.write(data['Sales_Change'])
elif species_option == 'Google_Reviews':
    st.write(data['Google_Reviews'])
elif species_option == 'Google_Scores':
    st.write(data['Google_Scores'])
elif species_option == 'Grocery_within_Zip':
    st.write(data['Grocery_within_Zip'])
elif species_option == 'Employee_Change':
    st.write(data['Employee_Change'])
elif species_option == 'county_personal_income':
    st.write(data['county_personal_income'])    
elif species_option == 'target':
    st.write(data['target']) 
elif species_option == 'County':
    st.write(data['County']) 
elif species_option == 'Estimated Labor Cost':
    st.write(data['Estimated Labor Cost']) 
elif species_option == 'Sales_per_employee':
    st.write(data['Sales_per_employee']) 
elif species_option == 'Square Footage':
    st.write(data['Square Footage'])
elif species_option == 'Supermarket_within_5_miles':
    st.write(data['Supermarket_within_5_miles'])
elif species_option == 'Credit Score Alpha':
    st.write(data['Credit Score Alpha'])
elif species_option == 'county_population':
    st.write(data['county_population'])
elif species_option == 'Year':
    st.write(data['Year'])
# Categorical Features
elif species_option == 'Company Name':
    st.write(data['Company Name'])
elif species_option == 'Address':
    st.write(data['Address'])
else:
    st.write("Select A Column")
    


# Show Plots
if st.checkbox("Simple Correlation Plot"):
    data = explore_data(my_dataset)
    plt.figure(figsize=(15,10))
    temp_5 = data.copy()
    temp_5.drop(['Year'],axis=1,inplace=True)
    cmap = sns.diverging_palette(h_neg=10,h_pos=240,as_cmap=True)
    corr=temp_5.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    st.write(sns.heatmap(corr, center=0,cmap=cmap, linewidths=1,mask=mask,annot=True, fmt=".2f")) 
    st.pyplot()

 
# Show Plots
if st.checkbox("Distribution of google scores in every county"):
    data = explore_data(my_dataset)
    fig2 = px.box(data,x='County',y='Google_Scores',template='seaborn')
    fig2.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
    st.plotly_chart(fig2)


# Show Plots
if st.checkbox("Estimated Labor Cost of Different Counties for Open Stores"):
    data = explore_data(my_dataset)
    temp_1 = data[data['target']==1][['Estimated Labor Cost','County']]
    st.write(sns.barplot(x="Estimated Labor Cost",y="County",data = temp_1))
    st.pyplot()



# Show Plots
if st.checkbox("Number of closed stores in different counties"):
    data = explore_data(my_dataset)   
    temp = data[data['target']==0][['Year','County']]
    year_count = temp['Year'].value_counts().rename_axis('Year').reset_index(name='Number of closed stores')
    fig3 = px.bar(year_count,x='Year', y='Number of closed stores')
    fig3.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
    st.plotly_chart(fig3)


# # Show Plots
# if st.checkbox("Correlation between county_personal_income & county_population"):
#     data = explore_data(my_dataset)
#     plt.figure(figsize=(15,10))
#     st.write(sns.jointplot(data.loc[:,'county_personal_income'], data.loc[:,'county_population'], kind="reg", color="#ce1414"))
#     st.pyplot()


# Show Plots
if st.checkbox("Sales_Change & Employee_Change"):
    data = explore_data(my_dataset)
    temp_6 = data.copy()
    temp_6['target']=temp_6['target'].astype('category')
    temp_6['target']=temp_6['target'].map({0:'closed',1:'open'})
    fig4 = px.scatter(temp_6, x='Employee_Change', y='Sales_Change', color='target', template='presentation')
    fig4.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
    st.plotly_chart(fig4)


# # Show Plots
# if st.checkbox("Sales_Change & Employee_Size & Google_Review"):
#     data = explore_data(my_dataset)
#     fig5 = px.scatter_3d(data, x='Google_Reviews', y='Credit Score Alpha', z='Sales_Change', color='target', template='ggplot2', size='Google_Scores')
#     fig5.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
#     st.plotly_chart(fig5)


# Show Plots
if st.checkbox("Distribution of Supermarket_within_5_miles for Open Stores"):
    data = explore_data(my_dataset)
    temp_4 = data[data['target']==1][['Supermarket_within_5_miles']]
    plt.ylabel('Probability')
    plt.xlabel('Number of Supermarket within 5 miles')
    plt.title('Distribution of Supermarket_within_5_miles for Open Stores')
    st.write(plt.hist(temp_4['Supermarket_within_5_miles'],density=True))
    st.pyplot()


# Show Plots
if st.checkbox("Distribution of Supermarket_within_5_miles for Closed Stores"):
    data = explore_data(my_dataset)
    temp_3 = data[data['target']==0][['Supermarket_within_5_miles']]
    plt.ylabel('Probability')
    plt.xlabel('Number of Supermarket within 5 miles')
    plt.title('Distribution of Supermarket_within_5_miles for Closed Stores')
    st.write(plt.hist(temp_3['Supermarket_within_5_miles'],density=True))
    st.pyplot()


# About
if st.button("About App"):
    st.subheader("Early Warning System for Small Business Dataset EDA App")
    st.text("Built with LMWGY Team")
    st.text("Thanks for Watching")

if st.checkbox("By"):
    st.text("LMWGY Team")

