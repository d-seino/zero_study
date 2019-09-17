from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile().GetList()

print(type(file_list))
# <class 'list'>

print(len(file_list))
# 9

print(type(file_list[0]))
# <class 'pydrive.files.GoogleDriveFile'>

for f in file_list:
    print(f['title'], '   \t', f['id'])
# file21         1hJ7WQDiZyefLCQsDBE8J5-Nz847Vp670
# dir2       1wmWf1fhJTgi3X1Y07t2T8KYm4GtYEgxP
# file111        1789K-xv4ereCSOKrDKiAQI5bBypjqtIB
# subdir1        1k154tW38rbXxj88fjV8IZVkgB3EZ7g2M
# file12         1QRndXjXG9p2MEnVuotGd-eCNE2vNpkfp
# file11         1nCotx1q3DEaRWQOqbPqbPS1rGMWXRt8q
# dir1       1qQEUlPaIiDR_WI3hNf25rXUCHrlZIK_y
# file2      1ewv3ht8J2T3oMFmBgpqeS8zWHyHJsEwg
# file1      1WY5-WfWxj-ovefoE1dzWEfzgt8wtfbwY