from ..package1_2 import module1_2

def func_1_1(called_from: str):
    print(f'{__name__}.func_1_1 is called from {called_from}')
    module1_2.func_1_2(__name__)