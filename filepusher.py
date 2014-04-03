#!/usr/bin/env python
# All dis was written by da boaf.
# All I did was paste it to dis file and upload.
# Tanks boaf. (http://github.com/boaf)

import ftplib
import os
import multiprocessing
import ctypes
import sys

def stdprint(text):
    sys.stdout.write(text)
    sys.stdout.flush()

server = 'ftp.example.com'
user = 'foo'
passwd = 'bar'

FTP_DIR = 'root-dir'
LOCAL_DIR = = '/foo'

all_files = []
print('Getting files')
for root, dirs, names in os.walk(LOCAL_DIR):
    if root != './' and names:
        all_files.extend([(root, name) for name in names])

total = len(all_files)
count = multiprocessing.Value(ctypes.c_int)
lock = multiprocessing.Lock()

def increment():
    with lock:
        count.value += 1
        stdprint('{0} of {1} uploaded'.format(count.value, total))

def do_work(files):
    ftp = ftplib.FTP_TLS(server, user, passwd)
    errors = []

    for d, f in files:
        local_path = os.path.join(d, f)
        remote_path = os.path.join(FTP_DIR, os.path.split(d)[1], f)
        try:
            ftp.storbinary('STOR {0}'.format(remote_path), open(local_path, 'rb'))
            stdprint('\rUploaded {0} => {1}\n'.format(local_path, remote_path))
            increment()
        except ftplib.all_errors as e:
            print(e)
            errors.append((e, (d, f)))

    ftp.close()
    return errors

print('Uploading\n')
pool = multiprocessing.Pool(4)
chunks = [all_files[i:i+len(all_files)/4] for i in xrange(0, len(all_files), len(all_files)/4)]
results = pool.map(do_work, chunks)
