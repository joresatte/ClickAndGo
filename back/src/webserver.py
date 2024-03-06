from flask import Flask, request
from flask_cors import CORS, cross_origin
from src.lib.utils import object_to_json
from src.domain.customer_data import Customer_data as client
from src.domain.employee import Employee
# import requests
import json

def create_app(repositories):
    app = Flask(__name__)
    CORS(app)#, resources=r'/api/*'

    # @app.route("/api/carrito", methods=["POST"])
    # def carrito_post_all():
    #     body= request.json
    #     phones= Carrito(**body)
    #     repositories["carrito"].save(phones)
    #     return object_to_json(phones)

    # @app.route("/api/employee_data", methods=["POST"])
    # def employee_post():
    #     body= request.json
    #     employee= Employee(**body)
    #     repositories["employee_data"].save(employee)
    #     return object_to_json(employee)
    
    @app.route("/api/get_login/Authenticated", methods=["POST"])
    @cross_origin(allow_headers=['Content-Type'])
    def get_login():
        data= request.json
        print(data)
        employee= repositories["employee_data"].get_by_identification_and_password(data['identification'], data['password'])
        if employee is None or (data['password']) != employee.password or (data['identification']) != employee.identification:
            return 'invalid log In', 401
        else:
            return employee.to_dict()
    
    @app.route("/api/all_pending/customers_data", methods=["GET"])
    @cross_origin(allow_headers=['Content-Type'])
    def get_pending_customers():
        customers = repositories['customer_data'].get_pending_data()
        # get_pending_customers.__name__ = func.__name__
        return object_to_json(customers)

    @app.route("/api/all_delivered/customers_data", methods=["GET"])
    @cross_origin(allow_headers=['Content-Type'])
    def get_delivered_customers():
        customers = repositories['customer_data'].get_delivered_data()
        return object_to_json(customers)
    
    @app.route("/api/one_customer/<id>", methods=["GET"])
    @cross_origin(allow_headers=['Content-Type'])
    def get_one_customer(id):
        one_customer = repositories['customer_data'].get_customer(id)
        if one_customer is not None:
            return object_to_json(one_customer)


    @app.route("/api/remove_one_customer/<id>", methods=["DELETE"])
    @cross_origin(allow_headers=['Content-Type'])
    def delete_one_customer(id):
        remove_one_customer = repositories['customer_data'].deleted_record_by_id(id)
        return ""
    
    @app.route("/api/customer_data/update/<id>", methods=["PUT"])
    @cross_origin(allow_headers=['Content-Type'])
    def update_customer_data(id):
        data = request.json
        print('---------data_request', data)
        if id!=data["id"] and data['status']!='Entregado':
            return '', 405
        else:
            client_data = client( **data)
            repositories["customer_data"].update_data(client_data)
            return '', 200



    # def pull_data_from_external_Api():
    #     url= 'https://api.covid19india.org/state_district_wise.json'
    #     header= {"Content-Type":"appliction/json"}
    #     response_API = requests.get(url, header)
    #     print(response_API.status_code)
    #     data = response_API.json #response_API.text
    #     print(data)
    #     parse_json= json.loads(data)
    #     active_case = parse_json['id']['cliente']['dni']['address']['phone']['delivery_note']['order_data']['orders_packages']['receptor_data']['returned_product']
    #     print("Active cases in South Andaman:", active_case)
    #     return active_case
    
    # def save_data_from_external_Api():
    #     drivers= pull_data_from_external_Api()
    #     for dr in drivers:
    #         name = dr["familyName"]
    #         number = dr["permanentNumber"]
    #         sql = 'INSERT INTO Drivers (name,number) VALUES(?,?)'
    #         val = (name,number)
    #         cur.execute(sql,val)

    return app
