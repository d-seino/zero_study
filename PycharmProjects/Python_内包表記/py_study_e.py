import os, glob, time

print([f for f in glob.glob("*") if os.stat(f).st_mtime > time.time() - 60 * 60 * 24])
