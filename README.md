# python-import-study
Repository for studying python import.

# About this repository
Pythonのimportの仕様についてきちんと理解するためのリポジトリ。
このリポジトリでは、特に記載がなければ常にmain.pyが存在するディレクトリからmain.pyを
実行することを前提とする。

# absolute_import
絶対importの挙動を確認するためのもの。
## ディレクトリ構造
```
.
├── __pycache__
│   └── module0.cpython-312.pyc
├── main.py
├── module0.py
├── package1
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── module1.cpython-312.pyc
│   └── module1.py
└── package2
    ├── __pycache__
    │   ├── module1_1.cpython-312.pyc
    │   └── module2.cpython-312.pyc
    ├── module2.py
    └── package2_1
        ├── __pycache__
        │   └── module2_1.cpython-312.pyc
        ├── module2_1.py
        └── module2_2.py
```
## ファイルごとのimport関係
* main: module1
* module1: module0, module2, module2_1

絶対importは、全てのモジュールが互いにimportすることが可能。  
例えば、module1が親ディレクトリにあるmodule0や兄弟のmodule2をimportできる。

## 実行確認コマンド
基本は、以下のコマンドで`main.py`を実行するシチュエーションを想定。
```
python main.py
```
module1だけを実行したい場合は以下のように実行。  実際の開発では、このようにしてモジュールごとにテストすることがある。  
`module1.py` において、`__name__ == '__main__'`となるが、絶対importの起点は上記コマンドで`absolute_import/`で`main.py`を実行した際と同じになる。
```
python -m package1.module1
```

# relative_import
相対importの挙動を確認するためのもの。

## ディレクトリ構造
```
.
├── __pycache__
│   └── module0.cpython-312.pyc
├── main.py
├── module0.py
├── package1
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── module1.cpython-312.pyc
│   │   └── module3.cpython-312.pyc
│   ├── module1.py
│   ├── module3.py
│   ├── package1_1
│   │   ├── __pycache__
│   │   │   └── module1_1.cpython-312.pyc
│   │   └── module1_1.py
│   └── package1_2
│       ├── __pycache__
│       │   └── module1_2.cpython-312.pyc
│       └── module1_2.py
└── package2
    ├── __init__.py
    ├── module2.py
    └── package2_1
        ├── __pycache__
        │   └── module2_1.cpython-312.pyc
        └── module2_1.py
```

## ファイルごとのimport関係
* main: module1
* module1: module3, module1_1
* module1_1: module1_2

相対importは、実行ファイルと同じ階層を経由するimportはできない。  
例えば、`main.py`を実行する場合、`module1.py`から`module2.py`や`module0.py`をimportできないという仕様。  
逆に、実行ファイルと同じ階層を経由しなければ親や兄弟パッケージでもimport できる。  
例えば、`module2_1.py`から`module2.py`をimportすることができる。  
また、別の例として、`main.py`から同じ階層の`package1`の中の`module1.py`をimportしようとしても失敗する。（これも同じ理由）

## 実行確認コマンド
基本は、以下のコマンドで`main.py`を実行するシチュエーションを想定。
```
python main.py
```
module1だけを実行したい場合は以下のように実行。  実際の開発では、このようにしてモジュールごとにテストすることがある。  
`module1.py` において、`__name__ == '__main__'`となるが、絶対importの起点は上記コマンドで`absolute_import/`で`main.py`を実行した際と同じになる。
```
python -m package1.module1
```