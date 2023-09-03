import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PerfilesService {
  private urlApi = 'http://192.168.111.18:8000/roles';

  constructor(private http: HttpClient) {}

  public getData(): Observable<any> {
    return this.http.get<any>(this.urlApi);
  }
}
