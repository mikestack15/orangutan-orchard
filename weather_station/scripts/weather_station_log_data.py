import string
import time
import os
from typing import NoReturn
import pandas as pd
from datetime import datetime

from weather_station_secrets import DATA_PATH
from weather_station_utilities import get_date_string

# Libraries for BME280.
import bme280
import smbus2

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Button module for magnet switches.
from gpiozero import Button

# Global timing constant. Data is dumped every hour. 60 records are recorded.
NUMBER_OF_ONE_MINUTE_INTERVALS = 60

# Data capture window for one record is 60 seconds.
MECH_DATA_COLLECT_WINDOW_SECONDS = 30
DATA_WINDOW_REMAINDER_SECONDS = 60 - MECH_DATA_COLLECT_WINDOW_SECONDS

# Hardware configuration for BME280.
BME_PORT = 1
BME_ADDRESS = 0x77 # Adafruit BME280 address. Other BME280s may be different.
BME_BUS = smbus2.SMBus(BME_PORT)
bme280.load_calibration_params(BME_BUS,BME_ADDRESS)

# Hardware SPI configuration  for MCP 3008.
SPI_PORT   = 0
SPI_DEVICE = 0
MCP = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Hardware configuration for rainfall and wind sensors.
RAINFALL_SENSOR = Button(16)
WIND_SPEED_SENSOR = Button(26)
WIND_TIME_INTERVAL = 10

# Rain and wind variables.
rainfall_count = 0
wind_switch_closures = 0
wind_interval = 10
wind_radius = 3

def get_bme_data() -> dict:
    bme280_data = bme280.sample(BME_BUS,BME_ADDRESS)
    return {"humidity":bme280_data.humidity,"temperature": bme280_data.temperature, "pressure":bme280_data.pressure}

def reset_sensor_counts() -> None:
    global rainfall_count
    global wind_switch_closures
    rainfall_count = 0
    wind_switch_closures = 0

def iterate_rainfall_count() -> None:
    global rainfall_count
    rainfall_count += 1

def iterate_wind_switch_count() -> None:
    global wind_switch_closures
    wind_switch_closures += 1

def get_rainfall_reading() -> int:
    # 20 drops of rain per ml.
    MDCWS = MECH_DATA_COLLECT_WINDOW_SECONDS
    DWRS = DATA_WINDOW_REMAINDER_SECONDS

    if rainfall_count == 0:
        return 0
    return rainfall_count / (MDCWS / (MDCWS + DWRS)) / 20

def get_wind_speed_reading() -> int:
    # Calculation from spec sheet: 2.4 km/h is roughly 1 closure per second.
    if wind_switch_closures == 0:
        return 0
    print(f"\n\n{wind_switch_closures}\n\n")
    return (wind_switch_closures / MECH_DATA_COLLECT_WINDOW_SECONDS * 2.4)

def get_wind_direction() -> int:
    #Read the ADC channel for voltage.
    voltage = int(MCP.read_adc(7))

    # Apprximate voltage ranges corresponding to each direction.

    # North
    if (voltage in range(0,70)):
        return 0
    
    # NorthEast
    elif (voltage in range(70, 120)):
        return 45
    
    # East
    elif voltage in range(120, 200):
        return 90

    # NorthWest
    elif voltage in range(200, 300):
        return 315

    # SouthEast
    elif voltage in range(300, 400):
        return 135

    # West
    elif voltage in range(400, 675):
        return 270

    # SouthWest
    elif voltage in range(675, 700):
        return 225

    # South
    elif voltage in range(700, 900):
        return 180

    # return -1 to indicate an error in the reading or a short.
    else:
        return -1

def get_weather_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(columns=['humidity','temperature','pressure','wind_direction','wind_speed','rainfall'])

    """Reset all switch state counters (wind and rainfall), set a timer for a collection window, 
        record the number of switch closures in the collection window, gather BME data, wait for the buffer
        window and concatenate all data to a DataFrame.
    """
    for i in range(NUMBER_OF_ONE_MINUTE_INTERVALS):
        reset_sensor_counts()
        RAINFALL_SENSOR.when_pressed = iterate_rainfall_count
        WIND_SPEED_SENSOR.when_pressed = iterate_wind_switch_count
        time.sleep(MECH_DATA_COLLECT_WINDOW_SECONDS)

        bme_dict = get_bme_data()

        humidity = int(bme_dict["humidity"])
        temperature = int(bme_dict["temperature"])
        pressure = int(bme_dict["pressure"])
        rainfall_ml_hr = int(get_rainfall_reading())
        wind_km_hr = int(get_wind_speed_reading())
        wind_direction = int(get_wind_direction())

        # print(f"\n \
        #     Humidity: {humidity} \n \
        #     Temperature: {temperature} \n \
        #     Pressure: {pressure} \n \
        #     Rainfall: {rainfall_ml_hr} \n \
        #     Wind_speed: {wind_km_hr} \n \
        #     wind_direction: {wind_direction} \n \
        # ")

        time.sleep(DATA_WINDOW_REMAINDER_SECONDS)
        concat_df = pd.DataFrame(
            [[humidity, temperature, pressure, wind_direction, wind_km_hr, rainfall_ml_hr]], 
            columns= ['humidity','temperature','pressure','wind_direction','wind_speed','rainfall']
        )  
        df = pd.concat([df, concat_df], ignore_index=True)
    return df

def main() -> None:
    """Create a new CSV file every 30 minutes, write a line of data every minute,
     and finally close file"""
    os.chdir(DATA_PATH)
    while(True):
        csv_file_name = get_date_string()
        df = get_weather_dataframe()
        df.to_csv(f"{csv_file_name}.csv")

if __name__ == "__main__":
    main()