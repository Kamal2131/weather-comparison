from fastapi import FastAPI
import os

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import compare, home, info

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



app.include_router(home.router)
app.include_router(compare.router)
app.include_router(info.router)


