good_request_data_1= {
        'id':'1',
        "picture":"picture",
        'cliente':"Darn Chambers",
        'dni':"0268-0131",
        'address':"4752 Hoffman Drive",
        'phone':"394 937 1775",
        "status":"Entergado",
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
            'customer_id': '2'
        }],
        'orders_packages': [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1' 
        }],
        'receptor_data': [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'
        }],
        'returned_product': [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'
        }]
    }


good_request_data_2= {
        'id':'1',
        "picture":"picture",
        'cliente':"Darn Chambers",
        'dni':"0268-0131",
        'address':"4752 Hoffman Drive",
        'phone':"394 937 1775",
        "status":"Entergado",
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
            'customer_id': '2'
        }],
        'orders_packages': [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1' 
        }],
        'receptor_data': [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'
        }],
        'returned_product': [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'
        }]
    }


bad_request_data_1= {
        'id':'2',
        "picture":"picture",
        'cliente':"Darn Chambers",
        'dni':"0268-0131",
        'address':"4752 Hoffman Drive",
        'phone':"394 937 1775",
        "status":"Entergado",
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
            'customer_id': '2'
        }],
        'orders_packages': [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1' 
        }],
        'receptor_data': [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':" ",
            'customer_id':'1'
        }],
        'returned_product': [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'
        }]
    }


bad_request_data_2= {
        'id':'2',
        "picture":"picture",
        'cliente':"Darn Chambers",
        'dni':"0268-0131",
        'address':"4752 Hoffman Drive",
        'phone':"394 937 1775",
        "status":"Entergado",
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
            'customer_id': '2'
        }],
        'orders_packages': [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1' 
        }],
        'receptor_data': [{
            'id':'6',
            'name':" ",
            'DNI':" ",
            'customer_id':'1'
        }],
        'returned_product': [{
            'id':'2',
            'unity':'2',
            'return_reason':" no ha gustado la leche",
            'order_number':"",
            'customer_id':'1'
        }]
    }

bad_request_data_3= {
        'id':'2',
        "picture":"picture",
        'cliente':"Darn Chambers",
        'dni':"0268-0131",
        'address':"4752 Hoffman Drive",
        'phone':"394 937 1775",
        "status":"Entergado",
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
            'customer_id': '2'
        }],
        'orders_packages': [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1' 
        }],
        'receptor_data': [{
            'id':'6',
            'name':" ",
            'DNI':" 255455255H",
            'customer_id':'1'
        }],
        'returned_product': [{
            'id':'2',
            'unity':'1',
            'return_reason':" devuelto el colacao no queria mas ",
            'order_number':"",
            'customer_id':'1'
        }]
    }

bad_request_data_3={
        'id':'1',
        "picture":"picture",
        'cliente':"Darn Chambers",
        'dni':"0268-0131",
        'address':"4752 Hoffman Drive",
        'phone':"394 937 1775",
        "status":"Entergado",
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
            'customer_id': '2'
        }],
        'orders_packages': [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "si",
            'customer_id':'1' 
        }],
        'receptor_data': [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'
        }],
        'returned_product': [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'
        }]
    }

bad_request_data_4= {
        'id':'1',
        "picture":"picture",
        'cliente':"Darn Chambers",
        'dni':"0268-0131",
        'address':"4752 Hoffman Drive",
        'phone':"394 937 1775",
        "status":"Entergado",
        'delivery_note': [{
            'id':'12',
            'note':"",
            'customer_id':'1'}],
        'order_data': [{
            'id':'2',
            'delivery_date':"3/7/2023",
            'delivery_time':"12:00",
            'order_number':'85',
            'delivery_time_interval':"12:00 - 12:30 ",
            'customer_id': '2'
        }],
        'orders_packages': [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1' 
        }],
        'receptor_data': [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'
        }],
        'returned_product': [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'
        }]
    }

bad_request_data_5= {
        'id':'1',
        "picture":"picture",
        'cliente':"Darn Chambers",
        'dni':"0268-0131",
        'address':"4752 Hoffman Drive",
        'phone':"394 937 1775",
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
            'customer_id': '2'
        }],
        'orders_packages': [{
            'id':'3',
            'drawers':[{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'}],
            'bags':[{"cold":'2', "frozen":'1'}],
            'substitutions': "No",
            'customer_id':'1' 
        }],
        'receptor_data': [{
            'id':'6',
            'name':"Wallas Mulhall",
            'DNI':"0899397964",
            'customer_id':'1'
        }],
        'returned_product': [{
            'id':'2',
            'unity':'2',
            'return_reason':"",
            'order_number':"",
            'customer_id':'1'
        }]
    }
