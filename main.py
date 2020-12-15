from db.roomTypes_db import roomTypesInDB
from db.roomTypes_db import update_room, get_room

from models.roomTypes_models import RoomIn, RoomOut

import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

####################################################
from fastapi.middleware.cors import CORSMiddleware
origins = [     #Origenes desde donde se permitira entrar a la app
    "http://localhost.tiangolo.com", 
    "https://localhost.tiangolo.com",
    "http://localhost", 
    "http://localhost:8080",
    "https://alohate-frontend.herokuapp.com",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,  #Agregar esos origenes al CORS
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
#####################################################

@api.get("/room/type/{roomName}")#Recibe la habitacion en la url
async def type_room(roomName: str):
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