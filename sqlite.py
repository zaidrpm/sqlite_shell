import sqlite3
import os
import sys
global conn
global aq
print ("Sqlite ----->")
def par(sql,l):
    global aq
    en=(sql.lower()).find("from")
    aq=[]
    j=7;i=7
    if(sql.find('*')<en):
        dfs=sql[en+5:len(sql)]+' '
        dfs=dfs[0:dfs.find(' ')]
        rdf=conn.execute('Pragma table_info ('+dfs+')')
        icu=0;
        rdf=rdf.fetchall()
        r=len(rdf)
        while(icu<r):
            aq.append(rdf[icu][1])
            icu+=1
    else:
        while(i<en):
            if(sql[i]==',' or en-1==i):
                aq.append(sql[j:i])
                j=i+1
            if(sql[i]==' '):
                j+=1
            i+=1
        i=0
        en=len(aq)
        while(i<en):
            tmp=aq[i]
            temp=tmp.find('.')
            if(temp>=0):
                aq[i]=tmp[temp+1:len(tmp)]
            i+=1
    while(len(aq)<l):
            aq.append('?')
    return



def squery(sql):
     global sd
     try:
         result=conn.execute(sql)
     except Exception as err:
         print ("Error",err)
         return
     a=result.fetchall()
     par(sql,len(a[0]))
     a.insert(0,aq)
     row=len(a)
     col=len(a[0])
     i=0;j=0;z=" ";ma=len(aq[0]);
     c=[]
     while(j<col):
         while(i<row):
             tmp=a[i][j]
             if tmp is not str:
                 tmp=str(tmp)
             if(len(tmp)>ma):
             	 ma=len(tmp)
             i+=1
         c.append(ma)
         j+=1
         i=0;
         ma=len(aq[j-1])
     
     i=0;j=0;
     while(i<row):
         while(j<col):
             tmp=a[i][j]
             if tmp is not str:
                 tmp=str(tmp)
             xx=c[j]-len(tmp)
             if(i==0):
                 print (" | ",'\033[95m'+tmp+'\033[0m',xx*z,end='')
             else:
                 print (" | ",tmp,xx*z,end='')
             if(col-j==1):
                 print ("|", end='')
             j+=1
         i+=1
         j=0
         print ('')
     conn.commit()
     return

def oquery(sql):
    try:
        res=conn.execute(sql)
        print (" Effected rows-> ",res.rowcount)
        conn.commit()
    except Exception as err:
        print (" Invalid sql",err)
    return
qwi=1
def st(db):
    try:
        global conn
        conn=sqlite3.connect(db)
        print ("Connected Successfully")
    except:
        print ("File path error!")
        sys.exit()
while(qwi==1):
    db=input("sqlite3>>Enter path to Db- ")
    #db="/sdcard/var.db"
    if os.path.isfile(db):
        st(db)
        break
    elif(db=='quit'):
        sys.exit()
    else:
        ui=input("No db exist with that name \nEnter y to create new: ")
        if(ui=='y'):
            st(db)
            break
        
global sd    
sql="yo"
while(qwi==1):
    sql=input("sqlite3>> ")
    if(len(sql)>6):
        sd=sql[0:6]
        sd=sd.lower()
    else:
        sd="no"
    if(sd=="select" or sd=="pragma"):
        squery(sql)
    elif(sql=="quit"):
        break
    else:
        oquery(sql)
conn.close()
