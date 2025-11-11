from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from bson import ObjectId
from services.database import fs

router = APIRouter()

@router.post("/delete_images")
async def delete_images(request: Request):
    form_data = await request.form()
    selected_ids = form_data.getlist("selected_images")

    if not selected_ids:
        return HTMLResponse("<h3>No images selected.</h3><a href='/api/gallery'>Back</a>")

    deleted = 0
    for image_id in selected_ids:
        try:
            fs.delete(ObjectId(image_id))
            deleted += 1
        except:
            pass

    return HTMLResponse(f"<h3>✅ Deleted {deleted} image(s).</h3><a href='/api/gallery'>Back</a>")
