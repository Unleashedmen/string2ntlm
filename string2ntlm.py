#!/usr/bin/env python3
# Unleashed

import hashlib

passwd = input('Enter your password: ')
print (hashlib.new('md4', passwd.encode('utf-16le')).hexdigest())
