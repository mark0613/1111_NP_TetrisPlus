from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


load_dotenv()

DB_SETTINGS = {
    "host" : os.getenv("DB_HOST"),
    "port" : int(os.getenv("DB_PORT")),
    "user" : os.getenv("DB_USER"),
    "password" : os.getenv("DB_PASSWORD"),
    "database" : os.getenv("DB_DATABASE"),
    "charset" : "utf8",
}
DB_URL = f"mysql+pymysql://{DB_SETTINGS['user']}:{DB_SETTINGS['password']}@{DB_SETTINGS['host']}:{DB_SETTINGS['port']}/{DB_SETTINGS['database']}"
DB_ENGINE = create_engine(DB_URL)
DB_SESSION = sessionmaker(autocommit=False, autoflush=False, bind=DB_ENGINE)

SERVER_PORT = os.getenv("SERVER_PORT")
