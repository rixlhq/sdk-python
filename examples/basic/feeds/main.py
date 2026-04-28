"""Read a feed and print the posts attached to it."""
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
    feed_id = os.environ.get("RIXL_FEED_ID") or sys.exit("missing RIXL_FEED_ID")
    base_url = os.environ.get("RIXL_BASE_URL", "http://localhost:8081")

    adapter = HttpxRequestAdapter(ApiKeyAuth(api_key))
    adapter.base_url = base_url
    client = RixlClient(adapter)

    page = await client.feeds.by_feed_id(feed_id).get()
    posts = page.data or []
    print(f"feed {feed_id} — {len(posts)} posts")
    for post in posts:
        print(f"  - {post.id}")


if __name__ == "__main__":
    asyncio.run(main())
