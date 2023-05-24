from config import Config
from cloud_db.database import engine_postgresql
from sqlalchemy.orm import sessionmaker
engine = engine_postgresql(
            username=Config.USERNAME,
            host=Config.HOST,
            database=Config.DATABASE,
            password=Config.PASSWORD,
            port=Config.PORT_DB
            )

Session = sessionmaker(bind=engine)

