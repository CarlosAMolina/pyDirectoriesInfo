#!/usr/bin/python

__author__ = "Carlos A. Molina"

import sys
from utility_db import DB
from utility_get import Get
from utility_show import Show

pyDB = DB()
get = Get()
show = Show()

path2study, showInTerminal = get.getArgsInfo (sys.argv)  # example: 'C:\Users\userName\folder' # not end with \
dictKey1 = 'dirPath'
dictKey2 = 'dirsInPath'
dictKey3 = 'filesInPath'
dictKeys = [dictKey1, dictKey2, dictKey3]

# get information
listDictsInfo = get.getDirectoriesInfo(path2study, dictKeys)

# show info
if showInTerminal != None:
	show.showListDicts(listDictsInfo, dictKeys)

# save data in DB
pyDB.workWithDB (listDictsInfo, dictKeys)