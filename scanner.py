# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 13:55:28 2023

@author: adila
"""

import requests

def xss_checker(target):
    payload  = "<script> alert(XSS);</script>"
    
    req = requests.post(target + payload)
    if payload in req.text:
        return 'False'
    else:
        return 'True'