import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private http:HttpClient) {}
  
  postMethod(url:string, data: any, httpOptions:any) {
    return this.http.post(url, data, httpOptions)
  }
  getMethod(url:string, httpOptions:any){
    return this.http.get(url, httpOptions)
  }
  updateMethod(url:string, data: any, httpOptions:any) {
    return this.http.post(url, data, httpOptions)
  }
}

