import { Component, EventEmitter, Input, Output } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatDividerModule} from '@angular/material/divider';
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Login } from '../../login';

@Component({
  selector: 'app-login-employee',
  standalone: true,
  imports: [CommonModule, 
            MatButtonModule, 
            MatDividerModule, 
            MatIconModule, 
            MatFormFieldModule, 
            MatInputModule, FormsModule ],
  templateUrl: './login-employee.component.html',
  styleUrl: './login-employee.component.css'
})
export class LoginEmployeeComponent {

  @Input()
  login!: Login;
  @Input()
  matIcons={
    send:'send',
    rotate_right:'rotate_right'
  }
  @Input()
  icon!:string;
  @Input()
  btnColor={
    color: 'primary',
  }
  @Input()
  btnColor_color!:string
  rotate={
    transform: 'rotate(0)',
    transition_duration: '0s'
  }
  
  @Output()
  sendEvent= new EventEmitter<Login>()
  handleClick(){
    console.log('clicked')
    this.sendEvent.emit(this.login)
  }

}
