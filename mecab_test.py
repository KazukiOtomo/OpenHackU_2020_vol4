import Mecab
import sys
import re
from collections import Counter

# ファイル読み込み
infile = 'C:\Users\kazuki.o\OneDrive\ドキュメント\OpenHackU_2020\mecab_test.txt' # ※txtファイルの格納場所は各自変えてください
with open(infile ,encoding="utf-8") as f:
    data = f.read()

parse = MeCab.Tagger().parse(data)
lines = parse.split('\n')
items = (re.split('[\t,]', line) for line in lines)

# 形態素解析の結果を表示
for item in items:
    print(item)

