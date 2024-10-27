import package2.module2
import package2.package2_1.module2_1
import module0  # 階層が上のモジュールでも絶対パスでimportできる

# エラーが発生するimport
# 絶対パスの起点がabsolute_importであるため、module2はimportできない
# import module2  
# 絶対パスの起点からその配下のモジュールを全て探索するわけではないため、module2_2はimportできない
# import module2_2 

def func_1(called_from: str):
    print(f'{__name__}.func_1 is called from {called_from}')
    module0.func_0(called_from=__name__)
    package2.module2.func_2(called_from=__name__)
    package2.package2_1.module2_1.func_2_1(called_from=__name__)

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
