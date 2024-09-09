#!/usr/bin/env python

import requests

def download_nuz(url):
    getrespon = requests.get(url)
    namafile = url.split("/")[-1]
    print(namafile)
    with open(namafile, "wb") as fileout:
        fileout.write(getrespon.content)

download_nuz("https://img.cintamobil.com/2020/10/28/radrgpyy/bmw-m3-gtr-street-legal-version-8f1e.jpg")