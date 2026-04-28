"""Upload an image end-to-end:

  1. Init     — tell the API you want to upload; it returns a presigned PUT URL.
  2. PUT      — push the bytes straight to storage (the API never sees them).
  3. Complete — tell the API the upload landed so it can finalize the record.
"""
import asyncio
import os
import sys

import httpx
from kiota_abstractions.authentication.authentication_provider import (
    AuthenticationProvider,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from models.internal_images_handler.complete_request import CompleteRequest
from models.internal_images_handler.upload_init_request import UploadInitRequest
from rixl_client import RixlClient

SAMPLE_IMAGE = "https://picsum.photos/seed/rixl/800/600.jpg"


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

    async with httpx.AsyncClient(timeout=300.0) as http:
        body = (await http.get(SAMPLE_IMAGE)).content
        print(f"downloaded {len(body)} bytes")

        init_req = UploadInitRequest()
        init_req.name = "sample.jpg"
        init_req.format = "jpeg"
        init = await client.images.upload.init.post(init_req)
        print(f"init: image_id={init.image_id}")

        await http.put(init.presigned_url, content=body, headers={"Content-Type": "image/jpeg"})

    complete = CompleteRequest()
    complete.image_id = init.image_id
    complete.attached_to_video = False
    img = await client.images.upload.complete.post(complete)
    print(f"complete: id={img.id} {img.width}x{img.height}")


if __name__ == "__main__":
    asyncio.run(main())
