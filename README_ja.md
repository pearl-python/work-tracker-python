# Work Tracker Python

CSV形式の作業データを読み込み、完了した作業の件数・合計時間・最長作業を集計するPython製の小型CLIツールです。

Pythonのクラス、CSV処理、関数分割、例外処理を組み合わせた実践学習として制作しました。

## 主な機能

* CSVファイルから作業データを読み込む
* CSVの各行を`Work`インスタンスへ変換する
* `done`状態の作業件数を集計する
* `done`状態の合計作業時間を計算する
* 最も時間の長い完了作業を取得する
* 不正なCSVデータを検出する
* 不正データが含まれている場合、不完全な集計結果を正常結果として表示しない

## CSV形式

1行につき、以下の3項目を記述します。

```text
name,time,status
```

例：

```csv
Python Learning,60,done
Image Creation,90,doing
Document Review,30,done
API Practice,45,done
```

`time`には整数を指定します。

`status`には主に以下を使用します。

```text
done
doing
```

## 実行方法

`work.csv`を`main.py`と同じ場所に配置します。

```text
work-tracker-python/
├─ main.py
├─ work.csv
├─ README.md
└─ README_ja.md
```

その後、以下を実行します。

```bash
python main.py
```

## 出力例

```text
done件数：3
done合計時間：135
done最長作業：Python Learning
done最長時間：60
```

## エラー処理

以下のような入力エラーを検出します。

* CSVファイルが存在しない
* `time`に整数へ変換できない値が含まれている
* CSVの列数が不足している

不正なデータが見つかった場合は、対象行やエラー内容を記録し、集計結果を正常な結果として表示しない設計にしています。

例：

```text
データに不具合があったため中断します
エラー行：2
エラー詳細：値が整数ではありません
エラーデータ：['Image Creation', 'abc', 'done']
```

## 使用しているPython要素

このプロジェクトでは、主に以下を使用しています。

```text
class
__init__
インスタンス属性
インスタンスメソッド
list
CSV
for
if
関数
try / except
FileNotFoundError
ValueError
IndexError
複数戻り値
```

## 設計上のポイント

CSVの各行をそのまま処理するのではなく、`Work`クラスのインスタンスへ変換してから集計しています。

これにより、

```python
work.name
work.time
work.status
work.is_done()
```

のように、作業データを統一した形で扱えるようにしています。

また、不正な行を単純に無視して集計を続けると、不完全なデータから誤った集計結果を出してしまう可能性があります。

そのため、不正データを検出した場合はエラー情報を残し、最終集計を中断する設計にしています。

## 今後追加したい機能

今後は以下のような改修を予定しています。

* コマンドライン引数からCSVファイルを指定
* 集計結果をCSVやJSONへ保存
* loggingによるログ出力
* 自動テストの追加
* pandasを利用した集計処理
* 処理のモジュール分割

## 制作目的

このプロジェクトでは、単に動くコードを書くことだけではなく、

* 処理を小さな関数へ分解する
* クラスを使ってデータを整理する
* 入力データの異常を考える
* 後から改修しやすい構造にする

といった、小規模なPythonツール開発の基礎を身につけることを目的としています。
