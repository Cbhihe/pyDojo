## Tutorial
(PyBCN April 2019 practice session by Ricardo Martinez)

<small>Ricardo Martinez [@lordrip](http://twitter.com/lordrip)</small>

<span>Topics: pythonanywhere.com & firebase push notifications</span>

---

### What is firebase?

<p>Firebase is set of cloud based services that Google offers with a free tier for testing and personal projects</p>
<p>This tutorial is about one of those services: Firebase Messaging. It is a service that allows us to send and receive push notifications on mobiles and web</p>

--

### What is pythonanywhere.com?

<p>pythonanywhere.com is a service that allows us to use python in the cloud. The scope of this service ranges from bash and python terminals, web applications with Django, Flask and more, an instance of MySQL to save data and also allows you to specify tasks that will be executed at certain times.</p>
<p>They also have a free tier program that admits small personal projects.</p>

---

### Tutorial build objective

<p>Build a simple app with Flask. The app will do three things:</p>
<ul>
   <li>receive a web token</li>
   <li>store it in a sqlite database3cw,</li>
   <li>subsequently send a push notifications</li>
</ul>
---

### Basic requirements

<ul>
  <li>Flask app</li>
  <li>Notifier</li>
  <li>Serve our app</li>
  <li>Schedule our notifier</li>
</ul>

---

### Flask app

<ul>
  <li>Serve static code (firebase.js, service worker and templates)</li>
  <li>Provide an endpoint for submit the token</li>
</ul>

--

## Simple Flask app

<pre><code class="hljs python">
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask"

app.run()
</code></pre>

--

## Render a template

<pre><code class="hljs python">
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home01.html')

app.run()
</code></pre>

--

## Using Blueprints

<pre><code class="hljs python">
from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return 'index.html'
</code></pre>

---

### Notifier.py

<ul>
  <li>A script that will be triggering push notifications to all users in our database</li>
</ul>

--

## Notifier

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

### Pythonanywhere

<ul>
  <li>Serve our web app</li>
  <li>Schedule our notifier.py</li>
</ul>

---
