import json
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.employee import Employee, Employee_Repository

def test_valid_employee_data():
    employee_repository = Employee_Repository(temp_file())
    app = create_app(repositories={"employee_data": employee_repository})
    client = app.test_client()
    
    employee= Employee(
        id='test_id',
        identification='test_identification',
        password='test_password'
    )
    employee_repository.save(employee)

    body= {
        'identification':'test_identification',
        'password':'test_password'}
    response = client.post("/api/get_login/Authenticated", json= body)
    assert response.status_code == 200
    if response.status_code==200:
        assert response.json=={'identification':'test_identification'}

def test_invalid_employee_data():
    employee_repository = Employee_Repository(temp_file())
    app = create_app(repositories={"employee_data": employee_repository})
    client = app.test_client()
    
    employee= Employee(
        id='test_id',
        identification='test_identification',
        password='test_password'
    )
    employee_repository.save(employee)

    body= {
        'identification':'test_identification',
        'password':'password'}
    response = client.post("/api/get_login/Authenticated", json= body)
    assert response.status_code != 200
    if response.status_code!=200:
        assert response.status_code== 401

def test_other_invalid_employee_data():
    employee_repository = Employee_Repository(temp_file())
    app = create_app(repositories={"employee_data": employee_repository})
    client = app.test_client()
    
    employee= Employee(
        id='test_id',
        identification='test_identification',
        password='test_password'
    )
    employee_repository.save(employee)

    body= {
        'identification':'identification',
        'password':'test_password'}
    response = client.post("/api/get_login/Authenticated", json= body)
    assert response.status_code != 200
    if response.status_code!=200:
        assert response.status_code== 401