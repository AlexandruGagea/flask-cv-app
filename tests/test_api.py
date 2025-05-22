def test_education_success(client):
    res = client.get("/education?token=supersecrettoken123")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_education_unauthorized(client):
    res = client.get("/education")
    assert res.status_code == 401
