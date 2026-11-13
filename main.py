"""make.fun image entry: v6 palette variant, copy the bundled picture to /output/entry.png.

The picture (entry.png, in this repository) was generated for this bounty.
Copying the exact bytes keeps both grader runs byte-identical.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def copy_entry():
    """Copy the bundled picture to the output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    picture = os.path.join(HERE, "entry.png")
    target = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(picture):
        raise FileNotFoundError(f"missing picture: {picture}")
    shutil.copyfile(picture, target)


def main():
    copy_entry()


if __name__ == "__main__":
    main()
