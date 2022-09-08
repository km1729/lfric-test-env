from psql import db, session, Base
from sqlalchemy import Float, Integer, String, DateTime, \
                         ForeignKey, Column

class model_config(Base):
    __tablename__= "model_config"
    id = Column(Integer, primary_key=True, autoincrement=True)    
    model = Column(String)
    resolution = Column(String) 
    thread = Column(String)
    process= Column(String)
    config = Column(String)
    columns1 = = Column(String)

class model_run(Base):
    __tablename__= "model_run"
    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, nullable=False)
    revision = Column(Integer)
    model_config_id = Column(Integer, ForeignKey('model_config.id'))

class model_profile(Base):
    __tablename__= "model_profile"
    id = Column(Integer, primary_key=True, autoincrement=True)
    routine = Column(String)
    min_time = Column(Float)
    mean_time = Column(Float)
    max_time =Column(Float)
    no_calls = Column(Integer)
    time_perc = Column(Float)
    time_per_call = Column(Float)
    model_run_id = Column(Integer, ForeignKey('model_run.id'))

Base.metadata.create_all(db)
