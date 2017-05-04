#!/usr/bin/python

__author__ = "Carlos A. Molina"

import os
from os import walk

class Get:

	def getArgsInfo (sef, args): # [script, path2study, showInTerminal]
		try:
			path2study = args[1]
			if path2study == '-':
				path2study = os.path.dirname(os.path.abspath(__file__)) # script's path
		except:
			path2study = os.path.dirname(os.path.abspath(__file__)) # script's path
		try:
			showInTerminal = args[2]
		except:
			showInTerminal = None
		return path2study, showInTerminal

	def getDirectoriesInfo (self, script2start, dictKeys):
		listDicts = []
		dictInfo = {dictKeys[0]:'', dictKeys[1]:'', dictKeys[2]:''}
		for (dirPath, dirNames, fileNames) in walk(script2start): #http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory
			dictInfo[dictKeys[0]] = dirPath
			dictInfo[dictKeys[1]] = dirNames
			dictInfo[dictKeys[2]] = fileNames
			listDicts.append(dictInfo)
			dictInfo = {dictKeys[0]:'', dictKeys[1]:'', dictKeys[2]:''}
		return listDicts # list of dicts