# @author: Jores Atte Mottoh
# @date: 26/10/2023
# @description: Delivery_note, Delivery_noteRepository class
# @project: Click and Go
# @modified by: 
# @modified date:

from src.domain.utils import Utils as U
from src.domain.table_fields import delivery_note_table_fields as delivery_fields, delivery_note_table_save_fields as delivery_save_fields


class Delivery_note:

    def __init__(self, 
                 id,
                 note, customer_id):
        self.id= id
        self.note= note
        self.customer_id= customer_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "note": self.note,
            "customer_id": self.customer_id}
    
class Delivery_noteRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= U.create_conn(self.database_path)
        return conn
    
    def init_tables(self):
        sql = U.create_data_tables(self, table_variables= delivery_fields, tableName= "delivery_notes")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_delivery_note(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='delivery_notes', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        note = Delivery_note(**data)
        return note

    def save_delivery_note(self, note):
        sql= U.getFullSaveDynamicQuery(self, table_variables= delivery_save_fields, tableName= "delivery_notes")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            # {"id": note.id, "name": note.name, "email": note.email, "subject": note.subject, "comments": note.comments}
            note.to_dict()
        )
        conn.commit()
