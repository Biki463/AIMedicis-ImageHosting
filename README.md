# 🩺 AIMedicis Image Hosting

A FastAPI-based image gallery application with MongoDB GridFS backend for storing, retrieving, and managing images. Perfect for medical imaging and document management systems.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Locally](#running-locally)
- [API Routes](#api-routes)
- [Deployment](#deployment)
- [Technologies](#technologies)
- [License](#license)

---

## ✨ Features

- ✅ **Image Gallery**: Browse all stored images in an interactive gallery
- ✅ **Image Upload/Retrieval**: Store and fetch images from MongoDB GridFS
- ✅ **Bulk Delete**: Select and delete multiple images at once
- ✅ **CORS Enabled**: Cross-origin requests supported
- ✅ **Responsive UI**: Clean, modern HTML interface
- ✅ **Vercel Ready**: Optimized for serverless deployment

---

## 📁 Project Structure

```
AIMedicis-ImageHosting/
├── api/
│   ├── index.py                    # FastAPI ASGI application entry point
│   ├── routes/
│   │   ├── __pycache__/
│   │   ├── home.py                 # Home route handler
│   │   ├── gallery.py              # Gallery view with all images
│   │   ├── images.py               # Image retrieval endpoint
│   │   └── delete.py               # Delete images endpoint
│   ├── Database/
│   │   ├── __pycache__/
│   │   └── database.py             # MongoDB & GridFS configuration
│   └── templates/
│       ├── gallery.html
│       └── home.html
├── requirements.txt                 # Python dependencies
├── vercel.json                      # Vercel deployment configuration
├── main.py                          # Optional: local development entry point
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

---

## 🔧 Installation

### Prerequisites
- Python 3.9+
- MongoDB Atlas account (or local MongoDB)
- pip or conda

### Step 1: Clone the Repository

```bash
git clone https://github.com/Biki463/AIMedicis-ImageHosting.git
cd AIMedicis-ImageHosting
```

### Step 2: Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n aimg python=3.11
conda activate aimg
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
COLLECTION_NAME=pdf_image_extraction
```

### Database Setup

1. Create a MongoDB Atlas account at https://www.mongodb.com/cloud/atlas
2. Create a cluster and get your connection string
3. Update `MONGO_URI` in `.env` and `api/Database/database.py`

**Important:** The application uses **GridFS** to store images, which is ideal for files larger than 16MB.

---

## 🚀 Running Locally

### Development Server

```bash
cd c:/Users/BikiKumarSah/Downloads/AIMedicis-ImageHosting
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

Then open your browser and visit:
- **Home**: http://localhost:8000/api/
- **Gallery**: http://localhost:8000/api/gallery

### Alternative: Using main.py

```bash
python main.py
```

---

## 🔌 API Routes

### 1. **Home Route**
- **Endpoint**: `GET /api/`
- **Description**: Returns the home page with welcome message
- **Response**: HTML page with links to gallery
- **File**: `api/routes/home.py`

```bash
curl http://localhost:8000/api/
```

**Response:**
```html
<h2>🩺 PDF Image Viewer</h2>
<p>Visit <a href='/api/gallery'>Gallery</a> to see all stored images.</p>
```

---

### 2. **Gallery Route**
- **Endpoint**: `GET /api/gallery`
- **Description**: Displays all images from MongoDB in a responsive gallery
- **Response**: HTML gallery page with image cards and checkboxes for deletion
- **File**: `api/routes/gallery.py`

**Features:**
- Displays all images stored in GridFS
- Shows filename for each image
- Checkboxes for bulk selection
- Delete button for selected images
- Modern CSS styling with flexbox layout

```bash
curl http://localhost:8000/api/gallery
```

**Response:** Interactive HTML gallery with images

---

### 3. **Get Image Route**
- **Endpoint**: `GET /api/images/{image_id}`
- **Description**: Retrieve a specific image by MongoDB ObjectId
- **Parameters**:
  - `image_id` (path parameter): MongoDB GridFS file ID
- **Response**: Image binary data (PNG format)
- **Status Codes**:
  - `200`: Success - image returned
  - `404`: Not Found - image doesn't exist
- **File**: `api/routes/images.py`

**Example:**
```bash
curl http://localhost:8000/api/images/507f1f77bcf86cd799439011 -o image.png
```

**Error Response (404):**
```json
{
  "detail": "Image not found"
}
```

---

### 4. **Delete Images Route**
- **Endpoint**: `POST /api/delete_images`
- **Description**: Delete one or multiple images from the gallery
- **Request Type**: Form data (multipart/form-data)
- **Parameters**:
  - `selected_images` (form field): Array of image IDs to delete
- **Response**: HTML confirmation page with number of deleted images
- **File**: `api/routes/delete.py`

**Example (using HTML form):**
```html
<form method="post" action="/api/delete_images">
  <input type="checkbox" name="selected_images" value="507f1f77bcf86cd799439011">
  <input type="checkbox" name="selected_images" value="507f1f77bcf86cd799439012">
  <button type="submit">Delete Selected</button>
</form>
```

**Response:**
```html
<h3>✅ Deleted 2 image(s).</h3><a href='/api/gallery'>Back</a>
```

---

## 📊 Database Schema

### MongoDB Collection Structure

```javascript
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "filename": "example_image.png",
  "contentType": "image/png",
  "length": 524288,
  "uploadDate": ISODate("2025-11-11T17:30:00Z"),
  // GridFS chunks stored separately
}
```

### GridFS Usage

GridFS is a MongoDB specification for storing and retrieving large files. Images are split into chunks:

- **Files Collection**: Metadata (filename, size, date)
- **Chunks Collection**: Binary data chunks (262KB each by default)

---

## 🌐 Deployment on Vercel

### Prerequisites
- Vercel account at https://vercel.com
- MongoDB Atlas connection string

### Step 1: Set Environment Variables

In Vercel Project Settings > Environment Variables, add:

```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
COLLECTION_NAME=pdf_image_extraction
```

### Step 2: Deploy

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel deploy --prod

# Or push to GitHub and deploy from Vercel Dashboard
git push origin main
```

### Step 3: Verify Deployment

Visit your Vercel deployment URL:

```
https://your-project.vercel.app/api/
https://your-project.vercel.app/api/gallery
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **fastapi** | Latest | Web framework |
| **uvicorn** | Latest | ASGI server |
| **pymongo** | Latest | MongoDB driver |
| **python-dotenv** | Latest | Environment variables |
| **jinja2** | Latest | Template engine |

---

## 🔐 Security Notes

- ⚠️ **CORS**: Currently allows all origins (`*`). Restrict in production:
  ```python
  CORSMiddleware(
      allow_origins=["https://yourdomain.com"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )
  ```

- ⚠️ **MongoDB URI**: Never commit `.env` files. Use Vercel environment variables.

- ⚠️ **Input Validation**: Add validation for image IDs to prevent injection attacks.

---

## 🐛 Troubleshooting

### Issue: "Image not found" on all requests
**Solution**: Verify MongoDB connection in `api/Database/database.py`

### Issue: CORS errors in browser
**Solution**: Check CORS middleware settings in `api/index.py`

### Issue: Vercel deployment fails
**Solution**: 
- Check `vercel.json` configuration
- Ensure `requirements.txt` has all dependencies
- Verify environment variables are set

---

## 📝 Example Usage

### Upload Image (via Python)

```python
import requests
from bson import ObjectId

# Using MongoDB directly
from Database.database import fs

with open("image.png", "rb") as f:
    file_id = fs.put(f, filename="my_image.png")
    print(f"Uploaded with ID: {file_id}")
```

### Retrieve Image (via Python)

```python
from Database.database import fs
from bson import ObjectId

file_id = ObjectId("507f1f77bcf86cd799439011")
image_data = fs.get(file_id).read()

with open("downloaded_image.png", "wb") as f:
    f.write(image_data)
```

---

## 🚀 Performance Tips

1. **Index MongoDB**: Create indexes on frequently queried fields
   ```javascript
   db.fs.files.createIndex({ uploadDate: -1 })
   ```

2. **Pagination**: Implement pagination for large galleries
   ```python
   files = list(fs.find().skip(page * 10).limit(10))
   ```

3. **Image Compression**: Compress images before upload to reduce storage

4. **Caching**: Add Redis caching for gallery metadata

---

## 📄 License

This project is owned by **Biki463** on GitHub.

---

## 📧 Contact & Support

- **GitHub**: https://github.com/Biki463/AIMedicis-ImageHosting
- **Issues**: Report bugs via GitHub Issues

---

## 🎯 Future Enhancements

- [ ] User authentication
- [ ] Image upload endpoint
- [ ] Search functionality
- [ ] Image metadata editing
- [ ] Role-based access control
- [ ] API documentation (Swagger UI)
- [ ] Rate limiting

---

**Last Updated**: November 11, 2025  
**Status**: ✅ Production Ready
