#!/usr/bin/env python3
from PIL import Image
import os, glob

for file in glob.glob("supplier-data/images/*.tiff"):
  im = Image.open(file).convert('RGB')
  im.resize((600,400)).save(file[:-4]+"jpeg","JPEG")

 #[linux-instance-IP-Address]/media/images/
