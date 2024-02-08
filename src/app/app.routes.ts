import { Routes } from '@angular/router';
import { LoginPageComponent } from './login/login-page/login-page.component';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
    {
        path:'',
        redirectTo: 'home',
        pathMatch: 'full'
    },
    {
        path:'home',
        title: 'home',
        component: HomeComponent
    },
    {
        path: 'loginPage',
        title: 'loginPage',
        component: LoginPageComponent
    },
    // {
    //     path: 'customersPage',
    //     component: 
    //   },
    //   {
    //     path: 'client/:id',
    //     component:
    //   },
];
