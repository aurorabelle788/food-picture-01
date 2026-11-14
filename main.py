"""food-picture-01 entry: copy the ramen photograph to /output/entry.png.

The image is a photorealistic bowl of ramen — chopsticks lifting steaming
noodles, chashu, a soft egg, nori — shipped in this repository as
entry.png (a JPEG, named entry.png per the competition rules). This
program only copies it to the output directory, unchanged.
"""

import os
import shutil

SRC_NAME = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), SRC_NAME)
    dst = os.path.join(out_dir, SRC_NAME)
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("incomplete copy: output size differs from source")
    with open(src, "rb") as f_src, open(dst, "rb") as f_dst:
        if f_src.read() != f_dst.read():
            raise RuntimeError("incomplete copy: output bytes differ from source")


if __name__ == "__main__":
    main()
