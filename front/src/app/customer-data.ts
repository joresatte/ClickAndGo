export interface CustomerData {
    id:number,
    picture: string,
    cliente:string,
    dni:string,
    address:string,
    phone:string,
    status: string,
    delivery_note:[{
      id:number,
      note:string,
      customer_id:number}],
    order_data: [{
      id:number,
      delivery_date:string,
      delivery_time:string,
      order_number:number,
      delivery_time_interval:string ,
      customer_id: number,
    }],
    orders_packages:[{
      id:number,
      substitutions: string,
      customer_id:number, 
      drawers:[{cold:number, frozen:number, dry:number, out_of_drawers:number}],
      bags:[{cold:number, frozen:number}],
    }],
    receptor_data:[{
      id:number,
      name:string,
      DNI:string,
      customer_id:number,
    }],
    returned_product: [{
      id:number,
      unity:number,
      return_reason:string,
      order_number:number,
      customer_id:number,
    }]
}
