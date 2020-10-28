import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';

import { ColaboradoresComponent } from './colaboradores.component';
import { ColaboradoresService } from './colaboradores.service'
import { PoTableModule, PoModule, PoPageModule } from '@po-ui/ng-components';


@NgModule({
  declarations: [
    ColaboradoresComponent,
  ],
  imports: [
    BrowserModule,    
    CommonModule,
    PoTableModule,
    PoModule,
    PoPageModule 
  ],
  providers: [ColaboradoresService]
})
export class ColaboradoresModule { }