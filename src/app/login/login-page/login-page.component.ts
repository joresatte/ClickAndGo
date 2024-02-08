import { Component } from '@angular/core';
import { AppLogoComponent } from '../../app-logo/app-logo.component';
import { LoginEmployeeComponent } from '../login-employee/login-employee.component';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [AppLogoComponent, LoginEmployeeComponent],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.css'
})
export class LoginPageComponent {

}
