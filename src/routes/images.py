from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from bson import ObjectId
from Database.database import fs

router = APIRouter()

@router.get("/images/{image_id}")
def get_image(image_id: str):
    try:
        grid_out = fs.get(ObjectId(image_id))
        return Response(content=grid_out.read(), media_type="image/png")
    except:
        raise HTTPException(status_code=404, detail="Image not found")
