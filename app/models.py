from app import db
from datetime import datetime
import uuid

class Base(db.Model):
    '''
    Base defines the common fields in the User and the Scores model.
    '''
    __abstract__ = True
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id = db.Column(db.String(20), primary_key=True, default=str(uuid.uuid4()))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
        db.session.flush()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        db.session.flush()

    def update(self):
        db.session.commit()
        return self

class User(Base):
    '''
    User defines the fields that hold a user information.
    '''
    email = db.Column(db.String(140), unique=True, nullable=False)
    username = db.Column(db.String(140), unique=True, nullable=False)
           
    def get_user(self, user_id):
        return self.query.filter_by(id=user_id).first()

    def get_users(self):
           return self.query.all()

    def __repr__(self):
        return "<User Id:%r, CreateAt:%r UpdatedAt:%r Username:%r, Email:%r >" % (
            self.id, self.created_at, self.updated_at, self.username, self.email)

class Level(Base):
    '''
    Level defines the fields that represent the score a user had after playing the game level.
    '''
    game_level  = db.Column(db.Integer)
    score = db.Column(db.Integer)
    user_id = db.Column(db.String(20), db.ForeignKey("user.id"), nullable=False)

    def get_level(self, score_id):
        return self.query.filter_by(id=score_id).first()

    def get_levels(self):
           return self.query.all()

    def __repr__(self):
        return "<Levels Id:%r, CreatedAt:%r, UpdatedAt:%r, Level:%r, Score:%r>" % (
            self.id, self.created_at, self.updated_at, self.game_level, self.score)

def format_time(timestamp):
    if timestamp is None:
        return ""
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def return_data(val):
    if isinstance(val, User):
        return {
            "CreatedAt": "" if val is None else format_time(val.created_at),
            "Email": "" if val is None else val.email,
            "ID": "" if val is None else val.id,
            "UpdatedAt": "" if val is None else format_time(val.updated_at),
            "Username": "" if val is None else val.username,
        }
    else: 
        return {
            "CreatedAt": "" if val is None else format_time(val.created_at),
            "ID": "" if val is None else val.id,
            "Level": "" if val is None else val.game_level,
            "Score": "" if val is None else val.score,
            "UpdatedAt": "" if val is None else format_time(val.updated_at),
            "UserID": "" if val is None else val.user_id,
        }