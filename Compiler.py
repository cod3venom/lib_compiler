"""
 * Project: Table.js.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 5/2/2021
 * Time: 9:32 AM
 * Github: https://github.com/cod3venom
"""

import os
import glob
from ArgParser import ArgParser

class Compiler:
    __files_map: dict = {}
    __full_code: str = ""

    def __init__(self, code_dir: str, file_ext: str, out_file: str, make_unreadable: bool = False):
        """
        :param code_dir:
        :param file_ext:
        :param out_file:
        """
        self.code_dir: str = code_dir
        self.file_ext: str = file_ext
        self.out_file: str = out_file
        self.make_unreadable: bool = make_unreadable


    def load_files(self):
        if os.path.exists(self.code_dir):
            for root, sub_dirs, files in os.walk(self.code_dir):
                for file in files:
                    if file.endswith(self.file_ext):
                        path = f"{root}{os.sep}{str(file)}"
                        self.__files_map[path] = self.read_files(path)


    def read_files(self, path: str) -> str:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as reader:
                return reader.read()
        return ""

    def write_file(self, path: str, data: str):
        with open(path, 'w', encoding='utf-8') as writer:
            writer.write(str(data))

    def build(self):
        for key in self.__files_map.keys():
            if self.make_unreadable:
                self.__full_code += self.__files_map[key].replace("\n", '')
            else:
                self.__full_code += self.__files_map[key]

        self.write_file(self.out_file, self.__full_code)
        print(self.__full_code)


if __name__ == "__main__":

    arg_parser = ArgParser()
    arg_parser.sysArgvTOdict()

    code_dir: str = ''
    file_ext: str = ''
    out_file: str = ''
    unreadable: bool = False

    if arg_parser.keyExists('code_dir'):
        code_dir = arg_parser.getValueOf('code_dir')

    if arg_parser.keyExists('file_ext'):
        file_ext = arg_parser.getValueOf('file_ext')

    if arg_parser.keyExists('out_file'):
        out_file = arg_parser.getValueOf('out_file')

    if arg_parser.keyExists('make_unreadable'):
        make_unreadable = arg_parser.getValueOf('make_unreadable')
        if int(make_unreadable) == 1:
            unreadable = True

    _compiler = Compiler(code_dir=code_dir,
                         file_ext=file_ext,
                         out_file=out_file,
                         make_unreadable=unreadable)
    _compiler.load_files()
    _compiler.build()
