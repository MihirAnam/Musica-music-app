from functions import *
from flask import *
from db_reg import *
from pathlib import Path
import shutil

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
@app.route("/index")
def open():
    path = str(Path.home())
    file=os.listdir(path)
    dlist=filterdownload(file)
    dlist=dlist[0:5]
    return render_template("index.html",image="show",dlisthome=dlist)

@app.route("/regpage")
def registerpage():
    return render_template("reg.html")


@app.route("/radio")
def radio():
    return render_template("index.html",radio="show")


@app.route("/playradio")
def playradio():
    link=request.args.get('link')
    name=request.args.get('rname')
    return render_template("index.html",radio="show",play="radio",rname=name,url=link)


@app.route("/register",methods=['post'])
def reg():
    username=request.form['username']
    email=request.form['email']
    password=request.form['password']
    t=(username,email,password)
    session['email']=email
    i=insertrec(t)
    if i=="error":
        return render_template("reg.html",e="exist")
    else:
        return render_template("index.html",r="registered" ,image="show",register="sucessful")
   

@app.route("/login",methods=['post'])
def login():
    email=request.form['email']
    password=request.form['password']
    t=[email,password]
    session['email']=email
    
    l=log(email)
    if t in l:
        return render_template("index.html",r="registered" ,image="show",login="sucessful")
    else:
        return render_template("reg.html",e="invalid")
        
   
@app.route("/search",methods=['GET'])
def search():
    user_query= request.args.get("searchmusic")
    ans1=query(user_query)
    return render_template("index.html",answer1=ans1,r="Results:")


@app.route("/play")
def playmusic():
    dir = 'static/audio/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))    
    link=request.args.get('link')
    imageurl=request.args.get('image')
    playmusic=play(link)
    dir1 = 'static/audio'
    mlist=[]
    for m in os.listdir(dir1):
        mlist.append(m)   
    return render_template("index.html",music_list=mlist,image="show",imagelink=imageurl)


@app.route("/dloffline", methods=['post'])
def dl():
    link=request.form['url']
    download(link)
    return redirect("/downloads")

@app.route("/downloads")
def downloads():
    path = str(Path.home() / "Downloads")
    file=os.listdir(path)
    dlist=filterdownload(file)
    return render_template("index.html",downloads=dlist , d="downloads")


@app.route("/playoffline")
def playmusicoffline():
    dir = 'static/downloads/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    link=request.args.get('link')
    path=str(Path.home() / "Downloads/" / link)
    url=path
    dest="static/downloads/song.mp3"
    shutil.copy(url, dest)
    return render_template("index.html",u=url,offlineurl=link,image="show",play="offline")


@app.route("/add",methods=['post'])
def watchlist():
    email=request.form['email']
    song_name=request.form['song_name']
    url=request.form['url']
    try:
        if session['email']!=email:
            v="nosession"
    except:
        return render_template("reg.html")
    
    t=(email,song_name,url)
    addwatchlist(t)
    return redirect("/view_watchlist?email="+email)
    

@app.route("/view_watchlist")
def view_watchlist():
    email=request.args.get('email')
    if email=="":
        return render_template("reg.html")
    else:
        wl=sel_watchlist(email)
        wl = wl[::-1]
        return render_template("index.html",wlist=wl,w="watchlist")
    

@app.route("/removewatchlist",methods=['post'])
def remove():
    email=request.form['email']
    song_name=request.form['song_name']
    t=(email,song_name)
    removewl(t)
    return redirect("/view_watchlist?email="+email)

@app.route('/logout')
def logout():
   session.pop('email', None)
   return redirect('/')



@app.route("/admin")
def admin():
    return render_template("adminindex.html",login="pending")


@app.route("/adminlogin",methods=['post'])
def al():
    username=request.form['user']
    password=request.form['password']
    t=(username,password)
    l=adminlogin(username)
    if t in l:
        ru=regusers()
        return render_template("adminindex.html",login="sucessful",regusers=ru)
    else:
        return render_template("adminindex.html",login="pending")
        

@app.route("/adminlogout")
def adminlogout():
    return redirect("/admin")


# if __name__ == "__main__":
#     app.run(debug=True,host="0.0.0.0")
