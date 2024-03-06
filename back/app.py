from src.webserver import create_app
from src.domain.customer_data import Customer_dataRepository
from src.domain.order_data import Order_dataRepository
from src.domain.order_packages import Order_packagesRepository
from src.domain.delivery_note import Delivery_noteRepository
from src.domain.returned_product import Returned_productRepository
from src.domain.receptor_data import Receptor_dataRepository
from src.domain.employee import Employee_Repository 
from waitress import serve
database_path = "data/database.db"

repositories = {
    "customer_data": Customer_dataRepository(database_path),
    "order_data": Order_dataRepository(database_path),
    "order_packages": Order_packagesRepository(database_path),
    "delivery_note": Delivery_noteRepository(database_path),
    "returned_product": Returned_productRepository(database_path),
    "receptor_data": Receptor_dataRepository(database_path),
    "employee_data": Employee_Repository(database_path)
}

app = create_app(repositories)
app.run(debug=True, host="0.0.0.0", port="5000")
# mode= "dev"
# if __name__ == '__main__':
#     if mode== "dev":
#     else:
#         serve(app, host="0.0.0.0", port=5000)
