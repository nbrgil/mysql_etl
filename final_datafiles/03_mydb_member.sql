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
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `login` varchar(45) NOT NULL,
  `enable` int(11) NOT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (556900,'Carlos','carlosjoao@gmail.com',1,'João'),(566310,'Canal','canal@labs.moip.com.br',1,'Moip'),(628952,'canal','manchacanal@hotmail.com',1,'da mancha'),(963347,'Feira','feira.amb@gmail.com',1,'Ambulante'),(1005890,'Débora','debora_marinho@gmail.com',1,'Marinho'),(1005925,'fabricio','fabricio.rosa.silva@gmail.com',1,'Rosa da Silva'),(1122832,'Ótica maria','atendimento@oticamaria.com.br',1,NULL),(1122838,'José Antônio','antonio.teixeira@gmail.com',1,'Teixeira'),(1122850,'Sayonara','sayonaraalphaville@gmail.com',1,'Alphaville'),(1122851,'integracao','integracao@labs.moip.com.br',1,'Moip'),(1122856,'fernando.lima','fernando.lima.andrade@gmail.com',1,'ANDRADE'),(1219160,'Maria Clara','maria_clara_ezequiel_molina@gmail.com',1,'Ezequiel Molina'),(1219405,'Leonardo','leonardosoares@gmail.com',1,'SOARES DE ARARIPE'),(1223434,'george','georgecoelhosantana@gmail.com',1,'coelho de santana'),(1284745,'Zezé','zezé_vitorino@gmail.com',1,'Vitorino'),(1296362,'Ayrton','ayrton_bragança@gmail.com',1,'bragança'),(1306620,'julia1996','julia1996_magalhães@gmail.com',1,'Magalhães'),(1342482,'gabriella','gabriella_matos_fiamenghi@gmail.com',1,'Matos Diaz Fiamenghi'),(1707068,'Clayton','clayton_kilpp@gmail.com',1,'Kilpp'),(2509974,'viviane','viviane_nigri@gmail.com',1,'Nigri'),(2533053,'Luciana','luciana_santos@gmail.com',1,'Santos'),(2573076,'Aparecida','aparecidamariaoliveira silva@gmail.com',1,'Maria de Oliveira Silva'),(2586897,'Kaliana','kaliana_sabino@gmail.com',1,'Sabino'),(2605374,'Antônio','antônio_galahardsilva@gmail.com',1,'galahardsilva'),(2660265,'Daviluiz','daviluiz_bandeira_alencar@gmail.com',1,'bandeira alencar'),(2697201,'Heitor','heitor_rezende@gmail.com',1,'rezende'),(2781310,'Rian','rian_@gmail.com',1,'de paula'),(2921679,'Maria de Fátima','maria_teves@gmail.com',1,'Teves'),(2921801,'Cecília','cecilia_amorim@gmail.com',1,'Amorim'),(2987164,'Márcio','marciopinotti@gmail.com',1,'Pinotti'),(3048157,'fabio','fabio_santossilva@gmail.com',1,'santos silva'),(3049112,'palo','palo_sgorlon_tironi@gmail.com',1,'SGORLON TIRONI'),(3049226,'SOraia','soraia_farias@gmail.com',1,'Farias'),(3050509,'Joelma','joelma_santos@gmail.com',1,'Santos'),(3052457,'Ricardo','ricardo_edyane.maria@gmail.com',1,'edyane.maria'),(3052731,'JOAQUIM','joaquim_melo@gmail.com',1,'MELO ARAUJO'),(3052773,'Patrícia','patrícia_ruiz@gmail.com',1,'Ruiz'),(3053886,'juliano','juliano_melo@gmail.com',1,'Melo'),(3056311,'feitocomcarinho','feitocomcarinho_oncelos@gmail.com',1,'oncelos'),(3060942,'matheus','matheus_joselmaekaua13@gmail.com',1,'joselmaekaua13'),(3061403,'max','max_matthaus@gmail.com',1,'Ane Matthaus'),(3061404,'anaclara','anaclara_silva@gmail.com',1,'Silva Da Silva'),(3061405,'Antônio','antônio_fernandesmenezes@gmail.com',1,'Fernandes Menezes'),(3061406,'Clarice','clarice_ribeiro@gmail.com',1,'Ribeiro'),(3061407,'Mariana','mariana_dejesus_santos@gmail.com',1,'de jesus santos'),(3061408,'Fernanda','fernanda_silva@gmail.com',1,'Silva'),(3061409,'Maria','maria_sausmikat@gmail.com',1,'sausmikat'),(3061410,'João','joão_laham_silva@gmail.com',1,'Laham Silva'),(3061411,'Ana','ana_oliveira@gmail.com',1,'Oliveira');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
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
