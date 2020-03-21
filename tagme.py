#! /usr/bin/python3
import os

path = os.getcwd()
for root, dirs, files in os.walk(path):
    for filename in files:
        if filename != '.DS_Store':  # warning: may not suitable for PNG files, I'm still work on it
            fullname = os.path.splitext(filename)[0]  # get the filename< without extensions>
            fulltag = (fullname.split("@")[-1]).split(",")
            fullpath = os.path.join(root, filename)

            # add escape characters to avoid error in shells
            fullpath = fullpath.replace(' ', r'\ ')
            fullpath = fullpath.replace('(', r'\(')
            fullpath = fullpath.replace(')', r'\)')

            for tag in fulltag:
                cmd = f"exiftool -keywords+='{tag}' -charset iptc=UTF8 -iptc:codedcharacterset=utf8 {fullpath}"
                # use '' on linux\unix
                os.system(cmd)
