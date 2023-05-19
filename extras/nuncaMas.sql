-- MariaDB dump 10.19  Distrib 10.6.12-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: NuncaMas
-- ------------------------------------------------------
-- Server version	10.6.12-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contacto`
--

DROP TABLE IF EXISTS `contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacto` (
  `idContacto` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idContacto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto`
--

LOCK TABLES `contacto` WRITE;
/*!40000 ALTER TABLE `contacto` DISABLE KEYS */;
INSERT INTO `contacto` VALUES (1,'Oscar','Flores','8186855951','oscar.floresl@udem.edu');
/*!40000 ALTER TABLE `contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contactoOrg`
--

DROP TABLE IF EXISTS `contactoOrg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contactoOrg` (
  `idContacto` int(11) NOT NULL,
  `idOrganizacion` int(11) NOT NULL,
  `rol` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idContacto`,`idOrganizacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contactoOrg`
--

LOCK TABLES `contactoOrg` WRITE;
/*!40000 ALTER TABLE `contactoOrg` DISABLE KEYS */;
INSERT INTO `contactoOrg` VALUES (1,1,'Administrador');
/*!40000 ALTER TABLE `contactoOrg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgViolencia`
--

DROP TABLE IF EXISTS `orgViolencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orgViolencia` (
  `idOrg` int(11) NOT NULL,
  `idViolencia` int(11) NOT NULL,
  PRIMARY KEY (`idOrg`,`idViolencia`),
  KEY `idViolencia` (`idViolencia`),
  CONSTRAINT `orgViolencia_ibfk_1` FOREIGN KEY (`idOrg`) REFERENCES `organizacion` (`idOrganizacion`),
  CONSTRAINT `orgViolencia_ibfk_2` FOREIGN KEY (`idViolencia`) REFERENCES `tiposViolencia` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgViolencia`
--

LOCK TABLES `orgViolencia` WRITE;
/*!40000 ALTER TABLE `orgViolencia` DISABLE KEYS */;
INSERT INTO `orgViolencia` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `orgViolencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organizacion`
--

DROP TABLE IF EXISTS `organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organizacion` (
  `idOrganizacion` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `descripcion` varchar(1000) DEFAULT NULL,
  `ubicacion` varchar(200) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `sitio` varchar(80) DEFAULT NULL,
  `logo` varchar(50) DEFAULT NULL,
  `nivelEmergencia` int(11) DEFAULT NULL,
  PRIMARY KEY (`idOrganizacion`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizacion`
--

LOCK TABLES `organizacion` WRITE;
/*!40000 ALTER TABLE `organizacion` DISABLE KEYS */;
INSERT INTO `organizacion` VALUES (1,'Inmujeres Instituto Nacional de las Mujeres','Informativa','El Instituto Nacional de las Mujeres Inmujeres es una institución gubernamental, a nivel federal, que trabaja para crear una cultura de igualdad libre de violencia y discriminación capaz de propiciar el desarrollo integral de todas las mujeres mexicanas. Somos la institución encargada de coordinar la política nacional de igualdad entre mujeres y hombres.',NULL,'5553226030',' contacto@inmujeres.gob.mx','gob.mx/inmujeres','INMUJERES.jpeg',1),(2,'CONAVIM - Comisión Nacional para Prevenir y Erradicar la Violencia contra las Mujeres ','Informativa','CONAVIM es una institución perteneciente a la Secretaría de la Gobernación de México, creada con el principal propósito de promover la cultura de respeto a los derechos humanos de las mujeres, así como la erradicación de la violencia hacia ellas.',NULL,'5552098907','conavim@segob.gob.mx','gob.mx/conavim','conavim.png',2),(3,'Consejo Nacional Para Prevenir la Discriminación Conapred','Informativa','El Consejo Nacional para Prevenir La Discriminación, CONAPRED, es un órgano de Estado creado por la Ley Federal para Prevenir y Eliminar la Discriminación (LFPED). El Consejo es la institución rectora para promover políticas y medidas tendientes a contribuir al desarrollo cultural y social y avanzar en la inclusión social y garantizar el derecho a la igualdad, que es el primero de los derechos fundamentales en la Constitución Federal.\n',NULL,'5552621490','quejas@conapred.org.mx','conapred.org.mx','CONAPRED.png',1),(4,'Fundación Por Tí Mujer','Informativa','Tiene como objeto el apoyo a los grupos más vulnerables de nuestro país mujeres, niños, niñas , adolecentes, adultos mayores indígenas y migrantes en estado de abandono y situación de violencia mediante acciones humanitarias y legales. ',NULL,'5536051329','info@portimujer.org\n','portimujer.org','fundacionPorTiMujer.jpeg',2),(5,'Agenda Cero','Ayuda de emergencia','Actualmente se enfocan en la atención de casos de violencia de género para mujeres adultas. El equipo está preparado en intervención en crisis, emergencias psicológicas en casos de violencia, atención a distancia con perspectiva de género y son especialistas en casos de cualquier tipo de violencia',NULL,'5574326061','ayudaenlinea@agendacero.org','agendacero.org','AgendaCero.png',3),(6,'Corazones Magicos','Ayuda de emergencia','Corazones Mágicos es un programa de Fundación Vida Plena IAP, especializado en la atención de la violencia sexual infantil, a través de 4 líneas de acción: la prevención, la rehabilitación, la capacitación y la incidencia en políticas públicas.',NULL,'4422236844\n','orazonesmagicos@gmail.com','corazonesmagicos.org','CorazonesMagicos.png',2),(7,'FUNDACIÓN ORIGEN ','Ayuda de emergencia','Somos una institución pionera y referente a nivel nacional e internacional en la atención integral, diálogo y escucha con las mujeres. Destacamos por nuestras metodologías innovadoras que generan impactos positivos y cambios de valor social en la atención integral de mujeres que sufren violencia, pobreza o vulnerabilidad. ',NULL,'018000151617\n','contacto@origenac.org','origenac.org','fundacionOrigen.jpeg',3),(19,'BORRAR','','',NULL,'','','','',NULL),(20,'Borrar','','',NULL,'','','','',NULL);
/*!40000 ALTER TABLE `organizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiposViolencia`
--

DROP TABLE IF EXISTS `tiposViolencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tiposViolencia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiposViolencia`
--

LOCK TABLES `tiposViolencia` WRITE;
/*!40000 ALTER TABLE `tiposViolencia` DISABLE KEYS */;
INSERT INTO `tiposViolencia` VALUES (1,'Psicológica'),(2,'Física'),(3,'Sexual'),(4,'Financiera'),(5,'Emocional'),(6,'Honor');
/*!40000 ALTER TABLE `tiposViolencia` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
INSERT INTO `admin` VALUES (1,'nuncaMas', '12345'),(2,'sysadmin', '12345');
UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-12 14:06:12
