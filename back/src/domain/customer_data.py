# @author: Jores Atte Mottoh
# @date: 24/10/2023
# @description: Customer_data, Customer_dataRepository class
# @project: Click and Go
# @modified by:
# @modified date:

from src.domain.utils import Utils as U
from src.domain.table_fields import customer_table_fields as customer_fields
from src.domain.table_fields import delivery_note_table_fields as delivery_fields, delivery_note_table_save_fields as delivery_save_fields
from src.domain.table_fields import order_data_table_fields as order_data_fields, order_data_table_save_fields as order_data_save_fields
from src.domain.table_fields import orders_packages_table_fields as orders_packages_fields, orders_packages_table_save_fields as orders_packages_save_fields
from src.domain.table_fields import receptor_data_table_fields as receptor_data_fields, receptor_data_table_save_fields as receptor_data_save_fields
from src.domain.table_fields import returned_product_table_fields as returned_product_fields, returned_product_table_save_fields as returned_product_save_fields

import json


class Customer_data:

    def __init__(self,
                id, picture, cliente, dni,
                address, phone, status, delivery_note, 
                order_data, orders_packages, 
                receptor_data, returned_product):
        self.id= id
        self.picture= picture
        self.dni= dni
        self.cliente= cliente
        self.dni= dni
        self.address= address
        self.phone= phone
        self.status= status
        self.delivery_note= delivery_note 
        self.order_data= order_data 
        self.orders_packages= orders_packages 
        self.receptor_data= receptor_data 
        self.returned_product= returned_product


    def to_dict(self):
        return {
            "id": self.id,
            "picture": self.picture,
            "dni": self.dni,
            "cliente": self.cliente,
            "address": self.address,
            "phone": self.phone,
            "status": self.status,
            "delivery_note": self.delivery_note,
            "order_data": self.order_data,
            "orders_packages": self.orders_packages,
            "receptor_data": self.receptor_data,
            "returned_product": self.returned_product}


