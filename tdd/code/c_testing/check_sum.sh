#!/bin/bash
set -x
gcc -c -fPIC sum.c -o sum.o
gcc -shared -Wl,-soname,libsum.so.1 -o libsum.so.1.0.1  sum.o
python2 test_c.py
