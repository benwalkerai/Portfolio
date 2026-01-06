from flask import Flask, render_template, redirect, flash, request, url_for 
#from flask_mail import Mail, Message
#from forms import ContactForm
#from config import Config
#from flask_wtf.csrf import CSRFProtect
#import os
#from os import environ as env
#import requests


#load_dotenv()
#ID1 = env.get("ID1")
#ID2 = env.get("ID2")
#KEY = env.get("KEY")
#ID3 = env.get("ID3")
#RECAPTCHA_PRIVATE_KEY = env.get("you-will-never-guess")
#RECAPTCHA_PUBLIC_KEY = env.get("you-wont-guess-again")

app = Flask(__name__)
#app.config.from_object(Config)
#app.config ['RECAPTCHA_USE_SSL'] = False
#app.config['RECAPTCHA_PUBLIC_KEY'] = RECAPTCHA_PUBLIC_KEY
#app.config['RECAPTCHA_PRIVATE_KEY'] = RECAPTCHA_PRIVATE_KEY
#app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}
#csrf = CSRFProtect(app)

#Add Mail app
#app.config['MAIL_SERVER'] = 'smtp.mail.me.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USERNAME'] = ID1
#app.config['MAIL_PASSWORD'] = KEY
#app.config['MAIL_DEFAULT_SENDER'] = ID3
#mail=Mail(app)

#Routes
#Home Page Route
@app.route('/', methods=['GET', 'POST'])
def index():
    #form = ContactForm()
    #if form.validate_on_submit():
    #    name = form.name.data
    #    email = form.email.data
    #    message = form.message.data

    #    msg = Message('New Contact Message', recipients=[ID2])  # Change recipients as needed
    #    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"
    #    mail.send(msg)
    #    flash('Thank you for submitting you message!')
    #    return render_template('index.html', form=form)
    return render_template('index.html')

#portfolio Page Route
@app.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

#@app.route('/contact', methods=['GET', 'POST'])
#def contact():
#    form = ContactForm()
#    if form.validate_on_submit():
#        name = form.name.data
#        email = form.email.data
#        message = form.message.data

#        msg = Message('New Contact Message', recipients=[ID2])  # Change recipients as needed
#        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"
#        mail.send(msg)
#        flash('Thank you for submitting you message!')
#        return render_template('index.html', form=form)
#    return render_template('index.html', form=form)

#@app.route('/contact', methods=['POST'])
#def contact():
#    #
#    #reCAPTCHA verification
#    recaptcha_response = request.form['RECAPTCHA_SITE_KEY']
#    data = {'secret': RECAPTCHA_SECRET_KEY, 'response':recaptcha_response}
#    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
#
#    result = r.json()
#
#    if result['success']:
#        name = request.form['name']
#        email = request.form['email']
#        message = request.form['message']
#        
#        msg = Message('New Contact Message', recipients=[ID2])  # Change recipients as needed
#        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"
#        mail.send(msg)
#
#        flash('Your message has been sent successfully!', 'success')
#    else:
#        flash('reCAPTCHA verification failed. Please try again.', 'danger')
#    return redirect(url_for('index'))

@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')

@app.context_processor
def inject_template_scope():
    injections = dict()
        
    def cookies_check():
        value = request.cookies.get('cookie_consent')
        return value == 'true'
    injections.update(cookies_check=cookies_check)
    return injections

@app.route('/sitemap.xml')
def site_map():
  return render_template('sitemap.xml', base_url='https://www.benwalkerdata.uk')

if __name__ == '__main__':
    app.run(debug=True)
