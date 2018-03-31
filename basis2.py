#pythonの関数のスコープ

#global変数の効果
'''
#これでいけるけど関数呼び出したときじゃなくてもいけるようにしたい
def get_global():
    local_var = "bbb"
    return local_var
print(get_global()) #bbb
'''

'''
global_var = "aaa"
def get_global():
    global_ver = "bbb"
    return global_var
get_global()
print(global_var)#aaaでちゃう
'''

'''
def get_global():
    local_var = "bbb"
    return local_var
print(local_var) #local_varないって言われる
'''

'''
global_var = "aaa"
def get_global():
    global a
    a = "bbb"
    return a
get_global()
print(a)#関数の中のaを出力させることができた
'''


