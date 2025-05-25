from infrastructure.db.models import Base
from infrastructure.db.session import engine

Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")