class Customer_dataRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= U.create_conn(self.database_path)
        return conn

    def init_tables(self):
        sql_list=[]
        customer_sql = U.createTable(self, tables_variables= customer_fields, tableName= "customers")
        delivery_sql = U.create_data_tables(self, table_variables= delivery_fields, tableName= "delivery_notes")
        order_d_sql = U.create_data_tables(self, table_variables= order_data_fields, tableName= "order_datas")
        order_p_sql = U.create_data_tables(self, table_variables= orders_packages_fields, tableName= "order_packages")
        receptor_sql = U.create_data_tables(self, table_variables= receptor_data_fields, tableName= "receptor_datas")
        returned_sql = U.create_data_tables(self, table_variables= returned_product_fields, tableName= "returned_products")
        sql_list.extend([customer_sql, delivery_sql, order_d_sql, order_p_sql, receptor_sql, returned_sql])
        sql= ";".join(sql_list)
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.executescript(sql)
        conn.commit()

    def get_delivered_data(self):
        customers_data_list= []
        sql = U.fullGetDynamicQuery(self, fields=['*'], tableName='customers', listConditions=['status'])
        print('query',sql)
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'status': 'Entregado'})
        data = cursor.fetchall()
        customers_data_list.extend([Customer_data(
            id=item['id'],
            picture=item['picture'],
            cliente=item['cliente'],
            dni=item['dni'],
            address=item['address'],
            phone=item['phone'],
            status=item['status'],
            delivery_note= json.loads(item['delivery_note']),
            order_data= json.loads(item['order_data']),
            orders_packages= json.loads(item['orders_packages']),
            receptor_data= json.loads(item['receptor_data']),
            returned_product= json.loads(item['returned_product'])) for item in data])
        return customers_data_list
    
    def get_pending_data(self):
        customers_data_list= []
        sql = U.fullGetDynamicQuery(self, fields=['*'], tableName='customers', listConditions=['status'])
        print('query',sql)
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'status': 'No entregado'})
        data = cursor.fetchall()
        customers_data_list.extend([Customer_data(
            id=item['id'],
            picture=item['picture'],
            cliente=item['cliente'],
            dni=item['dni'],
            address=item['address'],
            phone=item['phone'],
            status=item['status'],
            delivery_note= json.loads(item['delivery_note']),
            order_data= json.loads(item['order_data']),
            orders_packages= json.loads(item['orders_packages']),
            receptor_data= json.loads(item['receptor_data']),
            returned_product= json.loads(item['returned_product'])) for item in data])
        return customers_data_list

    def get_customer(self, id):
        # data_list=[]
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='customers', listConditions=['id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'id': id})
        data = cursor.fetchone()

        customer = Customer_data(
            id=data['id'],
            picture=data['picture'],
            cliente=data['cliente'],
            dni=data['dni'],
            address=data['address'],
            phone=data['phone'],
            status=data['status'],
            delivery_note= json.loads(data['delivery_note']),
            order_data= json.loads(data['order_data']),
            orders_packages= json.loads(data['orders_packages']),
            receptor_data= json.loads(data['receptor_data']),
            returned_product= json.loads(data['returned_product'])
        )

        return customer

    def update_data(self, request):
        sql= U.getFullUpdateDynamicQuery(self, table_variables= ['receptor_data', 'returned_product', 'status'], tableName= "customers", listConditions= ['id'])

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, 
                       {"id": request.id,
                        "picture": request.picture,
                        "dni": request.dni,
                        "cliente": request.cliente,
                        "address": request.address,
                        "phone": request.phone,
                        "status": request.status,
                        "delivery_note": json.dumps(request.delivery_note),
                        "order_data": json.dumps(request.order_data),
                        "orders_packages": json.dumps(request.orders_packages),
                        "receptor_data": json.dumps(request.receptor_data),
                        "returned_product": json.dumps(request.returned_product)
                        })
        conn.commit()

    def get_note(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='delivery_notes', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        note = dict(**data)
        print(note)
        return note

    def get_an_order(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='order_datas', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        order = dict(**data)
        return order

    def get_an_order_packages(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='order_packages', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        order_packages = dict(**data)
        return order_packages

    def get_the_receptor(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='receptor_datas', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        receptor = dict(**data)
        return receptor

    def get_the_returned(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='returned_products', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        returned = dict(**data)
        return returned

    def deleted_record_by_id(self, record):
        sql = U.fullDeleteDynamicQuery(self, tableName= "customers", listConditions=['id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, {"id": record}
        )
        conn.commit()

    def save_customer(self, request):
        sql= U.getFullSaveDynamicQuery(self, table_variables= customer_fields, tableName= "customers")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": request.id,
             "picture": request.picture,
             "dni": request.dni,
             "cliente": request.cliente,
             "address": request.address,
             "phone": request.phone,
             "status": request.status,
             "delivery_note": json.dumps(request.delivery_note),
             "order_data": json.dumps(request.order_data),
             "orders_packages": json.dumps(request.orders_packages),
             "receptor_data": json.dumps(request.receptor_data),
             "returned_product": json.dumps(request.returned_product)
             }
            #request.to_dict()
        )
        conn.commit()

    def save_delivery_note(self, note):
        sql= U.getFullSaveDynamicQuery(self, table_variables= delivery_save_fields, tableName= "delivery_notes")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": note.id,
             "note": note.note,
             "customer_id": note.customer_id}
        )
        conn.commit()

    def save_order_data(self, request):
        sql= U.getFullSaveDynamicQuery(self, table_variables= order_data_save_fields, tableName= "order_datas")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": request.id,
             "delivery_date": request.delivery_date,
             "order_number": request.order_number,
             "delivery_time": request.delivery_time,
             "delivery_time_interval": request.delivery_time_interval,
             "customer_id": request.customer_id}
        )
        conn.commit()

    def save_order_packages(self, request):
        sql= U.getFullSaveDynamicQuery(self, table_variables= orders_packages_save_fields, tableName= "order_packages")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": request.id,
             "drawers": json.dumps(request.drawers),
             "bags":json.dumps (request.bags),
             "substitutions": request.substitutions,
             "customer_id": request.customer_id}
        )
        conn.commit()

    def save_receptor_data(self, receptor):
        sql= U.getFullSaveDynamicQuery(self, table_variables= receptor_data_save_fields, tableName= "receptor_datas")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": receptor.id,
             "name": receptor.name,
             "DNI": receptor.DNI,
             "customer_id": receptor.customer_id}
        )
        conn.commit()

    def save_returned_product(self, returned):
        sql= U.getFullSaveDynamicQuery(self, table_variables= returned_product_save_fields, tableName= "returned_products")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": returned.id,
             "unity": returned.unity,
             "return_reason": returned.return_reason,
             "order_number": returned.order_number,
             "customer_id": returned.customer_id}
        )
        conn.commit()
