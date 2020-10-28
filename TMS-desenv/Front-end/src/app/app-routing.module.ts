import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AppComponent } from './app.component'
import { ClientesComponent } from './clientes/clientes.component'
import { ColaboradoresComponent } from './colaboradores/colaboradores.component'

const routes: Routes = [
  { path: '', component: AppComponent },
  { path: 'clientes', component: ClientesComponent },
  { path: 'colaboradores', component: ColaboradoresComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
