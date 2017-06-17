
-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

CREATE TABLE IF NOT EXISTS `mydb`.`member` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `login` VARCHAR(45) NOT NULL,
  `enable` INT NOT NULL,
  `last_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
;

CREATE TABLE IF NOT EXISTS `mydb`.`account` (
  `id` INT NOT NULL,
  `status` INT NULL,
  `type` INT NULL,
  `fee_type` INT NULL,
  `has_bonus_withdraw` INT NULL,
  `is_transparent` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `mydb`.`payment_method` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `maximum_installments` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`fee` (
  `id` INT NOT NULL,
  `member_id` INT NULL,
  `account_id` INT NULL,
  `payment_method_id` INT NULL COMMENT 'Forma de pagamento',
  `installment_number` INT NULL COMMENT 'Número da parcela',
  `minimum_fee_value` FLOAT NULL COMMENT 'Taxa mínima cobrada em todo pagamento',
  `variable_fee_percentage` FLOAT NULL COMMENT 'Taxa variável de acordo com o valor e método do pagamento',
  `antecipation_fee_percentage` FLOAT NULL COMMENT 'Taxa percentual aplicada para cada dia antecipado',
  PRIMARY KEY (`id`),
  INDEX `fk_account_tax_pf_idx` (`payment_method_id` ASC),
  UNIQUE INDEX `UN_FEE` (`account_id` ASC, `payment_method_id` ASC, `installment_number` ASC),
  INDEX `fk_fee_mb_idx` (`member_id` ASC),
  CONSTRAINT `fk_fee_acc`
    FOREIGN KEY (`account_id`)
    REFERENCES `mydb`.`account` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fee_pm`
    FOREIGN KEY (`payment_method_id`)
    REFERENCES `mydb`.`payment_method` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fee_mb`
    FOREIGN KEY (`member_id`)
    REFERENCES `mydb`.`member` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
