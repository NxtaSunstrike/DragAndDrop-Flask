from sqlalchemy import create_engine,text
from sqlalchemy import BigInteger,String,Integer
from sqlalchemy.orm import relationship,Mapped,mapped_column,DeclarativeBase,sessionmaker

from .config import settings

engine = create_engine(
    url = settings.db_url,
    echo=True
)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Cloths(Base):
    __tablename__ = 'cloths'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String)
    description:Mapped[str] = mapped_column(String(50))
    count:Mapped[int] = mapped_column(Integer)
    price:Mapped[int] = mapped_column(Integer)
    img_paths:Mapped[str] = mapped_column(String)

with engine.connect() as conn:
    Base.metadata.create_all(conn)
    conn.commit()


 
