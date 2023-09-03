import { Component, OnInit } from '@angular/core';
import { ApiService } from '../service/api.service';
import {MatSelectModule} from '@angular/material/select';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';


@Component({
  selector: 'app-crear-usuario',
  templateUrl: './crear-usuario.component.html',
  styleUrls: ['./crear-usuario.component.css'],

})
export class CrearUsuarioComponent implements OnInit {
  data: any[] = [];

  constructor (private apiService: ApiService) { }

  ngOnInit (): void {
    this.llenarData();
  }

  llenarData() {
    this.apiService.getData().subscribe( data => {
      this.data = data;
      console.log(this.data);
    }) 
  }

}



