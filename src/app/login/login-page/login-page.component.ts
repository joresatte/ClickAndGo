import { Component, OnInit } from '@angular/core';
import { AppLogoComponent } from '../../app-logo/app-logo.component';
import { LoginEmployeeComponent } from '../login-employee/login-employee.component';
import { Login } from '../../login';
import { Constant } from '../../service/constant';
import { AppService } from '../../service/app.service';
import { Router } from '@angular/router';
import { HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [AppLogoComponent, LoginEmployeeComponent],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.css'
})
export class LoginPageComponent implements OnInit {


  matIcons:any={}
  icon!:string;
  btnColor:any={}
  btnColor_color!:string;
  rotate:any={}
  loginUser: Login={
    identification: '',
    password: ''
  }
  ngOnInit(): void {
    this.icon= 'send'
    this.btnColor_color= 'primary'
  }
  options={
    headers: new HttpHeaders({'Content-Type': 'application/json'})
  }
  data?:any;
  constructor(private serv: AppService, private router: Router){}
  handledClick(e: Login){
    this.loginUser= e
    console.log(this.loginUser.identification, this.loginUser.password)
    if (this.loginUser.identification!='' && this.loginUser.password!=''){
      const body= JSON.stringify({
        identification: this.loginUser.identification,
        password: this.loginUser.password
      })
      try {
        this.serv.postMethod(`${Constant.login_Path}/get_login/Authenticated`, body, this.options).subscribe(async (response:any)=>{
          if (response!= undefined || response!= null) {
            this.data= await response
            console.log('data',this.data)
            console.log(this.data.identification)
            this.router.navigate(['/optionPage'])
          } else {
            alert('Ooops something went wrong')
          }
        })
      } catch (error) {
        console.log(error)
      }
    }else{
      try {
        this.btnColor_color= this.btnColor.color='warn'
      } catch (error) {
        console.log('bad')
      }finally{
        setTimeout(()=>{
          alert('all fields are required')
          this.btnColor_color= this.btnColor.color='primary'
        }, 100)
      }
    }
  }
}
