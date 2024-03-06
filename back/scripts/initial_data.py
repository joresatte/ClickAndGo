import sys
from sys import path
#path.append("../../")
sys.path.insert(0, "")
from src.domain.customer_data import Customer_dataRepository as repo_cl, Customer_data as cl
from src.domain.employee import Employee_Repository as repo, Employee as u
from src.domain.img import picture
database_path = "data/database.db"

cliente_1= cl(
    id='1',
    picture= picture,
    cliente="Divan court",
    dni="0268-0131",
    address="4752 Hoffman Drive",
    phone="394 937 1775",
    status= "No entregado",
    delivery_note= [{
        'id':'12',
        'note':"Construction Expeditor",
        'customer_id':'1'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"12:00",
        'order_number':'85',
        'delivery_time_interval':"12:00 - 12:30 ",
        'customer_id': '1',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'1', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'1'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'1',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'1',
    }],
)

cliente_5= cl(
    id='5',
    picture= picture,
    cliente="Chambers donavan ",
    dni="0268-0535",
    address="4752 Hoffman Drive",
    phone="394 937 5775",
    status= "No entregado",
    delivery_note= [{
        'id':'52',
        'note':"Construction Expeditor",
        'customer_id':'5'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"52:00",
        'order_number':'85',
        'delivery_time_interval':"52:00 - 52:30 ",
        'customer_id': '5',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'5', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'5'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'5',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'5',
    }],
)

cliente_2= cl(
    id='2',
    picture= picture,
    cliente="Sara denet",
    dni="0268-0232",
    address="4752 Hoffman Drive",
    phone="394 937 2775",
    status= "No entregado",
    delivery_note= [{
        'id':'22',
        'note':"Construction Expeditor",
        'customer_id':'2'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"22:00",
        'order_number':'85',
        'delivery_time_interval':"22:00 - 22:30 ",
        'customer_id': '2',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'2', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'2'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'2',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'2',
    }],
)

cliente_3= cl(
    id='3',
    picture= picture,
    cliente="Ivan west",
    dni="0268-0333",
    address="4752 Hoffman Drive",
    phone="394 937 3775",
    status= "No entregado",
    delivery_note= [{
        'id':'32',
        'note':"Construction Expeditor",
        'customer_id':'3'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"32:00",
        'order_number':'85',
        'delivery_time_interval':"32:00 - 32:30 ",
        'customer_id': '3',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'3', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'3'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'3',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'3',
    }],
)

cliente_4= cl(
    id='4',
    picture= picture,
    cliente="kaert noise",
    dni="0268-0434",
    address="4752 Hoffman Drive",
    phone="394 937 4775",
    status= "No entregado",
    delivery_note= [{
        'id':'42',
        'note':"Construction Expeditor",
        'customer_id':'4'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"42:00",
        'order_number':'85',
        'delivery_time_interval':"42:00 - 42:30 ",
        'customer_id': '4',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'4', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'4'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'4',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'4',
    }],
)

cliente_6= cl(
    id='6',
    picture= picture,
    cliente="Darn Chambers",
    dni="0268-0636",
    address="4752 Hoffman Drive",
    phone="394 937 6775",
    status= "No entregado",
    delivery_note= [{
        'id':'62',
        'note':"Construction Expeditor",
        'customer_id':'6'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"62:00",
        'order_number':'85',
        'delivery_time_interval':"62:00 - 62:30 ",
        'customer_id': '6',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'6',
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'6'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'6',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'6',
    }],
)

cliente_7= cl(
    id='7',
    picture= picture,
    cliente="keneth caraly",
    dni="0268-0737",
    address="4752 Hoffman Drive",
    phone="394 937 7775",
    status= "No entregado",
    delivery_note= [{
        'id':'72',
        'note':"Construction Expeditor",
        'customer_id':'7'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"72:00",
        'order_number':'85',
        'delivery_time_interval':"72:00 - 72:30 ",
        'customer_id': '7',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'7', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'7'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'7',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'7',
    }],
)

cliente_8= cl(
    id='8',
    picture= picture,
    cliente="Noise kart",
    dni="0268-0434",
    address="4752 Hoffman Drive",
    phone="394 937 4775",
    status= "Entregado",
    delivery_note= [{
        'id':'42',
        'note':"Construction Expeditor",
        'customer_id':'4'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"42:00",
        'order_number':'85',
        'delivery_time_interval':"42:00 - 42:30 ",
        'customer_id': '4',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'4', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'4'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'4',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'4',
    }],
)

cliente_9= cl(
    id='9',
    picture= picture,
    cliente="Chamb divan",
    dni="0268-0636",
    address="4752 Hoffman Drive",
    phone="394 937 6775",
    status= "Entregado",
    delivery_note= [{
        'id':'62',
        'note':"Construction Expeditor",
        'customer_id':'6'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"62:00",
        'order_number':'85',
        'delivery_time_interval':"62:00 - 62:30 ",
        'customer_id': '6',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'6',
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'6'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'6',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'6',
    }],
)

cliente_10= cl(
    id='10',
    picture= picture,
    cliente="John kenedy",
    dni="0268-0737",
    address="4752 Hoffman Drive",
    phone="394 937 7775",
    status= "Entregado",
    delivery_note= [{
        'id':'72',
        'note':"Construction Expeditor",
        'customer_id':'7'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"72:00",
        'order_number':'85',
        'delivery_time_interval':"72:00 - 72:30 ",
        'customer_id': '7',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'7', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'7'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'7',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'7',
    }],
)
cliente_11= cl(
    id='11',
    picture= picture,
    cliente="knededy sarf",
    dni="0268-0737",
    address="4752 Hoffman Drive",
    phone="394 937 7775",
    status= "Entregado",
    delivery_note= [{
        'id':'72',
        'note':"Construction Expeditor",
        'customer_id':'7'}],
    order_data= [{
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"72:00",
        'order_number':'85',
        'delivery_time_interval':"72:00 - 72:30 ",
        'customer_id': '7',
    }],
    orders_packages= [{
        'id':'3',
        'substitutions': "No",
        'customer_id':'7', 
        'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out_of_drawers": '0'}],
        'bags':[{"cold":'2', "frozen":'7'}],
    }],
    receptor_data= [{
        'id':'6',
        'name':"",
        'DNI':"",
        'customer_id':'7',
    }],
    returned_product= [{
        'id':'2',
        'unity':0,
        'return_reason':"",
        'order_number':"",
        'customer_id':'7',
    }],
)

path_repo= repo_cl(database_path)
path_repo.save_customer(cliente_1)
path_repo.save_customer(cliente_2)
path_repo.save_customer(cliente_3)
path_repo.save_customer(cliente_4)
path_repo.save_customer(cliente_5)
path_repo.save_customer(cliente_6)
path_repo.save_customer(cliente_7)
path_repo.save_customer(cliente_8)
path_repo.save_customer(cliente_9)
path_repo.save_customer(cliente_10)
path_repo.save_customer(cliente_11)

def save_employee_initial_data(employees):
    path_repo= repo(database_path)
    for employee in employees:
        path_repo.save(employee)
    return 'Saved successfully'

employee_1= u(
    id= 'test_id_1',
    identification='test_identification_1',
    password='test_password_1'
)
employee_2= u(
    id= 'test_id_2',
    identification='test_identification_2',
    password='test_password_2'
)

if __name__ == '__main__':
    employee_list= [employee_1, employee_2]
    save_employee_initial_data(employee_list)