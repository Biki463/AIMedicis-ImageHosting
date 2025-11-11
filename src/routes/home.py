from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>🩺 PDF Image Viewer</h2>
    <p>Visit <a href='/api/gallery'>Gallery</a> to see all stored images.</p>
    """
