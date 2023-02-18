# station.py

from datetime import datetime
from flask import abort, make_response
import uuid
import sensor as sn
import observation as ms
import my_database as db

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    return list(db.STATION.values())

def create(station):
    name = station.get("name")
    description = station.get("description")
    lat = station.get("lat")
    lon = station.get("lon")
    alt = station.get("altitude")
    my_uuid = str(uuid.uuid4())

    if name and name not in db.STATION:
        db.STATION[name] = {
            "name": name,
            "description": description,
            "uuid": my_uuid,
            "lat": lat,
            "lon": lon,
            "alt": alt,
            "timestamp": get_timestamp(),
            "sensors": [sn.create(s,station=uuid) for s in (station.get("sensors") or [])],
        }
        return db.STATION[name], 201
    else:
        abort(
            406,
            f"Station with name {name} already exists",
        )
def read_one(name):
    if name in db.STATION:
        return db.STATION[name]
    else:
        abort(
            404, f"Station with name {name} not found"
        )
def update(name, station):
    if name in db.STATION:
        db.STATION[name]["timestamp"] = get_timestamp()
        return db.STATION[name]
    else:
        abort(
            404,
            f"Station with name {name} not found"
        )

def delete(name):
    if name in db.STATION:
        del db.STATION[name]
        return make_response(
            f"{name} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Station with name {name} not found"
        )
