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
import {MatFormFieldModule} from '@angular/material/form-field';
import { BooleanInput } from '@angular/cdk/coercion';
import {MatTooltipModule} from '@angular/material/tooltip';
// import { HttpHeaders } from '@angular/common/http';
import {MatSnackBar} from '@angular/material/snack-bar';
@Component({
  selector: 'app-form-data',
  standalone: true,
  imports: [CommonModule, FormsModule, MatFormFieldModule, 
            MatGridListModule, MatCardModule, MatTabsModule,
            AppLogoComponent, MatListModule,MatInputModule,
            MatMenuModule, MatIconModule, MatButtonModule, MatTooltipModule],
  templateUrl: './form-data.component.html',
  styleUrl: './form-data.component.css'
})
export class FormDataComponent implements OnInit{

  loading: boolean= false;
  style!:string;
  class!:any;
  @Input()
  formData!:CustomerData;
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
  ngOnInit(): void {
    this.checkStatus()
  }
  checkStatus(){
    this.status==true? this.class='status-delivered': this.class= 'status-pending'
  }
  // getSeverity (product: CustomerData) {
  //     switch (product.phone) {
  //         case 'INSTOCK':
  //             return 'success';

  //         case 'LOWSTOCK':
  //             return 'warning';

  //         case 'OUTOFSTOCK':
  //             return 'danger';

  //         default:
  //             return null;
  //     }
  // };
  @Input()
  showDetailForm:boolean= false
  @Input()
  disabledBtnSubmit:BooleanInput;
  @Input()
  showLoad:boolean=false
  disabled: BooleanInput= true;
  @Input()
  isEnabled:boolean= false
  @Input()
  showFooter:boolean= true
  @Input()
  submit:string= 'Guardar'
  @Input()
  updateResponse:string='Unsaved'
  @Input()
  icon:string='send'//error
  @Input()
  btn_btn:any='btn_btn'
  @Input()
  btn_color:string= 'primary'
  constructor(private snackBar: MatSnackBar){
  }
  @Output()
  sendEmitter= new EventEmitter<CustomerData>()
  submitData(arg: CustomerData){
    this.sendEmitter.emit(arg)
  }
}
