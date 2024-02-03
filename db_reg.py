from flask import redirect
import pymysql as p

def getconnection():
    return p.connect(host="localhost", user="root", password="", database="musicapp")

def insertrec(t):
    try:
        db = getconnection()
        cr = db.cursor()
        sql = "insert into reg_details(username,email,password) values(%s,%s,%s)"
        cr.execute(sql, t)
        db.commit()
        db.close()
    except:
        a="error"
        return a
  
def addwatchlist(t):
    db = getconnection()
    cr = db.cursor()
    sql = "insert into watchlist(email,song_name,url) values(%s,%s,%s)"
    cr.execute(sql, t)
    db.commit()
    db.close()
  


def displayrec():
    db = getconnection()
    cr = db.cursor()
    sql = "select * from reg_details"
    cr.execute(sql)
    data = cr.fetchall()
    db.commit()
    db.close()
    return data


def removewl(t):
    db = getconnection()
    cr = db.cursor()
    sql = "delete from watchlist where email=%s and song_name=%s"
    cr.execute(sql, t)
    db.commit()
    db.close()


def log(id):
    db = getconnection()
    cr = db.cursor()
    sql = "select email,password from reg_details where email=%s"
    cr.execute(sql, id)
    data = cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data


def selectrec(id):
    db = getconnection()
    cr = db.cursor()
    sql = "select email from reg_details where email=%s"
    cr.execute(sql, id)
    data = cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data

def checkreg(email):
    sel=selectrec(email)
    for i in sel:
        for j in i:
            if j==email:
                page="reg"
                return page
            else:
                page="home"
    if page=="home":
        return page

def sel_watchlist(id):
    db = getconnection()
    cr = db.cursor()
    sql = "select song_name,url from watchlist where email=%s"
    cr.execute(sql, id)
    data = cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data


def updaterec(t):
    db = getconnection()
    cr = db.cursor()
    sql = "update reg_details set name=%s,email=%s,passw=%s,contact=%s where id=%s"
    cr.execute(sql, t)
    db.commit()
    db.close()

def adminlogin(user):
    db = getconnection()
    cr = db.cursor()
    sql = "select username,password from adminlogin where username=%s"
    cr.execute(sql, user)
    data = cr.fetchall()
    db.commit()
    db.close()
    return data

def regusers():
    db = getconnection()
    cr = db.cursor()
    sql = "select * from reg_details"
    cr.execute(sql)
    data = cr.fetchall()
    db.commit()
    db.close()
    return data