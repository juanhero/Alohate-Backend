from db.roomTypes_db import roomTypesInDB
from db.roomTypes_db import update_room, get_room
from db.user_db import UserInDB
from db.user_db import update_user, get_user

from models.roomTypes_models import RoomIn, RoomOut
from models.user_models import UserIn, UserOut

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

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):#Recibe el usuario
    user_in_db = get_user(user_in.username)#Verifica si el usuario existe
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in.password != user_in_db.password:
        raise HTTPException(status_code=403, detail="Contraseña incorrecta")
    return {"Existe": True}

@api.put("/room/reserve/{roomName}")
async def make_reserve(roomName: str):
    room_in_db = get_room(roomName)

    if room_in_db == None:
        raise HTTPException(status_code=404, detail="La habitación no existe")

    if room_in_db.available == False:
        raise HTTPException(status_code=403, detail="La habitación no esta disponible")
        
    room_in_db.available = False 
    update_room(room_in_db) 

    return True
