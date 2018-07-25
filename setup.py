#!/usr/bin/env python2
import os
import cfgfile
configdir = cfgfile.DEFAULT_INSTALL
os.system('chmod +x RoKSploit.py PyVenom_v0.1.py')
os.system('mv RoKSploit.py roksploit')
os.system('mv PyVenom_v0.1.py pyvenom')
os.system('cp roksploit ' + configdir)
os.system('cp pyvenom ' + configdir)
print "Installation Done... Run RoKSploit by typing in roksploit"

