import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot
#import matplotlib.pyplot as plt
# Load the model from the pickle file
df_train=pd.read_csv("Life Expectancy Data.csv")
with open('Model1.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
st.set_page_config(layout="wide")
title = '<p style="font-family: Arial, Helvetica, sans-serif;text-align:center; font-size: 50px;color:blue;text-shadow: 2px 2px #080000;">LIFE EXPECTANCY PREDICTION </p>'
st.markdown(title, unsafe_allow_html=True)
new_title = '<p style="font-family:sans-serif; font-size: 20px;text-align: left;">Explore our advanced life expectancy predictor! Harnessing demographics and medical data, our innovative model forecasts a nations longevity. Empower decision-makers with insightful projections. Uncover trends, plan for the future, and contribute to a healthier society. Discover the science of longevity with our cutting-edge platform. </p>'
st.markdown(new_title, unsafe_allow_html=True)
new_title1 = '<p style="font-family:sans-serif; font-size: 25px;text-align: left;color:blue;"><br>About the data</p>'
st.markdown(new_title1, unsafe_allow_html=True)
new_title2 = '<p style="font-family:sans-serif; font-size: 20px;text-align: left;">This web application was built from the data provided by Global Health Observatory (GHO), data repository under World Health Organization (WHO) keeps track of the health status as well as many other related factors for all countries. The data contains health factors for 193 countries has been collected from the same WHO data repository website and its corresponding economic data was collected from United Nation website. Among all categories of health-related factors only those critical factors were chosen which are more representative. </p>'
st.markdown(new_title2, unsafe_allow_html=True)
new_title3 = '<p style="font-family:sans-serif; font-size: 20px;text-align: left;"><br> Based on this data, an ensemble model was pre-trained. Users can enter data in the below fields which is given as input for the model. For the entered data, the application predicts the life expectancy[in yrs].This output is interpreted as an average life expectancy for a country.    </p>'
st.markdown(new_title3, unsafe_allow_html=True)
new_title4 = '<p style="font-family:sans-serif; font-size: 25px;text-align: left;color:blue;"><br>Enter the following details</p>'
st.markdown(new_title4, unsafe_allow_html=True)
page_bg_img = """
<style>
.stApp {
background-image: url("https://static.vecteezy.com/system/resources/thumbnails/002/221/733/original/abstract-flowing-light-ombre-gradient-background-free-video.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    Adult_Mortality = st.number_input('Enter the adult mortality rate:')
with col2:
    Infant_Deaths = st.number_input('Enter the Number of Infant Deaths per 1000 population:')
with col1:
    Alcohol = st.number_input('Enter the Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol):')
with col2:
    Expenditure_Percentage = st.number_input('Enter the expenditure on health as a percentage of Gross Domestic Product per capita(%):')
with col1:
    Hepatitis_B = st.number_input('Enter the Hepatitis B (HepB) immunization coverage among 1-year-olds (%):')
with col2:
    Measles = st.number_input('Enter the number of Measles reported cases per 1000 population')
with col1:
    BMI = st.number_input('Enter the average Body mass index of the entire population')
with col2:
    Polio = st.number_input('Enter Polio (Pol3) immunization coverage among 1-year-olds (%):')
with col1:
    Diphtheria = st.number_input('Enter the Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%):')
with col2:
    HIV_AIDS = st.number_input('Enter number of Deaths per 1 000 live births HIV/AIDS (0-4 years):')
with col1:
    GDP = st.number_input('Enter Gross Domestic Product per capita (in USD):')
with col2:
    Population = st.number_input('Enter Population of the country:')
with col1:
    Thinness_10_19_years = st.number_input('Enter Prevalence of thinness among children and adolescents for Age 10 to 19 (% ):')
with col2:
    Thinness_5_9_years = st.number_input('Enter Prevalence of thinness among children for Age 5 to 9(%):')
with col1:
    Income_composition = st.number_input('Enter Human Development Index in terms of income composition of resources (index ranging from 0 to 1):')    
with col2:
    Schooling = st.number_input('Enter Number of years of Schooling(years):')    
button_placeholder = st.empty()

# Create a button to display the DataFrame in the center
if all([Adult_Mortality, Infant_Deaths, Alcohol, Expenditure_Percentage, Hepatitis_B,
        Measles, BMI, Polio, Diphtheria, HIV_AIDS, GDP, Population, Thinness_10_19_years,
        Thinness_5_9_years, Income_composition, Schooling]):


    # Create DataFrame
    columns = ['Adult Mortality', 'Infant Deaths', 'Alcohol', 'Expenditure Percentage',
               'Hepatitis B', 'Measles', 'BMI', 'Polio', 'Diphtheria', 'HIV/AIDS',
               'GDP', 'Population', 'Thinness 1-19 years', 'Thinness 5-9 years',
               'Income Composition', 'Schooling']

    data = {
        'Adult Mortality': [Adult_Mortality],
        'Infant Deaths': [Infant_Deaths],
        'Alcohol': [Alcohol],
        'Expenditure Percentage': [Expenditure_Percentage],
        'Hepatitis B': [Hepatitis_B],
        'Measles': [Measles],
        'BMI': [BMI],
        'Polio': [Polio],
        'Diphtheria': [Diphtheria],
        'HIV/AIDS': [HIV_AIDS],
        'GDP': [GDP],
        'Population': [Population],
        'Thinness 1-19 years': [Thinness_10_19_years],
        'Thinness 5-9 years': [Thinness_5_9_years],
        'Income Composition': [Income_composition],
        'Schooling': [Schooling]
    }

    df = pd.DataFrame(data, columns=columns)
    new_title3 = '<p style="font-family:sans-serif; font-size: 20px;text-align: left;"><br>The entered data is</p>'
    st.markdown(new_title3, unsafe_allow_html=True)
    # Display the DataFrame
    st.dataframe(df)
    col1, col2, col3 , col4, col5,col6,col7 = st.columns(7)
    if col4.button('Check Prediction'):
        prediction = loaded_model.predict(df)
        st.success(f'The predicted life expectancy is: {prediction}')
        new_title4 = '<p style="font-family:sans-serif; font-size: 25px;text-align: left;"><br>Visualization</p>'
        st.markdown(new_title4, unsafe_allow_html=True)
        new_title5 = '<p style="font-family:sans-serif; font-size: 20px;text-align: left;"><br> This visualization plots the predicted life expectancy value for the entered data among the previously present life expectancy values of other countries. This gives the user an idea to evalaute different factors that affect life expectancy. </p>'
        st.markdown(new_title5, unsafe_allow_html=True)
        fig = px.scatter(df_train, y="Life expectancy ",title='Actual vs Predicted Life Expectancy',labels={'Life Expectancy': 'Training Data'}) 
        fig.add_trace(go.Scatter(y=prediction,mode='markers',marker=dict(color='red'),marker_symbol = 'star',marker_size = 15,name='Predicted Life Expectancy'))
        fig.update_layout(title_text='Comparison between Actual Vs. Predicted life Expectancy', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_size=18, font_color='white')
        with st.container(): 
            st.plotly_chart(fig,use_container_width=True)

else:
    st.warning("Please fill in all the fields before checking the prediction.")
