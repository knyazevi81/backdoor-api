from fastapi import APIRouter
from database.db import Database
from database.models import Computer


route = APIRouter(tags=["employer"])


@route.post("/register")
def register_my_pc(pc_name: int):
    pass
