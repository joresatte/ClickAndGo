import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { CustomerData } from '../customer-data';
import { Observable, map, tap } from 'rxjs';
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
  updateMethod(url:string, data: any):Observable<HttpResponse<any>> {
    return this.http.put<any>(url, data,{
      headers:new HttpHeaders({'Content-Type': 'application/json'}),
      observe: 'response',
    })
  }
  async getdataById(url:string, httpOptions:any): Promise<CustomerData | undefined> {
    const json = await fetch(url, httpOptions);
    const res = await json.json() ?? {};
    return res
  }
}

