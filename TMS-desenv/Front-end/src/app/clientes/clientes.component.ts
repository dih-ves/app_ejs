import { Component, OnInit, ViewChild } from '@angular/core';

import { ClientesService } from  './clientes.service';
import { Cliente } from './cliente.model';
import {
  PoTableAction,
  PoTableColumn,
  PoModalAction,
  PoModalComponent,
  PoDynamicFormField,
  PoDynamicFormComponent,
  PoNotificationService,
  PoDialogService,
} from '@po-ui/ng-components';
import { PoPageAction, PoPageFilter } from '@po-ui/ng-components';
import { HtmlTagDefinition } from '@angular/compiler';

@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.scss'],
  providers: [PoNotificationService]
})
export class ClientesComponent implements OnInit {

  columns: Array<PoTableColumn>;  // Colunas da tabela
  actions_page: Array<PoPageAction>; // Ações da página
  actions_table: Array<PoTableAction>; // Ações da tabela
  disclaimerGroup; // Apresenta os filtros criados
  labelFilter: string = ''; // Label do filtro
  cliente: Cliente = new Cliente(); // Array contendo todos os clientes retornados pelo Backend
  listaClientes: Array<any>; // Array com os campos dos clientes apresentados na lista
  listaClientesFiltrados: Array<any>;  // Array com os campos dos clientes apresentados na lista após filtros
  tituloTela: string;

  private disclaimers = [];
  public tipoOp: string = '' // Tipo de operação que está sendo feita de acordo com botão selecionado

  clienteForm = {}
  camposForm: Array<PoDynamicFormField>;
  @ViewChild(PoModalComponent, { static: true }) poModal: PoModalComponent; // Modal com formulário
  @ViewChild(PoDynamicFormComponent, { static: true }) poForm: PoDynamicFormComponent; // Modal com formulário

  constructor(
    private clientesService: ClientesService,
     private poNotification: PoNotificationService,
     private poDialogService: PoDialogService
     ) { }

  ngOnInit(): void {
    this.poNotification.setDefaultDuration(5000);
    this.actions_page = [
      {label: '+ Incluir', action: this.Incluir.bind(this)}
    ];
    this.actions_table = [
      {action: this.visualizar.bind(this), label: 'Visualizar'},
      {action: this.alterar.bind(this), label: 'Alterar'},
      {action: this.excluir.bind(this), label: 'Excluir'},
    ];
    this.disclaimerGroup = {
      title: 'Filters',
      disclaimers: [],
      change: this.onChangeDisclaimer.bind(this)
    }
    this.columns = this.clientesService.getColumns()
    this.listaClientes = [{
      id: 1, 
      nome_cliente: 'DATAPREV', 
      cnpj: '44474145895', telefone: '(11) 2222-2222', 
      contato: 'Felipe', 
      depto: 'Faturamento', email: 'email@gmail.com'
    },
    {
      id: 2, 
      nome_cliente: 'São Paulo Turismo S/A', 
      cnpj: '44474145895', telefone: '(11) 2222-2222', 
      contato: 'Elizeu', 
      depto: 'Financeiro', email: 'email@gmail.com'      
    }];
    this.listaClientesFiltrados = [...this.listaClientes];
    this.criaForm();
  }

  /**
   * Funções responsáveis pelo filtro da tabela 
   */
  filter() {
    const filters = this.disclaimers.map(disclaimer => disclaimer.value);
    filters.length ? this.hiringProcessesFilter(filters) : this.resetFilterHiringProcess();
  }

  public readonly filterSettings: PoPageFilter = {
    action: this.filterAction.bind(this),
    placeholder: 'Search'
  };  

  filterAction(labelFilter: string | Array<string>) {
    const filter = typeof labelFilter === 'string' ? [labelFilter] : [...labelFilter];
    this.populateDisclaimers(filter);
    this.filter();
  }

  hiringProcessesFilter(filters) {
    this.listaClientesFiltrados = this.listaClientes.filter(item => {
      return Object.keys(item).some(key => !(item[key] instanceof Object) && this.includeFilter(item[key], filters));
    });
  }

  includeFilter(item, filters) {
    return filters.some(filter => String(item).toLocaleLowerCase().includes(filter.toLocaleLowerCase()));
  }

  onChangeDisclaimer(disclaimers) {
    this.disclaimers = disclaimers;
    this.filter();
  }

  populateDisclaimers(filters: Array<any>) {
    this.disclaimers = filters.map(value => ({ value }));

    if (this.disclaimers && this.disclaimers.length > 0) {
      this.disclaimerGroup.disclaimers = [...this.disclaimers];
    } else {
      this.disclaimerGroup.disclaimers = [];
    }
  }

  resetFilterHiringProcess() {
    this.listaClientesFiltrados = [...this.listaClientes];
  }
  // Fim das funções de filtro

  /** Executa ao fecha o modal */
  close: PoModalAction = {
    action: () => {
      this.closeModal();
    },
    label: 'Cancelar',
    danger: true
  };

  /** Executa ao confirmar o modal */
  confirm: PoModalAction = {
    action: () => {
      if (this.tipoOp == 'V') {
          this.closeModal()
      } else {
          if (this.validCp()) {
            for (let i = 0; this.camposForm.length > i; i++) {
              var campo = this.camposForm[i].property;
              this.cliente[campo] = this.poForm.value.hasOwnProperty(campo) ? this.poForm.value[campo] : ''
            }  
            if (this.tipoOp == 'I') {
              this.clientesService.incluirCliente(this.cliente);
  
              this.poNotification.success('Cliente Incluido com Sucesso!!!');
            } else {
              this.clientesService.alterarCliente(this.cliente);
  
              this.poNotification.success('Cliente Alterado com Sucesso!!!');              
            }

            this.poModal.close();            
          }
        }
      },
    label: 'Confirmar'
  };

