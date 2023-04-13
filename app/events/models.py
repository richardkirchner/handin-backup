from app.extensions.database import db, CRUDMixin

class event(db.Model,CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    date = db.Column(db.Integer)
    desc =db.Column(db.String(1024))
    # event_date = db.relationship('event_date', backref='event', uselist=False, lazy=True)
    # event_discription = db.relationship('event_discription', backref='event', uselist=False, lazy=True)


# class event_date(db.Model,CRUDMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     event_date = db.Column(db.Integer)
#     event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

# class event_discription(db.Model,CRUDMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     event_discription = db.Column(db.String(250))
#     event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
