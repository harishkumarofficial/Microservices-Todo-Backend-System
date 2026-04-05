from fastapi import FastAPI
from app.api.routes.todo_routes import router as todo_router
from app.api.routes.user_status_routes import router as user_status_routers

app = FastAPI()

app.include_router(todo_router)
app.include_router(user_status_routers)