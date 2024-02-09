from flask import redirect
import pandas as pd

def get_data_frame(file_path):
    return pd.read_excel(file_path)

def save_data_frame(data_frame, file_path):
    data_frame.to_excel(file_path, index=False)

def insertrec(t, file_path="reg_details.xlsx"):
    try:
        df = get_data_frame(file_path)
        new_row = pd.DataFrame([t], columns=["username", "email", "password"])
        df=pd.concat([df,new_row])
        # df = df.append(new_row, ignore_index=True)
        save_data_frame(df, file_path)
    except Exception as e:
        print("Error:", e)
        return "error"

def addwatchlist(t, file_path="watchlist.xlsx"):
    try:
        df = get_data_frame(file_path)
        new_row = pd.DataFrame([t], columns=["email", "song_name", "url"])
        df=pd.concat([df,new_row])
        # df = df.append(new_row, ignore_index=True)
        save_data_frame(df, file_path)
    except Exception as e:
        print("Error:", e)

# Modify the displayrec function to return a DataFrame
def displayrec(file_path="reg_details.xlsx"):
    try:
        df = get_data_frame(file_path)
        return df
    except Exception as e:
        print("Error:", e)

# Modify the removewl function to remove rows from the DataFrame
def removewl(t, file_path="watchlist.xlsx"):
    try:
        df = get_data_frame(file_path)
        df = df[(df['email'] != t[0]) | (df['song_name'] != t[1])]
        save_data_frame(df, file_path)
    except Exception as e:
        print("Error:", e)

# Modify the log function to query the DataFrame
def log(id, file_path="reg_details.xlsx"):
    try:
        df = get_data_frame(file_path)
        data = df[df['email'] == id][['email', 'password']].values.tolist()
        return data
    except Exception as e:
        print("Error:", e)

# Modify the selectrec function to query the DataFrame
def selectrec(id, file_path="reg_details.xlsx"):
    try:
        df = get_data_frame(file_path)
        data = df[df['email'] == id][['email']].values.tolist()
        return data
    except Exception as e:
        print("Error:", e)

# Modify the checkreg function to use the selectrec function
def checkreg(email, file_path="reg_details.xlsx"):
    sel = selectrec(email, file_path)
    if sel:
        page = "reg"
    else:
        page = "home"
    return page

# Modify the sel_watchlist function to query the DataFrame
def sel_watchlist(id, file_path="watchlist.xlsx"):
    try:
        df = get_data_frame(file_path)
        data = df[df['email'] == id][['song_name', 'url']].values.tolist()
        return data
    except Exception as e:
        print("Error:", e)

# Modify the updaterec function to update rows in the DataFrame
def updaterec(t, file_path="reg_details.xlsx"):
    try:
        df = get_data_frame(file_path)
        df.loc[df['id'] == t[4], ['name', 'email', 'passw', 'contact']] = t[:4]
        save_data_frame(df, file_path)
    except Exception as e:
        print("Error:", e)

def adminlogin(user, file_path="adminlogin.xlsx"):
    try:
        df = get_data_frame(file_path)
        data = df[df['username'] == user][['username', 'password']].values.tolist()
        return data
    except Exception as e:
        print("Error:", e)

def regusers(file_path="reg_details.xlsx"):
    try:
        df = get_data_frame(file_path)
        return df
    except Exception as e:
        print("Error:", e)

# import pymysql as p

# def getconnection():
#     return p.connect(host="localhost", user="root", password="", database="musicapp")

# def insertrec(t):
#     try:
#         db = getconnection()
#         cr = db.cursor()
#         sql = "insert into reg_details(username,email,password) values(%s,%s,%s)"
#         cr.execute(sql, t)
#         db.commit()
#         db.close()
#     except:
#         a="error"
#         return a
  
# def addwatchlist(t):
#     db = getconnection()
#     cr = db.cursor()
#     sql = "insert into watchlist(email,song_name,url) values(%s,%s,%s)"
#     cr.execute(sql, t)
#     db.commit()
#     db.close()
  


# def displayrec():
#     db = getconnection()
#     cr = db.cursor()
#     sql = "select * from reg_details"
#     cr.execute(sql)
#     data = cr.fetchall()
#     db.commit()
#     db.close()
#     return data


# def removewl(t):
#     db = getconnection()
#     cr = db.cursor()
#     sql = "delete from watchlist where email=%s and song_name=%s"
#     cr.execute(sql, t)
#     db.commit()
#     db.close()


# def log(id):
#     db = getconnection()
#     cr = db.cursor()
#     sql = "select email,password from reg_details where email=%s"
#     cr.execute(sql, id)
#     data = cr.fetchall()
#     print(data)
#     db.commit()
#     db.close()
#     return data


# def selectrec(id):
#     db = getconnection()
#     cr = db.cursor()
#     sql = "select email from reg_details where email=%s"
#     cr.execute(sql, id)
#     data = cr.fetchall()
#     print(data)
#     db.commit()
#     db.close()
#     return data

# def checkreg(email):
#     sel=selectrec(email)
#     for i in sel:
#         for j in i:
#             if j==email:
#                 page="reg"
#                 return page
#             else:
#                 page="home"
#     if page=="home":
#         return page

# def sel_watchlist(id):
#     db = getconnection()
#     cr = db.cursor()
#     sql = "select song_name,url from watchlist where email=%s"
#     cr.execute(sql, id)
#     data = cr.fetchall()
#     print(data)
#     db.commit()
#     db.close()
#     return data


# def updaterec(t):
#     db = getconnection()
#     cr = db.cursor()
#     sql = "update reg_details set name=%s,email=%s,passw=%s,contact=%s where id=%s"
#     cr.execute(sql, t)
#     db.commit()
#     db.close()

# def adminlogin(user):
#     db = getconnection()
#     cr = db.cursor()
#     sql = "select username,password from adminlogin where username=%s"
#     cr.execute(sql, user)
#     data = cr.fetchall()
#     db.commit()
#     db.close()
#     return data

# def regusers():
#     db = getconnection()
#     cr = db.cursor()
#     sql = "select * from reg_details"
#     cr.execute(sql)
#     data = cr.fetchall()
#     db.commit()
#     db.close()
#     return data
