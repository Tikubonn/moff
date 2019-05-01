
# Moff

\| 日本語 \| [English](README.md) \|

MoffはMarkdownの方言のひとつです。
自家製のMarkdownが欲しかったので書きました。Python製です。
画像の表示だけでなく、マルチデバイスに対応した「画像・映像・音声」にも対応しています。
それ以外は他のMarkdownとだいたい一緒です。

```markdown
# Moff 
# とは

MoffはMarkdownの方言のひとつです。
Moffは画像だけでなく、マルチデバイスに対応した「画像・映像・音声」にも対応しています。

@image example.jpg
@image @case @src example1x.jpg 1x
@image @case @src example2x.jpg 2x

@video 
@video @src example.mp4
@video @src example.webm
@video @thumbnail thumbnail.jpg

@audio 
@audio @src example.mp3
@audio @src example.webm
```

```html
<h1>Moffとは</h1>
<p>
  MoffはMarkdownの方言のひとつです。
  Moffは画像だけでなく、マルチデバイスに対応した「画像・映像・音声」にも対応しています。
</p>
<a href="example.jpg" target="_blank">
  <img src="example.jpg" srcset="example1x.jpg 1x, example2x.jpg 2x" decoding="async">
</a>
<video preload="none" poster="thumbnail.jpg" controls>
  <source src="example.mp4" type="video/mpeg">
  <source src="example.webm" type="video/webm">
</video>
<audio preload="none" controls>
  <source src="example.mp3" type="audio/mpeg">
  <source src="example.webm" type="audio/webm">
</audio>
```

## ライブラリとして利用

Pythonのライブラリとして利用する場合には、
`mohh.parser`モジュールで定義されている`Parser`クラスを利用することで、MoffのソースコードをHTMLの構造体に変換できます。
`Parser`クラスにはファイル入力から変換を行う`.parse()`メソッドと、文字列から変換を行う`.parse_string()`メソッドが用意されています。
詳細はwikiをご参照ください。

```python
from moff.parser import Parser
from sys import stdout

with open("入力ファイル", "r") as instream:
  parser = Parser()
  node = parser.parse(instream)
  node.write(stdout) # or print(str(node))
```

## コマンドラインから利用

Moffはインストール後に下記のように呼び出すことができます。

```shell
moff "入力ファイル" --output-file "出力ファイル"
```

```shell
python -m moff "入力ファイル" --output-file "出力ファイル"
```

対応している引数は下記のとおりです。

| 引数 | 概要 | 
| ---- | ---- |
| `入力ファイル` | 入力元となるファイルを指定します。未指定の場合には標準入力が使用されます。 | 
| `--output-file` `-o` | 出力先となるファイルを指定します。未指定の場合には標準出力が使用されます。 | 
| `--prefix-path` | 画像・映像・音声のファイルパスが相対パスだった場合に、前方に連結されるパスです。未指定の場合には連結されません。 | 
| `--version` `-v` | コマンドのバージョン情報を出力後に終了します。 | 
| `--help` `-h` | コマンドのヘルプ情報を出力後に終了します。 | 

## 仕様

詳細はwikiに書いてあります。ご参照ください。

## 導入方法

`setup.py`が同梱されていますので、同梱されているディレクトリに移動し、下記のコマンドを実行してください。

```bash
python setup.py install
```

## ライセンス

Moffは[MITライセンス](LICENSE)で提供されています。
