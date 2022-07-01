## Tutorial
PyBCN April 2019 practice session by Ricardo Martinez [@lordrip](http://twitter.com/lordrip)

### Topics
<ul>
   <li>pythonanywhere.com</li>
   <li>firebase push notifications</li>
</ul>

---

### What is firebase?

<p>Firebase is set of cloud based services, offered by Google with a free tier program for testing small personal projects. This tutorial focuses on one of those services: Firebase Messaging. It allows sending and receiving push notifications on mobiles and web pages.</p>
--

### What is pythonanywhere.com?

<p>pythonanywhere.com is a Python cloud service. The scope of this service includes Bash and Python terminals, Django web apps, Flask, MySQL to save data and a `cron` facility to specify tasks to be executed at specific times. The service has a free tier program that admits small personal projects.</p>
---

### Tutorial build objective

<p>Build a simple app with Flask. The app does three things:</p>
<ul>
   <li>receive a web token</li>
   <li>store it in a sqlite database3cw,</li>
   <li>subsequently send a push notification</li>
</ul>
---

### Tutorial basic requirements

<ul>
  <li>Flask app</li>
  <li>Notifier</li>
  <li>Serve our app</li>
  <li>Schedule our notifier</li>
</ul>

---

### Flask app functionality and code

<ul>
  <li>Serve static code (firebase.js, service worker and templates)</li>
  <li>Provide an endpoint for submit the token</li>
</ul>

--

#### Simple Flask app

<pre><code class="hljs python">
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask"

app.run()
</code></pre>

--

#### Render a template

<pre><code class="hljs python">
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home01.html')

app.run()
</code></pre>

--

#### Using Blueprints

<pre><code class="hljs python">
from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return 'index.html'
</code></pre>

---

### Notifier.py functionality and code

<ul>
  <li>A script that will be triggering push notifications to all users in our database</li>
</ul>

--

#### Notifier

<pre><code class="hljs python">
import requests
from models import User
from sqlalchemy import create_engine, orm

def notify_all():
    engine = create_engine('sqlite:///notifications.db')
    session = orm.sessionmaker(bind=engine)()

    for record in session.query(User).all():
        data["to"] = record.token

        req = requests.post(fcm_url, json=data, headers=headers)
        print(req.json())


if __name__ == "__main__":
    notify_all()
</code></pre>

---

### Pythonanywhere functionality and code

<ul>
  <li>Serve our web app</li>
  <li>Schedule our notifier.py</li>
</ul>

---
