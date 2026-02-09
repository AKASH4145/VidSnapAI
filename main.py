from flask import Flask, render_template, request
import uuid
import os
from werkzeug.utils import secure_filename
import subprocess

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create" , methods=["GET","POST"])
def create():
    myid=uuid.uuid1()

    if request.method=="POST":
        print(request.files.keys())
        u_id=str(request.form.get("uuid"))
        desc=request.form.get("text")
        print(u_id,type(u_id))
        print(desc)
        input_file=[]
        for key , Value in request.files.items():
           print(f"Key: {key} | Value: {Value}")
           file=request.files[key]
           if file:
             filename = secure_filename(file.filename)
             if not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],u_id))):
                 os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], u_id))
             file.save(os.path.join(app.config['UPLOAD_FOLDER'], u_id , filename))
             input_file.append(file.filename)
             with open(os.path.join(app.config['UPLOAD_FOLDER'], u_id , "desc.txt"),"w") as f:
                       f.write(desc)
             for i in input_file:
                 a = i

                 name = a.split(" (")[0]        # "screenshot"
                 number = a.split("(")[1].split(")")[0]   # "167"

                 new_name = f"{name}_{number}.png"
                

                 with open(os.path.join(app.config['UPLOAD_FOLDER'], u_id , "input.txt"),"a") as f:
                     f.write(f"file '{new_name}'\n duration 1\n")         

    return render_template("create.html",myid=myid)

@app.route("/gallery")
def gallery():
    reel=os.listdir("static/reels")
    print (reel)
    return render_template("gallery.html", reels=reel)


app.run(debug=True)