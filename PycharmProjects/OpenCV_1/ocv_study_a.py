import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "http://uta.pw/gazoubbs/attach/12-hama.jpg"
local = "hama.jpg"
req.urlretrieve(url, local)



