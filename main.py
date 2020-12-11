from db.roomTypes_db import roomTypesInDB
from db.roomTypes_db import update_room, get_room

from models.roomTypes_models import RoomIn, RoomOut

import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()


@api.get("/room/type/{roomName}")#Recibe la habitacion en la url
async def get_roomType(roomName: str):
    room_in_db = get_room(roomName)#Verifica si la habitacion existe
    if room_in_db == None:
        raise HTTPException(status_code=404, detail="La habitación no existe")

    room_out = RoomOut(**room_in_db.dict())#Mapea la habitacion al RoomOut
    return room_out

@api.post("/room/auth/")
async def auth_room(room_in: RoomIn):#Recibe la habitacion
    room_in_db = get_room(room_in.roomName)#Verifica si la habitacion existe
    if room_in_db == None:
        raise HTTPException(status_code=404, detail="La habitación no existe")
    return {"Existe": True}