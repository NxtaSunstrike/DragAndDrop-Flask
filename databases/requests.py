from .database import Cloths,Session
from sqlalchemy import select

def add_cloth(cloth:dict[str|int]):
    with Session() as session:
        with session.begin():
            
            new_cloth = Cloths(
                name = cloth['name'],
                description = cloth['description'],
                count = cloth['count'],
                price = cloth['price'],
                img_paths = ','.join(cloth['img_paths'])
            )
        session.add(new_cloth)
        session.commit()

def get_cloths():
    with Session() as session:
        result = session.execute(select(Cloths))
        return result.scalars().all()

def get_cloth_by_id(id):
    with Session() as session:
        result = session.execute(select(Cloths).where(Cloths.id == id))
        return result.scalars().first()