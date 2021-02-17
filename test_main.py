import pytest

# To use the Akita/FastAPI integration, replace FastAPI's TestClient
# with akita_fastapi.testclient.TestClient.
#
# from fastapi.testclient import TestClient
from akita_fastapi.testclient import TestClient

from main import app, User

user_1 = "2b9046ac-6112-11eb-ae07-3e22fb0d93ba"
user_2 = "38c15834-6112-11eb-86fb-3e22fb0d93ba"

@pytest.fixture(scope="module")
def client():
    with TestClient(app, har_file_path="my_trace.har") as client:
        yield client

def test_get_user(client):
    response = client.get(f'/users/{user_2}')
    assert response.status_code == 200
    assert response.json()['email'] == "alice@adventuring.org"

def test_file_crud(client):
    # Create file 1
    f1 = client.post(f'/users/{user_1}/files', json={
        'contents': 'Ode to Akita: A poem.'
    })
    assert f1.status_code == 201
    assert 'id' in f1.json()

    # List files
    files = client.get(f'/users/{user_1}/files')
    assert files.status_code == 200
    assert len([f for f in files.json()['files'] if f['contents'] == 'Ode to Akita: A poem.']) == 1

    # Get file 1
    get_f1 = client.get(f'/users/{user_1}/files/{f1.json()["id"]}')
    assert get_f1.status_code == 200
    assert get_f1.json()['contents'] == 'Ode to Akita: A poem.'

    # Create file 2
    f2 = client.post(f'/users/{user_1}/files', json={
        'contents': 'Ode to Akita: Another poem.'
    })
    assert get_f1.status_code == 200

    # List files
    files = client.get(f'/users/{user_1}/files')
    assert files.status_code == 200
    assert len(files.json()['files']) == 2

    # Uncomment to test DELETE file:
    # # Delete file 2
    # deleted = client.delete(f'/users/{user_1}/files/{f2.json()["id"]}')
    # assert deleted.status_code == 204
    #
    # # Try to get deleted file 2
    # bad_get_f1 = client.get('/users/{user_1}/files/{f2.json()["id"]}')
    # assert bad_get_f1.status_code == 404

