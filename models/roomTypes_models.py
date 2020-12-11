from pydantic import BaseModel

class RoomIn(BaseModel):
    roomName: str

class RoomOut(BaseModel):
    roomName: str
    roomType: str
    value: int