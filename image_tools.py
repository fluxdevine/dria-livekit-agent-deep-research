import os
import aiohttp
from typing import List

IMAGE_API_URL = os.environ.get("IMAGE_API_URL", "http://localhost:8081")

async def generate_image(prompt: str, num_images: int = 1) -> List[str]:
    """Generate images from a text prompt via a local image generation API."""
    url = f"{IMAGE_API_URL}/generate"
    payload = {"prompt": prompt, "num_images": num_images}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            resp.raise_for_status()
            data = await resp.json()
            return data.get("images", [])

async def edit_image(image_url: str, prompt: str) -> str:
    """Edit an existing image based on the prompt via a local API."""
    url = f"{IMAGE_API_URL}/edit"
    payload = {"image_url": image_url, "prompt": prompt}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            resp.raise_for_status()
            data = await resp.json()
            return data.get("edited_image", "")
