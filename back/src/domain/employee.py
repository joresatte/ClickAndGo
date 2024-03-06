from src.domain.table_fields import employee_data_table_fields as employee_fields
from src.domain.utils import Utils


class Employee:
    def __init__(self, id, identification, password):
        self.id = id
        self.identification = identification
        self.password = password

    def to_dict(self):
        return {
            "identification": self.identification,
        }


class Employee_Repository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = Utils.create_conn(self.database_path)
        return conn

    def init_tables(self):
        sql = Utils.createTable(self, tables_variables= employee_fields, tableName= "employees")
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_employee_by_id(self, id):
        sql = Utils.fullGetDynamicQuery(self, fields= ['*'], tableName= "employees", listConditions=['id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Employee(
                id= data['id'],
                identification= data['identification'],
                password= data['password']
            )

        return user

    def get_by_identification_and_password(self, identification, password):
        sql = Utils.fullGetDynamicQuery(self, fields= ['*'], tableName= "employees", listConditions=['identification', 'password'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"identification": identification, "password": password})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Employee(
                id= data['id'],
                identification= data['identification'],
                password= data['password']
            )

        return user

    def save(self, user):
        sql= Utils.getFullSaveDynamicQuery(self, table_variables= employee_fields, tableName= "employees")
        
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": user.id, "identification": user.identification, "password": user.password}
        )
        conn.commit()



