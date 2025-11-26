from fastapi import FastAPI
from .routes import router
import uvicorn
def create_api():
    app = FastAPI()
    app.include_router(router)
    return app

def run_api():
    options = {
        "host" :'0.0.0.0',
        "port" : 8000,
        "reload" : True
    }
    uvicorn.run("src.app:create_api",**options)