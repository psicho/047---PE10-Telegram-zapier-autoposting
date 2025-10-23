import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("STABILITY_API_KEY")

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "red cat with blue eyes wearing a pink heart shaped glasses without lenses ultrahd", # Меняем промпт на свой
        "output_format": "jpeg", # Меняем формат "webp" на "jpeg"
    },
)

if response.status_code == 200:
    with open("story.jpg", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))