#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 打开文件：
file_obj = file("文件路径","模式")
# 打开文件的模式有：
# r，以只读方式打开文件
# w，打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a，打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# w+，打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

with
#当with代码块执行完毕时，内部会自动关闭并释放文件资源
#为了避免打开文件后忘记关闭，可以通过管理上下文，即：

with open('login','w+') as f:
    f.write(’nihao ,Alex‘)


读取文件的内容：
# 一次性加载所有内容到内存
obj.read()

# 一次性加载所有内容到内存，并根据行分割成字符串
obj.readlines()

# 每次仅读取一行数据
for line in obj:
    print line

#写文件的内容：
obj.write('内容')

#关闭文件句柄：
obj.close()