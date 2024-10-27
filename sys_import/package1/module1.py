import sys 
import os

# package1の兄弟ディレクトリpackage2をパッケージ探索対象に追加
root_dir = os.path.dirname(os.path.dirname(__file__))  
pkg2_dir = os.path.join(root_dir, 'package2')  
sys.path.append(pkg2_dir)  

# package2を探索対象に追加したので記載の必要がなくなる
import module2  # = package2.module2
import package2_1.module2_1  # = package2.package2_1.module2_1
import module0  # sys_importでmain.pyを実行すれば、importが可能


def func_1(called_from: str):
    print(f'{__name__}.func_1 is called from {called_from}')
    module0.func_0(called_from=__name__)
    module2.func_2(called_from=__name__)
    package2_1.module2_1.func_2_1(called_from=__name__)


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
