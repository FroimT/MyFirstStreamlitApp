import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Hello Wilders, welcome to my application!')


st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.write(df_cars)

#st.line_chart(df_weather['MAX_TEMPERATURE_C'])


viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

st.write("We see a negative correlation between mpg and the size of the cars engines, i.e. cylinders, cubicinches and horsepower. Accordingly we see a positive correlation between the cars weights and these parameters")

region = st.text_input("Let's filter by region (US, Europe, Japan):")

df_cars.loc[df_cars['continent'].str.contains(region)]