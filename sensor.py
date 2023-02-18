# sensor.py

from datetime import datetime
from flask import abort, make_response
import uuid
import observation as mm
import my_database as db

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    return list(db.SENSOR.values())

def create(sensor, station=None):
    name = sensor.get("name")
    description = dsensor.get("description")
    lat = sensor.get("lat")
    lon = sensor.get("lon")
    alt = sensor.get("altitude")
    my_uuid = str(uuid.uuid4())

    if name and name not in SENSOR:
        db.SENSOR[name] = {
            "name": name,
            "description": description,
            "my_uuid": my_uuid,
            "lat": lat,
            "lon": lon,
            "alt": alt,
            "observation123s": [mm.create(m,sensor=my_uuid) for m in (sensor.get("observation123s") or [])],
            "timestamp": get_timestamp(),
        }
        return SENSOR[name], 201
    else:
        abort(
            406, f"Sensor with name {name} already exists",
        )
def read_one(name):
    if name in db.SENSOR:
        return db.SENSOR[name]
    else:
        abort(
            404, f"Sensor with name {name} not found"
        )
def update(name, sensor):
    if name in db.SENSOR:
        db.SENSOR[name]["timestamp"] = get_timestamp()
        return db.SENSOR[name]
    else:
        abort(
            404,
            f"Sensor with name {name} not found"
        )

def delete(name):
    if name in db.SENSOR:
        del db.SENSOR[name]
        return make_response(
            f"{name} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Sensor with name {name} not found"
        )
