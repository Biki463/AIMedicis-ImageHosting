from fastapi import FastAPI
from routes.home import router as home_router
from routes.gallery import router as gallery_router
from routes.images import router as images_router
from routes.delete import router as delete_router

app = FastAPI()

# Add routes
app.include_router(home_router)
app.include_router(gallery_router)
app.include_router(images_router)
app.include_router(delete_router)
