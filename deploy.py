import subprocess
import mpy_cross
import os

PORT = '/dev/ttyUSB0'
OUT_DIR = './build'


FILES = [
    # (input file, output file)
    # if output file ends with .mpy - will compile with mpy-cross
    # ('my_module/__init__.py', 'my_module/__init__.mpy'),
    # ('my_module/misc.py', 'my_module/misc.mpy'),
]


def cross_compile(file):
    print('cross_compile {}'.format(file))
    name, ext = os.path.splitext(file)
    out = os.path.join(OUT_DIR, name + '.mpy')

    try:
        os.makedirs(os.path.dirname(out))
    except FileExistsError:
        pass

    p = mpy_cross.run(file, '-o', out)
    p.wait()
    return out


def upload(file, destination):
    print('Uploading', file, destination)
    subprocess.call(['ampy', '-p', PORT, 'put', file, destination])


ensured_dirs = []


def ensure_dir_exists(path):
    global ensured_dirs
    current_path = ''
    for directory in os.path.dirname(path).split('/'):
        current_path = os.path.join(current_path, directory)
        if current_path in ensured_dirs:
            continue

        subprocess.call(['ampy', '-p', PORT, 'mkdir', current_path])

        ensured_dirs.append(current_path)


def main():
    try:
        os.makedirs(OUT_DIR)
    except FileExistsError:
        pass

    for file in FILES:
        if isinstance(file, str):
            path = file
            destination = file
        else:
            path, destination = file

        ext = os.path.splitext(destination)[1]
        ensure_dir_exists(destination)

        if not os.path.exists(path):
            print(f'Path {path} does not exist')
            exit(1)

        if ext == '.mpy':
            path = cross_compile(path)

        upload(path, destination)


main()
