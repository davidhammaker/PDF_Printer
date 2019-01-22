import os
import sys
import shutil
from glob import glob
from datetime import date
import time


if __name__ == '__main__':
    text_file_path = sys.argv[1]
    print(text_file_path)
    with open(text_file_path, 'r') as paths:
        for path in paths:
            files_discovered = False
            all_files = []
            new_home = f'{path}'[:-1] \
                       + f'/printed_{date.today()}'
            for file in glob(f'{path}'[:-1] + '*'):
                if file.endswith('.pdf'):
                    if not files_discovered:
                        files_discovered = True
                        if not glob(new_home):
                            os.mkdir(new_home)
                    all_files.append(file)
            for file in all_files:
                os.startfile(file, 'print')
            if files_discovered:
                time.sleep(10)
            for file in all_files:
                shutil.move(file, new_home)
