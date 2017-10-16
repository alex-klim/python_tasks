import shutil
import click
import time
import os
import glob
from distutils.dir_util import copy_tree
from concurrent.futures import ThreadPoolExecutor


def start_tasks(operation, files, dst, threads, pool):
    print('here we go')
    if operation == 'copy':
        for fil in files:
            print('fil: ', fil)
            print('isdir: ', os.path.isdir(fil))
            if os.path.isdir(fil):
                pool.submit(copy_tree, fil, dst)
            else:
                pool.submit(shutil.copy, fil, dst)
    elif operation == 'move':
        for fil in files:
            pool.submit(shutil.move, fil, dst)
    print('done')

@click.command()
@click.option('--operation', type=click.Choice(['copy', 'move']), help='choose copy or move')
@click.option('--src', multiple=True, help='source files to copy')
@click.option('--dst', default='.', type=click.Path())
@click.option('--threads', default=1, help='number of threads to execute')
def foo(operation, src, dst, threads):
    with ThreadPoolExecutor(max_workers=threads) as pool:
        print('let"s get started, threads: {}'.format(threads))
        print("src: ", src)

        if not os.path.exists(dst):
            os.makedirs(dst)
        
        for sr in src:
            newdst = dst
            files = []
            if os.path.isdir(sr):
                head, tail = os.path.split(sr)
                os.makedirs(dst+tail)
                newdst = dst+tail
                files.append(sr)
            else:
                for ifile in glob.glob(sr):
                    files.append(ifile)
            print(files)
            start_tasks(operation, files, newdst, threads, pool)      

        pool.shutdown()  

if __name__ == "__main__":
    foo()