from flask import Flask, render_template, redirect, flash, request, url_for 

app = Flask(__name__)

#Routes
#Home Page Route
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#portfolio Page Route
@app.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

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
