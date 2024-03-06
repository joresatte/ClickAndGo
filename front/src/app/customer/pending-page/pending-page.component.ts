import { Component, OnInit } from '@angular/core';
import { FormDataComponent } from '../form-data/form-data.component';
import { AppService } from '../../service/app.service';
import { CustomerData } from '../../customer-data';
import { Constant } from '../../service/constant';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AppLogoComponent } from '../../app-logo/app-logo.component';
import { FilterLayoutComponent } from '../filter-layout/filter-layout.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-pending-page',
  standalone: true,
  imports: [FormDataComponent, CommonModule, FormsModule, AppLogoComponent, FilterLayoutComponent],
  templateUrl: './pending-page.component.html',
  styleUrl: './pending-page.component.css'
})
export class PendingPageComponent implements OnInit{

  layout!:string;
  inputValue:string= ''
  status!:boolean
  customerslist!:CustomerData[];
  newCustomerList!:CustomerData[]
  currentPage:string= 'pendingPage'
  
  ngOnInit(): void {
    this.getData()
    Constant.currentPage=this.currentPage
  }
  getActiveGrid(e: string) {
    this.layout= e
    // console.log(this.layout)
  }
  constructor(private serv: AppService, private router: Router){
  }
  getActiveList(e:string){
    this.layout= e
  }
  onChanged(e:string){
    this.inputValue= e
  }
  getData(){
    const url= `${Constant.login_Path}/all_pending/customers_data`
    const options:any= {}
    try {
      this.serv.getMethod(url, options).subscribe((res:any)=>{
        if (res!=null) {
          this.customerslist= res 
          // console.log(this.customerslist)
          this.newCustomerList= this.customerslist
          this.newCustomerList.find((item)=>{
            item['status']=='Entregado'?this.status= true: this.status= false
            // console.log(this.status)
          })
        }
      })
    } catch (error) {
      console.log(error)
    }
  }
  
  filterData():CustomerData[]{
      const text= this.inputValue
     if(text==''){
      return this.customerslist
     }else{
      return this.customerslist.filter((element: any) => {
        return element.address.toLocaleUpperCase().includes(text.toLocaleUpperCase())||
        element.dni.toLocaleUpperCase().includes(text.toLocaleUpperCase())||
        element.cliente.toLocaleUpperCase().includes(text.toLocaleUpperCase())||
        element.phone.toLocaleUpperCase().includes(text.toLocaleUpperCase())
      });
     }
  }
  onClicked(e:any){
    if(e){
      this.router.navigate(['/detailPage', e])
    }
  }
  
  filterBy(obj:CustomerData[]) {
    const objList:any = []
    if(true){
      var result = Object.keys(obj).reduce(function(r:any, e:any) {
      console.log(e)
      if (e.indexOf() != -1) {
          console.log(e.indexOf())
          objList.push(obj[e]);
      } else {
        Object.values((obj[e])).filter((k:{ status: string; })=> {
          console.log('this is k',k)
          if (k.status== 'Entregado') {
              // console.log(k)
              // console.log(obj[e])
              // r.push(obj[e])
          }
        })
      }
      }, [])
    }
  }
}
