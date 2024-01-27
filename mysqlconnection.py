import pymysql
import csv
conn=pymysql.Connection(user='root',password='root',host='localhost',port=3306,db='pooji')
#print(conn)
cur=conn.cursor()

def createtable():
    query='''create table mca(
    id int(2) primary key,
    name varchar(20));

    '''
    cur.execute(query)
#createtable()

def insertrecord(sid,name):
    record=(sid,name)
    query="insert into mca(id,name) values(%s,%s)"#%record
    cur.execute(query,record)
    conn.commit()
#insertrecord()

    
    #to fetch single record from table
def singlerecord(sid):
    record=(sid)
    query='select * from mca where id=%s'
       
    cur.execute(query,record)
    records=cur.fetchall()
    for row in records:
        print(row)
#singlerecord(1)

def read_records():
   query='select * from mca'
   cur.execute(query)
   records=cur.fetchall()
   for row in records:
       print(row)
#    with open('records.csv','w') as csvfile:
#        data=csv.writer(csvfile)
#        data.writerow(['id','name'])
#        for row in records:     
#         data.writerow(row)
#read_records()
  
def updaterecord(name,sid):
     record=(name,sid)
     query="update mca set name=%s where id=%s"
     cur.execute(query,record)
     conn.commit()
# updaterecord('siri',2)
def deleterecord(sid):
   
   query="delete from mca where id=%s"
   cur.execute(query,sid)
   conn.commit()
# deleterecord(2)




#to delete all records
def truncate():
   query='truncate table mca'
   cur.execute(query)
#truncate()
#to send records from excel to mysql  
def readrecord():
    with open('records.csv','r') as file:
        data=csv.reader(file)
        data=list(data)
        for row in range(1,len(data)):

         insertrecord(*data[row])
        
#readrecord()


