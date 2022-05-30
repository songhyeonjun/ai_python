import sys
from tkinter import messagebox


from db.mysql import read, read2
if __name__ == '__main__':
    all = read()
    all2 = read2()
    context = {'all' : all, 'all2' : all2}
    for one in all:
        print(one)
    for one in all2:
        print(one)
    print(all)
    print(all2)
    print(context)
