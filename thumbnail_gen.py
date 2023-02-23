from pathlib import Path, PosixPath
import logging
import shutil
import os
from typing import NamedTuple

import click
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

class Piece(NamedTuple):
    '''class that holds an image's file name, source path, target thumbnail path'''
    filename: str
    fullres_path: PosixPath
    thumbnail_path: PosixPath
    
    def __str__(self):
        return f"{self.filename} {str(self.fullres_path)}"

def write_fullres_to_thumb(fullres_path, thumbnail_path, dry_run=False):
    if os.path.isdir(Path(thumbnail_path).parent):
        logging.info(f"{W}{thumbnail_path} exists.")
        pass
    else:
        Path(thumbnail_path).parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"{W}[DIR]{thumbnail_path} created.")

    if dry_run:
        logging.info(f"{W}[DRYRUN], {thumbnail_path} not modified")
        return
    else:
        logging.info(f"{G}[COPY] from: {fullres_path} to {thumbnail_path}")
        shutil.copy(fullres_path, thumbnail_path)   
        with Image.open(thumbnail_path) as img:     
            img.thumbnail(THUMBNAIL_MAX_SIZE)
            img.save(thumbnail_path)
            logging.info(f"{G} [THUMBNAIL]{thumbnail_path} generated. {img.size}")

@click.command()
@click.option('--dry-run', default=False, help="Don't generate or modify any files")

def thumbnail_gen(dry_run: bool):
        
    if dry_run:
        print("Dry run, no file will be generated")
        
    ROOT = Path("/home/fivsh")
    FULLRES_PATHS = []
    FULLRES_PATHS.append(Path(ROOT.joinpath("img/portfolio")))
    FULLRES_PATHS.append(Path(ROOT.joinpath("img/portfolio_photogrammetry")))
    
    THUMBNAIL_PATHS = []
    THUMBNAIL_PATHS.append(Path(ROOT.joinpath("img200/portfolio")))
    THUMBNAIL_PATHS.append(Path(ROOT.joinpath("img200/portfolio_photogrammetry")))
    
    
    global EXT
    EXT = ['.jpg', '.png', '.jpeg'] # needs period for suffix
    global THUMBNAIL_MAX_SIZE
    THUMBNAIL_MAX_SIZE = (400, 800)

    for p in FULLRES_PATHS:
        logging.info(f"Fullres Image Path: {p}")
    
    for p in THUMBNAIL_PATHS:
        logging.info(f"Thumbnail Image Path: {p}")
    
    logging.info(f"Image Extensions: {EXT}")
    logging.info(f"Max Thumbnail Size: {THUMBNAIL_MAX_SIZE}")

    image_pieces = []
    for subdir in FULLRES_PATHS:
        for p in subdir.iterdir():
            if p.suffix in EXT:
                print(p.name, p.resolve())
                image_pieces.append(Piece(p.name, 
                                          p.resolve(), 
                                          Path(str(p.resolve()).replace('img', 'img200'))))
    
    missing_pieces = []
    for piece in image_pieces:
        if not Path(piece.thumbnail_path).is_file():
            missing_pieces.append(piece)

    current_thumbnail = set(image_pieces).difference(set(missing_pieces))
    logging.info(f"Number of fullres images: {len(image_pieces)}")
    logging.info(f"Number of thumbnails: {len(current_thumbnail)}")


    if len(image_pieces) != len(current_thumbnail):
        logging.warning(f"{O}{len(missing_pieces)} thumbnails missing")
        for f in missing_pieces:
            logging.info(f)
    else:
        logging.info(f'{G} No thumbnail missing')

    if missing_pieces:
        for img in missing_pieces:
            img_name, og_img_path, thumbnail_path = img
            write_fullres_to_thumb(og_img_path, thumbnail_path, dry_run)
    else:
        logging.info(f"{G} All thumbnail present. Nothing done")
        
if __name__ == '__main__':
    thumbnail_gen()