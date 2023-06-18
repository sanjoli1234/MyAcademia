from argparse import BooleanOptionalAction
from asyncio.windows_events import NULL
from contextlib import nullcontext
from ctypes.wintypes import BOOLEAN
from curses import raw
from http.client import HTTPResponse
from inspect import Parameter
from smtpd import DebuggingServer
from sqlite3 import paramstyle
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import datetime, date
import calendar
from _curses import *
from curses import raw
# def add_months(sourcedate, months):
#     month = sourcedate.month - 1 + months
#     year = sourcedate.year + month // 12
#     month = month % 12 + 1
#     day = min(sourcedate.day, calendar.monthrange(year,month)[1])
#     return datetime.date(year, month, day)
# Importing defaultdict
from collections import defaultdict
import cx_Oracle
id=()

conn=cx_Oracle.connect('system/agarwal@//localhost:1521/orcl')

# with open('D:\documents\passportsizephoto.jpeg', 'rb') as f:
#     img_data = f.read()


def home(request):
    # cursor=conn.cursor()
    # cursor.execute("""
    # insert into abbb values ( :blobdata)""",
    # blobdata=img_data)
    # cursor.execute("select * from abbb")
    # blob_data = cursor.fetchone()
    # print("CLOB length:", blob_data)
    return render(request,"loginpage.html")

def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        passwd = request.POST['passwd']
        # print(user,passwd)
        # print(user)
        if user.isnumeric():

            cur=conn.cursor()
            # sql="""Select username from LOGIN where username=:uuser and password=:ppasswd"""
            # cur.execute(sql,uuser=user,ppasswd=passwd)
            cur.execute("select username from login where username='{}' and password='{}'".format(user,passwd))
           
            global id
            id=(cur.fetchone())
            # print((cur.fetchone()))
            # print("id",id)
            if (id):
                return render(request,'homepage.html')
            else:
                messages.info(request,"*invalid credentials")
                return redirect("/")    
        else:
            messages.info(request,"*invalid credentials")
            return redirect("/")
def logout(request):
    return redirect("/")            

def change(request):
    return render(request,'changepasswd.html')
def respond(request):
    if request.method == 'POST':
        user = request.POST['username']
        opasswd = request.POST['oldp']
        npasswd = request.POST['newp']
        if user.isnumeric():
            global id
            print(id)
            cur=conn.cursor()
            cur.execute("Select username from login where username='{}' and password='{}'".format(id[0],opasswd))
            
            if (id):
                cur.execute("update login set password='{}' where username='{}' and password='{}'".format(npasswd,id[0],opasswd))
                conn.commit()
                messages.info(request,"Password Changed")
                return redirect("/")
            else:
                messages.info(request,"Invalid details")
                return redirect("/")
    
        else:
            messages.info(request,"Invaid details")
            return redirect("/")
def pers(request):
    cur=conn.cursor()
    global id
    cur.execute("select * from student where roll_no='{}'".format(id[0]))
    
    if id:
        san=cur.fetchone()
        dic={
    'first_name' : san[1] ,
    'roll_no' : san[0],
    'second_name' : san[2],
    'email' : san[4],
    'dob' : datetime.date(san[5]),
    'branch': san[6],
    'address': san[8],
     'father': san[7],
     'mother' : san[9],
     'gender' : san[3],
     'total' : san[10],
     'semester':san[11]
}
    # print(cur.fetchone())
    return render(request,'persinfo.html',dic)
def sub(request):
    cur=conn.cursor()
  
    global id
    # print(id)
    cur.execute("select * from student where roll_no='{}'".format(id[0]))
    idd=cur.fetchone()
    cur.execute("select course_code from semester where branches='{}' and semester ='{}'".format(idd[6],idd[11]))
    if id:
        tan = cur.fetchmany()
        ll=[]
        for i in tan:
            c=conn.cursor()
            c.execute("select * from scourse where course_code ='{}'".format(i[0]))
            s=c.fetchone()
            dic={}
            dic['course_code'] =s[0]
            dic['course_name'] =s[1]
            dic['course_credit'] = s[2]
            ll.append(dic)
    return render(request,'subject_registered.html',{'ll':ll}  )

def lib(request):
    cur=conn.cursor()
    global id
    cur.execute("select * from slib where roll_no='{}'".format(id[0]))
    if id:
        # dic = defaultdict(list)
        san=cur.fetchmany()
        l=[]
        for i in san:
            c=conn.cursor()
            c.execute("select * from sfine where id='{}'".format(i[0]))
            s=c.fetchone()
            due=datetime((i[4]).year + int((i[4]).month / 12), (((i[4]).month % 12) + 1), min(i[4].day, calendar.monthrange(datetime.date(i[4]).year,datetime.date(i[4]).month)[1]))
            # due=add_months(datetime.date(i[4]),1)
            dic={}
            dic['book_id']=i[2]
            dic['book_name']=(i[3])
            dic['issue_date']=(datetime.date(i[4]))
            dic['due_date']=(datetime.date(due))
            if i[5]:
                dic['return_date']=(datetime.date(i[5]))
            else:
                dic["return_date"]=('-')
            if s:
                
                dic['fine']=(s[1])
               
                if s[3]:
                    dic['fine_paid']=(s[3])
                else:
                    dic['fine_paid']=('no')
                #else:
                    #dic['fine_pais'].append('no') 
            else:
                dic['fine']=('-')
                dic['fine_paid']=('-')

            l.append(dic)
            # san=cur.fetchone()
                
       
                 
    # print(cur.fetchone())
        # print(l)
        return render(request,'library.html',{'l':l})
