#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from openai import OpenAI

client = OpenAI(api_key="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")

def generate_summary(AI_function_being_called):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize the following text in clear bullet points."},
            {"role": "user", "content": AI_function_being_called}
        ]
    )

    return response.choices[0].message.content


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




