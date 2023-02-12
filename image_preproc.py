from pathlib import Path
import json
import logging
import os

import imagesize

logging.basicConfig(level=logging.INFO)

# list of (post_name, post_dir, dir_fullres, dir_thumbnail)
PROC_DIR = [("3drenders", "./portfolio/", "./img/portfolio/", "./img200/portfolio/"),
            ]
OUTPUT_DIR = "./_data/"
EXT = ('*.jpg', '*.png', '*.jpeg')

json_shit = []

logging.info(f"To process {PROC_DIR}")
logging.info(f"Output to {OUTPUT_DIR}")
logging.info(f"For extensions {EXT}")

def get_images(file_path, extensions):
    logging.info(f"Getting file {file_path} matching {extensions}")

    files = []
    for ext in extensions:
        files.extend(Path(file_path).glob(ext))
    return files

for shit in PROC_DIR:
    logging.info(f"Iterating through {shit}")
    post_name, post_dir, dir_fullres, dir_thumbnail = shit
    images = get_images(dir_fullres, EXT)
    for image in images:
        img_width, img_height = imagesize.get(image)
        
        json_shit.append(dict({
            'filename': image.name,
            'thumbnail_path': dir_thumbnail[1:] + image.name, # path need to be relative for the script to work
            'fullres_path': dir_fullres[1:] + image.name, # but truncated in production as the cwd is different
            'alt': "", # optional, red description.yaml in post_dir
            'width': img_width,
            'height': img_height
        }))

        logging.info(f"Appending {json_shit[-1]}")

    with open(os.path.join(OUTPUT_DIR, post_name + '.json'), 'w') as f_out:
        logging.info(f"Writting json to {f_out}")
        json.dump(json_shit, f_out, indent=4)
        logging.info(f"Finished")
       
