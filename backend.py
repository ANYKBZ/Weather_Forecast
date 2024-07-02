import requests
API_KEY = 75dcd59c7d0083abd85b77b793609c35

def get_data(place, forecast_days, kind):
    url = f"api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ =="__main__":
    get_data()
