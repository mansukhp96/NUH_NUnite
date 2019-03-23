import copy
import flask
import json
import os
import random
import requests

app = flask.Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8sUz\n\xec]/'
event_dir = 'events'

events = {}
users = {}

db_url = "https://nunite-34b5.restdb.io/rest/students-1"
db_headers = {
    'content-type': "application/json",
    'x-apikey': "905eeebb5594cfa05f380980a450c66c731fe",
    'cache-control': "no-cache"
    }
response = requests.request("GET", db_url, headers=db_headers)
# print(response.text)
data = response.json()
print("Loading from cloud")
for thing in data:
#    print(thing)
#    print(thing['last_name'])
    if 'type' in thing:
        new_type = thing['type']
        thing_name = thing['name']
        if new_type == 'event':
            events[thing_name] = thing
            print(events[thing_name])
        elif new_type == 'user':
            users[thing_name] = thing
        print('Loaded new %s: %s' % (new_type, thing_name))
print(events)
# for event in os.listdir(event_dir):
#    print('Loading', event)
#    events[event] = json.loads(open(os.path.join(event_dir, event)).read())


@app.route('/')
def index():
#    return flask.render_template('index.html', events=events)#event_names=zip(events.keys(), map(lambda q: q['name'], events.values())))
    return flask.render_template('homepage.html', events=events)#event_names=zip(events.keys(), map(lambda q: q['name'], events.values())))


@app.route('/event/<id>')
def event(id):
    if id not in events:
        return flask.abort(404)
    event = copy.deepcopy(events[id])
    return flask.render_template('event.html', id=id, event=event)


@app.route('/create')
def create():
    return flask.render_template('create_event.html', id=id, event=event)


@app.route('/register')
def register():
    return flask.render_template('register_user.html')


@app.route('/add_event', methods=['POST'])
def add_event():
    flask.flash("Event created")

    return flask.render_template('index.html', events=events)


@app.route('/add_user', methods=['POST'])
def add_user():
    flask.flash("Welcome to NUnite!")
    return flask.render_template('index.html', events=events)


if __name__ == '__main__':
    app.run(debug=True)
