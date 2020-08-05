from app import db


class ServiceGroup(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60), unique=True, nullable=False)


    def __repr__(self):
        return self.name

class Transaction(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    client=db.Column(db.String(60), unique=True, nullable=False)
    service=db.Column(db.String(100))
    service_group_id=db.Column(db.Integer, db.ForeignKey('service_group.id'))
    service_group = db.relationship("ServiceGroup")
    created_at = db.Column(db.Date)
    renewal=db.Column(db.Date)
    amount=db.Column(db.String(50))
    status=db.Column(db.String(10))

    def __repr__(self):
        return self.id

class Order(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    client=db.Column(db.String(60), unique=True, nullable=False)
    service=db.Column(db.String(100))
    service_group_id=db.Column(db.Integer, db.ForeignKey('service_group.id'))
    service_group = db.relationship("ServiceGroup")
    created_at = db.Column(db.Date)
    renewal=db.Column(db.Date)
    amount=db.Column(db.String(50))
    status=db.Column(db.String(10))

    def __repr__(self):
        return self.id

db.create_all()
