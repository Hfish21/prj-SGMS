from mongoengine import *
import hug
import mongoengine
from datetime import datetime, timedelta
from pprint import pprint
from random import randint
import random
import json
from bson.objectid import ObjectId
from pymongo import MongoClient

connect('DMK1_DATA', host='127.0.0.1', port=27017)

class SensorLog(Document):
    created_on = DateTimeField(required=True, default=datetime.utcnow)
    temperature = FloatField(required=True, default=0.00)
    humidity = FloatField(required=True, default=0.00)
    barometric_pressure = FloatField(required=True, default=0.00)
    solar_radiation = FloatField(required=True, default=0.00)
    soil_moisture = FloatField(required=True, default=0.00)

    def display(self):
        output = '''Temp - {0}
        Humd - {1}
        BarP - {2}
        SolR - {3}
        Soil - {4}'''.format(self.temperature, self.humidity, self.barometric_pressure, self.solar_radiation, self.soil_moisture)

        print(output)

    def to_dict(self):
        log_dict = {
                "TEMP" : self.temperature,
                "HUMD" : self.humidity,
                "BARP" : self.barometric_pressure,
                "SOLR" : self.solar_radiation,
                "SOIL" : self.soil_moisture
                }

        return log_dict
