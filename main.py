#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261123.

The repository holds entry.png, a one-page newspaper image that sums up
the world news of Monday 23 November 2026. This program copies that
image to the output location the grader expects:

    /output/entry.png

When the MAKEFUN_OUTPUT_DIR environment variable is set, it is used as
the output directory instead of /output (that is how the program is run
locally for testing). Only the Python standard library is used, and the
program needs no network access.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def source_path():
    """Return the path of the image stored beside this program."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def output_path():
    """Return where the entry image must be written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, IMAGE_NAME)


def main():
    src = source_path()
    dst = output_path()
    if not os.path.isfile(src):
        print(f"error: {src} not found", file=sys.stderr)
        return 1
    with open(src, "rb") as fh:
        magic = fh.read(8)
    # The image in this entry is a PNG; anything else means a bad repo.
    if not magic.startswith(b"\x89PNG"):
        print("error: entry image is not a PNG file", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size > 1048576:
        print(f"error: output is {size} bytes, over the 1 MiB cap", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
