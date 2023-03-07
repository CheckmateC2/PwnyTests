#!/usr/bin/env python3

##
#
# This test works only on Linux distro, because of
#   session.details['Platform'] = "linux"
#
##

import os
import socket

from pwny.session import PwnySession

sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(1)
c, _ = sock.accept()

session = PwnySession()
session.details['Platform'] = "linux"
session.open(c)

session.download('/bin/sh', '/tmp/sh')
os.system('diff /tmp/sh /bin/sh; rm /tmp/sh')
session.upload('/bin/sh', '/tmp/sh')
os.system('diff /tmp/sh /bin/sh; rm /tmp/sh')
