from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from .game import GameState

game = GameState()

app = FastAPI()
app.mount("/game", StaticFiles(directory="./client", html=True), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/game/index.html")

@app.post("/join")
async def join(name: Annotated["str", Form()]):
    print("joining game")
    game.add_player(name)
    return {"username": name}

# @app.post("/action")
# async def action():
#     pass
