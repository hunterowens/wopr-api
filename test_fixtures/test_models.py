from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Boolean, DateTime, Date, Column, Float
from geoalchemy2 import Geometry

Base = declarative_base()

class Master(Base):
    __tablename__ = 'dat_master'
    master_row_id = Column(Integer, primary_key=True)
    start_date = Column(Date, default=None)
    end_date = Column(Date, default=None)
    current_flag = Column(Boolean)
    location = Column(String)
    latitude = Column(Float(precision=53))
    longitude = Column(Float(precision=53))
    obs_date = Column(Date, default=True)
    obs_ts = Column(DateTime)
    geotag1 = Column(String(length=50))
    geotag2 = Column(String(length=50))
    geotag3 = Column(String(length=50))
    dataset_name = Column(String(length=50))
    dataset_row_id = Column(Integer)
    geom = Column(Geometry(geometry_type=u'POINT', srid=4326))

class Crime(Base):
    __tablename__ = 'dat_chicago_crimes_all'
    chicago_crimes_all_row_id = Column(Integer, primary_key=True, nullable=False)
    start_date = Column(Date, default=None)
    end_date = Column(Date, default=None)
    current_flag = Column(Boolean)
    id = Column(Integer)
    case_number = Column(String(length=10))
    orig_date = Column(DateTime)
    block = Column(String(length=50))
    iucr = Column(String(length=10))
    primary_type = Column(String(length=100))
    description = Column(String(length=100))
    location_description = Column(String(length=50))
    arrest = Column(Boolean)
    domestic = Column(Boolean)
    beat = Column(String(length=10))
    district = Column(String(length=5))
    ward = Column(Integer)
    community_area = Column(String(length=10))
    fbi_code = Column(String(length=10))
    x_coordinate = Column(Integer)
    y_coordinate = Column(Integer)
    year = Column(Integer)
    updated_on = Column(DateTime, default=None)
    latitude = Column(Float(precision=53))
    longitude = Column(Float(precision=53))
    location = Column(String(length=50))

class BusinessLicense(Base):
    __tablename__ = 'dat_chicago_business_licenses'
    chicago_business_licenses_row_id = Column(Integer, primary_key=True, nullable=False)
    start_date = Column(Date, default=None)
    end_date = Column(Date, default=None)
    current_flag = Column(Boolean)
    id = Column(String(length=20))
    license_id = Column(Integer)
    account_number = Column(Integer)
    site_number = Column(Integer)
    legal_name = Column(String(length=150))
    doing_business_as_name = Column(String(length=150))
    address = Column(String(length=80))
    city = Column(String(length=30))
    state = Column(String(length=2))
    zip_code = Column(String(length=5))
    ward = Column(Integer)
    precinct = Column(Integer)
    police_district = Column(Integer)
    license_code = Column(Integer)
    license_description = Column(String(length=100))
    license_number = Column(Integer)
    application_type = Column(String(length=50))
    payment_date = Column(Date, default=None)
    license_term_start_date = Column(Date, default=None)
    license_term_expiration_date = Column(Date, default=None)
    date_issued = Column(Date, default=None)
    license_status = Column(String(length=10))
    license_status_change_date = Column(Date, default=None)
    latitude = Column(Float(precision=53))
    longitude = Column(Float(precision=53))
    location = Column(String(length=50))
