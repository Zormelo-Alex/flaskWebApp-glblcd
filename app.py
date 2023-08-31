from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from flask_mail import Mail, Message

load_dotenv()
app = Flask(__name__)

# def connect_to_db() -> sqlite3.Connection:
#     conn = sqlite3.connect('sqlitedb.db')
#     return conn

app.config['MAIL_SERVER']= str(os.getenv('MAIL_SERVER'))
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


# app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = 'ec8d1dd0ed8211'
# app.config['MAIL_PASSWORD'] = '0692ad77bd71cc'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

print(type(app.config['MAIL_SERVER']))
print(type(app.config['MAIL_PORT']))
print(type(app.config['MAIL_USERNAME']))
print(type(app.config['MAIL_PASSWORD']))
print(type(app.config['MAIL_USE_TLS']))
print(type(app.config['MAIL_USE_SSL']))

mail = Mail(app)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.get("/signup")
@app.post("/signup")
def signup():
    if request.method == "POST":
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']

        try:
            con = connect_to_db()
            con.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INT PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                );
            ''')
            con.execute('''
            INSERT INTO users(
                    firstname,lastname,email
                ) VALUES (?,?,?)
            ''',(firstname,lastname,email))
            con.commit()
            con.close()
            return str("Sucess")
        except sqlite3.Error as e:
            return str(e)
    return render_template('signup.html')

@app.post('/mail')
@app.get('/mail')
def send_mail():
    if request.method == 'POST':
        name = request.form.get('fullName')
        email = request.form.get('email')
        message_sent = request.form.get('message')
        message = Message(
            subject = f"How are you doing today? {name}",
            recipients = ["alexzormelo9@gmail.com"],
            sender = email
        )
        message.body = message_sent
        
        try:
            mail.send(message)
            return render_template('thankYou.html')
        except Exception as e:
            return ("error occured ", e)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')