import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';

import { ClientesComponent } from './clientes.component';
import { ClientesService } from './clientes.service'
import { PoTableModule, PoModule, PoPageModule } from '@po-ui/ng-components';


@NgModule({
  declarations: [
    ClientesComponent,
  ],
  imports: [
    BrowserModule,    
    CommonModule,
    PoTableModule,
    PoModule,
    PoPageModule 
  ],
  providers: [ClientesService]
})
export class ClientesModule { }
