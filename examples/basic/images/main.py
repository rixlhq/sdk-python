"""List images in your project, optionally fetch one by ID."""
import asyncio
import os
import sys

from kiota_abstractions.authentication.authentication_provider import (
    AuthenticationProvider,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from rixl_client import RixlClient


class ApiKeyAuth(AuthenticationProvider):
    def __init__(self, key: str) -> None:
        self.key = key

    async def authenticate_request(self, request, additional_authentication_context=None):
        request.headers.add("X-API-Key", self.key)


async def main() -> None:
    api_key = os.environ.get("RIXL_API_KEY") or sys.exit("missing RIXL_API_KEY")
    base_url = os.environ.get("RIXL_BASE_URL", "http://localhost:8081")

    adapter = HttpxRequestAdapter(ApiKeyAuth(api_key))
    adapter.base_url = base_url
    client = RixlClient(adapter)

    page = await client.images.get()
    items = page.data or []
    print(f"listed {len(items)} images")
    for img in items:
        print(f"  - {img.id}")

    if image_id := os.environ.get("IMAGE_ID"):
        img = await client.images.by_image_id(image_id).get()
        print(f"image {img.id}: {img.width}x{img.height}")


if __name__ == "__main__":
    asyncio.run(main())
