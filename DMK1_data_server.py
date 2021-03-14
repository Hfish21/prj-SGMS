import hug
import mongoengine
from datetime import datetime, timedelta
from random import randint
import random
import json
from bson.objectid import ObjectId
from pymongo import MongoClient
from models import SensorLog


@hug.post('/data')
def create_data(text):
    data_list = text.split('/')

    log = SensorLog()
    log.temperature = float(data_list[0])
    log.humidity = float(data_list[1])
    log.barometric_pressure = float(data_list[2])
    log.solar_radiation = float(data_list[3])
    log.soil_moisture = float(data_list[4])

    log.save()
    log.display()

@hug.get('/data')
def retreive_data():

    logs = []

    for l in SensorLog.objects():
        logs.append(l.to_dict())

    return logs
