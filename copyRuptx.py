import os
import shutil

# コピー元ディレクトリ（POSCAR2NPt1～POSCAR2NPt36が格納されているディレクトリ）
source_dir = '/home/7/ue02347/POSCARRuPtxfix'

# コピー先ディレクトリの親フォルダ（RuPt1 ～ RuPt36 を格納するディレクトリ）
destination_parent_dir = '/home/7/ue02347/RuPtxfixcalc'

# 1から36までのディレクトリを作成し、それぞれにファイルをコピー
for i in range(1, 37):
    dir_name = f"RuPt{i}"
    destination_dir = os.path.join(destination_parent_dir, dir_name)
    
    # ディレクトリを作成
    os.makedirs(destination_dir, exist_ok=True)
    
    # コピー元ディレクトリからファイルをコピー
    source_filename = f"POSCAR2fixNPt{i}"  # コピー元ファイル名 (例: POSCAR2NPt1)
    source_file = os.path.join(source_dir, source_filename)

    if os.path.isfile(source_file):  # ファイルが存在する場合
        destination_file = os.path.join(destination_dir, 'POSCAR')  # 名前をPOSCARに変更
        shutil.copy(source_file, destination_file)
        print(f"Copied {source_filename} to {destination_file}")
