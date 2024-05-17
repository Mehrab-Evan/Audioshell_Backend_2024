from fastapi import APIRouter
# from api.login import login
from api.login import router as login_router

api_router = APIRouter()

# Include other routers here as needed
api_router.include_router(login_router, tags=["login"])
# You can include more routers here for other functionalities
# api_router.include_router(login.router, tags=["login"])
# You can include more routers here for other functionalities

# No need to define endpoints here, just include other routers
