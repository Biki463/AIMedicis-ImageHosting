"""
Main FastAPI Application
This is the development entry point. 
For Vercel deployment, use api/index.py
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.home import router as home_router
from routes.gallery import router as gallery_router
from routes.images import router as images_router
from routes.delete import router as delete_router

app = FastAPI(title="AIMedicis Image Hosting", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(home_router)
app.include_router(gallery_router)
app.include_router(images_router)
app.include_router(delete_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

