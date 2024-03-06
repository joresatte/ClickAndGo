# @author: Jores Atte Mottoh
# @date: 25/10/2023
# @description: Order_packages, Order_packagesRepository class
# @project: Click and Go
# @modified by: 
# @modified date:

from src.domain.utils import Utils as U
from src.domain.table_fields import orders_packages_table_fields as orders_packages_fields, orders_packages_table_save_fields as orders_packages_save_fields
import json

class Order_packages:

    def __init__(self, 
                 id, drawers= {'cold':int, 'frozen':int, 'dry':int, 'out of drawers': int}, 
                 bags={'cold':int, 'frozen':int},
                 substitutions=str, customer_id=str):
        self.id= id
        self.drawers= drawers
        self.bags= bags
        self.substitutions= substitutions
        self.customer_id= customer_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "drawers": self.drawers,
            "bags": self.bags,
            "substitutions": self.substitutions,
            "customer_id": self.customer_id}
    
class Order_packagesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= U.create_conn(self.database_path)
        return conn
    
    def init_tables(self):
        sql = U.create_data_tables(self, table_variables= orders_packages_fields, tableName= "order_packages")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_an_order_packages(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='order_packages', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        order_packages = Order_packages(**data)
        return order_packages

    def save_order_packages(self, record):
        sql= U.getFullSaveDynamicQuery(self, table_variables= orders_packages_save_fields, tableName= "order_packages")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": record.id, 
             "drawers": json.dumps(record.drawers), 
             "bags":json.dumps (record.bags), 
             "substitutions": record.substitutions, 
             "customer_id": record.customer_id}
        )
        conn.commit()
