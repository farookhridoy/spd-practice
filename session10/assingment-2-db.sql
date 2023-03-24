/*
SQLyog Ultimate
MySQL - 8.0.30 : Database - spd_query_practice
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `insurance_type` enum('TERMLIFE','HEALTH','ENDOWMENT') NOT NULL,
  `risk` enum('LOW','MEDIUM','HIGH') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`id`,`user_id`,`insurance_type`,`risk`) values 
(1,6697,'TERMLIFE','MEDIUM'),
(2,6697,'TERMLIFE','MEDIUM'),
(3,6697,'HEALTH','MEDIUM'),
(4,6698,'TERMLIFE','MEDIUM'),
(5,6698,'HEALTH','MEDIUM'),
(6,6697,'TERMLIFE','LOW'),
(7,6697,'HEALTH','LOW'),
(8,6656,'TERMLIFE','HIGH'),
(9,6697,'ENDOWMENT','HIGH'),
(10,4084,'ENDOWMENT','HIGH'),
(11,3052,'HEALTH','HIGH'),
(12,4146,'HEALTH','LOW'),
(13,4112,'ENDOWMENT','LOW'),
(14,4112,'TERMLIFE','MEDIUM');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
