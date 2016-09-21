#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid

__appname__    = "pymessage"
__author__     = "Marco Sirabella, Owen Davies"
__copyright__  = ""
__credits__    = "Marco Sirabella, Owen Davies"
__license__    = "new BSD 3-Clause"
__version__    = "0.0.1"
__maintainers__= "Marco Sirabella, Owen Davies"
__email__      = "msirabel@gmail.com, dabmancer@dread.life"
__status__     = "Prototype"
__module__     = ""

mac = hex(uuid.getnode())

hexmac = mac[0] + ''.join([mac[i-1] + ':' + mac[i] for i in range(len(mac)) if i % 2 == 0 and (i != 0 and i != len(mac))]) + mac[-1]

print(hexmac)
