def test_signup_success_adds_participant(client):
    email = "newstudent@mergington.edu"

    response = client.post(f"/activities/Chess%20Club/signup?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"

    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_duplicate_returns_400(client):
    existing_email = "michael@mergington.edu"

    response = client.post(f"/activities/Chess%20Club/signup?email={existing_email}")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_signup_unknown_activity_returns_404(client):
    response = client.post("/activities/Unknown%20Club/signup?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
