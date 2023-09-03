import { Component, OnInit } from '@angular/core';
import { PerfilesService } from '../service/perfiles.service';

@Component({
  selector: 'app-crear-usuario',
  templateUrl: './crear-usuario.component.html',
  styleUrls: ['./crear-usuario.component.css'],
})
export class CrearUsuarioComponent implements OnInit {
  data: any[] = [];

  constructor(private perfilesService: PerfilesService) {}

  ngOnInit(): void {
    this.llenarData();
  }

  llenarData() {
    this.perfilesService.getData().subscribe((data) => {
      this.data = data;
      console.log(this.data);
    });
  }
}
