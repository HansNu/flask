-- MariaDB dump 10.19  Distrib 10.6.12-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: nuncaMas
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
/*!40000 ALTER TABLE `contactoOrg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organizacion`
--

DROP TABLE IF EXISTS `organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organizacion` (
  `idOrganizacion` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` varchar(1000) DEFAULT NULL,
  `ubicacion` varchar(200) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `sitio` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`idOrganizacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizacion`
--

LOCK TABLES `organizacion` WRITE;
/*!40000 ALTER TABLE `organizacion` DISABLE KEYS */;
INSERT INTO `organizacion` VALUES (1,'Inmujeres Instituto Nacional de las Mujeres','El Instituto Nacional de las Mujeres Inmujeres es una institución gubernamental, a nivel federal, que trabaja para crear una cultura de igualdad libre de violencia y discriminación capaz de propiciar el desarrollo integral de todas las mujeres mexicanas. Somos la institución encargada de coordinar la política nacional de igualdad entre mujeres y hombres.',NULL,'55 5322 6030','\n contacto@inmujeres.gob.mx','gob.mx/inmujeres'),(2,'CONAVIM - Comisión Nacional para Prevenir y Erradicar la Violencia contra las Mujeres ','CONAVIM es una institución perteneciente a la Secretaría de la Gobernación de México, creada con el principal propósito de promover la cultura de respeto a los derechos humanos de las mujeres, así como la erradicación de la violencia hacia ellas.',NULL,'55 5209 8907','conavim@segob.gob.mx','gob.mx/conavim'),(3,'Consejo Nacional Para Prevenir la Discriminación Conapred','El Consejo Nacional para Prevenir La Discriminación, CONAPRED, es un órgano de Estado creado por la Ley Federal para Prevenir y Eliminar la Discriminación (LFPED). El Consejo es la institución rectora para promover políticas y medidas tendientes a contribuir al desarrollo cultural y social y avanzar en la inclusión social y garantizar el derecho a la igualdad, que es el primero de los derechos fundamentales en la Constitución Federal.\n',NULL,'55 5262 1490','quejas@conapred.org.mx','conapred.org.mx'),(4,'Fundación Por Tí Mujer','Tiene como objeto el apoyo a los grupos más vulnerables de nuestro país mujeres, niños, niñas , adolecentes, adultos mayores indígenas y migrantes en estado de abandono y situación de violencia mediante acciones humanitarias y legales. ',NULL,'55 3605 1329','info@portimujer.org\n','portimujer.org'),(5,'Agenda Cero','Actualmente se enfocan en la atención de casos de violencia de género para mujeres adultas. El equipo está preparado en intervención en crisis, emergencias psicológicas en casos de violencia, atención a distancia con perspectiva de género y son especialistas en casos de cualquier tipo de violencia',NULL,'55 7432 6061','ayudaenlinea@agendacero.org','agendacero.org'),(6,'Corazones Magicos','Corazones Mágicos es un programa de Fundación Vida Plena IAP, especializado en la atención de la violencia sexual infantil, a través de 4 líneas de acción: la prevención, la rehabilitación, la capacitación y la incidencia en políticas públicas.',NULL,'44 2223 6844\n','orazonesmagicos@gmail.com','corazonesmagicos.org'),(7,'FUNDACIÓN ORIGEN ','Somos una institución pionera y referente a nivel nacional e internacional en la atención integral, diálogo y escucha con las mujeres. Destacamos por nuestras metodologías innovadoras que generan impactos positivos y cambios de valor social en la atención integral de mujeres que sufren violencia, pobreza o vulnerabilidad. ',NULL,'01800 01 51 617\n','contacto@origenac.org','origenac.org');
/*!40000 ALTER TABLE `organizacion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-09 23:33:46
