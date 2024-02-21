import { Routes } from '@angular/router';
import { LoginPageComponent } from './login/login-page/login-page.component';
import { HomeComponent } from './home/home.component';
import { CustomersPageComponent } from './customer/customers-page/customers-page.component';
import { SelectOptionPageComponent } from './customer/select-option-page/select-option-page.component';
import { PendingPageComponent } from './customer/pending-page/pending-page.component';
import { DeliveredPageComponent } from './customer/delivered-page/delivered-page.component';
import { DetailPageComponent } from './customer/detail-page/detail-page.component';

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
    {
        path: 'optionPage',
        component: SelectOptionPageComponent
    },
    {
        path: 'pendingPage',
        component: PendingPageComponent
    },
    {
        path: 'deliveredPage',
        component: DeliveredPageComponent
    },
    {
        path: 'detailPage',
        component: DetailPageComponent
    },
    { 
        path: 'customerPage', 
        component: CustomersPageComponent, 
        children: [
            
        //    { path: 'user/:name', component: UserCmp }
        ]
    }
    //   {
    //     path: 'client/:id',
    //     component:
    //   },
];