def teach(request):
    cur=conn.cursor()
  
    global id
    # print(id)
    cur.execute("select * from student where roll_no='{}'".format(id[0]))
    idd=cur.fetchone()
    cur.execute("select course_code from semester where branches='{}' and semester ='{}'".format(idd[6],idd[11]))
    if id:
        tan = cur.fetchmany()
        # print(tan[1])
        ll=[]
        for i in tan:
            dic={}
            dic['course_code'] =i[0]
            # print(i)
            c=conn.cursor()
            c.execute("select * from steach where course_code ='{}' and branches='{}'".format(i[0],idd[6]))
            
            s=c.fetchone()
            # print(s)
            if s:
                
                c.execute("select * from steacher where teacher_id='{}'".format(s[1]))
                s=c.fetchone()
                if s:
                    
                    dic['teacher_id'] =s[0]
                    dic['teacher_name'] = s[1]
                    dic['teacher_contact']=s[2]
                    
            else:
                # print(s)
                dic['teacher_id'] =('-')
                dic['teacher_name'] = ('-')
                dic['teacher_contact']=('-')
            ll.append(dic)
    return render(request,'teacher.html',{'ll':ll})



def mst(request):
    cur=conn.cursor()
  
    global id
    # print(id)
    cur.execute("select * from student where roll_no='{}'".format(id[0]))
    idd=cur.fetchone()
    cur.execute("select course_code from semester where branches='{}' and semester ='{}'".format(idd[6],idd[11]))
    if id:
        tan = cur.fetchmany()
        # print(tan[1])
        ll=[]
        for i in tan:
            
            # dic['course_code'] =i[0]
            # print(i)
            c=conn.cursor()
            ss=i[0]+'_MST'
            # print(ss)
            # c.execute(" EXECUTE IMMEDIATE select * from " || ss || " where roll_no ='{}' ".format(id[0]))
            
            raw_cursor = cur.connection.cursor()
            a = raw_cursor.var(int) # or raw_cursor.var(float)
            b=raw_cursor.var(int)
            # print(type(int(id[0])))
            c.callproc('sem',[int(id[0]),ss,a,b])
            
            # s=c.fetchone
            # print(a.getvalue(),b.getvalue())
            if a.getvalue()>0:
                dic={}
                dic['course_code'] =i[0]
                dic['max_marks'] = a.getvalue()
                dic['obtain_marks']=b.getvalue()
                ll.append(dic)
                
    # print(ll)   
    return render(request,'mst.html',{'ll':ll})

def est(request):
    cur=conn.cursor()
  
    global id
    # print(id)
    cur.execute("select * from student where roll_no='{}'".format(id[0]))
    idd=cur.fetchone()
    cur.execute("select course_code from semester where branches='{}' and semester ='{}'".format(idd[6],idd[11]))
    if id:
        tan = cur.fetchmany()
        # print(tan[1])
        ll=[]
        for i in tan:
            
            # dic['course_code'] =i[0]
            # print(i)
            c=conn.cursor()
            ss=i[0]+'_EST'
            # print(ss)
            # c.execute(" EXECUTE IMMEDIATE select * from " || ss || " where roll_no ='{}' ".format(id[0]))
            
            raw_cursor = cur.connection.cursor()
            a = raw_cursor.var(int) # or raw_cursor.var(float)
            b=raw_cursor.var(int)
            # print(type(int(id[0])))
            c.callproc('sem',[int(id[0]),ss,a,b])
            
            # s=c.fetchone
            # print(a.getvalue(),b.getvalue())
            if a.getvalue()>0:
                dic={}
                dic['course_code'] =i[0]
                dic['max_marks'] = a.getvalue()
                dic['obtain_marks']=b.getvalue()
                ll.append(dic)
                
    # print(ll)   
    return render(request,'est.html',{'ll':ll})
def sessional(request):
    cur=conn.cursor()
  
    global id
    # print(id)
    cur.execute("select * from student where roll_no='{}'".format(id[0]))
    idd=cur.fetchone()
    cur.execute("select course_code from semester where branches='{}' and semester ='{}'".format(idd[6],idd[11]))
    if id:
        tan = cur.fetchmany()
        # print(tan[1])
        ll=[]
        for i in tan:
            
            # dic['course_code'] =i[0]
            # print(i)
            c=conn.cursor()
            ss=i[0]+'_SESSIONAL'
            # print(ss)
            # c.execute(" EXECUTE IMMEDIATE select * from " || ss || " where roll_no ='{}' ".format(id[0]))
            
            raw_cursor = cur.connection.cursor()
            a = raw_cursor.var(int) # or raw_cursor.var(float)
            b=raw_cursor.var(int)
            # print(type(int(id[0])))
            c.callproc('sem',[int(id[0]),ss,a,b])
            
            # s=c.fetchone
            # print(a.getvalue(),b.getvalue())
            if a.getvalue()>0:
                dic={}
                dic['course_code'] =i[0]
                dic['max_marks'] = a.getvalue()
                dic['obtain_marks']=b.getvalue()
                ll.append(dic)
                
    # print(ll)   
    return render(request,'sessional.html',{'ll':ll})
def grades(request):
    pass
                
def hostelalloc(request):
    pass
def mess(request):
    pass  