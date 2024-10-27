# 子パッケージのモジュールから親パッケージのモジュールを参照できるか確認するためのモジュール

def func_0(called_from: str):
    print(f'{__name__}.func_0 is called from {called_from}')
