#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

__appname__    = ""
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""

recipient = sys.argv[1]
message = sys.argv[2]
print(message)
os.system("osascript sendMessage.scpt {} {}".format(recipient, message))
