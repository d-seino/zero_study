import os, glob

# 重複ファイルがあるかどうかを調べるディレクトリ --- (*1)
target_dir = './check'
# ファイルの一覧を得る --- (*2)
files = glob.glob(target_dir + "/*")
# 繰り返し重複があるか調べる --- (*3)
for f1 in files:
    with open(f1, "rb") as f1p:
        f1body = f1p.read()  # 内容 --- (*4)
    # 繰り返し調べる --- (*5)
    for f2 in files:
        # 同一ファイルなら比較しない --- (*6)
        if f1 == f2: continue
        # ファイルの内容を比較 --- (*7)
        with open(f2, "rb") as f2p:
            f2body = f2p.read()
        if f1body == f2body:
            print(f1, "==", f2)
print("ok")