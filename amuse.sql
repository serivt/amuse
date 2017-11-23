-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: 0.0.0.0    Database: amuse
-- ------------------------------------------------------
-- Server version	5.5.58

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add grupo',7,'add_grupo'),(20,'Can change grupo',7,'change_grupo'),(21,'Can delete grupo',7,'delete_grupo'),(22,'Puede ver grupos',7,'view_grupo'),(23,'Can add pago',8,'add_pago'),(24,'Can change pago',8,'change_pago'),(25,'Can delete pago',8,'delete_pago'),(26,'Puede ver pagos',8,'view_pago'),(27,'Can add categoria',9,'add_categoria'),(28,'Can change categoria',9,'change_categoria'),(29,'Can delete categoria',9,'delete_categoria'),(30,'Puede ver categorias',9,'view_categoria'),(31,'Can add persona',10,'add_persona'),(32,'Can change persona',10,'change_persona'),(33,'Can delete persona',10,'delete_persona'),(34,'Puede ver personas',10,'view_persona'),(35,'Can add rol',11,'add_rol'),(36,'Can change rol',11,'change_rol'),(37,'Can delete rol',11,'delete_rol'),(38,'Puede ver roles',11,'view_rol'),(39,'Can add tarea',12,'add_tarea'),(40,'Can change tarea',12,'change_tarea'),(41,'Can delete tarea',12,'delete_tarea'),(42,'Puede ver tareas',12,'view_tarea'),(43,'Can add habilidad',13,'add_habilidad'),(44,'Can change habilidad',13,'change_habilidad'),(45,'Can delete habilidad',13,'delete_habilidad'),(46,'Can add personaje',14,'add_personaje'),(47,'Can change personaje',14,'change_personaje'),(48,'Can delete personaje',14,'delete_personaje'),(49,'Puede ver personajes',14,'view_personaje'),(50,'Can add proyecto',15,'add_proyecto'),(51,'Can change proyecto',15,'change_proyecto'),(52,'Can delete proyecto',15,'delete_proyecto'),(53,'Puede ver proyectos',15,'view_proyecto');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(5,'contenttypes','contenttype'),(9,'grupos','categoria'),(7,'grupos','grupo'),(8,'grupos','pago'),(13,'personas','habilidad'),(10,'personas','persona'),(11,'personas','rol'),(12,'personas','tarea'),(14,'proyectos','personaje'),(15,'proyectos','proyecto'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-11-23 01:01:07'),(2,'auth','0001_initial','2017-11-23 01:01:08'),(3,'admin','0001_initial','2017-11-23 01:01:08'),(4,'admin','0002_logentry_remove_auto_add','2017-11-23 01:01:08'),(5,'contenttypes','0002_remove_content_type_name','2017-11-23 01:01:08'),(6,'auth','0002_alter_permission_name_max_length','2017-11-23 01:01:08'),(7,'auth','0003_alter_user_email_max_length','2017-11-23 01:01:08'),(8,'auth','0004_alter_user_username_opts','2017-11-23 01:01:08'),(9,'auth','0005_alter_user_last_login_null','2017-11-23 01:01:08'),(10,'auth','0006_require_contenttypes_0002','2017-11-23 01:01:08'),(11,'auth','0007_alter_validators_add_error_messages','2017-11-23 01:01:08'),(12,'auth','0008_alter_user_username_max_length','2017-11-23 01:01:08'),(13,'grupos','0001_initial','2017-11-23 01:01:08'),(14,'grupos','0002_auto_20171104_2304','2017-11-23 01:01:08'),(15,'personas','0001_initial','2017-11-23 01:01:08'),(16,'personas','0002_auto_20171105_0000','2017-11-23 01:01:08'),(17,'personas','0003_auto_20171105_0219','2017-11-23 01:01:08'),(18,'personas','0004_auto_20171105_0226','2017-11-23 01:01:08'),(19,'personas','0005_auto_20171105_0340','2017-11-23 01:01:08'),(20,'personas','0006_rol_estado','2017-11-23 01:01:08'),(21,'personas','0007_remove_persona_grupos_dirige','2017-11-23 01:01:08'),(22,'grupos','0003_pago','2017-11-23 01:01:08'),(23,'grupos','0004_pago_estado','2017-11-23 01:01:08'),(24,'grupos','0005_auto_20171108_1121','2017-11-23 01:01:08'),(25,'grupos','0006_auto_20171108_1121','2017-11-23 01:01:08'),(26,'grupos','0007_grupo_estudiantes','2017-11-23 01:01:08'),(27,'grupos','0008_auto_20171108_1129','2017-11-23 01:01:08'),(28,'grupos','0009_auto_20171113_1525','2017-11-23 01:01:08'),(29,'grupos','0010_auto_20171114_2150','2017-11-23 01:01:09'),(30,'grupos','0011_auto_20171119_1559','2017-11-23 01:01:09'),(31,'personas','0008_auto_20171113_1525','2017-11-23 01:01:09'),(32,'personas','0009_persona_tipo_persona','2017-11-23 01:01:09'),(33,'personas','0010_auto_20171114_2150','2017-11-23 01:01:09'),(34,'personas','0011_auto_20171119_1559','2017-11-23 01:01:09'),(35,'personas','0012_auto_20171120_0248','2017-11-23 01:01:09'),(36,'personas','0013_tarea','2017-11-23 01:01:09'),(37,'personas','0014_auto_20171122_0144','2017-11-23 01:01:09'),(38,'proyectos','0001_initial','2017-11-23 01:01:09'),(39,'proyectos','0002_auto_20171113_1632','2017-11-23 01:01:09'),(40,'proyectos','0003_personaje_estado','2017-11-23 01:01:09'),(41,'proyectos','0004_auto_20171114_2150','2017-11-23 01:01:09'),(42,'proyectos','0005_auto_20171119_1559','2017-11-23 01:01:09'),(43,'sessions','0001_initial','2017-11-23 01:01:09');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupos_categoria`
--

DROP TABLE IF EXISTS `grupos_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupos_categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` longtext,
  `valor_cuota` double NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos_categoria`
