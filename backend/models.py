from server import db


class CityModel(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True, nullable = False)
    open_id = db.Column(db.Integer, nullable = False)
    
    @classmethod
    def find_by_open_id(cls, open_id):
       return cls.query.filter_by(open_id = open_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



