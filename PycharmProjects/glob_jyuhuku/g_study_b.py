import os, glob, hashlib

# 重複ファイルがあるかどうかを調べるディレクトリ
target_dir = './check'
body_dict = {}


# ファイルの内容を返す関数 --- (*1)
def get_body(fname):
    with open(fname, "rb") as f:
        return f.read()


# ファイルの一覧を得て重複があるか調べる --- (*2)
files = glob.glob(target_dir + "/*")
for f in files:
    # ファイルを開いてハッシュ値を調べる --- (*3)
    body = get_body(f)
    v = hashlib.sha256(body).hexdigest()
    if v in body_dict:  # 重複しているか --- (*4)
        f2 = body_dict[v]
        # 念のため実際に合致しているか調べる --- (*5)
        if body == get_body(f2):
            print(f, "==", f2)
            # 実際に削除するなら以下のコメントを外す ---- (*5a)
            # os.remove(f)
    else:
        body_dict[v] = f  # --- (*6)
print("ok")