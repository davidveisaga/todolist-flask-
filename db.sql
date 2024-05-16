CREATE DATABASE IF NOT EXISTS `db_flask_todo`;

USE `db_flask_todo`;

CREATE TABLE `db_flask_todo`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `task` VARCHAR(500) NULL,
  PRIMARY KEY (`id`));