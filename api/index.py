from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from routes.home import router as home_router
from routes.gallery import router as gallery_router
from routes.images import router as images_router
from routes.delete import router as delete_router

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes with /api prefix
app.include_router(home_router, prefix="/api")
app.include_router(gallery_router, prefix="/api")
app.include_router(images_router, prefix="/api")
app.include_router(delete_router, prefix="/api")
