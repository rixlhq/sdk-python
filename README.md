# RIXL Python SDKs

This repository contains the Python SDK split by service instead of one flat generated client.

## Layout

- `sdk/feeds` -> package `rixl_feeds_sdk`
- `sdk/videos` -> package `rixl_videos_sdk`
- `sdk/images` -> package `rixl_images_sdk`

Each service folder is a standalone Python package with its own `pyproject.toml`, `setup.py`, and generated client code.

## Install Examples

Install a local service package:

```sh
pip install ./sdk/videos
```

Then import the generated package:

```python
import rixl_videos_sdk
```

## Regenerate

Generate all services:

```sh
./scripts/generate.sh
```

Generate one service:

```sh
./scripts/generate.sh --service feeds
```

Regenerate from a fresh OpenAPI file:

```sh
./scripts/generate.sh --spec /path/to/public.swagger.json --service images
```
