import os
import shutil

# コピー元ディレクトリ（コピーしたいファイルが格納されているディレクトリ）
source_dir = '/home/7/ue02347/RuPtxother'

# コピー先ディレクトリの親フォルダ（例: Tsubameの作業ディレクトリ）
destination_parent_dir = '/home/7/ue02347/RuPtxfixcalc'

# 1から36までのディレクトリにファイルを追加
for i in range(1, 37):
    dir_name = f"RuPt{i}"
    destination_dir = os.path.join(destination_parent_dir, dir_name)

    # コピー元ディレクトリからファイルを追加
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        if os.path.isfile(source_file):  # ファイルのみをコピー
            shutil.copy(source_file, destination_dir)  # 既存のディレクトリにファイルを追加
            print(f"Copied {filename} to {destination_dir}")
