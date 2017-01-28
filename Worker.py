import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging


def fetch_data():
    token = '019c63269f1f45e3'
    url = 'http://api.wunderground.com/api/' + token + '/conditions/q/CA/San_Francisco.json'
    r = requests.get(url).json()
    data = r['current_observation']

    location = data['observation_location']['full']
    weather = data['weather']
    wind_str = data['wind_string']
    temp = data['temp_f']
    humidity = data['relative_humidity']
    precip = data['precip_today_string']
    icon_url = data['icon_url']
    observation_time = data['observation_time']


    print('Location ' , location , ' Weather ', weather, ' Wind_str ', wind_str, ' Temp ', temp, ' humidity ',  humidity, ' Precip ', precip, ' icon_url ', icon_url, ' observation time ', observation_time)



    # open db
    try:
        conn = psycopg2.connect(dbname='weather', user='postgres', host='localhost', password='', port=5433)
        print('Open DB successfully')
    except:
        print(datetime.now(), 'Unable to connect to the database')
        logging.exception('Unable to connect to the database')
        return
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # write data to DB
    cur.execute("""INSERT INTO "Station_reading" (location, weather, wind_str, temp, humidity, precip, icon_url, observation_time)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""", (location, weather, wind_str, temp, humidity, precip, icon_url, observation_time))


    conn.commit()
    cur.close()
    conn.close()

    print('Data Write', datetime.now())

fetch_data()



