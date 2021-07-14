import csv
import os
from pprint import pprint as pp
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from sqlalchemy.orm.session import Session

sqlite = 'sqlite:///sql.db'

Base = declarative_base()

class License(Base):
    __tablename__ = 'licenses'
    
    id = Column(Integer, primary_key=True)
    """ Primary key """
    name = Column(String(255))
    """ License holder's name """
    address = Column(String(255))
    """ Address """
    postcode = Column(String(255))
    """ Postcode """
    city = Column(String(255))
    """ City """
    license_granting_date = Column(String(255))
    """ License granting date in format dd.mm.yyyy """
    license_type = Column(String(255))
    """ License type as a string (in Finnish) """
    business_id = Column(String(255))
    """ Business id or N/A if not applicable """
    created_at  = Column(DateTime, default=datetime.utcnow)
    """ Automatically generated date and time of insertion """

    def __repr__(self):
        """ String representation of the object """
        return "<License (name='%s', created_at='%s')>" % (self.name, self.created_at)

db = create_engine(sqlite)
Session = sessionmaker(bind=db)

#Base.metadata.create_all(db)

def insert2db(name, address, postcode, city, date, type, businessid):
    new_row = License(name=name, address=address, postcode=postcode, city=city, license_granting_date=date, license_type=type, business_id=businessid)
    db = Session()
    db.add(new_row)
    db.commit()
    id = new_row.id
    db.close()
    return id    
 
pp(insert2db('test','test','test','test','test','test','test'))
   