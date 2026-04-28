# Examples

Self-contained scripts. Each file imports the SDK and runs one task.

## Setup

```bash
cd examples
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
export RIXL_API_KEY=<copied from the dashboard>
export RIXL_BASE_URL=http://localhost:8081   # optional, defaults to https://api.rixl.com

python auth/main.py              # show both auth flows in one file (API key or client JWT)
python basic/images/main.py      # list images, fetch by IMAGE_ID
python basic/videos/main.py      # list videos, fetch by VIDEO_ID
python basic/feeds/main.py       # read a feed (needs RIXL_FEED_ID)
python basic/posts/main.py       # fetch a post (needs RIXL_FEED_ID + RIXL_POST_ID)
python advanced/images/main.py   # full image upload pipeline
python advanced/videos/main.py   # full video upload pipeline
```
