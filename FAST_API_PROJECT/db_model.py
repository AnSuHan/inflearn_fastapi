from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class GangnamguPopulatationDbModel(Base):
    __tablename__ = 'gangnamgu_population'
    
    # db 각 컬럼 할당
    administrative_agency = Column(String)
    total_population = Column(Integer)
    male_population = Column(Integer)
    female_population = Column(Integer)
    sex_ratio = Column(Float)
    number_of_households = Column(Integer)
    number_of_people_per_household = Column(Float)
    id = Column(Integer, primary_key=True)