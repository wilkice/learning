'''使用进程池实现文件夹的整体拷贝

在拷贝文件的文件时，如果文件夹中的文件很多，那么一个一个拷贝，效率会很低下

可以使用多任务的形式来实现文件夹下的文件进行同时拷贝。提高拷贝效率
TODO: support move subdirectory and symbolic links
'''

import multiprocessing
import shutil
import os


# move files
def movefile(new_directory, original_file_path):
    shutil.move(original_file_path, new_directory)
    print(multiprocessing.current_process().pid)  # see which process is working


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
    original_directory = input('Pls input the directory u want to move: ')
    new_directory = input('Pls input the directory u want to move to: ')
    oldpathlist = []
    get_old_and_new_path()
    pool = multiprocessing.Pool(8)
    for original_file_path in oldpathlist:
        pool.apply_async(movefile, args=(new_directory, original_file_path))
    pool.close()
    pool.join()
    print('All files have been moved to new directory! ')
