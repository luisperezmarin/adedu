import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PerfilesService } from '../service/perfiles.service';
import { UsuariosService } from '../service/usuarios.service';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css'],
})
export class RegistroComponent implements OnInit {
  hide: boolean = true;
  data: any[] = [];
  @Input() usuarioObj = {
    Nombres: '',
    Apellidos: '',
    Edad: 4,
    Correo: '',
    Password: '',
    RolID: 1,
  };

  constructor(
    private apiService: PerfilesService,
    private usuarioService: UsuariosService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.llenarData();
  }

  llenarData() {
    this.apiService.getData().subscribe((data) => {
      this.data = data;
      console.log(this.data);
    });
  }
  agregarUsuario(data: any) {
    console.log(this.usuarioObj);
    this.usuarioService
      .agregarUsuario(this.usuarioObj)
      .subscribe((data: {}) => {
        this.router.navigate(['/']);
        alert('Usuario agregado correctamente');
      });
  }
}
