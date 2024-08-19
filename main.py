import json
from function import *

import streamlit as st
import requests

st.title("SMI WEATHER APPLICATION")
user_option = st.text_input("ENTER LOCATION", placeholder="Get Weather Info of Any Location")

# api = "http://api.weatherapi.com/v1/current.json?key=e09fb8315197455dac1115933231611&q=London&aqi=yes"
api2 = f"http://api.weatherapi.com/v1/current.json?key=e09fb8315197455dac1115933231611&q={user_option}&aqi=yes"
# getAPI = requests.get(api).json()
getAPI = requests.get(api2).json()

user_location = getAPI["location"]["name"]
st.subheader("Weather Information")

Temperature = getAPI["current"]["temp_c"]
AtmosphericCondition = getAPI["current"]["condition"]["text"]
WindSpeed = getAPI["current"]["wind_kph"]
wind_degree = getAPI["current"]["wind_degree"]
wind_dir = getAPI["current"]["wind_dir"]
Precipitation = getAPI["current"]["precip_mm"]
Humidity = getAPI["current"]["humidity"]
DewPoint = getAPI["current"]["dewpoint_c"]
Ultraviolet = getAPI["current"]["uv"]
Amount_of_Carbon_In_Air = getAPI["current"]["air_quality"]["co"]

if not user_option:
    st.warning("Please enter a location")
elif user_option == user_location:
    st.info(f"""Weather Information below based on your present location\n
Temperature: {Temperature}_c\n
Atmospheric Condition: {AtmosphericCondition}\n
Wind Speed: {WindSpeed}kph\n
Wind Degree & Direction: {wind_degree}{wind_dir}\n
Precipitation: {Precipitation}\n
Humidity: {Humidity}\n
Dew Point: {DewPoint}\n
Ultraviolet: {Ultraviolet}\n
The Amount Of Carbon In Air: {Amount_of_Carbon_In_Air}
""")
elif user_option != user_location:
    st.warning(f"{user_option} weather information is presently not available")
else:
    st.error("Invalid")

