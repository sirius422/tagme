#! /usr/bin/python3
import os

path = os.getcwd()
for root, dirs, files in os.walk(path):
    for filename in files:
        if filename != '.DS_Store' or filename.endswith(
                'original'):
            fullname = os.path.splitext(filename)[0]  # get the filename< without extensions>

            # add escape characters to avoid error in shells
            filename = filename.replace("'", r"\'")  # no single quote in path
            filename = filename.replace(' ', r'\ ')
            filename = filename.replace('(', r'\(')
            filename = filename.replace(')', r'\)')

            fulltag = (fullname.split("@")[-1]).split(",")
            fullpath = os.path.join(root, filename)

            for tag in fulltag:
                cmd = """exiftool -keywords+="{}" -charset iptc=UTF8 -iptc:codedcharacterset=utf8 {}""".format(tag,
                                                                                                                fullpath)
                # seems like that double quote also works on linux, use this because of the keyword like Girls'frontline
                os.system(cmd)
