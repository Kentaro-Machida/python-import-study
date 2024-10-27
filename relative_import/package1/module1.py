from .module3 import func_3
from .package1_1 import module1_1

# エラーが発生するimport
# from .package2.module2 import func_2
# ModuleNotFoundError: No module named 'package1.package2'となる
# つまり、package1の内部のみを探索しているため、package2はimportできない

# from ..package2.module2 import func_2
# from ..module0 import func_0
# attempted relative import beyond top-level package となる
# つまり、このファイルが置いてあるpackage1の親ディレクトリは探索できない

def func_1(called_from: str):
    print(f'{__name__}.func_1 is called from {called_from}')
    func_3(called_from=__name__)
    module1_1.func_1_1(called_from=__name__)

if __name__ == '__main__':
    """
    モジュール単体で実行された場合の処理（単体テストをイメージ）
    このモジュールだけを直接実行したい場合は、プロジェクトのルートディレクトリ(absolute_import配下)で以下のコマンドを実行する
    python -m package1.module1
    もし、以下のコマンドで実行すると、エラーmodule1が起点のため、module2がimportできない
    python package1.module1.py
    つまり-mオプションをつけて「モジュールとして実行する」というのは、モジュールを呼び出すであろう
    スクリプトの位置を絶対パスの起点にするということ
    """
    func_1(called_from=__name__)
