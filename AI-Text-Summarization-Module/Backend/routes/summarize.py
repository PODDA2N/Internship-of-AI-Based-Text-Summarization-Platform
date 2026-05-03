#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import APIRouter, UploadFile, File
from services.pdf_service import extract_text_from_pdf
from services.ai_service import generate_summary
from utils.text_cleaner import clean_text

router = APIRouter()

@router.post("/summarize-file")
async def summarize_file(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    cleaned = clean_text(text)
    summary = generate_summary(cleaned)
    return {"summary": summary}

