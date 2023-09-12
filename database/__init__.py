from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Подключение и выбор СУБД
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
sessions = sessionmaker(bind=engine)

Base = declarative_base()

# импорт всех моделей
from database import models

# генератор подключений
def get_db():
    db = sessions()
    try:
        yield db

    except:
        db.rollback()
        raise

    finally:
        db.close()




