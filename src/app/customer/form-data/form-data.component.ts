import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CustomerData } from '../../customer-data';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatCardModule} from '@angular/material/card';
import { AppLogoComponent } from '../../app-logo/app-logo.component';
import {MatListModule} from '@angular/material/list';
import {MatMenuModule} from '@angular/material/menu';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';
import {MatTabsModule} from '@angular/material/tabs';
@Component({
  selector: 'app-form-data',
  standalone: true,
  imports: [CommonModule, FormsModule, 
            MatGridListModule, MatCardModule, MatTabsModule,
            AppLogoComponent, MatListModule,MatInputModule,
            MatMenuModule, MatIconModule, MatButtonModule],
  templateUrl: './form-data.component.html',
  styleUrl: './form-data.component.css'
})
export class FormDataComponent implements OnInit{

  loading: boolean= false;
  style!:string;
  class!:any;
  @Input()
  status!:boolean;
  @Input()
  layout!:string;
  @Output()
  sendHandleClick= new EventEmitter<any>()
  handleClick(e:any) {
    this.sendHandleClick.emit(e)
  }
  onSortChange(){
    console.log('text changed')
  }
  @Input()
  formData!:CustomerData;
  ngOnInit(): void {
    this.checkStatus()
  }
  checkStatus(){
    this.status==true? this.class='status-delivered': this.class= 'status-pending'
  }
  getSeverity (product: CustomerData) {
      switch (product.phone) {
          case 'INSTOCK':
              return 'success';

          case 'LOWSTOCK':
              return 'warning';

          case 'OUTOFSTOCK':
              return 'danger';

          default:
              return null;
      }
  };
}
