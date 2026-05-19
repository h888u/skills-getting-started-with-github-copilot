def test_get_activities_returns_seed_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, dict)
    assert len(data) == 9
    assert "Chess Club" in data


def test_each_activity_has_expected_fields(client):
    response = client.get("/activities")
    data = response.json()

    for details in data.values():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["description"], str)
        assert isinstance(details["schedule"], str)
        assert isinstance(details["max_participants"], int)
        assert isinstance(details["participants"], list)
