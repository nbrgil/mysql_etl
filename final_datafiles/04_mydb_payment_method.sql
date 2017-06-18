-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `payment_method`
--

DROP TABLE IF EXISTS `payment_method`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment_method` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `maximum_installments` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_method`
--

LOCK TABLES `payment_method` WRITE;
/*!40000 ALTER TABLE `payment_method` DISABLE KEYS */;
INSERT INTO `payment_method` VALUES (1,'MoIP',1),(2,'MoIP',1),(3,'Cartao de Credito',12),(4,'Cartao de Debito',1),(5,'Cartao de Credito',12),(6,'Cartao de Credito',12),(7,'Cartao de Credito',12),(8,'Transferencia',1),(9,'Boleto',1),(10,'Financiamento',1),(11,'Saque',1),(12,'Financiamento',1),(13,'Transferencia',1),(14,'Boleto',1),(15,'Cartao de Debito',6),(16,'Saque',1),(17,'Financiamento',1),(18,'Transferencia',1),(19,'Cartao de Debito',6),(20,'Boleto',1),(21,'Financiamento',1),(22,'Transferencia',1),(23,'Cartao de Debito',6),(24,'Boleto',1),(25,'Saque',1),(26,'Financiamento',1),(27,'Transferencia',1),(28,'Cartao de Debito',1),(29,'Cartao de Debito',6),(30,'Boleto',1),(31,'Financiamento',1),(32,'Transferencia',1),(33,'Cartao de Debito',1),(34,'Cartao de Credito',6),(35,'Boleto',1),(36,'Saque',1),(37,'Cartao de Credito',10),(38,'Cartao de Debito',1),(39,'Saque',1),(40,'Saque',1),(41,'Saque',1),(42,'Saque',1),(43,'Saque',1),(44,'Saque',1),(45,'Saque',1),(46,'Saque',1),(47,'Saque',1),(48,'Saque',1),(49,'Saque',1),(50,'Saque',1),(51,'Saque',1),(52,'Saque',1),(53,'Saque',1),(54,'Saque',1),(55,'Saque',1),(56,'Saque',1),(57,'Cartao de Credito',12),(58,'MoIP',1),(59,'Saque',1),(60,'Saque',1),(61,'Saque',1),(62,'Saque',1),(63,'Saque',1),(64,'Saque',1),(65,'Saque',1),(66,'Saque',1),(67,'Saque',1),(68,'Saque',1),(69,'Saque',1),(70,'Saque',1),(71,'Saque',1),(72,'Saque',1),(73,'Boleto',1),(74,'Cartao de Credito',12),(75,'Cartao de Credito',12),(76,'Cartao de Credito',1),(77,'Boleto',1),(78,'Debito Automatico',1),(79,'Debito Automatico',1),(80,'Debito Automatico',1),(81,'Debito Automatico',1),(82,'Cartao de Credito',12),(83,'Transferencia',1),(84,'Debito Automatico',1),(85,'Debito Automatico',1),(86,'Debito Automatico',1),(87,'Debito Automatico',1),(88,'Saque',1),(89,'Saque',1),(90,'Saque',1),(91,'Boleto',1),(92,'Saque',1),(93,'Cartao de Credito',12),(94,'Cartao de Credito',12),(101,'Boleto',1),(103,'Cartao de Credito - MPOS',12),(104,'Cartao de Debito - MPOS',1),(105,'Cartao de Credito - MPOS',12),(106,'Cartao de Debito - MPOS',1),(107,'Saque',1),(108,'Saque',1),(109,'Cartao de Credito - MPOS',12),(110,'Saque',1),(111,'Cartao de Credito',12);
/*!40000 ALTER TABLE `payment_method` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-18 19:30:05
