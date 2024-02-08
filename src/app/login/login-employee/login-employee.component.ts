import { Component } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatDividerModule} from '@angular/material/divider';
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login-employee',
  standalone: true,
  imports: [CommonModule, MatButtonModule, MatDividerModule, MatIconModule, MatFormFieldModule, MatInputModule, FormsModule],
  templateUrl: './login-employee.component.html',
  styleUrl: './login-employee.component.css'
})
export class LoginEmployeeComponent {

  // showCloseBtn:boolean= false
  loading:boolean= false
  login= {
    identification:'',
    password: '',
  }
  matIcons={
    send:'send',
    rotate_right:'rotate_right'
  }
  icon= this.matIcons.send
  rotate={
    transform: 'rotate(0)',
    transition_duration: '0s'
  }
  handleClick(): boolean{
    console.log('clicked')
    this.icon= this.matIcons.rotate_right
    this.rotate.transform= 'rotateX(-180deg)'
    this.rotate.transition_duration= '2s'
    return true

  }

}
