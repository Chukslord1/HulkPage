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

class Reminder(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    text=db.Column(db.String(200), unique=True, nullable=False)
    status=db.Column(db.String(10))
    period=db.Column(db.String(10))
    time=db.Column(db.Date)


class Pay_Invoice(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(100))
    status = db.Column(db.String(10))
    create_date=db.Column(db.Date)
    last_pay_date=db.Column(db.Date)
    tax_type=db.Column(db.String(20))
    tax_exempt=db.Column(db.String(10))
    description=db.Column(db.String(100))
    amount=db.Column(db.Integer())

class Ticket(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    topic=db.Column(db.String(200))
    department=db.Column(db.String(50))
    staff=db.Column(db.String(100))
    create_date=db.Column(db.Date)
    status=db.Column(db.String(20))

db.create_all()
