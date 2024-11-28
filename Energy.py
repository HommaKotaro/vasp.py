import os

# 出力ファイルのパス
output_file = 'energy_values.txt'

# ファイル名のリスト (例: RuPt1, RuPt2, ..., RuPt36)
directories = [f"RuPt{i}" for i in range(1, 37)]

# energy_values.txt を開く（既存の内容を上書きする）
with open(output_file, 'w') as f:
    for dir_name in directories:
        outcar_path = os.path.join(dir_name, 'OUTCAR')  # 各ディレクトリ内のOUTCARファイルのパス
        try:
            with open(outcar_path, 'r') as outcar_file:
                lines = outcar_file.readlines()
                last_energy = None
                # energy(sigma->0) = の行を逆順に探して最後に見つかった値を取得
                for line in reversed(lines):
                    if 'energy(sigma->0)' in line:
                        # 行からエネルギーの値を抽出
                        last_energy = line.split('=')[-1].strip()
                        break

                if last_energy:
                    # 結果を出力ファイルに書き込む
                    f.write(f"{dir_name}: {last_energy}\n")
                else:
                    f.write(f"{dir_name}: energy not found\n")
        except FileNotFoundError:
            f.write(f"{dir_name}: OUTCAR file not found\n")

print(f"Energy values written to {output_file}")

