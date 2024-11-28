import os

# ディレクトリ名を生成し、作成する
for i in range(1, 37):
    dir_name = f"RuPt{i}"  # 'RuPt1', 'RuPt2', ..., 'RuPt36'
    os.makedirs(dir_name, exist_ok=True)  # 存在しない場合のみディレクトリを作成
    print(f"Created directory: {dir_name}")

