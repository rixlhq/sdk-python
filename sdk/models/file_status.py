from enum import Enum

class FileStatus(str, Enum):
    Uploading = "uploading",
    Uploaded = "uploaded",
    Processing = "processing",
    Preparing = "preparing",
    Ready = "ready",
    Error = "error",

