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
import { HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-detail-page',
  standalone: true,
  imports: [AppLogoComponent, CommonModule, 
            FormsModule, MatCardModule, MatButtonModule, 
            MatFormFieldModule, MatInputModule,
            MatTooltipModule, MatIconModule],
  templateUrl: './detail-page.component.html',
  styleUrl: './detail-page.component.css'
})
export class DetailPageComponent implements OnInit{
  route: ActivatedRoute = inject(ActivatedRoute);
  id:any
  load:string= 'Loading...'
  showLoad:boolean=false
  customerData!:CustomerData
  navTitle:string= 'Comprobante de la entrega'
  customer!:CustomerData
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
  constructor(private serv: AppService){
    this.id= String(this.route.snapshot.params['id'])
  }
  ngOnInit(): void {
    this.getCustomerData()
  }
  getCustomerData(){
    try {
      const url:string= `${Constant.login_Path}/one_customer/${this.id}`
      const options:any={}
      this.serv.getMethod(url, options).subscribe((res:any)=>{
        this.customerData= res
        this.customerStatus= this.customerData['status']
        console.log(this.customerStatus)
        if(this.customerStatus== 'Entregado'){
          this.isEnabled= true
          this.disabledBtnSubmit= true
          this.showFooter= false
        }
      })
    } catch (error) {
      console.log(error)
    }
  }
  submitData(data:CustomerData){
    console.log(data)
    const options={
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    }
    const url= `${Constant.login_Path}/customer_data/update/${this.id}`
    const check= this.isValidData(data)
    if(check==false){
      alert('error')
    }else{
      // console.log(body)
      this.serv.updateMethod(url, data, options).subscribe((res:any)=>{
        if(res.status== 200){
          setTimeout(()=>{
            this.disabledBtnSubmit= true
          }, 3000)
          return this.updateResponse = 'Saved'
        }else{
          this.icon= 'error'
          this.btn_color= 'warn'
          setTimeout(()=>{
            this.icon= 'send'
            this.btn_color= 'primary'
          }, 3000)
          return this.updateResponse
        }
      })
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
