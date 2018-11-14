'''使用进程实现文件夹的整体拷贝

在拷贝文件的文件时，如果文件夹中的文件很多，那么一个一个拷贝，效率会很低下

可以使用多任务的形式来实现文件夹下的文件进行同时拷贝。提高拷贝效率

TODO: support move subdirectory and symbolic links
'''

import multiprocessing
import shutil
import os

# move files
def movefile(newfilepath, i):
    shutil.move(i, newfilepath)
    print(multiprocessing.current_process().pid) # see which process is working


# get all files' path in that directory
def get_old_and_new_path():
    filelists = os.listdir(original_directory)
    for i in filelists:
        filename = os.path.join(original_directory, i)
        oldpathlist.append(filename)


    # t = os.walk(original_directory)
    # for path, directory, filenames in t:
    #     for name in filenames:
    #         oldfilepath = os.path.join(path, name)
    #         oldpathlist.append(oldfilepath)


if __name__ == '__main__':
    original_directory = 'C:/Users\牛奶加冰\Pictures\Screenshots'
    newfilepath = 'C:/Users/牛奶加冰/Desktop/2'
    oldpathlist = []
    get_old_and_new_path()
    for k in oldpathlist:
        pool = multiprocessing.Process(target=movefile, args=(newfilepath, k))
        pool.start()
    print('All files have been moved to new directory! ')
