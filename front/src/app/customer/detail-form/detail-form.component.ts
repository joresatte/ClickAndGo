import { Component, EventEmitter, Input, OnInit, Output, inject } from '@angular/core';
// import { ActivatedRoute } from '@angular/router';
// import { AppService } from '../../service/app.service';
// import { Constant } from '../../service/constant';
import { CustomerData } from '../../customer-data';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { BooleanInput } from '@angular/cdk/coercion';
import {MatIconModule} from '@angular/material/icon';
import {MatTooltipModule} from '@angular/material/tooltip';
// import { HttpHeaders } from '@angular/common/http';
import {MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-detail-form',
  standalone: true,
  imports: [CommonModule, 
    FormsModule, MatCardModule, MatButtonModule, 
    MatFormFieldModule, MatInputModule,
    MatTooltipModule, MatIconModule],
  templateUrl: './detail-form.component.html',
  styleUrl: './detail-form.component.css'
})
export class DetailFormComponent {

  @Input()
  disabledBtnSubmit:BooleanInput;
  @Input()
  showLoad:boolean=false
  @Input()
  customerData!:CustomerData
  @Input()
  customer!:CustomerData
  // formData!:CustomerData
  inputType!: string;

  disabled: BooleanInput= true;
  @Input()
  isEnabled:boolean= false
  @Input()
  showFooter:boolean= true
  @Input()
  customerStatus!:any;
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
