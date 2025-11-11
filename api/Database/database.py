import os
from pymongo import MongoClient
import gridfs

# ⚠️ Do NOT use fallback here. Vercel must provide this.
MONGO_URI = "mongodb+srv://21cs191:biki12345@cluster0.nberai4.mongodb.net/"  # Raises error if not provided

client = MongoClient(MONGO_URI)

# Choose your DB
db = client["pdf_image_extraction"]

# Enable GridFS
fs = gridfs.GridFS(db)
