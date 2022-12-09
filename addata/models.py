from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

 
class Breadcrumb(db.Model):
    __tablename__ = 'breadcrumbs'

    id = db.Column(db.Integer, primary_key = True)
    advertiser_id= db.Column(db.String(50))
    platform= db.Column(db.String(25))
    location_at= db.Column(db.BigInteger)
    local_location_at = db.Column(db.DateTime)
    latitude= db.Column(db.Float)
    longitude= db.Column(db.Float)
    horizontal_accuracy= db.Column(db.Float)
    vertical_accuracy= db.Column(db.Float)
    heading= db.Column(db.Float)
    speed= db.Column(db.Float)
    ipv_4= db.Column(db.String(25))
    ipv_6= db.Column(db.String(25))
    final_country= db.Column(db.String(5))
    region= db.Column(db.String(50))
    iso_region= db.Column(db.String(20))
    geohash= db.Column(db.String(20))
    user_agent= db.Column(db.String(250))
    background= db.Column(db.Float)
    publisher_id= db.Column(db.String(50))
    wifi_ssid= db.Column(db.String(50))
    wifi_bssid= db.Column(db.String(25))
    tech_signals= db.Column(db.String(250))
    carrier= db.Column(db.String(50))
    manufacturer= db.Column(db.String(50))
    device_model= db.Column(db.String(25))
    network= db.Column(db.String(25))

    