SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

CREATE DATABASE IF NOT EXISTS `loanbank` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `loanbank`;

-- --------------------------------------------------------
--
-- Table structure for table `users`
--
DROP TABLE IF EXISTS `users`;
CREATE TABLE `loanbank`.`users` (
 `id` INT NOT NULL AUTO_INCREMENT ,
 `username` TEXT NOT NULL UNIQUE ,
 `type` TEXT NOT NULL ,

 PRIMARY KEY (`id`)
 ) ENGINE = InnoDB AUTO_INCREMENT=1;
-- --------------------------------------------------------

--
-- Table structure for table `loan_terms`
--
DROP TABLE IF EXISTS `terms`;
CREATE TABLE `loanbank`.`terms` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` TEXT NOT NULL UNIQUE,
  `type` BOOLEAN NOT NULL,
  `min` INT NOT NULL DEFAULT 0,
  `MAX` INT NOT NULL DEFAULT 999999999,
  `duration` INT NOT NULL MIN 6 MAX 120,
  `interest` INT NOT NULL DEFAULT MIN 0 MAX 100,
   PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT=1;
-- --------------------------------------------------------

--
-- Table structure for table `loan`
--
DROP TABLE IF EXISTS `loans`;
CREATE TABLE `loanbank`.`loans` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `accepted` BOOLEAN DEFAULT 0,
  `value` INT NOT NULL,
  `type` BOOLEAN NOT NULL,
  `terms_id` INT NOT NULL,
  `users_id` INT NOT NULL,
   PRIMARY KEY (`id`)
   KEY `terms_id` (`terms_id`),
   KEY `users_id` (`users_id`),
) ENGINE = InnoDB AUTO_INCREMENT=1;
-- --------------------------------------------------------

--
-- Constraints for tables
--
ALTER TABLE `loans`
  ADD CONSTRAINT `fk_loans_terms` FOREIGN KEY (`terms_id`) REFERENCES `terms` (`id`);
  
ALTER TABLE `loans`
  ADD CONSTRAINT `fk_loans_users` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`);


SET FOREIGN_KEY_CHECKS=1;

