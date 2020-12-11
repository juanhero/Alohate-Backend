from typing import Dict
from pydantic import BaseModel

class roomTypesInDB(BaseModel):
    roomName: str
    roomType: str
    value: int

database_roomName = Dict[str, roomTypesInDB]
database_roomName = {
    "201": roomTypesInDB(**{"roomName":"201",
                            "roomType":"sencillo",
                            "value":12000}),
    "202": roomTypesInDB(**{"roomName":"202",
                            "roomType":"doble",
                            "value":34000}),
    "301": roomTypesInDB(**{"roomName":"301",
                            "roomType":"pent - house",
                            "value":34000}),
    "302": roomTypesInDB(**{"roomName":"302",
                            "roomType":"king",
                            "value":34000}),
    "401": roomTypesInDB(**{"roomName":"401",
                            "roomType":"queen",
                            "value":34000}),
}

def get_room(roomName: str):
    if roomName in database_roomName.keys():
        return database_roomName[roomName]
    else:
        return None

def update_room(room_in_db: roomTypesInDB):
    database_roomName[room_in_db.roomName] = room_in_db
    return room_in_db