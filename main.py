import streamlit as st
import plotly.express as px 
from backend import get_data


# add title, text input, slider, and select box, and subheader 
st.header("Weather Forecase for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value =1, max_value = 5, help="Select  the number of forecasted days")

option = st.selectbox("Select data to veiw", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {place.title()}")


if place:


    # Get the city timeline and temp/sky data
    filter_data = get_data(place,days)
    if filter_data == "page not found":
        st.info("Please Enter the correc city name")
    else:

        if option == "Temperature":
            temperatures = [dict['main']['temp']/10 for dict in filter_data]
            print(temperatures)
            dates = [dict["dt_txt"] for dict in filter_data]
            #Create the temparature/sky data
            fig = px.line(x=dates, y=[temp / 10 for temp in temperatures] , labels={"x": "Date","y":"Temparatures (C)"})
            st.plotly_chart(fig)


        if option == "Sky":
            sky_conditions = [dict['weather'][0]['main']  for dict in filter_data]
            images = {
                "Clear":"images/clear.png",
                "Clouds":"images/cloud.png",
                "Snow":"images/snow.png",
                "Rain":"images/rain.png"
                }
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image=image_path, width=115)
            