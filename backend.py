import requests
import pandas as pd

API_key = ""


def get_data(place,forecast_days=None):
    
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    nr_value = 8*forecast_days
    filter_data = filter_data[:nr_value]

    return filter_data
    

    
if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast_days=2))
