from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

load_dotenv()

NGROK_TOKEN = os.getenv("NGROK_TOKEN")


import uvicorn

HOST = "0.0.0.0"
PORT = int("8000")
USE_NGROK = True 

app = FastAPI()

if USE_NGROK:
    from pyngrok import ngrok

    # https://dashboard.ngrok.com/get-started/your-authtoken
    ngrok.set_auth_token(NGROK_TOKEN)

    public_url = ngrok.connect(PORT).public_url
    print(f"ngrok tunnel {public_url}")


#app.include_router(auth_route)
#app.include_router(admin_route)

if __name__ == '__main__':
    print(f"API rinnung {HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)