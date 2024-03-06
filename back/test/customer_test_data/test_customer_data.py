from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.customer_data import Customer_data, Customer_dataRepository

def test_get_pending_data():
    customer_repository = Customer_dataRepository(temp_file())
    app = create_app(repositories={"customer_data": customer_repository})
    client = app.test_client()
    
    first_cliente= Customer_data(
        id=1,
        picture="picture",
        cliente="Darn Chambers",
        dni="0268-0131",
        address="4752 Hoffman Drive",
        phone="394 937 1775",
        status="No entregado",
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
            'customer_id': '2'}],
        orders_packages= [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1'}],
        receptor_data= [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'}],
        returned_product= [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'}]
    )
    second_cliente= Customer_data(
        id=2,
        picture="picture",
        cliente="Townsend Moakson",
        dni="49999-608",
        address="9 Victoria Junction",
        phone="436 246 3857",
        status="No entregado",
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
            'customer_id': '2'}],
        orders_packages= [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1'}],
        receptor_data= [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'}],
        returned_product= [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'}]
    )

    customer_repository.save_customer(first_cliente)
    customer_repository.save_customer(second_cliente)

    response = client.get("/api/all_pending/customers_data")
    if len(response.json)!= 2:
        assert False, 'fail assertion'
    assert response.json ==[
            {"id":"1",
            "picture":"picture",
            "cliente":"Darn Chambers",
            "dni":"0268-0131",
            "address":"4752 Hoffman Drive",
            "phone":"394 937 1775",
            "status":"No entregado",
            'delivery_note': [{
                'id':'12',
                'note':"Construction Expeditor",
                'customer_id':'1'}],
            'order_data': [{
                'id':'2',
                'delivery_date':"3/7/2023",
                'delivery_time':"12:00",
                'order_number':'85',
                'delivery_time_interval':"12:00 - 12:30 ",
                'customer_id': '2'}],
            'orders_packages': [{
                'id':'3',
                'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
                'bags':[{"cold":'2', "frozen":'1'}],
                'substitutions': "No",
                'customer_id':'1'}],
            'receptor_data': [{
                'id':'6',
                'name':"Wallas Mulhall",
                'DNI':"0899397964",
                'customer_id':'1'}],
            'returned_product': [{
                'id':'2',
                'unity':'2',
                'return_reason':"",
                'order_number':"",
                'customer_id':'1'}]
        },
            {"id":"2",
            "picture":"picture",
            "cliente":"Townsend Moakson",
            "dni":"49999-608",
            "address":"9 Victoria Junction",
            "phone":"436 246 3857",
            "status":"No entregado",
            'delivery_note': [{
                'id':'12',
                'note':"Construction Expeditor",
                'customer_id':'1'}],
            'order_data': [{
                'id':'2',
                'delivery_date':"3/7/2023",
                'delivery_time':"12:00",
                'order_number':'85',
                'delivery_time_interval':"12:00 - 12:30 ",
                'customer_id': '2'}],
            'orders_packages': [{
                'id':'3',
                'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
                'bags':[{"cold":'2', "frozen":'1'}],
                'substitutions': "No",
                'customer_id':'1'}],
            'receptor_data': [{
                'id':'6',
                'name':"Wallas Mulhall",
                'DNI':"0899397964",
                'customer_id':'1'}],
            'returned_product': [{
                'id':'2',
                'unity':'2',
                'return_reason':"",
                'order_number':"",
                'customer_id':'1'}]
        }
    ]

def return_only_one_pending_data_test():
    customer_repository = Customer_dataRepository(temp_file())
    app = create_app(repositories={"customer_data": customer_repository})
    client = app.test_client()
    
    first_cliente= Customer_data(
        id=1,
        picture="picture",
        cliente="Darn Chambers",
        dni="0268-0131",
        address="4752 Hoffman Drive",
        phone="394 937 1775",
        status="Entregado",
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
            'customer_id': '2'}],
        orders_packages= [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1'}],
        receptor_data= [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'}],
        returned_product= [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'}]
    )
    second_cliente= Customer_data(
        id=2,
        picture="picture",
        cliente="Townsend Moakson",
        dni="49999-608",
        address="9 Victoria Junction",
        phone="436 246 3857",
        status="No entregado",
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
            'customer_id': '2'}],
        orders_packages= [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1'}],
        receptor_data= [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'}],
        returned_product= [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'}]
    )

    customer_repository.save_customer(first_cliente)
    customer_repository.save_customer(second_cliente)

    response = client.get("/api/all_pending/customers_data")
    if len(response.json)!= 1:
        assert False, 'fail assertion'
    assert response.json ==[
            
            {"id":"2",
            "picture":"picture",
            "cliente":"Townsend Moakson",
            "dni":"49999-608",
            "address":"9 Victoria Junction",
            "phone":"436 246 3857",
            "status":"No entregado",
            'delivery_note': [{
                'id':'12',
                'note':"Construction Expeditor",
                'customer_id':'1'}],
            'order_data': [{
                'id':'2',
                'delivery_date':"3/7/2023",
                'delivery_time':"12:00",
                'order_number':'85',
                'delivery_time_interval':"12:00 - 12:30 ",
                'customer_id': '2'}],
            'orders_packages': [{
                'id':'3',
                'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
                'bags':[{"cold":'2', "frozen":'1'}],
                'substitutions': "No",
                'customer_id':'1'}],
            'receptor_data': [{
                'id':'6',
                'name':"Wallas Mulhall",
                'DNI':"0899397964",
                'customer_id':'1'}],
            'returned_product': [{
                'id':'2',
                'unity':'2',
                'return_reason':"",
                'order_number':"",
                'customer_id':'1'}]
        }
    ]

def get_delivered_data():
    customer_repository = Customer_dataRepository(temp_file())
    app = create_app(repositories={"customer_data": customer_repository})
    client = app.test_client()
    
    first_cliente= Customer_data(
        id=1,
        picture="picture",
        cliente="Darn Chambers",
        dni="0268-0131",
        address="4752 Hoffman Drive",
        phone="394 937 1775",
        status="No entregado",
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
            'customer_id': '2'}],
        orders_packages= [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1'}],
        receptor_data= [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'}],
        returned_product= [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'}]
    )
    second_cliente= Customer_data(
        id=2,
        picture="picture",
        cliente="Townsend Moakson",
        dni="49999-608",
        address="9 Victoria Junction",
        phone="436 246 3857",
        status="Entregado",
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
            'customer_id': '2'}],
        orders_packages= [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1'}],
        receptor_data= [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'}],
        returned_product= [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'}]
    )

    customer_repository.save_customer(first_cliente)
    customer_repository.save_customer(second_cliente)

    response = client.get("/api/all_delivered/customers_data")
    if len(response.json)!= 1:
        assert False, 'fail assertion'
    assert response.json ==[
            
            {"id":"2",
            "picture":"picture",
            "cliente":"Townsend Moakson",
            "dni":"49999-608",
            "address":"9 Victoria Junction",
            "phone":"436 246 3857",
            "status":"No entregado",
            'delivery_note': [{
                'id':'12',
                'note':"Construction Expeditor",
                'customer_id':'1'}],
            'order_data': [{
                'id':'2',
                'delivery_date':"3/7/2023",
                'delivery_time':"12:00",
                'order_number':'85',
                'delivery_time_interval':"12:00 - 12:30 ",
                'customer_id': '2'}],
            'orders_packages': [{
                'id':'3',
                'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
                'bags':[{"cold":'2', "frozen":'1'}],
                'substitutions': "No",
                'customer_id':'1'}],
            'receptor_data': [{
                'id':'6',
                'name':"Wallas Mulhall",
                'DNI':"0899397964",
                'customer_id':'1'}],
            'returned_product': [{
                'id':'2',
                'unity':'2',
                'return_reason':"",
                'order_number':"",
                'customer_id':'1'}]
        }
    ]