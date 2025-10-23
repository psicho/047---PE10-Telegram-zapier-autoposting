import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL", "https://api.proxyapi.ru/openai/v1")
openai = OpenAI(api_key=api_key, base_url=base_url)

def generate_post(topic):
    prompt_title = f"Придумайте привлекательный заголовок для поста на тему: {topic}"
    response_title = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_title}],
        max_tokens=50,
        n=1,
        temperature=0.7,
    )
    title = response_title.choices[0].message.content.strip()

    prompt_meta = f"Напишите краткое, но информативное мета-описание для поста с заголовком: {title}"
    response_meta = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_meta}],
        max_tokens=100,
        n=1,
        temperature=0.7,
    )
    meta_description = response_meta.choices[0].message.content.strip()

    prompt_post = f"Напишите подробный и увлекательный пост для блога на тему: {topic}. Используйте короткие абзацы, подзаголовки, примеры и ключевые слова для лучшего восприятия и SEO-оптимизации."
    response_post = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_post}],
        max_tokens=2048,
        n=1,
        temperature=0.7,
    )
    post_content = response_post.choices[0].message.content.strip()

    return {
        "title": title,
        "meta_description": meta_description,
        "post_content": post_content
    }

if __name__ == "__main__":
    print(generate_post('Машина времени'))