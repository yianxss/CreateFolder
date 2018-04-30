import os
from os import path
import shutil


class PyFolder(object):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    @staticmethod
    def clean_dir(c_dir):
        """
        :param c_dir: 要清理的路径
        :return: 删除所有的文件和文件夹，删除成功返回True,否则False
        """
        if not path.exists(c_dir):
            raise OSError('路径不存在')
        list_dir = os.listdir(c_dir)
        for item in list_dir:
            if path.isfile(item):
                file_full_dir = path.join(list_dir, item)
                try:
                    os.remove(file_full_dir)
                except os.error as e:
                    print("删除失败--{}".format(list_dir), e)
            elif path.isdir(item):
                if not path.splitext(item)[1].lower() == '.svn':
                    shutil.rmtree(file_full_dir, True)
        if len(os.listdir(c_dir)) == 0:
            return True
        else:
            return False

    def join_dirs(self, f_names, join_base_dir=True):
        """
        :param f_names: type-list--要合并的路径["a",2,'b']
        :param join_base_dir: 是否和创建的路径合并，默认True
        :return: 返回路径
        """
        if f_names is None:
            raise TypeError('f_names not None')
        else:
            sep = os.sep
            join_dir = sep.join(f_names)
            if join_base_dir:
                return path.join(self.base_dir, join_dir)
            else:
                return join_dir

    def create_folders(self, full_path, clean_dir=False):
        """
        :param full_path: 要创建文件夹的全路径
        :param clean_dir: 如果文件夹已经存在是否清理，默认不清理
        :return: 创建成功范围True

        """
        if path.isdir(full_path):
            if clean_dir:
                self.clean_dir(full_path)
                os.makedirs(full_path)
                return True
        else:
            os.makedirs(full_path)
            return True


if __name__ == '__main__':
    s = PyFolder(r'F:\01 Python相关\04 储存\DM - 副本')
    print(s.clean_dir(r'F:\01 Python相关\04 储存\DM - 副本'))
