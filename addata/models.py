from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Breadcrumb(db.Model):
    __tablename__ = 'breadcrumbs'

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.BigInteger)
    advertiser_id = db.Column(db.Text)
    platform = db.Column(db.Text)
    location_at = db.Column(db.BigInteger)
    local_location_at = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    horizontal_accuracy = db.Column(db.Float)
    vertical_accuracy = db.Column(db.Float)
    heading = db.Column(db.Float)
    speed = db.Column(db.Float)
    ipv_4 = db.Column(db.Text)
    ipv_6 = db.Column(db.Text)
    final_country = db.Column(db.Text)
    region = db.Column(db.Text)
    iso_region = db.Column(db.Text)
    geohash = db.Column(db.Text)
    user_agent = db.Column(db.Text)
    background = db.Column(db.Float)
    publisher_id = db.Column(db.Text)
    wifi_ssid = db.Column(db.Text)
    wifi_bssid = db.Column(db.Text)
    tech_signals = db.Column(db.Text)
    carrier = db.Column(db.Text)
    manufacturer = db.Column(db.Text)
    device_model = db.Column(db.Text)
    network = db.Column(db.Text)


class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    time_processed = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    
