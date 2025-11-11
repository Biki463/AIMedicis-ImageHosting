from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from services.database import fs

router = APIRouter()

@router.get("/gallery", response_class=HTMLResponse)
def gallery():
    files = list(fs.find())

    if not files:
        return HTMLResponse("<h3>No images found in MongoDB 😢</h3>")

    html = """
    <html>
    <head>
        <title>MongoDB Image Gallery</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f5f5f5; text-align: center; }
            form { display: inline-block; }
            .gallery { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 30px; }
            .card { background: white; padding: 10px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); width: 220px; }
            img { width: 200px; height: auto; border-radius: 8px; }
            h4 { margin: 8px 0; font-size: 14px; color: #444; }
            input[type=checkbox] { transform: scale(1.5); margin-top: 10px; }
            button { margin-top: 20px; padding: 8px 20px; font-size: 15px; border: none; background-color: #ff4d4d; color: white; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #e60000; }
        </style>
    </head>
    <body>
        <h2>🖼️ Image Gallery</h2>
        <form method="post" action="/api/delete_images">
            <div class='gallery'>
    """

    for f in files:
        img_url = f"/api/images/{f._id}"
        html += f"""
        <div class='card'>
            <img src='{img_url}' alt='{f.filename}' />
            <h4>{f.filename}</h4>
            <input type="checkbox" name="selected_images" value="{f._id}">
        </div>
        """

    html += """
            </div>
            <button type="submit">🗑️ Delete Selected</button>
        </form>
    </body></html>
    """
    return HTMLResponse(html)
