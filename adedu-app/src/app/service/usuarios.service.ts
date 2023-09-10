import { Injectable } from '@angular/core';
import { Observable, throwError, catchError, retry } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

export class Usuario {
  Nombres?: string;
  Apellidos?: string;
  Edad?: number;
  Correo?: string;
  Password?: string;
  RolID?: number;
}

@Injectable({
  providedIn: 'root',
})
export class UsuariosService {
  baseURL: string = 'http://192.168.111.18:8000';

  constructor(private http: HttpClient) {}

  httpHeader = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  agregarUsuario(data: any): Observable<Usuario> {
    return this.http
      .post<Usuario>(
        this.baseURL + '/usuarios',
        JSON.stringify(data),
        this.httpHeader
      )
      .pipe(retry(1), catchError(this.handleError));
  }
  handleError(err: any) {
    let message = '';
    if (err.error instanceof ErrorEvent) {
      message = err.error.message;
    } else {
      message = `Error Code: ${err.status}\nMessage: ${err.message}`;
    }
    console.log(message);
    return throwError(() => {
      message;
    });
  }
}
