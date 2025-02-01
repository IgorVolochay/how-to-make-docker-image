import json
import random

from fastapi import FastAPI, APIRouter

class Jokes:
    def __init__(self):
        with open("./dataset.json", "r") as dataset:
            self.jokes_list:list = json.load(dataset)["jokes"]
        dataset.close()
        self.router = APIRouter()
        self.set_urls()

    def set_urls(self):
        self.router.add_api_route("/get_joke", self.get_random_joke, methods=["GET"])
    
    async def get_random_joke(self):
        return {"joke": random.choice(self.jokes_list)}


app = FastAPI()
jokes = Jokes()
app.include_router(jokes.router)