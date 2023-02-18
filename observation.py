# observation123.py

from datetime import datetime
from flask import abort, make_response
import uuid
import my_database as db

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    return list(db.MEASUREMENT.values())

def create(observation123, sensor=None):
    name = observation123.get("name")
    description = observation123.get("description")
    lat = observation123.get("lat")
    lon = observation123.get("lon")
    alt = observation123.get("altitude")
    unit = observation123.get("unit")
    my_uuid = str(uuid.uuid4())
    parent = sensor

    if name and name not in db.MEASUREMENT:
        db.MEASUREMENT[name] = {
            "name": name,
            "description": description,
            "uuid": my_uuid,
            "lat": lat,
            "lon": lon,
            "alt": alt,
            "unit": unit,
            "timestamp": get_timestamp(),
            "parent": parent,
        }
        return db.MEASUREMENT[name], 201
    else:
        abort(
            406,
            f"Observation123 with name {name} already exists",
        )
def read_one(name):
    if name in db.MEASUREMENT:
        return db.MEASUREMENT[name]
    else:
        abort(
            404, f"Observation123 with name {name} not found"
        )
def update(name, observation123):
    if name in db.MEASUREMENT:
        db.MEASUREMENT[name]["timestamp"] = get_timestamp()
        return db.MEASUREMENT[name]
    else:
        abort(
            404,
            f"Observation123 with name {name} not found"
        )

def delete(name):
    if name in db.MEASUREMENT:
        del db.MEASUREMENT[name]
        return make_response(
            f"{name} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Observation123 with name {name} not found"
        )
