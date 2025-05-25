# scripts/load_fake_clientes.py
from infrastructure.db.session import SessionLocal
from infrastructure.db.models import Tabela_TBClientes

fake_clientes = [
    {"Nome": "João da Silva", "Email": "joao@email.com", "Telefone": "11999999999",
        "Documento": "123.456.789-00", "Endereco": "Rua A, 123"},
    {"Nome": "Maria Oliveira", "Email": "maria@email.com", "Telefone": "11888888888",
        "Documento": "987.654.321-00", "Endereco": "Rua B, 456"},
    {"Nome": "Oficina Mecânica Zoom", "Email": "zoom@oficina.com", "Telefone": "11777777777",
        "Documento": "12.345.678/0001-99", "Endereco": "Av. Mecânica, 999"},
]


def main():
    session = SessionLocal()
    try:
        for data in fake_clientes:
            # Evita duplicatas por Documento
            exists = session.query(Tabela_TBClientes).filter_by(
                Documento=data["Documento"]).first()
            if not exists:
                cliente = Tabela_TBClientes(**data)
                session.add(cliente)
        session.commit()
        print("Clientes de exemplo adicionados com sucesso!")
    finally:
        session.close()


if __name__ == "__main__":
    main()
