# RIXL Python SDK

The official RIXL Python SDK offers a clean and pythonic way to interact with the RIXL API. It supports asynchronous operations and provides type hints for a better developer experience.

## Components

The SDK is organized into the following modules:

- **rixl_feeds_sdk**: Community and content feeds.
- **rixl_videos_sdk**: Video management and processing.
- **rixl_images_sdk**: Image upload and processing.

## Installation

You can install the SDK modules using pip:

```bash
pip install rixl-feeds-sdk rixl-videos-sdk rixl-images-sdk
```

## Quick Start

```python
from rixl_feeds_sdk import FeedsApi

api = FeedsApi()
# response = api.get_discover_feed()
```

## Documentation

Comprehensive documentation can be found at [docs.rixl.com](https://docs.rixl.com).
