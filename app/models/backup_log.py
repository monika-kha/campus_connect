
from datetime import datetime
from app import db


class BackupLog(db.Model):
    __tablename__ = "backup_logs"

    id = db.Column(db.Integer, primary_key=True)
    s3_key = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="SUCCESS")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
