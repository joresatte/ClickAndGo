# @author: Jores Atte Mottoh
# @date: 24/10/2023
# @description: class that contains useful methods 
# @project: Duty-place
# @modified by: jores Atte Mottoh 
# @modified date: 26/10/2023
import sqlite3

class Utils:

    def create_conn(self):
        conn = sqlite3.connect(self)
        conn.row_factory = sqlite3.Row
        return conn

    def createTable(self, tables_variables, tableName):
        requiredCeateString= 'create table if not exists'
        query= " "
        Query= ''
        if len(tables_variables)>0:
            for i in tables_variables:
                if i== 'id':
                    query+= requiredCeateString +' '
                    query+= tableName
                    query+='('
                    query+= i + ' ' + 'varchar primary key, '
                if i!= 'id':
                    query+= i + ' ' + 'varchar, '
        Query= f"{query[:-2]+ ')'}"
        return Query
    
    def TableTocreate(self, tableName, tables_variables):
        requiredCeateString= 'create table if not exists'
        query= " "
        Query= ''
        if len(tables_variables)>0:
            for i in tables_variables:
                if 'id' in i and i!='id':
                    query+= requiredCeateString +' '
                    query+= tableName
                    query+='('
                    query+= i + ' ' + 'varchar primary key, '
                if 'id' not in i:
                    query+= i + ' ' + 'varchar, '
        Query= f"{query[:-2]+ ')'}"
        return Query
    
    """
     create table if not exists contacts_categories (
               contact_id varchar,
               category_id varchar,
               FOREIGN KEY (contact_id) REFERENCES contacts(id),
               FOREIGN KEY (category_id) REFERENCES categories(id)
            );
    """
    """
    select * , 
    (select * from delivery_notes where customre_id=: ), 
    (select * from order_datas where customre_id=:), 
    (select * from order_packages where customre_id=:), 
    (select * from receptor_datas where customre_id=:),
    (select * from returned_products where customre_id=:) 
    from customers where id=:
    """
    #Añadido 26/10/2023
    def create_data_tables(self, tableName, table_variables):
        requiredCeateString= 'create table if not exists'
        query_parts = []
        query= ''
        if len(table_variables)>0:
            query+= requiredCeateString+' '+ tableName+ '('
            query_parts.extend([ i for i in table_variables])
            query+= ', '.join(query_parts)
            query+=')'
        return query


    def getFullSaveDynamicQuery(self, tableName, table_variables):
        query_parts = []
        queryParts = []
        requiredInsertString = 'insert or replace into'
        query= ''
        requiredString='values'  
        if len(table_variables) > 0:
            query+= requiredInsertString+' '+ tableName+ '('
            query_parts.extend([ i for i in table_variables])
            query+= ', '.join(query_parts)
            query+= ')'
            query+= ' '+ requiredString+ '('
            x= lambda a: ':'+ a
            queryParts.extend([x(i) for i in table_variables])
            query+= ', '.join(queryParts)
            query+= ')'
        return query
    
    def getFullUpdateDynamicQuery(self, table_variables, tableName, listConditions):
        query_parts = []
        queryParts = []
        requiredInsertString = 'UPDATE'
        query= ""
        requiredString='SET'  
        if len(table_variables) > 0:
            query+= requiredInsertString+' '+ tableName+ ' '
            query+= requiredString +' '
            query_parts.extend([ table_variables[i]+'=:'+table_variables[i]  for i in range(len(table_variables))])
            query+= ', '.join(query_parts)
            query+= ' '+'where'+ ' '
            x= lambda a: a +'=:'+ a
            queryParts.extend([x(listConditions[i]) for i in range(len(listConditions))])
            query+= ' and '.join(queryParts)
        return query
    
    def fullGetDynamicQuery(self, fields, tableName, listConditions):
        queryParts = []
        requiredInsertString = 'SELECT'
        query= ""
        requiredString='FROM'  
        if len(fields) > 0:
            query+= requiredInsertString+' '
            query+=', '.join(fields)+' '
            query+= requiredString +' '+ tableName
        if len(listConditions)>0:
            query+= ' '+'where'+ ' '
            x= lambda a: a +'=:'+ a
            queryParts.extend([x(listConditions[i]) for i in range(len(listConditions))])
            query+= ' and '.join(queryParts)

        return query
    
    def fullDeleteDynamicQuery(self, tableName, listConditions):
        queryParts = []
        requiredInsertString = 'DELETE'
        query= ""
        requiredString='FROM' 
        try:
            if len(listConditions)>0:
                query+= requiredInsertString+' '
                query+= requiredString +' '+ tableName
                query+= ' '+'where'+ ' '
                x= lambda a: a +'=:'+ a
                queryParts.extend([x(listConditions[i]) for i in range(len(listConditions))])
                query+= ' and '.join(queryParts)
            else:
                raise Exception('The conditions list can not be empty')
        except Exception as  error:
            return (error.args)
    
        return query
