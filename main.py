import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")
if place:
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperature = [dict["main"]["temp"]/10 for dict in filtered_data]
            print(type(temperature))
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "weather_images/clear.png", "Clouds": "weather_images/cloud.png", "Rain": "weather_images/rain.png", "Snow": "weather_images/Snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=110)
    except KeyError:
        st.write("Incorrect City Name")
