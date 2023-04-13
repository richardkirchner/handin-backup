from flask import Blueprint, Flask, render_template, redirect, url_for, send_file, request, current_app
from .models import event
#from app.events.models import event, event_date, event_discription, events
#from .services.create_event import create_event
from app.extensions.database import db


blueprint = Blueprint('events',__name__)

@blueprint.route('/events')
def get_events():
  events = event.query.all()
  page_number = request.args.get('page', 1, type=int)
  events_pagination = event.query.paginate(page=page_number, max_per_page=current_app.config['EVENTS_MAX_PER_PAGE'])
  return render_template('events.html',events_pagination=events_pagination, events=events)

@blueprint.route('/register', methods=('GET','POST'))
def post_events():

  if request.method == 'POST':
    new_event=event(
      name=request.form['event'],
      date=request.form['event_date'],
      desc=request.form['event_discription']
    )
    print(db)
    db.session.add(new_event)
    db.session.commit()
    print("new event is saved", new_event)
    return redirect(url_for('events.get_events'))
  return render_template('register.html')


@blueprint.route('/')
def index():
  return render_template('index.html')

@blueprint.route('/register')
def register():
  return render_template('register.html')

def register_blueprint(app: Flask):
   #app.register_blueprint(users.routes.blueprint)
   app.register_blueprint(event.routes.blueprint)


