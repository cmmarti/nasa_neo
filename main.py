from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/feed/today")
def feed(request=Request):
    return templates.TemplateResponse("feed.html", {
        "request": request
    })
