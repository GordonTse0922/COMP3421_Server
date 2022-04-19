from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base
db=SQLAlchemy()
migrate = Migrate()
Base = declarative_base()