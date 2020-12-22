from typing import Dict
from pydantic import BaseModel

class roomTypesInDB(BaseModel):
    roomName: str
    roomType: str
    value: int
    available: bool

database_roomName = Dict[str, roomTypesInDB]
database_roomName = {
    "201": roomTypesInDB(**{"roomName":"201",
                            "roomType":"Sencillo",
                            "value":12000,
                            "available": True}),
    "202": roomTypesInDB(**{"roomName":"202",
                            "roomType":"Doble",
                            "value":34000,
                            "available": True}),
    "301": roomTypesInDB(**{"roomName":"301",
                            "roomType":"Pent - House",
                            "value":34000,
                            "available": True}),
    "302": roomTypesInDB(**{"roomName":"302",
                            "roomType":"King",
                            "value":34000,
                            "available": True}),
    "401": roomTypesInDB(**{"roomName":"401",
                            "roomType":"Queen",
                            "value":34000,
                            "available": True}),
}

def get_room(roomName: str):
    if roomName in database_roomName.keys():
        return database_roomName[roomName]
    else:
        return None

def update_room(room_in_db: roomTypesInDB):
    database_roomName[room_in_db.roomName] = room_in_db
    return room_in_db