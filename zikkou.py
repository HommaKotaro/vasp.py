import os
import subprocess

# 親ディレクトリ（例: RuPtディレクトリ群があるディレクトリ）
parent_dir = "/home/7/ue02347/RuPtxfixcalc"

# 1から36までのディレクトリで qsub を実行
for i in range(1, 37):
    dir_name = f"RuPt{i}"
    dir_path = os.path.join(parent_dir, dir_name)
    
    if os.path.isdir(dir_path):  # ディレクトリが存在するか確認
        # 現在のディレクトリを変更して qsub 実行
        print(f"Submitting job in: {dir_path}")
        subprocess.run(["qsub","-g","tga-ishikawalab","run_vasp.sh"], cwd=dir_path)
    else:
        print(f"Directory {dir_name} does not exist.")

# ジョブの状態を確認
subprocess.run(["qstat"])
