import atheris 
import sys
import zlib 
import requests
#testing response and request flow
def fuzz_testing(data): 
    inp = data.decode("UTF-8")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_value}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200: 
        raise ValueError(f"Unexpected response: {response.status_code}")
#testing data validation
def data_wrangling(data):
    inp = data.decode("UTF-8")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_value}&appid={api_key}&units=metric"
    response = requests.get(url)
    if not isinstance(inp, str):
        print(f"Non-string input triggered: {input_data}")
        return
atheris.Setup()
atheris.Fuzz(fuzz_testing, data_wrangling)
