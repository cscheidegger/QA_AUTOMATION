from api_client import APIClient

def test_api_flow():
    client = APIClient()
    username = "testuser"
    password = "Password123!"

    # 1. Criar Usuário
    user = client.create_user(username, password)
    user_id = user["userID"]
    assert "userID" in user

    # 2. Gerar Token
    token = client.generate_token(username, password)["token"]
    assert token

    # 3. Verificar Autorização
    assert client.authorize_user(username, token)

    # 4. Listar Livros
    books = client.list_books()
    assert len(books) > 0

    # 5. Reservar Dois Livros
    chosen_books = [books[0]["isbn"], books[1]["isbn"]]
    reservation = client.reserve_books(user_id, token, chosen_books)
    assert reservation

    # 6. Detalhes do Usuário
    user_details = client.get_user_details(user_id, token)
    assert len(user_details["books"]) == 2
