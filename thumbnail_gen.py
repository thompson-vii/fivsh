from pathlib import Path
import logging
import shutil
import os

import PIL
from PIL import Image
from numpy import source

logging.basicConfig(level=logging.INFO)
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

def write_fullres_to_thumb(fullres_path, thumbnail_path, dry_run=False):
    if os.path.isdir(Path(thumbnail_path).parent):
        logging.info(f"{W}{thumbnail_path} exists.")
        pass
    else:
        Path(thumbnail_path).parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"{W}[DIR]{thumbnail_path} created.")

    if dry_run:
        logging.info(f"{W}[DRYRUN], {thumbnail_path} not modified")
    else:
        logging.info(f"{G}[COPY] from: {fullres_path} to {thumbnail_path}")
        shutil.copy(fullres_path, thumbnail_path)   
        with Image.open(thumbnail_path) as img:     
            img.thumbnail(THUMBNAIL_MAX_SIZE)
            img.save(thumbnail_path)
            logging.info(f"{G} [THUMBNAIL]{thumbnail_path} generated. {img.size}")

ROOT = Path(__file__)
FULLRES_PATH = ROOT.parent.joinpath("img")
THUMBNAIL_PATH = ROOT.parent.joinpath("img200")
EXT = ['.jpg', '.png', '.jpeg'] # needs period for suffix

THUMBNAIL_MAX_SIZE = (400, 800)

logging.info(f"Fullres Image Path: {FULLRES_PATH}")
logging.info(f"Thumbnail Image Path: {THUMBNAIL_PATH}")
logging.info(f"Image Extensions: {EXT}")
logging.info(f"Max Thumbnail Size: {THUMBNAIL_MAX_SIZE}")

"""
for img in FULLRES_PATH.rglob('*.*'): # * only returns file with no extensions 
    if img.suffix in EXT:
        print(str(img))
        fullres_images.append((img.name, str(img)))
"""

fullres_images = [(img.name, str(img)) for img in FULLRES_PATH.rglob('*.*') if img.suffix in EXT]
thumbnail_images = [(img.name, str(img).replace("img200", "img")) for img in THUMBNAIL_PATH.rglob('*.*') if img.suffix in EXT]

missing_images = set(fullres_images).difference(set(thumbnail_images))

logging.info(f"Number of fullres images: {len(fullres_images)}")
logging.info(f"Number of thumbnails: {len(thumbnail_images)}")


if len(fullres_images) != len(thumbnail_images):
    logging.warning(f"{O}{len(missing_images)} thumbnails missing")
    for _, miss in missing_images:
        logging.info(miss)

if missing_images:
    for img in missing_images:
        img_name, og_img_path = img
        new_thumbnail_path = og_img_path.replace("img", "img200")

        write_fullres_to_thumb(og_img_path, new_thumbnail_path, dry_run=False)
else:
    logging.info(f"{G} All thumbnail present. Nothing done")