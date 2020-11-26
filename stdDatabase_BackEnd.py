import sqlite3
import pymysql.cursors


def studentData():
	conn=sqlite3.connect("student.db")
	cur = conn.cursor()
	cur.execute("CREATE  TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, StdID text, Firstname text,Surname text,DoB text,\
		Age text, Gender text, Address text,Mobile text)")
	conn.commit()
	conn.close()

def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
	conn=sqlite3.connect("student.db")
	cur =conn.cursor()
	cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
	conn.commit()
	conn.close()

def viewData():
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM student")
	row=cur.fetchall()
	conn.close()
	return row 

def deleteRec(id):
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM student WHERE id=?",id)
	conn.commit() 
	conn.close()

def searchData(StdID="", Firstname="", Surname="",DoB="" ,Age="" , Gender="", Address="" ,Mobile=""):
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR \
		Mobile=?",(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
	rows=cur.fetchall()
	conn.close()
	return rows
def dataUpdate(id,StdID="", Firstname="", Surname="",DoB="" ,Age="" , Gender="", Address="" ,Mobile=""):
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("UPDATE student SET StdID=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=?, WHERE id=?",\
	             (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
	conn.commit() 
	conn.close()

