from package1 import module1

# エラーが発生するimport
# 実行ファイルと同じ階層にあるパッケージやモジュールは相対importできない
# from .package1 import module1

if __name__ == '__main__':
    module1.func_1(__name__)