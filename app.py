from flask import Flask, render_template
from dotenv import load_dotenv
import os
from flask_mail import Mail, Message

load_dotenv()
app = Flask(__name__)

# app.config['MAIL_SERVER']= str(os.getenv('MAIL_SERVER'))
# app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
# app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
# app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))
# app.config['MAIL_USE_TLS'] = bool(os.getenv('MAIL_USE_TLS'))
# app.config['MAIL_USE_SSL'] = bool(os.getenv('MAIL_USE_SSL'))


app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'ec8d1dd0ed8211'
app.config['MAIL_PASSWORD'] = '0692ad77bd71cc'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

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

@app.route("/mail")
def send():
    message = Message(
        subject= "BUTTON EVENT",
        recipients= ["alexzormelo9@gmail.com"],
        sender= "alexanderdodzizee@gmail.com"
    )

    message.body = "I pushed the button"
    try:
        mail.send(message)
        return "sent successfully"
    except Exception as e:
        return ("error occured ", e)


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')