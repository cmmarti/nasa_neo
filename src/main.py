from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import repo

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/feed")
def feed(request=Request):
    response = repo.feed()

    return response

    # return templates.TemplateResponse("feed.html", {
    #     "request": request
    # })
