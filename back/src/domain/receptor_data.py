# @author: Jores Atte Mottoh
# @date: 26/10/2023
# @description: Receptor_data, Receptor_dataRepository class
# @project: Click and Go
# @modified by: 
# @modified date:

from src.domain.utils import Utils as U
from src.domain.table_fields import receptor_data_table_fields as receptor_data_fields, receptor_data_table_save_fields as receptor_data_save_fields

class Receptor_data:

    def __init__(self, 
                 id, name, 
                 DNI,customer_id):
        self.id= id
        self.name= name
        self.DNI= DNI
        self.customer_id= customer_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "DNI": self.DNI,
            "customer_id": self.customer_id}
    
class Receptor_dataRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= U.create_conn(self.database_path)
        return conn
    
    def init_tables(self):
        sql = U.create_data_tables(self, table_variables= receptor_data_fields, tableName= "receptor_datas")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_the_receptor(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='receptor_datas', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        receptor = Receptor_data(**data)
        return receptor

    def save_receptor_data(self, record):
        sql= U.getFullSaveDynamicQuery(self, table_variables= receptor_data_save_fields, tableName= "receptor_datas")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            # {"id": record.id, "name": record.name, "email": record.email, "subject": record.subject, "comments": record.comments}
            record.to_dict()
        )
        conn.commit()
