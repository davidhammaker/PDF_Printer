import os
import shutil
from glob import glob
from datetime import date
import time


if __name__ == '__main__':
    with open('paths.txt', 'r') as paths:
        for path in paths:
            files_discovered = False
            all_files = []
            new_home = f'{path}'[:-1] \
                       + f'/printed_{date.today()}'
            for file in glob(f'{path}'[:-1] + '*'):
                if file.endswith('.pdf'):
                    if not files_discovered:
                        files_found = True
                        if not glob(new_home):
                            os.mkdir(new_home)
                    all_files.append(file)
            for file in all_files:
                os.startfile(file, 'print')
            time.sleep(10)
            for file in all_files:
                shutil.move(file, new_home)