  /** Fecha modal */
  closeModal() {
    this.poModal.close();
  }  

  visualizar(cliente) {
    this.tituloTela = "Clientes - Visualizar";
    this.clienteForm = [];
    for (let i = 0; this.listaClientes.length > i; i++) {
      if (cliente.id == this.listaClientes[i].id) {
        this.clienteForm = this.listaClientes[i]
      }
    }
    this.tipoOp = 'V';
    this.poModal.open();
  }

  Incluir() {
    this.tituloTela = "Clientes - Incluir"
    this.clienteForm = [];
    this.tipoOp = 'I'
    this.poModal.open();   

  }

  alterar(cliente) {
    this.tituloTela = "Clientes - Alterar"
    this.clienteForm = [];
    this.tipoOp = 'A'    
    for (let i = 0; this.listaClientes.length > i; i++) {
      if (cliente.id == this.listaClientes[i].id) {
        this.clienteForm = this.listaClientes[i]
      }
    }
    this.poModal.open();   
  }

  confirmaExclusao(cliente) {
    
    this.clientesService.excluirCliente(cliente.id);
  }
  
  excluir(cliente) {

    this.poDialogService.confirm({
      title: 'Clientes - Excluir',
      message: `Confirma a exclusão do cliente ${cliente.id} - ${cliente.nome_cliente}`,
      confirm: () => this.confirmaExclusao(cliente)})
  }  

  criaForm() {

    console.log(this.poForm);
    var desabilitaCampos = this.tipoOp == 'A' ? true : false
    this.camposForm = [
      {property: 'nome_cliente', label: 'Cliente', divider: 'Cadastrais', required: true, minLength: 3, maxLength: 50, disabled: desabilitaCampos },
      {property: 'cnpj', label: 'CNPJ', required: true, minLength: 14 , maxLength: 20, mask: '999.999.999/9999-99', disabled: desabilitaCampos},
      {property: 'telefone', label: 'Telefone', required: true, minLength: 10, maxLength: 14, mask: '(99)9999-99999', disabled: desabilitaCampos },
      {property: 'contato', label: 'Contato', required: true, minLength: 3, maxLength: 20, disabled: desabilitaCampos},
      {property: 'dpto.', label: 'DPTO', required: true, minLength: 3, maxLength: 15, disabled: desabilitaCampos },
      {property: 'email', label: 'E-mail', required: true, minLength: 3, maxLength: 30, disabled: desabilitaCampos },
      {property: 'pregao', label: 'Pregão',divider: 'Contrato', required: true, minLength: 3, maxLength: 6, disabled: desabilitaCampos },
      {property: 'processo', label: 'Processo Compras', required: true, minLength: 3, maxLength: 15, disabled: desabilitaCampos },
      {property: 'contrato', label: 'Contrato',  required: true, minLength: 3, maxLength: 15, disabled: desabilitaCampos },
      {property: 'linha', label: 'Linha', required: true, minLength: 3, maxLength: 50, disabled: desabilitaCampos },    
      {property: 'endereco', label: 'Endereço', divider: 'Endereço', required: true, minLength: 3, maxLength: 30, disabled: desabilitaCampos },
      {property: 'cep', label: 'CEP', required: true, minLength: 8, maxLength: 8, disabled: desabilitaCampos },
      {property: 'bairro', label: 'Bairro', required: true, minLength: 3, maxLength: 20, disabled: desabilitaCampos },
      {property: 'estado', label: 'Estado', required: true, minLength: 3, maxLength: 20, disabled: desabilitaCampos },
      {property: 'uf', label: 'UF', required: true, minLength: 2, maxLength: 2, disabled: desabilitaCampos },
      {property: 'insc_estadual', label: 'Insc. Estadual', required: true, minLength: 3, maxLength: 12, disabled: desabilitaCampos },
      {property: 'insc_municipal', label: 'Insc Municipal', required: true, minLength: 3, maxLength: 12, disabled: desabilitaCampos },
    ]   
  }

  validCampos() {
    
    if (this.tipoOp == 'V') {
      var inputs = document.getElementsByTagName('po-input');
      for (let i = 0; inputs.length > i; i++) {
        inputs[i].getElementsByClassName("po-field-container-content")[0].getElementsByTagName('input')[0].setAttribute("readonly","true");
      }       
    }
  }

  /**
   * Valida o preenchimento dos campos obrigatórios
   */
  validCp(): boolean {

    var camposInvalidos: string = "";

    for (let i = 0; this.camposForm.length > i; i++) {
      if (this.camposForm[i].required) {
        if (!this.poForm.value.hasOwnProperty(this.camposForm[i].property)) {
          camposInvalidos += this.camposForm[i].label+'; \n '
        } else if (this.poForm.value[this.camposForm[i].property].toString().trim() == "") {
          camposInvalidos += this.camposForm[i].label+'; \n '
        }
      }
    }

    if (camposInvalidos.length == 0) {
      return true
    } else {
      this.poDialogService.alert({
        title: 'Alerta',
        message: `Campos obrigatórios não preenchidos: \n  ${camposInvalidos}`})
    }
  }
}
