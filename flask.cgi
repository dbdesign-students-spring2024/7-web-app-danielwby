#!/home/bw2427/.pyenv/versions/3.9.1/bin/python

import os
import sys
os.environ.setdefault('REQUEST_METHOD', 'GET')
#sys.path.insert(0, '/misc/linux/centos7/x86_64/local/stow/python-3.6/lib/python3.6/site-packages/')
from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)
