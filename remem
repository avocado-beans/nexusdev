# importing Flask and other modules
from flask import Flask, request, render_template 
from email_sender import *
 
# Flask constructor
app = Flask(__name__)   
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
       full_name = request.form.get("full_name")
       email = request.form.get("email")
       phone_number = request.form.get("phone_number") 
       message = request.form.get("message")
       msg = "Full Name "+full_name+"\n"+"Email "+email+"\n"+"Phone Number "+phone_number+"\n"+"Message "+message

       # this is the email of the recipient of the message form
       # currently my email but you can change it to yours to get the from message
       # check your spam, that's where i found the messages at first
       recipient = "orthodoxrabbibillclinton42@gmail.com"
       send_email(recipient, msg)
       print("kace.yokohama@gmail.com", email, phone_number, message)
    return render_template("index.html")

@app.route('/about', methods =["GET", "POST"])
def about():
    return render_template("about.html")
    
@app.route('/contact', methods =["GET", "POST"])
def contact():
    if request.method == "POST":
       full_name = request.form.get("full_name")
       email = request.form.get("email")
       phone_number = request.form.get("phone_number") 
       message = request.form.get("message")
       msg = "Full Name "+full_name+"\n"+"Email "+email+"\n"+"Phone Number "+phone_number+"\n"+"Message "+message

       recipient = "orthodoxrabbibillclinton42@gmail.com"
       send_email(recipient, msg)
       print("kace.yokohama@gmail.com", email, phone_number, message)
    return render_template("contact.html")
    
@app.route('/service', methods =["GET", "POST"])
def service():
    return render_template("service.html")
    
    
if __name__=='__main__':
   app.run()

