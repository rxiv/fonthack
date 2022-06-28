#! /usr/bin/python

import sys
import os

from fontTools.ttLib import TTFont

font = sys.argv[1]

f=TTFont(font)
f["OS/2"].fsType=0
f.save(font)

