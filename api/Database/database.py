import os
from pymongo import MongoClient
import gridfs

# ⚠️ Do NOT use fallback here. Vercel must provide this.
MONGO_URI = os.environ.get("MONGO_URI")  # Raises error if not provided
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")

client = MongoClient(MONGO_URI)

# Choose your DB
db = client[COLLECTION_NAME]

# Enable GridFS
fs = gridfs.GridFS(db)
