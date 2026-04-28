"""List videos in your project, optionally fetch one by ID."""
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

    page = await client.videos.get()
    items = page.data or []
    print(f"listed {len(items)} videos")
    for v in items:
        print(f"  - {v.id}")

    if video_id := os.environ.get("VIDEO_ID"):
        v = await client.videos.by_video_id(video_id).get()
        print(f"video {v.id}")


if __name__ == "__main__":
    asyncio.run(main())
