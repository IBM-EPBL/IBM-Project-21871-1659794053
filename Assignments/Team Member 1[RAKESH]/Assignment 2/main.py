import random
import time
while (1):
    Temperature = random.randint(0, 100)
    Humidity = random.randint(0, 100)
    if Temperature>60 and Humidity>60:
        print("ALERT!! Detected temperature: " + str(Temperature) + "°C" + " " + "Detected humidity: " + str(Humidity))
    elif Temperature > 60:
        print("ALERT!! Detected temperature: " + str(Temperature) + "°C")
    elif Humidity > 60:
        print("ALERT!! Detected humidity: " + str(Humidity))
    time.sleep(1)