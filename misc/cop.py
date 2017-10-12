import shutil
import click
import time
import os
from concurrent.futures import ThreadPoolExecutor


# def copyfileobj(fsrc, fdst, length=16*1024):
#     """copy data from file-like object fsrc to file-like object fdst"""
#     print('fsrc: {}, fdst: {}'.format(fsrc, fdst))
#     while 1:
#         buf = fsrc.read(length)
#         if not buf:
#             break
#         fdst.write(buf)

# def movefileobj(fsrc, fdst, length=16*1024):
#     """move data from file-like object fsrc to file-like object fdst"""
#     while 1:
#         buf = fsrc.read(length)
#         if not buf:
#             break
#         fdst.write(buf)
#     os.remove(fsrc)


def start_tasks(operation, files, dst, threads):
    with ThreadPoolExecutor(max_workers=threads) as pool:
        print('here we go')
        if operation == 'copy':
            for fil in files:
                if os.path.isdir(fil):
                    shutil.copytree(fil, dst)
                else:
                    shutil.copy(fil, dst)
                shutil.copy()

        elif operation == 'move':
            for fil in files:
                shutil.move(fil, dst)
        pool.shutdown()
    time.sleep(10)
    print('yse')

@click.command()
@click.option('--operation', type=click.Choice(['copy', 'move']), help='choose copy or move')
@click.option('--src', type=click.Path(exists=True), multiple=True, help='source files to copy')
@click.option('--dst', default='.', type=click.Path())
@click.option('--threads', default=1, help='number of threads to execute')
def foo(operation, src, dst, threads):
    print('starttyrem, threads: {}'.format(threads))
    
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    files = []
    for sfile in src:
        for ifile in glob.glob(sfile):
            files.append(ifile)
    
    start_tasks(operation, files, dst, threads)

if __name__ == "__main__":
    foo()