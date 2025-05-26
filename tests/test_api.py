def test_education_success(client):
    res = client.get("/education?token=supersecrettoken123")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_education_unauthorized(client):
    res = client.get("/education")
    assert res.status_code == 401

def test_experience_success(client):
    res = client.get("/experience?token=supersecrettoken123")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_experience_unauthorized(client):
    res = client.get("/experience")
    assert res.status_code == 401

def test_personal_success(client):
    res = client.get("/personal?token=supersecrettoken123")
    assert res.status_code == 200
    assert isinstance(res.get_json(), dict)

def test_personal_unauthorized(client):
    res = client.get("/personal")
    assert res.status_code == 401