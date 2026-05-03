#!/usr/bin/env python
# coding: utf-8

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





# In[ ]:





# In[ ]:





# In[ ]:




