import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService } from '../../service/app.service';
import { Constant } from '../../service/constant';
import { CustomerData } from '../../customer-data';
import { AppLogoComponent } from '../../app-logo/app-logo.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { BooleanInput } from '@angular/cdk/coercion';
import {MatIconModule} from '@angular/material/icon';
import {MatTooltipModule} from '@angular/material/tooltip';
import {MatSnackBar} from '@angular/material/snack-bar';
import { FormDataComponent } from '../form-data/form-data.component';

@Component({
  selector: 'app-detail-page',
  standalone: true,
  imports: [AppLogoComponent, CommonModule, 
            FormsModule, MatCardModule, MatButtonModule, 
            MatFormFieldModule, MatInputModule,
            MatTooltipModule, MatIconModule, FormDataComponent],
  templateUrl: './detail-page.component.html',
  styleUrl: './detail-page.component.css'
})
export class DetailPageComponent implements OnInit{
  pageName:string= 'detailPage'
  route: ActivatedRoute = inject(ActivatedRoute);
  id:any
  load:string= 'Loading...'
  showLoad:boolean=false
  showDetailForm:boolean= false;
  customerData: CustomerData={
    id: 0,
    picture: '',
    cliente: '',
    dni: '',
    address: '',
    phone: '',
    status: '',
    delivery_note: [{
      id:0,
      note:'',
      customer_id:0
    }],
    order_data: [{
      id:0,
      delivery_date:'',
      delivery_time:'',
      order_number:0,
      delivery_time_interval:'' ,
      customer_id: 0,
    }],
    orders_packages: [{
      id:0,
      substitutions: '',
      customer_id:0, 
      drawers:[{cold:0, frozen:0, dry:0, out_of_drawers:0}],
      bags:[{cold:0, frozen:0}],
    }],
    receptor_data: [{
      id:0,
      name:'',
      DNI:'',
      customer_id:0,
    }],
    returned_product: [{
      id:0,
      unity:0,
      return_reason:'',
      order_number:0,
      customer_id:0,}]
  }
  navTitle:string= 'Comprobante de la entrega'
  inputType!: string;
  addNumber:number=0
  disabled: BooleanInput= true;
  disabledBtnSubmit:BooleanInput;
  isEnabled:boolean= false
  showFooter:boolean= true
  customerStatus!:any;
  submit:string= 'Guardar'
  updateResponse:string='Unsaved'
  icon:string='send'//error
  btn_btn:any='btn_btn'
  btn_color:string= 'primary'
  serv: AppService = inject(AppService);
  constructor(private snackBar: MatSnackBar){
    // const options:any={}
    this.id= this.route.snapshot.params['id']
    // const url:string= `${Constant.login_Path}/one_customer/${this.id}`
    // this.serv.getdataById(url, options).then(data =>{
    //   this.customerData= data!
    //   this.customerStatus= data?.status
    //   if(this.customerStatus == 'Entregado'){
    //     this.isEnabled= true
    //     this.disabledBtnSubmit= true
    //     this.showFooter= false
    //   }
    // })
  }
  ngOnInit(): void {
    this.pageName=='detailPage'? this.showDetailForm= true: this.showDetailForm= false
    this.getCustomerData()!
  }
  getCustomerData(){
    const url:string= `${Constant.login_Path}/one_customer/${this.id}`
    const options:any={}
    this.serv.getdataById(url, options).then(data =>{
      if(data!= undefined){
         this.customerData= data
        if(data.status == 'Entregado'){
          this.isEnabled= true
          this.disabledBtnSubmit= true
          this.showFooter= false
        }
      }
    })
    
  }
  openSnackBar(message: string, action:string, duration: number) {
    this.snackBar.open(message, action, {
      duration: duration,
      verticalPosition: 'bottom', // 'top' | 'bottom'
      horizontalPosition: 'end', //'start' | 'center' | 'end' | 'left' | 'right'
      panelClass: ['red-snackbar'],
    });
  }
  async submitData(data:CustomerData){
    // const options={
    //   method: "PUT",
    //   headers: new HttpHeaders({'Content-Type': 'application/json'}),
    //   observe: 'response',
    // }
    const url= `${Constant.login_Path}/customer_data/update/${this.id}`
    const check= this.isValidData(data)
    if(check==false){
      alert('error')
    }else{
      // console.log(body)
      const body=JSON.stringify({
        id:data.id,
        picture: data.picture,
        cliente:data.cliente,
        dni:data.dni,
        address:data.address,
        phone:data.phone,
        status: data.status,
        delivery_note:data.delivery_note,
        order_data: data.order_data,
        orders_packages:data.orders_packages,
        receptor_data:data.receptor_data,
        returned_product: data.returned_product
      })
      console.log(body)
      this.serv.updateMethod(url, body).subscribe(
        resp => {
          const keys = resp.headers.keys();
          console.log(resp.status, keys);
          const resStatus = resp.status;
          if (resStatus== 200) {
            const action= 'Cancel'
            const duration= 3000
            const message= 'Saved successfully'
            setTimeout(() => {
              this.snackBar.open(message, action, {
                duration: duration,
                verticalPosition: 'bottom', // 'top' | 'bottom'
                horizontalPosition: 'end', //'start' | 'center' | 'end' | 'left' | 'right'
                panelClass: ['red-snackbar'],
              });
            }, 3000);
            window.location.reload();
            this.disabledBtnSubmit = true;
            return this.updateResponse = 'Saved';
          } else {
            const action= 'Cancel'
            const duration= 3000
            const message= 'Fail to save data'
            this.snackBar.open(message, action, {
              duration: duration,
              verticalPosition: 'bottom', // 'top' | 'bottom'
              horizontalPosition: 'end', //'start' | 'center' | 'end' | 'left' | 'right'
              panelClass: ['red-snackbar'],
            });
            this.icon = 'error';
            this.btn_color = 'warn';
            setTimeout(() => {
              this.icon = 'send';
              this.btn_color = 'primary';
            }, 3000);
            return this.updateResponse;
          }
        }
      )
    }
  }
  isValidData(data:any){
    if(
      data.returned_product[0].return_reason!=''&& data.returned_product[0].unity > 0 ||
      data.returned_product[0].return_reason==''&& data.returned_product[0].unity == 0 &&
      data.receptor_data[0].name!='' && data.receptor_data[0].DNI!=''){
      console.log(data.returned_product[0].unity, data.returned_product[0].return_reason)
      data.status='Entregado'
      return true
    }else{
      this.icon= 'error'
      this.btn_color= 'warn'
      setTimeout(()=>{
        this.icon= 'send'
        this.btn_color= 'primary'
      }, 3000)
      return false
    }
  }
}
