def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200

    expected = 'This is a CI/CD Pipeline with Kubernetes test. \n Im making changes too!'
    assert expected == res.get_data(as_text=True)
