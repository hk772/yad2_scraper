from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'

    p_id = Column(Integer, primary_key=True)
    city = Column(String(50))
    street = Column(String(50))
    street_num = Column(Integer)
    property_type = Column(String(50))
    area = Column(String(50))
    room_num = Column(Integer)
    floor = Column(Integer)
    size = Column(Integer)
    price = Column(Integer)
    property_category = Column(String(50), primary_key=True)

    def __init__(self, p_id, city, street, street_num, property_type, area, room_num, floor, size, price, property_category):
        self.p_id = p_id
        self.city = city
        self.street = street
        self.street_num = street_num
        self.property_type = property_type
        self.area = area
        self.room_num = room_num
        self.floor = floor
        self.size = size
        self.price = price
        self.property_category = property_category


class RentalProperty(Property):
    __mapper_args__ = {'polymorphic_identity': 'rental'}


class ForSaleProperty(Property):
    __mapper_args__ = {'polymorphic_identity': 'for_sale'}