import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from db_api import app as db_api
from logic_api import app as logic_api

app = FastAPI()

app.include_router(db_api)
app.include_router(logic_api)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)