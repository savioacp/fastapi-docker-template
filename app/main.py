import fastapi
from .controllers import index_controller

app = fastapi.FastAPI()


@app.get("/")
def index():
    return index_controller.index()
