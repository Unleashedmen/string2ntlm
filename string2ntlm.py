#!/usr/bin/env python3
# Unleashed

import hashlib

passwd = input('\nEnter your password: ')
print ("NTLM hash:" + hashlib.new('md4', passwd.encode('utf-16le')).hexdigest())
