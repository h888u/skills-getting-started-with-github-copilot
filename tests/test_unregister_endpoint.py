def test_unregister_success_removes_participant(client):
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/Chess%20Club/signup?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete("/activities/Unknown%20Club/signup?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_non_participant_returns_404(client):
    response = client.delete("/activities/Chess%20Club/signup?email=not-enrolled@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