--

LOCK TABLES `grupos_categoria` WRITE;
/*!40000 ALTER TABLE `grupos_categoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupos_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupos_grupo`
--

DROP TABLE IF EXISTS `grupos_grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupos_grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` longtext,
  `estado` tinyint(1) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `fecha_inactivacion` datetime DEFAULT NULL,
  `categoria_id` int(11) NOT NULL,
  `director_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grupos_grupo_categoria_id_6d8bdfba_fk_grupos_categoria_id` (`categoria_id`),
  KEY `grupos_grupo_director_id_a0e11886_fk_personas_persona_id` (`director_id`),
  CONSTRAINT `grupos_grupo_director_id_a0e11886_fk_personas_persona_id` FOREIGN KEY (`director_id`) REFERENCES `personas_persona` (`id`),
  CONSTRAINT `grupos_grupo_categoria_id_6d8bdfba_fk_grupos_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `grupos_categoria` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos_grupo`
--

LOCK TABLES `grupos_grupo` WRITE;
/*!40000 ALTER TABLE `grupos_grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupos_grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupos_grupo_estudiantes`
--

DROP TABLE IF EXISTS `grupos_grupo_estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupos_grupo_estudiantes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grupo_id` int(11) NOT NULL,
  `persona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `grupos_grupo_estudiantes_grupo_id_persona_id_f360fdc0_uniq` (`grupo_id`,`persona_id`),
  KEY `grupos_grupo_estudia_persona_id_bc8deaaa_fk_personas_` (`persona_id`),
  CONSTRAINT `grupos_grupo_estudiantes_grupo_id_c300338b_fk_grupos_grupo_id` FOREIGN KEY (`grupo_id`) REFERENCES `grupos_grupo` (`id`),
  CONSTRAINT `grupos_grupo_estudia_persona_id_bc8deaaa_fk_personas_` FOREIGN KEY (`persona_id`) REFERENCES `personas_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos_grupo_estudiantes`
--

LOCK TABLES `grupos_grupo_estudiantes` WRITE;
/*!40000 ALTER TABLE `grupos_grupo_estudiantes` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupos_grupo_estudiantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupos_pago`
--

DROP TABLE IF EXISTS `grupos_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupos_pago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `valor_pago` double NOT NULL,
  `alerta_pago` tinyint(1) NOT NULL,
  `grupo_id` int(11) NOT NULL,
  `persona_id` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grupos_pago_grupo_id_43f16df2_fk_grupos_grupo_id` (`grupo_id`),
  KEY `grupos_pago_persona_id_99799f72_fk_personas_persona_id` (`persona_id`),
  CONSTRAINT `grupos_pago_persona_id_99799f72_fk_personas_persona_id` FOREIGN KEY (`persona_id`) REFERENCES `personas_persona` (`id`),
  CONSTRAINT `grupos_pago_grupo_id_43f16df2_fk_grupos_grupo_id` FOREIGN KEY (`grupo_id`) REFERENCES `grupos_grupo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos_pago`
--

LOCK TABLES `grupos_pago` WRITE;
/*!40000 ALTER TABLE `grupos_pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupos_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_habilidad`
--

DROP TABLE IF EXISTS `personas_habilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_habilidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_habilidad`
--

LOCK TABLES `personas_habilidad` WRITE;
/*!40000 ALTER TABLE `personas_habilidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_habilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_persona`
--

DROP TABLE IF EXISTS `personas_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_persona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `primer_nombre` varchar(255) NOT NULL,
  `segundo_nombre` varchar(255) DEFAULT NULL,
  `primer_apellido` varchar(255) NOT NULL,
  `segundo_apellido` varchar(255) DEFAULT NULL,
  `correo` varchar(50) NOT NULL,
  `tipo_identificacion` smallint(6) DEFAULT NULL,
  `numero_identificacion` varchar(50) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `rh` smallint(6) DEFAULT NULL,
  `eps` varchar(50) DEFAULT NULL,
  `imagen_perfil` varchar(100) DEFAULT NULL,
  `telefono` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `tipo_persona` smallint(6) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `correo` (`correo`),
  UNIQUE KEY `numero_identificacion` (`numero_identificacion`),
  KEY `personas_persona_usuario_id_757630d6_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `personas_persona_usuario_id_757630d6_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_persona`
--

LOCK TABLES `personas_persona` WRITE;
/*!40000 ALTER TABLE `personas_persona` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_persona_acudiente`
--

DROP TABLE IF EXISTS `personas_persona_acudiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_persona_acudiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_persona_id` int(11) NOT NULL,
  `to_persona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personas_persona_acudien_from_persona_id_to_perso_ce93721d_uniq` (`from_persona_id`,`to_persona_id`),
  KEY `personas_persona_acu_to_persona_id_719389b4_fk_personas_` (`to_persona_id`),
  CONSTRAINT `personas_persona_acu_to_persona_id_719389b4_fk_personas_` FOREIGN KEY (`to_persona_id`) REFERENCES `personas_persona` (`id`),
  CONSTRAINT `personas_persona_acu_from_persona_id_032429aa_fk_personas_` FOREIGN KEY (`from_persona_id`) REFERENCES `personas_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_persona_acudiente`
--

LOCK TABLES `personas_persona_acudiente` WRITE;
/*!40000 ALTER TABLE `personas_persona_acudiente` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_persona_acudiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_persona_habilidades`
--

DROP TABLE IF EXISTS `personas_persona_habilidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_persona_habilidades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `persona_id` int(11) NOT NULL,
  `habilidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personas_persona_habilid_persona_id_habilidad_id_ee377b29_uniq` (`persona_id`,`habilidad_id`),
  KEY `personas_persona_hab_habilidad_id_3d86f350_fk_personas_` (`habilidad_id`),
  CONSTRAINT `personas_persona_hab_habilidad_id_3d86f350_fk_personas_` FOREIGN KEY (`habilidad_id`) REFERENCES `personas_habilidad` (`id`),
  CONSTRAINT `personas_persona_hab_persona_id_66dd3b9e_fk_personas_` FOREIGN KEY (`persona_id`) REFERENCES `personas_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_persona_habilidades`
--

LOCK TABLES `personas_persona_habilidades` WRITE;
/*!40000 ALTER TABLE `personas_persona_habilidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_persona_habilidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_persona_roles`
--

DROP TABLE IF EXISTS `personas_persona_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_persona_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `persona_id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personas_persona_roles_persona_id_rol_id_3a9d7b9f_uniq` (`persona_id`,`rol_id`),
  KEY `personas_persona_roles_rol_id_26f047de_fk_personas_rol_id` (`rol_id`),
  CONSTRAINT `personas_persona_roles_rol_id_26f047de_fk_personas_rol_id` FOREIGN KEY (`rol_id`) REFERENCES `personas_rol` (`id`),
  CONSTRAINT `personas_persona_rol_persona_id_54b977ee_fk_personas_` FOREIGN KEY (`persona_id`) REFERENCES `personas_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_persona_roles`
--

LOCK TABLES `personas_persona_roles` WRITE;
/*!40000 ALTER TABLE `personas_persona_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_persona_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_rol`
--

DROP TABLE IF EXISTS `personas_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_rol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` longtext,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_rol`
--

LOCK TABLES `personas_rol` WRITE;
/*!40000 ALTER TABLE `personas_rol` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_tarea`
--

DROP TABLE IF EXISTS `personas_tarea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_tarea` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `fecha_limite` date NOT NULL,
  `estado` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_tarea`
--

LOCK TABLES `personas_tarea` WRITE;
/*!40000 ALTER TABLE `personas_tarea` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_tarea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_tarea_grupos_responsable`
--

DROP TABLE IF EXISTS `personas_tarea_grupos_responsable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_tarea_grupos_responsable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tarea_id` int(11) NOT NULL,
  `grupo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personas_tarea_grupos_re_tarea_id_grupo_id_a83a1c4a_uniq` (`tarea_id`,`grupo_id`),
  KEY `personas_tarea_grupo_grupo_id_d624b190_fk_grupos_gr` (`grupo_id`),
  CONSTRAINT `personas_tarea_grupo_grupo_id_d624b190_fk_grupos_gr` FOREIGN KEY (`grupo_id`) REFERENCES `grupos_grupo` (`id`),
  CONSTRAINT `personas_tarea_grupo_tarea_id_96df5c06_fk_personas_` FOREIGN KEY (`tarea_id`) REFERENCES `personas_tarea` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_tarea_grupos_responsable`
--

LOCK TABLES `personas_tarea_grupos_responsable` WRITE;
/*!40000 ALTER TABLE `personas_tarea_grupos_responsable` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_tarea_grupos_responsable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_tarea_persona_responsable`
--

DROP TABLE IF EXISTS `personas_tarea_persona_responsable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas_tarea_persona_responsable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tarea_id` int(11) NOT NULL,
  `persona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personas_tarea_persona_r_tarea_id_persona_id_65e0dec0_uniq` (`tarea_id`,`persona_id`),
  KEY `personas_tarea_perso_persona_id_031781cb_fk_personas_` (`persona_id`),
  CONSTRAINT `personas_tarea_perso_persona_id_031781cb_fk_personas_` FOREIGN KEY (`persona_id`) REFERENCES `personas_persona` (`id`),
  CONSTRAINT `personas_tarea_perso_tarea_id_5fce5c40_fk_personas_` FOREIGN KEY (`tarea_id`) REFERENCES `personas_tarea` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_tarea_persona_responsable`
--

LOCK TABLES `personas_tarea_persona_responsable` WRITE;
/*!40000 ALTER TABLE `personas_tarea_persona_responsable` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_tarea_persona_responsable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectos_personaje`
--

DROP TABLE IF EXISTS `proyectos_personaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proyectos_personaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `proyecto_id` int(11) NOT NULL,
  `descripcion` longtext,
  `persona_id` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `proyectos_personaje_proyecto_id_3cbded62_fk_proyectos` (`proyecto_id`),
  KEY `proyectos_personaje_persona_id_5bff90b9_fk_personas_persona_id` (`persona_id`),
  CONSTRAINT `proyectos_personaje_persona_id_5bff90b9_fk_personas_persona_id` FOREIGN KEY (`persona_id`) REFERENCES `personas_persona` (`id`),
  CONSTRAINT `proyectos_personaje_proyecto_id_3cbded62_fk_proyectos` FOREIGN KEY (`proyecto_id`) REFERENCES `proyectos_proyecto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectos_personaje`
--

LOCK TABLES `proyectos_personaje` WRITE;
/*!40000 ALTER TABLE `proyectos_personaje` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyectos_personaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectos_proyecto`
--

DROP TABLE IF EXISTS `proyectos_proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proyectos_proyecto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` longtext,
  `fecha_creacion` date NOT NULL,
  `fecha_interpretacion` date NOT NULL,
  `valor_boleta` double NOT NULL,
  `lugar` varchar(512) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  `director_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `proyectos_proyecto_director_id_4ed0799b_fk_personas_persona_id` (`director_id`),
  CONSTRAINT `proyectos_proyecto_director_id_4ed0799b_fk_personas_persona_id` FOREIGN KEY (`director_id`) REFERENCES `personas_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectos_proyecto`
--

LOCK TABLES `proyectos_proyecto` WRITE;
/*!40000 ALTER TABLE `proyectos_proyecto` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyectos_proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectos_proyecto_grupos`
--

DROP TABLE IF EXISTS `proyectos_proyecto_grupos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proyectos_proyecto_grupos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proyecto_id` int(11) NOT NULL,
  `grupo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `proyectos_proyecto_grupos_proyecto_id_grupo_id_715230a2_uniq` (`proyecto_id`,`grupo_id`),
  KEY `proyectos_proyecto_grupos_grupo_id_011c66ac_fk_grupos_grupo_id` (`grupo_id`),
  CONSTRAINT `proyectos_proyecto_grupos_grupo_id_011c66ac_fk_grupos_grupo_id` FOREIGN KEY (`grupo_id`) REFERENCES `grupos_grupo` (`id`),
  CONSTRAINT `proyectos_proyecto_g_proyecto_id_71f15dd0_fk_proyectos` FOREIGN KEY (`proyecto_id`) REFERENCES `proyectos_proyecto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectos_proyecto_grupos`
--

LOCK TABLES `proyectos_proyecto_grupos` WRITE;
/*!40000 ALTER TABLE `proyectos_proyecto_grupos` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyectos_proyecto_grupos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-23  1:04:24
