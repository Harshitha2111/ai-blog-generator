import json
import importlib.util
import sys

# Explicitly load app.py (stable inside Docker)
spec = importlib.util.spec_from_file_location("app", "/app/app.py")
app_module = importlib.util.module_from_spec(spec)
sys.modules["app"] = app_module
spec.loader.exec_module(app_module)

app = app_module.app


# ---------- Test Case 1: Mental Health - Short ----------
def test_mental_health_short():
    client = app.test_client()

    with open("tests/test_data.json") as f:
        data = json.load(f)["mental_health_short"]

    response = client.post("/", data=data)

    assert response.status_code == 200
    print("✅ Test Case 1 Passed: Mental Health (Short blog)")


# ---------- Test Case 2: Mental Health - Medium ----------
def test_mental_health_medium():
    client = app.test_client()

    with open("tests/test_data.json") as f:
        data = json.load(f)["mental_health_medium"]

    response = client.post("/", data=data)

    assert response.status_code == 200
    print("✅ Test Case 2 Passed: Mental Health (Medium blog)")


# ---------- Test Case 3: Robotics - Long ----------
def test_robotics_long():
    client = app.test_client()

    with open("tests/test_data.json") as f:
        data = json.load(f)["robotics_long"]

    response = client.post("/", data=data)

    assert response.status_code == 200
    print("✅ Test Case 3 Passed: Robotics (Long blog)")
