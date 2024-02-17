from fastapi import APIRouter

route = APIRouter(tags=["dash_proces"])


@route.get("/dashboard")
async def send_pc_status():
    pass