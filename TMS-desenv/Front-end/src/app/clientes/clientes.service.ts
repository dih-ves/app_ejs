import { Injectable } from '@angular/core';

import { PoTableColumn } from '@po-ui/ng-components';
import { Cliente } from './cliente.model';

@Injectable({
  providedIn: 'root'
})
export class ClientesService {

  constructor() { }

/*
          public id:number,
        public nome_cliente:string,
        public pregao:string,
        public processo_compras:string,
        public contrato:string,
        public linha:string,
        public cnpj:string,
        public insc_estadual:string,
        public insc_municipal:string,
        public endereco:string,
        public bairro:string,
        public cep:string,
        public estado:string,
        public uf:string,
        public telefone:string,
        public contato:string,
        public depto:string,
        public email:string,*/
        
  getColumns(): Array<PoTableColumn> {
    return [
      {property: 'id', type: 'number', label: 'Código', width: '7%'},
      {property: 'nome_cliente', type: 'string', label: 'Cliente', width: '30%'},
      {property: 'cnpj', type: 'string', label: 'CNPJ'},
      {property: 'telefone', type: 'string', label: 'Telefone'},
      {property: 'contato', type: 'string', label: 'Contato'},
      {property: 'depto', type: 'string', label: 'Depto'},
      {property: 'email', type: 'string', label: 'E-mail'}
    ]
  }

  incluirCliente(cliente: Cliente) {

  }

  alterarCliente(cliente: Cliente) {

  }  

  excluirCliente(idCliente) {

  }
}
