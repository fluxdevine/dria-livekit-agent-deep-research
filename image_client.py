import aiohttp

class ImageServiceClient:
    def __init__(self, model_url: str, api_key: str | None = None):
        self.model_url = model_url
        self.api_key = api_key

    async def generate_image(self, prompt: str, **kwargs):
        payload = {"prompt": prompt, **kwargs}
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.post(self.model_url, json=payload, headers=headers) as resp:
                resp.raise_for_status()
                return await resp.json()

    async def edit_image(self, image_data: bytes, prompt: str, **kwargs):
        data = aiohttp.FormData()
        data.add_field("prompt", prompt)
        data.add_field("image", image_data, filename="image.png")
        for k, v in kwargs.items():
            data.add_field(k, str(v))
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.post(self.model_url, data=data, headers=headers) as resp:
                resp.raise_for_status()
                return await resp.json()
