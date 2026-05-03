#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.summarize import router

app = FastAPI()

# Enable CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Backend is running"}


# In[ ]:


from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from services.pdf_service import extract_text_from_pdf
from services.ai_service import generate_summary
from utils.text_cleaner import clean_text

router = APIRouter()

# Request model
class TextRequest(BaseModel):
    text: str

# 📌 Text Summarization
@router.post("/summarize")
async def summarize_text(request: TextRequest):
    cleaned = clean_text(request.text)
    summary = generate_summary(cleaned)
    return {"summary": summary}

# 📌 PDF Summarization
@router.post("/summarize-file")
async def summarize_file(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    cleaned = clean_text(text)
    summary = generate_summary(cleaned)
    return {"summary": summary}


# In[ ]:


import pdfplumber
import io

def extract_text_from_pdf(file):
    text = ""

    with pdfplumber.open(io.BytesIO(file.file.read())) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    return text


# In[ ]:


def clean_text(text):
    return text.replace("\n", " ").strip()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




