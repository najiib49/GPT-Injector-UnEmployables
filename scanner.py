# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 13:55:28 2023

@author: adila
"""

import requests

def xss_checker(target):
    if target[0:5]=='https':
        return 'True'
    else:
        return 'False'