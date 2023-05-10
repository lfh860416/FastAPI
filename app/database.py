from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:170213@localhost/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"


# engine is responsible for establishing the connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# need session to talk to the sql database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
 
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host = "localhost", database = "fastapi2",
#                                 user = "postgres", password = "170213",
#                                 cursor_factory= RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
