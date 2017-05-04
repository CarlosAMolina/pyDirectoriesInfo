#!/usr/bin/python

__author__ = "Carlos A. Molina"

class Show:

	def showListDicts(self, listDicts, dictKeys):
		for listDict in listDicts:
			print 'Path: ' + listDict[dictKeys[0]]
			print '\tDirectories in path: ',
			print (", ".join((word) for word in listDict[dictKeys[1]]))
			print '\tFiles in path: ',
			print (", ".join((word) for word in listDict[dictKeys[2]]))