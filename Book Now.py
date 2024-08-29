#!C:\Python\python.exe
import cgi
import mysql.connector
print("Content-Type:/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>","welcome","</h1>")
form=cgi.FieldStorage()
fname=form.getvalue("fname")
fmob=form.getvalue("mobno")
froom=form.getvalue("Rooms")
fmail=form.getvalue("Gmail")
print("<h1>",fname,fmob,froom,fmail,"</h1>")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hotel"
 )
mycursor=mydb.cursor()
sql="INSERT INTO booking(Name,Mobilenumber,Room,Email)INTO VALUES(%s,%s,%s,%s)"
val=(fname,fmob,froom,fmail)
mycursor.execute(sql,val)
mydb.commit()
print("</body>")
print("</html>")
