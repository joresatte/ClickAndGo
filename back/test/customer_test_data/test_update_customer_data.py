from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.customer_data import Customer_data, Customer_dataRepository
from src.domain.test_data import good_request_data_1, bad_request_data_1, bad_request_data_2, bad_request_data_3, bad_request_data_4, bad_request_data_5

def setup():
    customer_data_repository = Customer_dataRepository(temp_file())
    app = create_app(repositories={"customer_data": customer_data_repository})
    client = app.test_client()

    first_cliente= Customer_data(
        id='1',
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
            'customer_id': '2'
        }],
        orders_packages= [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1' 
        }],
        receptor_data= [{
            'id':'6',
            'name':"",
            'DNI':"test",
            'customer_id':'1'
        }],
        returned_product= [{
            'id':'2',
            'unity':'2',
            'return_reason':"test",
            'order_number':"",
            'customer_id':'1'
        }]
    )
    customer_data_repository.save_customer(first_cliente)
    return client

def test_update_good_data():
    client= setup()
    request_data= client.put('/api/customer_data/update/1', json= good_request_data_1)
    if request_data==200:
        return True, 'Successfully'
    response= client.get("/api/one_customer/1")
    if response== 200:
        assert True, 'Successfully'
    assert len(response.json)== 12
    assert response.json== good_request_data_1

def test_update_bad_request():
    client= setup()
    request_data= client.put('/api/customer_data/update/1', json= bad_request_data_1)
    if request_data==405:
        return True
    
def test_update_another_bad_request():
    client= setup()
    request_data= client.put('/api/customer_data/update/1', json= bad_request_data_2)
    if request_data==405:
        return True

def test_another_bad_request():
    client= setup()
    request_data= client.put('/api/customer_data/update/1', json= bad_request_data_3)
    if request_data==405:
        return True


def test_bad_request():
    client= setup()
    request_data= client.put('/api/customer_data/update/1', json= bad_request_data_4)
    if request_data==405:
        return True

def test_bad_request_data():
    client= setup()
    request_data= client.put('/api/customer_data/update/1', json= bad_request_data_5)
    if request_data==405:
        return True
        