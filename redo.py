#!/usr/bin/env python
import os
os.system('cp CNAME /tmp/SAVED_LB_CNAME')
os.system('cp redo.py /tmp/SAVED_LB_SCRIPT')
os.system('rm -r ./*')
os.system('cp -r ../react_language/build/* .')
os.system('mv /tmp/SAVED_LB_CNAME ./CNAME')
os.system('git add -A') 
os.system('mv /tmp/SAVED_LB_SCRIPT ./redo.py')
os.system('chmod +x ./redo.py')
