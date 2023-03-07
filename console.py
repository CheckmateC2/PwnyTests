#!/usr/bin/env python3

##
#
# This test works only on Linux distro, because of
#   session.details['Platform'] = "linux"
#
##

import socket

from pwny.session import PwnySession

sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(1)
c, _ = sock.accept()

session = PwnySession()
session.details['Platform'] = "linux"
session.open(c)

session.interact()
