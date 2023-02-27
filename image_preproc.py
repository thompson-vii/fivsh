from pathlib import Path, PosixPath
import json
import logging
import os
from typing import NamedTuple

import imagesize

class SwipeDirectory(NamedTuple):
    json_filename: str
    dir_fullres: list[Path]
    dir_thumbnail: list[Path]
    
class ImageData():
    
    
    def __init__(self, source: Path):
        self.source_path = source
        self.thumbnail_path: Path = self.derive_thumbnail_path(self.source_path)
        self.filename: str = self.source_path.name
        self.json_fullres_path: str = "/" + "/".join(self.source_path.parts[-3:])
        self.json_thumbnail_path: str = "/" + "/".join(self.thumbnail_path.parts[-3:])
        self.alt_text: str
        self.width, self.height = imagesize.get(self.source_path)
    
    def derive_thumbnail_path(self, source: Path):
        return Path(str(source).replace("img", "img200"))

    def get_json(self):
        return dict({
            'filename': self.filename,
            'thumbnail_path': self.json_thumbnail_path, # path need to be relative for the script to work
            'fullres_path': self.json_fullres_path, # but truncated in production as the cwd is different
            'alt': "", # optional, read description.yaml
            'width': self.width,
            'height': self.height
        })
        
def get_files(paths: list[Path], extensions: list[str]) -> list[ImageData]:
    logging.info(f"Getting files in {paths} matching {extensions}")

    image_objects: list[ImageData] = []
    for dir in paths:
        for f in dir.iterdir():
            if f.suffix in EXT:
                image_objects.append(ImageData(f.resolve()))
                logging.info(f"{f} found")

    return image_objects

def write_json(output_dir: Path, filename: str, json_data):
    with open(os.path.join(output_dir, filename), 'w') as f_out:
        logging.info(f"Writting json to {f_out.name}")
        json.dump(json_shit, f_out, indent=4)
        logging.info(f"Finished")
       
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    ROOT = Path("/home/fivsh")
    OUTPUT_DIR = Path("/home/fivsh/_data/")
    EXT = ['.jpg', '.png', '.jpeg']

    '''
    swipe = SwipeDirectory("3drenders.json",
                       [ROOT.joinpath("img/portfolio"), ROOT.joinpath("img/portfolio_photogrammetry")],
                       [ROOT.joinpath("img200/portfolio"), ROOT.joinpath("img200/portfolio_photogrammetry")])
    '''
    
    swipe = SwipeDirectory("3drenders.json",
                       [ROOT.joinpath("img/portfolio")],
                       [ROOT.joinpath("img200/portfolio")])
    
    for p in swipe.dir_fullres:
        logging.info(f"To process {p}")
    logging.info(f"Output to {OUTPUT_DIR}")
    logging.info(f"For extensions {EXT}")
    

    json_shit = []    
    images = get_files(swipe.dir_fullres, EXT)
    for i in images:
        json_shit.append(i.get_json())
        
    print(json_shit)
    write_json(OUTPUT_DIR, swipe.json_filename, json_shit)
        
    