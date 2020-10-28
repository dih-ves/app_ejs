import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'TMS';
  menus = [
    { label: 'Cadastros', subItems: [
      {label: 'Clientes', link: './clientes'},
      {label: 'Colaboradores', link: './colaboradores'}
      ] 
    }
  ]
}
