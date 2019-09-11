import os
# os.getcwd()
# #os.chdir(r'd:/')
# os.curdir #当前目录.
# os.pardir #父级目录
dd = os.path.dirname(os.getcwd())
#os.makedirs(dd+'/youzhen/kk')
#os.listdir('dirname')
# os.chdir(os.path.dirname(os.getcwd()))
# print(os.getcwd())
# os.rename('god','youzhen')
#os.name
#os.system('python os_len.py')
# for key,value in os.environ.items():
#     print(key,value)
# print(os.path.abspath(os.getcwd()))
print(os.path.split(os.path.split(os.getcwd())[0])[0])