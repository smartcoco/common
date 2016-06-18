#!coding=gbk

import os

def search_file(keyword, where):
    '''根据关键字查找某路径下是否有某文件，并打印文件路径'''
    where = os.path.abspath(where)
    for d in os.listdir(where):
        if  os.path.isfile(os.path.join(where,d)):
            if keyword.upper() in d.upper():
                print os.path.join(where, d).decode('gbk')
        else:
            if d == 'System Volume Information':
                continue
            search_file(keyword,os.path.join(where, d))


if __name__ == '__main__':
    search_file(r'开发','f:\\')