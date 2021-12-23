# Experiments
アルゴリズム等のプログラム実験用のリポジトリ

## compression
LZ78 圧縮プログラム

## requirement
tqdm : 圧縮,解凍の進捗確認のため
```bash
% pip install -r requirements.txt
```

## usage
```bash
% cd compression
% python main.py <任意のファイルパス>
```

* 任意のファイル名（拡張子込み）に.presが付加されたファイルが生成
* .presのファイルを指定するとファイルが解凍される
* 単体のファイル指定のみ対応
