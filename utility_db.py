#!/usr/bin/python

#https://www.tutorialspoint.com/python/python_database_access.htm

__author__ = "Carlos A. Molina"

import sqlite3

class DB:

	def __init__(self):
		self.dbName = 'results.db'
		self.dbTable = 'pathsDirFiles'
		self.dbColumn1 = 'path'
		self.dbColumn2 = 'dirsInPath'
		self.dbColumn3 = 'filesInPath'
		self.dbColumn4 = 'inclusionDateTimeUTC'
		self.dbColumns = [self.dbColumn1, self.dbColumn2, self.dbColumn3, self.dbColumn4]

	def init (self, dbName=None):
		if dbName == None:
			dbName = self.dbName
		# Open database connection. Connection Object is returned
		db = sqlite3.connect(dbName)
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		return db, cursor

	def end (self, dbObject):
		# disconnect from server
		dbObject.close()

	def dbCheckTableColumnsNone (self, dbTable=None, dbColumns=None):
		if dbTable == None:
			dbTable = self.dbTable
		if dbColumns == None:
			dbColumns = self.dbColumns
		return dbTable, dbColumns

	def createTable (self, cursorObject, dbTable=None, dbColumns=None):
		dbTable, dbColumns = self.dbCheckTableColumnsNone (dbTable, dbColumns)
		# drop table if it already exist using execute() method
		cursorObject.execute("DROP TABLE IF EXISTS " + dbTable)
		# create table as per requirement
		sql = 'CREATE TABLE ' + dbTable + """(
			""" + dbColumns[0] + """ TEXT,
			""" + dbColumns[1] + """ TEXT,
			""" + dbColumns[2] + """ TEXT,
			""" + dbColumns[3] + """ TEXT)"""
		cursorObject.execute(sql)

	def showVersion (self, cursorObject):
		# execute SQL query using execute() method
		cursorObject.execute("SELECT SQLITE_VERSION()")
		# fetch a single row using fetchone() method
		version = cursorObject.fetchone()
		print "\nDatabase version : %s " % version

	def saveData (self, dbObject, cursorObject, dbNewData, dbTable=None, dbColumns=None):
		dbTable, dbColumns = self.dbCheckTableColumnsNone (dbTable, dbColumns)
		# prepare SQL query to INSERT a record into the database
		sql = "INSERT INTO %s \
			(%s, %s, %s, %s) \
			VALUES ('%s', '%s', '%s', CURRENT_TIMESTAMP)" % \
			(dbTable, \
			dbColumns[0],dbColumns[1],dbColumns[2],dbColumns[3], \
			dbNewData[0],dbNewData[1],dbNewData[2])
		try:
			# execute the SQL command
			cursorObject.execute(sql)
			# Commit your changes in the database
			dbObject.commit()
			#print 'Information has been written in DB'
		except:
			# rollback in case there is any error
			print 'Error while writing data in DB'
			dbObject.rollback()

	def retrieveData (self, cursorObject, conditionColumn=None, conditionOperator=None, conditionParameters=None, dbTable=None):
		dbTable = self.dbCheckTableColumnsNone (dbTable)[0]
		if conditionColumn == None:
			sql = 'SELECT * FROM %s;' %dbTable
		else:
			sql = 'SELECT * FROM %s WHERE %s %s "%s"' %(dbTable, conditionColumn, conditionOperator, conditionParameters)
		if cursorObject.execute(sql) > 0:
			return cursorObject.fetchall()
		else:
			return -1

	def workWithDB (self, listDictsInfo, dictKeys):
		db, cursor = self.init ()
		for listDict in listDictsInfo:
			newData = [listDict[dictKeys[0]], ", ".join((word) for word in listDict[dictKeys[1]]), ", ".join((word) for word in listDict[dictKeys[2]])]
			self.saveData (db, cursor, newData)
		self.end (db)