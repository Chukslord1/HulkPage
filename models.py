from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy import relationship
from flask_appbuilder import Model



class ServiceGroup(Model):
    id= Column(Integer, primary_key=True)
    name=Column(Integer, unique=True, nullable=False)


    def __str__(Self):
        return self.name

class Transaction(Model):
    id= Column(Integer, primary_Key=True)
    client=Column(String(60), unique=True, nullable=False)
    service=Column(String(100))
    service_group_id=Column(Integer, ForeignKey('service_group.id'))
    service_group = relationship("ServiceGroup")
    created_at = Column(Date)
    renewal=Column(Date)
    amount=Column(String(50))
    status=Column(String(10))

    def __str__(self):
        return self.id
