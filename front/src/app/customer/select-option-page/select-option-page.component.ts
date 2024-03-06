import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import { AppLogoComponent } from '../../app-logo/app-logo.component';
import { CommonModule } from '@angular/common';
import { Constant } from '../../service/constant';
import { Router } from '@angular/router';
import { AppService } from '../../service/app.service';
import { CustomerData } from '../../customer-data';

@Component({
  selector: 'app-select-option-page',
  standalone: true,
  imports: [CommonModule, FormsModule, MatCardModule, MatButtonModule, AppLogoComponent],
  templateUrl: './select-option-page.component.html',
  styleUrl: './select-option-page.component.css'
})
export class SelectOptionPageComponent implements OnInit {

  pendingCustomerslist!:CustomerData[];
  deliveredCustomerslist!:CustomerData[];
  pendingListLenght!:number;
  deliveredListLenght!:number
  note:string='total:'

  @Output()
  sendEmitter= new EventEmitter<string>()
  goTo:string=''
  date= new Date().toLocaleDateString()
  constructor(private serv: AppService, private router: Router){}
  getPendingData(){
    const url= `${Constant.login_Path}/all_pending/customers_data`
    const options:any= {}
    try {
      this.serv.getMethod(url, options).subscribe((res:any)=>{
        if (res!=null) {
          this.pendingCustomerslist= res
          // console.log(this.pendingCustomerslist)
          this.pendingListLenght= this.pendingCustomerslist.length
        }
      })
    } catch (error) {
      console.log(error)
    }
  }
  getDeliveredData(){
    const url= `${Constant.login_Path}/all_delivered/customers_data`
    const options:any= {}
    try {
      this.serv.getMethod(url, options).subscribe((res:any)=>{
        if (res!=null) {
          this.deliveredCustomerslist= res
          // console.log(this.deliveredCustomerslist)
          this.deliveredListLenght= this.deliveredCustomerslist.length
        }
      })
    } catch (error) {
      console.log(error)
    }
  }
  onclicked() {
    this.router.navigate(['/deliveredPage'])
    this.goTo= 'deliveredPage'
    Constant.currentPage= this.goTo
    // this.sendEmitter.emit(this.goTo)
  }
  onclick() {
    this.router.navigate(['/pendingPage'])
    this.goTo= 'pendingPage'
    Constant.currentPage= this.goTo
    // this.sendEmitter.emit(this.goTo)
  }
  ngOnInit(): void {
    this.getPendingData()
    this.getDeliveredData()
  }

}
