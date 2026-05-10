#will contain two API 
#current weather API & Geocoding API
import requests

#return coordinates , while handling exception
def get_coordinate(s):
    while True:
        country_code = input("Country code: ").upper()
        state = input("State name: ").capitalize()
        city = input("City name: ").capitalize()

        try:
            coord = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?"
                                 f"q={city},{state},{country_code}&limit=1&appid={s}")
        except requests.exceptions.ConnectionError:
            print("No Internet")
            continue
        except requests.exceptions.Timeout:
            print("Request Timed Out")
            continue
        except requests.RequestException:
            print("Request Error")
            continue
        for coords in coord.json():
            x= coords["lat"]
            y=coords["lon"]
        
        return x,y,city 


#returning weather, while handling exception
def get_weather(s,x,y):
    try:
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather"
                           f"?lat={x}&lon={y}&appid={s}")
    except requests.exceptions.ConnectionError:
        return "No Internet"        
    except requests.exceptions.Timeout:
        return "Request Timed Out"   
    except requests.RequestException:
        return "Request Error"
    
    #converting in json file
    weather =weather.json()
    
    #in weather->key("weather")-> value(a list)->
    # at 0 index->dict.->key("description")->weather cond
    weather_cond = weather["weather"][0]["description"]  

    #in weather->key("main")->dict.-> have all required values
    temp = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"]
    humidity = weather["main"]["humidity"]
    
    return weather_cond,temp,feels_like,humidity



if __name__=="__main__": #runs only when you run this file, not when import in other
    #get_coordinate("eb1e43412af9c1e2de5b0cde0114e9ed")  
    get_weather("eb1e43412af9c1e2de5b0cde0114e9ed","51.5073219","-0.1276474") 
    