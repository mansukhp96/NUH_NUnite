import copy
import flask
import json
import os
import random

app = flask.Flask(__name__)
event_dir = 'events'

events = {}
for event in os.listdir(event_dir):
    print('Loading', event)
    events[event] = json.loads(open(os.path.join(event_dir, event)).read())


@app.route('/')
def index():
    return flask.render_template('index.html', event_names=zip(events.keys(), map(lambda q: q['name'], events.values())))


@app.route('/event/<id>')
def event(id):
    if id not in events:
        return flask.abort(404)
    event = copy.deepcopy(events[id])
    return flask.render_template('event.html', id=id, event=event)


@app.route('/register')
def register():
    return flask.render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)