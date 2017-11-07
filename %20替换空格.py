#_*_coding:utf-8_*_
def replaceSpace(s):
    # write code here
    s = list(s)
    count = len(s)
    for i in range(0, count):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)
s = 'Hello world,we all happy'
print replaceSpace(s)