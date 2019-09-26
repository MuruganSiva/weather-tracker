import requests
import csv
import datetime, os, sys

#api endpoint
URL = "https://api.openweathermap.org/data/2.5/weather?zip=27523,us&appid=9c61800f2c5a80e734ecf74c97fdb6f7"

#params
zip = "27523"
country = "us"
appid = "9c61800f2c5a80e734ecf74c97fdb6f7"

PARAMS = {'zip': zip + ','+ country , appid : appid}

# create HTTP request
httpclient = requests.get(url = URL, params = PARAMS)

# get the response as JSON
current_data = httpclient.json()

# write the response to csv
filename = os.path.join(sys.path[0], 'weather_data.csv')

with open(filename, mode= 'a') as weather_file:
    weather_writer = csv.writer(weather_file, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #append to the csv
    weather_writer.writerow([datetime.datetime.now().strftime("%m-%d-%Y"),
     current_data['main']['temp'],
     current_data['main']['temp_max'],
     current_data['main']['temp_min'],
     current_data['main']['humidity']
     ])

    print("Data written to the csv;from git update")
