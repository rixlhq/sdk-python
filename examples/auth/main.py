"""One file showing both auth flows. Pick one by setting env vars:

  - API key:    RIXL_API_KEY=...
  - Client JWT: RIXL_CLIENT_ID=..., RIXL_CLIENT_SECRET=..., RIXL_PROJECT_ID=..., RIXL_SUBJECT=...

Copy the credentials from the RIXL dashboard.
"""
import asyncio
import os
import sys

import httpx
from kiota_abstractions.authentication.authentication_provider import (
    AuthenticationProvider,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from rixl_client import RixlClient


# Sends a fixed header on every request. Swap in for Kiota's stock providers,
# which reject non-HTTPS URLs (so localhost dev fails).
class HeaderAuth(AuthenticationProvider):
    def __init__(self, name: str, value: str) -> None:
        self.name, self.value = name, value

    async def authenticate_request(self, request, additional_authentication_context=None):
        request.headers.add(self.name, self.value)


async def mint_token(base_url: str, payload: dict) -> str:
    async with httpx.AsyncClient(timeout=30.0) as c:
        resp = await c.post(f"{base_url}/clientauth/token", json=payload)
        resp.raise_for_status()
        return resp.json()["access_token"]


async def pick_auth(base_url: str) -> AuthenticationProvider:
    if api_key := os.environ.get("RIXL_API_KEY"):
        print("auth: API key")
        return HeaderAuth("X-API-Key", api_key)

    client_id = os.environ.get("RIXL_CLIENT_ID")
    client_secret = os.environ.get("RIXL_CLIENT_SECRET")
    if not client_id or not client_secret:
        sys.exit("set RIXL_API_KEY, or RIXL_CLIENT_ID + RIXL_CLIENT_SECRET + RIXL_PROJECT_ID + RIXL_SUBJECT")

    print("auth: client JWT")
    token = await mint_token(base_url, {
        "client_id": client_id,
        "client_secret": client_secret,
        "subject": os.environ["RIXL_SUBJECT"],
        "project_id": os.environ["RIXL_PROJECT_ID"],
    })
    return HeaderAuth("Authorization", f"Bearer {token}")


async def main() -> None:
    base_url = os.environ.get("RIXL_BASE_URL", "http://localhost:8081")

    auth = await pick_auth(base_url)
    adapter = HttpxRequestAdapter(auth)
    adapter.base_url = base_url
    client = RixlClient(adapter)

    page = await client.images.get()
    print(f"auth ok — listed {len(page.data or [])} images")


if __name__ == "__main__":
    asyncio.run(main())
