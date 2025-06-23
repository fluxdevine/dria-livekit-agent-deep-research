import os
import aiohttp
import logging

logger = logging.getLogger(__name__)

async def _post(url: str, payload: dict) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            if resp.status != 200:
                text = await resp.text()
                raise RuntimeError(f"Request failed with status {resp.status}: {text}")
            return await resp.json()

async def generate_image(prompt: str) -> str:
    """Generate an image from a text prompt using a local Stable Diffusion API."""
    url = os.environ.get("IMAGE_GEN_URL", "http://localhost:5004/generate")
    try:
        data = await _post(url, {"prompt": prompt})
        return data.get("url") or data.get("path", "")
    except Exception as e:
        logger.error(f"generate_image failed: {e}")
        raise

async def edit_image(image_path: str, instructions: str) -> str:
    """Edit an image using a local Stable Diffusion API."""
    url = os.environ.get("IMAGE_EDIT_URL", "http://localhost:5004/edit")
    try:
        data = await _post(url, {"image": image_path, "instructions": instructions})
        return data.get("url") or data.get("path", "")
    except Exception as e:
        logger.error(f"edit_image failed: {e}")
        raise
