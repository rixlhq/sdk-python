"""Fetch a single post inside a feed. Posts always live under a feed —
there's no top-level posts collection.
"""
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
    post_id = os.environ.get("RIXL_POST_ID") or sys.exit("missing RIXL_POST_ID")
    base_url = os.environ.get("RIXL_BASE_URL", "http://localhost:8081")

    adapter = HttpxRequestAdapter(ApiKeyAuth(api_key))
    adapter.base_url = base_url
    client = RixlClient(adapter)

    post = await client.feeds.by_feed_id(feed_id).by_post_id(post_id).get()
    print(f"post {post.id}")


if __name__ == "__main__":
    asyncio.run(main())
