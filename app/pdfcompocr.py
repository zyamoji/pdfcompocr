#!/usr/bin/env python3
import subprocess
import argparse

# 引数処理
parser = argparse.ArgumentParser()
parser.add_argument("filenames", nargs='*', help="Please input filename")
parser.add_argument("--compress", action="store_true")
parser.add_argument("--ocr", action="store_true")
args = parser.parse_args()

# 圧縮処理
def compress(filename):
  print(f"pdf compress is started. Please wait...")
  command = f"gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile='{filename[:-4]}-compress.pdf' '{filename}'"
  ret = subprocess.run(command, shell=True, capture_output=True, text=True)
  print(ret.stdout)
  print(command)

# OCR処理
def ocr(filename):
  print(f"pdf ocr is started. Please wait....")
  command = f"ocrmypdf -l jpn '{filename}' '{filename[:-4]}_ocr.pdf'"
  ret = subprocess.run(command, shell=True, capture_output=True, text=True)

  print(ret.stdout)
  print(ret.stderr)
  print(command)

# メイン処理、ファイルは複数渡せるようにする
for file in args.filenames:
  print(f"operation started with {file}.")
  # 圧縮とOCR両方の場合は、先に圧縮（こちらの方がファイルサイズが小さくなる）
  if args.compress and args.ocr:
    compress(file)
    #　中間ファイル名は指定する
    ocr(file[:-4]+"-compress.pdf")
  # 圧縮のみ
  elif args.compress:
    compress(file)
  # OCRのみ
  elif args.ocr:
    ocr(file)
  # オプションがどちらもない時
  else:
    print("Please input option")