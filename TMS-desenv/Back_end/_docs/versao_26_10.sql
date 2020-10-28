-- MySQL Script generated by MySQL Workbench
-- Tue Oct 27 14:50:13 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tms
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tms
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tms` DEFAULT CHARACTER SET utf8 ;
USE `tms` ;

-- -----------------------------------------------------
-- Table `tms`.`cargo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`cargo` (
  `id` INT NOT NULL,
  `nome` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tms`.`departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`departamento` (
  `id` INT NOT NULL,
  `nome` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tms`.`grupo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`grupo` (
  `id` INT NOT NULL,
  `nome` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tms`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`usuario` (
  `id` INT NOT NULL,
  `user_name` VARCHAR(30) NOT NULL,
  `nome` VARCHAR(30) NOT NULL,
  `sobrenome` VARCHAR(30) NULL,
  `email` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(16) NOT NULL,
  `cargo_id` INT NOT NULL,
  `departamento_id` INT NOT NULL,
  `grupo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `id_usuario_UNIQUE` (`user_name` ASC) VISIBLE,
  INDEX `fk_usuario_cargo1_idx` (`cargo_id` ASC) VISIBLE,
  INDEX `fk_usuario_departamento1_idx` (`departamento_id` ASC) VISIBLE,
  INDEX `fk_usuario_grupo1_idx` (`grupo_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuario_cargo1`
    FOREIGN KEY (`cargo_id`)
    REFERENCES `tms`.`cargo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuario_departamento1`
    FOREIGN KEY (`departamento_id`)
    REFERENCES `tms`.`departamento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuario_grupo1`
    FOREIGN KEY (`grupo_id`)
    REFERENCES `tms`.`grupo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Tabela de usuarios';


-- -----------------------------------------------------
-- Table `tms`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`cliente` (
  `id` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `pregao` VARCHAR(20) NULL,
  `processo_compras` VARCHAR(20) NULL,
  `contrato` VARCHAR(20) NULL,
  `linha` VARCHAR(30) NULL,
  `contato` VARCHAR(30) NULL,
  `departamento_contato` VARCHAR(30) NULL,
  `fone` VARCHAR(20) NULL,
  `email` VARCHAR(100) NULL,
  `cpf` VARCHAR(30) NULL,
  `cnpj` VARCHAR(30) NULL,
  `inscricao_estadual` VARCHAR(30) NULL,
  `inscricao_municipal` VARCHAR(30) NULL,
  `logradouro` VARCHAR(100) NULL,
  `numero` INT NULL,
  `bairro` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  `cep` VARCHAR(12) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
COMMENT = 'Tabela de clientes';


-- -----------------------------------------------------
-- Table `tms`.`colaborador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`colaborador` (
  `id` INT NOT NULL,
  `nome` VARCHAR(30) NOT NULL,
  `sobrenome` VARCHAR(30) NOT NULL,
  `admissao` DATE NULL,
  `demissao` DATE NULL,
  `fone` VARCHAR(20) NULL,
  `ctps` VARCHAR(30) NULL,
  `rg` VARCHAR(30) NULL,
  `cpf` VARCHAR(30) NULL,
  `cnh` VARCHAR(30) NULL,
  `categoria` VARCHAR(30) NULL,
  `logradouro` VARCHAR(100) NULL,
  `numero` INT NULL,
  `bairro` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  `cep` VARCHAR(12) NULL,
  `departamento_id` INT NOT NULL,
  `cargo_id` INT NOT NULL,
  `grupo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_colaborador_departamento1_idx` (`departamento_id` ASC) VISIBLE,
  INDEX `fk_colaborador_cargo1_idx` (`cargo_id` ASC) VISIBLE,
  INDEX `fk_colaborador_grupo1_idx` (`grupo_id` ASC) VISIBLE,
  CONSTRAINT `fk_colaborador_departamento1`
    FOREIGN KEY (`departamento_id`)
    REFERENCES `tms`.`departamento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_colaborador_cargo1`
    FOREIGN KEY (`cargo_id`)
    REFERENCES `tms`.`cargo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_colaborador_grupo1`
    FOREIGN KEY (`grupo_id`)
    REFERENCES `tms`.`grupo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Tabela de colaboradores';


-- -----------------------------------------------------
-- Table `tms`.`controleColaborador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`controleColaborador` (
  `id` INT NOT NULL,
  `ano` YEAR NOT NULL,
  `mes` VARCHAR(5) NOT NULL,
  `cartao_ponto` VARCHAR(5) NOT NULL,
  `recibo_vr` VARCHAR(5) NOT NULL,
  `recibo_vt` VARCHAR(5) NOT NULL,
  `colaborador_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_controleColaborador_colaborador1_idx` (`colaborador_id` ASC) VISIBLE,
  CONSTRAINT `fk_controleColaborador_colaborador1`
    FOREIGN KEY (`colaborador_id`)
    REFERENCES `tms`.`colaborador` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tms`.`veiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`veiculo` (
  `id` INT NOT NULL,
  `marca` VARCHAR(45) NULL,
  `placa` VARCHAR(45) NOT NULL,
  `ano` YEAR NULL,
  `renavam` VARCHAR(45) NOT NULL,
  `mes_licenciamento` VARCHAR(5) NULL,
  `vencimento_ipva` DATE NULL,
  `status` VARCHAR(45) NULL,
  `valor_ipva` DECIMAL(19,2) NULL,
  `valor_licenciamento` DECIMAL(19,2) NULL,
  `valor_dpvat` DECIMAL(19,2) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `placa_UNIQUE` (`placa` ASC) VISIBLE,
  UNIQUE INDEX `renavam_UNIQUE` (`renavam` ASC) VISIBLE)
ENGINE = InnoDB
COMMENT = 'Tabela de controle de frota ';


-- -----------------------------------------------------
-- Table `tms`.`multa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`multa` (
  `id` INT NOT NULL,
  `codigo_ait` VARCHAR(45) NOT NULL COMMENT 'Código de auto de infração',
  `data` DATE NOT NULL,
  `hora` TIME NOT NULL,
  `local` VARCHAR(255) NOT NULL,
  `descricao` VARCHAR(255) NOT NULL,
  `valor` DECIMAL(19,2) NULL,
  `status` VARCHAR(255) NULL,
  `veiculo_id` INT NOT NULL,
  `colaborador_id` INT NOT NULL,
  PRIMARY KEY (`id`, `veiculo_id`),
  INDEX `fk_multa_veiculo1_idx` (`veiculo_id` ASC) VISIBLE,
  INDEX `fk_multa_colaborador1_idx` (`colaborador_id` ASC) VISIBLE,
  CONSTRAINT `fk_multa_veiculo1`
    FOREIGN KEY (`veiculo_id`)
    REFERENCES `tms`.`veiculo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_multa_colaborador1`
    FOREIGN KEY (`colaborador_id`)
    REFERENCES `tms`.`colaborador` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Tabela de registro de multas';


-- -----------------------------------------------------
-- Table `tms`.`fornecedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`fornecedor` (
  `id` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `nome_fantasia` VARCHAR(30) NULL,
  `tipo_produto` VARCHAR(30) NOT NULL,
  `cnpj` VARCHAR(30) NULL,
  `inscricao_estadual` VARCHAR(30) NULL,
  `inscricao_municipal` VARCHAR(30) NULL,
  `fone` VARCHAR(20) NULL,
  `contato` VARCHAR(30) NULL,
  `departamento_contato` VARCHAR(30) NULL,
  `email` VARCHAR(100) NULL,
  `logradouro` VARCHAR(100) NULL,
  `numero` INT NULL,
  `bairro` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  `cep` VARCHAR(12) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = 'tabela com o registro de fornecedores';


-- -----------------------------------------------------
-- Table `tms`.`cartaoCombustivel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`cartaoCombustivel` (
  `id` INT NOT NULL,
  `numero` INT NULL,
  `tipo` VARCHAR(45) NULL,
  `senha` VARCHAR(45) NULL,
  `unidade` VARCHAR(45) NULL,
  `status` VARCHAR(45) NULL,
  `fornecedor_id` INT NOT NULL,
  `veiculo_id` INT NOT NULL,
  `colaborador_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cartaoCombustivel_fornecedor1_idx` (`fornecedor_id` ASC) VISIBLE,
  INDEX `fk_cartaoCombustivel_veiculo1_idx` (`veiculo_id` ASC) VISIBLE,
  INDEX `fk_cartaoCombustivel_colaborador1_idx` (`colaborador_id` ASC) VISIBLE,
  CONSTRAINT `fk_cartaoCombustivel_fornecedor1`
    FOREIGN KEY (`fornecedor_id`)
    REFERENCES `tms`.`fornecedor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cartaoCombustivel_veiculo1`
    FOREIGN KEY (`veiculo_id`)
    REFERENCES `tms`.`veiculo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cartaoCombustivel_colaborador1`
    FOREIGN KEY (`colaborador_id`)
    REFERENCES `tms`.`colaborador` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Tabela registro de Cartão Combustível';


-- -----------------------------------------------------
-- Table `tms`.`Combustivel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`Combustivel` (
  `id` INT NOT NULL,
  `data` DATE NULL,
  `litro` DECIMAL(19,2) NULL,
  `preco` DECIMAL(19,2) NOT NULL,
  `veiculo_id` INT NOT NULL,
  `colaborador_id` INT NOT NULL,
  `fornecedor_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Combustivel_veiculo1_idx` (`veiculo_id` ASC) VISIBLE,
  INDEX `fk_Combustivel_colaborador1_idx` (`colaborador_id` ASC) VISIBLE,
  INDEX `fk_Combustivel_fornecedor1_idx` (`fornecedor_id` ASC) VISIBLE,
  CONSTRAINT `fk_Combustivel_veiculo1`
    FOREIGN KEY (`veiculo_id`)
    REFERENCES `tms`.`veiculo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Combustivel_colaborador1`
    FOREIGN KEY (`colaborador_id`)
    REFERENCES `tms`.`colaborador` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Combustivel_fornecedor1`
    FOREIGN KEY (`fornecedor_id`)
    REFERENCES `tms`.`fornecedor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Tabela de registro de consumo de combustível';


-- -----------------------------------------------------
-- Table `tms`.`manutencaoVeiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`manutencaoVeiculo` (
  `id` INT NOT NULL,
  `data_inicial` DATE NOT NULL,
  `data_final` DATE NULL,
  `veiculo_id` INT NOT NULL,
  `colaborador_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_manutencaoVeiculo_veiculo1_idx` (`veiculo_id` ASC) VISIBLE,
  INDEX `fk_manutencaoVeiculo_colaborador1_idx` (`colaborador_id` ASC) VISIBLE,
  CONSTRAINT `fk_manutencaoVeiculo_veiculo1`
    FOREIGN KEY (`veiculo_id`)
    REFERENCES `tms`.`veiculo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_manutencaoVeiculo_colaborador1`
    FOREIGN KEY (`colaborador_id`)
    REFERENCES `tms`.`colaborador` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tms`.`rdvo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`rdvo` (
  `id` INT NOT NULL,
  `posto` VARCHAR(30) NOT NULL,
  `ltu` INT NOT NULL COMMENT 'Código da Linha de transferencia Urbana',
  `inicio_viagem` DATE NOT NULL,
  `hodometro_ini` INT NOT NULL,
  `hodometro_fim` INT NOT NULL,
  `cliente_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_rdvo_cliente1_idx` (`cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_rdvo_cliente1`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `tms`.`cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Tabela de registro diario de viagens e ocorrências';


-- -----------------------------------------------------
-- Table `tms`.`task`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`task` (
  `id` INT NOT NULL,
  `nome` VARCHAR(255) NULL,
  `descricao` VARCHAR(255) NULL,
  `observacao` VARCHAR(255) NULL,
  `inicio` DATE NULL,
  `fim` DATE NULL,
  `prioridade` VARCHAR(45) NULL,
  `status` VARCHAR(45) NULL,
  `usuario_id` INT NOT NULL,
  `grupo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_task_usuario1_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_task_grupo1_idx` (`grupo_id` ASC) VISIBLE,
  CONSTRAINT `fk_task_usuario1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `tms`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_task_grupo1`
    FOREIGN KEY (`grupo_id`)
    REFERENCES `tms`.`grupo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Tabela de registro de tarefas em geral';


-- -----------------------------------------------------
-- Table `tms`.`ddsp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`ddsp` (
  `id` INT NOT NULL,
  `data` DATE NOT NULL,
  `hodometro_ini` INT NOT NULL,
  `hodometro_fim` INT NOT NULL,
  `horario_ini` TIME NOT NULL,
  `horario_fim` TIME NOT NULL,
  `intervalo_ini` VARCHAR(45) NOT NULL,
  `intervalo_fim` VARCHAR(45) NOT NULL,
  `usuario_sr` VARCHAR(255) NOT NULL,
  `colaborador_id` INT NOT NULL,
  `veiculo_id` INT NOT NULL,
  `valor_hora` DECIMAL(19,2) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ddsp_colaborador1_idx` (`colaborador_id` ASC) VISIBLE,
  INDEX `fk_ddsp_veiculo1_idx` (`veiculo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ddsp_colaborador1`
    FOREIGN KEY (`colaborador_id`)
    REFERENCES `tms`.`colaborador` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ddsp_veiculo1`
    FOREIGN KEY (`veiculo_id`)
    REFERENCES `tms`.`veiculo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Tabela do demonstrativo diario de servico prestado';


-- -----------------------------------------------------
-- Table `tms`.`itemManutencao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`itemManutencao` (
  `id` INT NOT NULL,
  `tipo` VARCHAR(45) NULL COMMENT 'Tipo de item (peca, lavagem, óleo, serviço)',
  `nome` VARCHAR(45) NULL COMMENT 'nome do item/peca/servico',
  `preco` DECIMAL(19,2) NULL,
  `fornecedor_id` INT NOT NULL,
  `manutencaoVeiculo_id` INT NOT NULL,
  PRIMARY KEY (`id`, `manutencaoVeiculo_id`),
  INDEX `fk_itemManutencao_fornecedor1_idx` (`fornecedor_id` ASC) VISIBLE,
  INDEX `fk_itemManutencao_manutencaoVeiculo1_idx` (`manutencaoVeiculo_id` ASC) VISIBLE,
  CONSTRAINT `fk_itemManutencao_fornecedor1`
    FOREIGN KEY (`fornecedor_id`)
    REFERENCES `tms`.`fornecedor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_itemManutencao_manutencaoVeiculo1`
    FOREIGN KEY (`manutencaoVeiculo_id`)
    REFERENCES `tms`.`manutencaoVeiculo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tms`.`blacklistToken`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`blacklistToken` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `token` VARCHAR(200) NULL,
  `blacklisted_em` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;