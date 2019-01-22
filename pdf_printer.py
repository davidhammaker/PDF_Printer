import os
from glob import glob
from datetime import date


if __name__ == '__main__':
    with open('paths.txt', 'r') as paths:
        for path in paths:
            for file in glob(f'{path}'[:-1] + '*'):
                if file.endswith('.pdf'):
                    os.startfile(file, 'print')
