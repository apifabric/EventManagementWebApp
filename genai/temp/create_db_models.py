# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Event(Base):
    """Description: Holds details about events in the management system."""

    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    duration = Column(Integer)  # duration in minutes, calculated to ensure max time of 45 mins

    # Logic attributes
    overlap_check = Column(Boolean)



# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    event1 = Event(name="Meeting", start_time=date(2023, 10, 3), end_time=date(2023, 10, 3), duration=30, overlap_check=False)
    event2 = Event(name="Workshop", start_time=date(2023, 10, 3, 11), end_time=date(2023, 10, 3, 11, 45), duration=45, overlap_check=False)
    event3 = Event(name="Conference", start_time=date(2023, 10, 3, 14), end_time=date(2023, 10, 3, 15), duration=60, overlap_check=True)
    event4 = Event(name="Seminar", start_time=date(2023, 10, 3, 16), end_time=date(2023, 10, 3, 17, 30), duration=90, overlap_check=True)
    
    
    
    session.add_all([event1, event2, event3, event4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
