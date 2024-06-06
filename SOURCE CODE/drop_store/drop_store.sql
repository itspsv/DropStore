-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 12, 2022 at 01:48 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drop_store`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add userdetails model', 7, 'add_userdetailsmodel'),
(26, 'Can change userdetails model', 7, 'change_userdetailsmodel'),
(27, 'Can delete userdetails model', 7, 'delete_userdetailsmodel'),
(28, 'Can view userdetails model', 7, 'view_userdetailsmodel'),
(29, 'Can add device model', 8, 'add_devicemodel'),
(30, 'Can change device model', 8, 'change_devicemodel'),
(31, 'Can delete device model', 8, 'delete_devicemodel'),
(32, 'Can view device model', 8, 'view_devicemodel'),
(33, 'Can add file model', 9, 'add_filemodel'),
(34, 'Can change file model', 9, 'change_filemodel'),
(35, 'Can delete file model', 9, 'delete_filemodel'),
(36, 'Can view file model', 9, 'view_filemodel');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `device_details`
--

DROP TABLE IF EXISTS `device_details`;
CREATE TABLE IF NOT EXISTS `device_details` (
  `device_id` int(11) NOT NULL AUTO_INCREMENT,
  `device-type` varchar(200) NOT NULL,
  `device-name` varchar(200) NOT NULL,
  `device-ip` varchar(200) NOT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `device_user_id` int(11) DEFAULT NULL,
  `device-status` varchar(200) DEFAULT NULL,
  `device-node` varchar(100) DEFAULT NULL,
  `device-server` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`device_id`),
  KEY `device_details_device_user_id_9f08fe75` (`device_user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `device_details`
--

INSERT INTO `device_details` (`device_id`, `device-type`, `device-name`, `device-ip`, `datetime_created`, `device_user_id`, `device-status`, `device-node`, `device-server`) VALUES
(21, 'mobile', 'iphone 14', '12a1daad', '2022-11-12 13:06:31.107636', 1, 'accepted', 'Asia', 'Europe (Frankfurt)'),
(22, 'laptop', 'macbook', '112dasdas', '2022-11-12 13:06:31.110636', 1, 'accepted', 'Asia', 'Europe (Frankfurt)'),
(23, 'mobile', 'samsung', 'sdss1231', '2022-11-08 09:42:03.073488', 2, 'accepted', 'North America', NULL),
(24, 'laptop', 'acer nitro 5', '133wf33', '2022-11-08 09:42:39.077382', 2, 'accepted', 'North America', NULL),
(25, 'tablet', 'ipad', 'sdfe1211', '2022-11-08 13:00:17.038351', 2, 'accepted', 'North America', NULL),
(27, 'camera', 'Sony a900', '192.168.29.157', '2022-11-09 05:45:14.552155', 2, 'accepted', 'North America', NULL),
(32, 'Camera', 'Sony a900', '192.168.29.157.2', '2022-11-12 13:06:31.113634', 1, 'accepted', 'Asia', 'Europe (Frankfurt)');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'mainapp', 'userdetailsmodel'),
(8, 'edge_node', 'devicemodel'),
(9, 'edge_node', 'filemodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'mainapp', '0001_initial', '2022-11-05 08:16:49.021950'),
(2, 'mainapp', '0002_userdetailsmodel_delete_camera_reg_delete_lap_reg_and_more', '2022-11-05 08:16:49.111946'),
(3, 'mainapp', '0003_userdetailsmodel_user_status', '2022-11-05 08:31:28.384689'),
(4, 'contenttypes', '0001_initial', '2022-11-05 09:09:30.848124'),
(5, 'auth', '0001_initial', '2022-11-05 09:09:32.508026'),
(6, 'admin', '0001_initial', '2022-11-05 09:09:32.915052'),
(7, 'admin', '0002_logentry_remove_auto_add', '2022-11-05 09:09:32.937995'),
(8, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-05 09:09:32.960994'),
(9, 'contenttypes', '0002_remove_content_type_name', '2022-11-05 09:09:33.188983'),
(10, 'auth', '0002_alter_permission_name_max_length', '2022-11-05 09:09:33.271978'),
(11, 'auth', '0003_alter_user_email_max_length', '2022-11-05 09:09:33.356972'),
(12, 'auth', '0004_alter_user_username_opts', '2022-11-05 09:09:33.377970'),
(13, 'auth', '0005_alter_user_last_login_null', '2022-11-05 09:09:33.462963'),
(14, 'auth', '0006_require_contenttypes_0002', '2022-11-05 09:09:33.468965'),
(15, 'auth', '0007_alter_validators_add_error_messages', '2022-11-05 09:09:33.489965'),
(16, 'auth', '0008_alter_user_username_max_length', '2022-11-05 09:09:33.580956'),
(17, 'auth', '0009_alter_user_last_name_max_length', '2022-11-05 09:09:33.667954'),
(18, 'auth', '0010_alter_group_name_max_length', '2022-11-05 09:09:33.765947'),
(19, 'auth', '0011_update_proxy_permissions', '2022-11-05 09:09:33.793946'),
(20, 'auth', '0012_alter_user_first_name_max_length', '2022-11-05 09:09:33.933935'),
(21, 'edge_node', '0001_initial', '2022-11-05 09:09:33.988935'),
(22, 'edge_node', '0002_alter_upload_data_file_size', '2022-11-05 09:09:34.076927'),
(23, 'edge_node', '0003_upload_data_file', '2022-11-05 09:09:34.152922'),
(24, 'edge_node', '0004_ip_data_lap_data_tab_data', '2022-11-05 09:09:34.362910'),
(25, 'edge_node', '0005_delete_ip_data_delete_lap_data_delete_tab_data_and_more', '2022-11-05 09:09:34.387937'),
(26, 'sessions', '0001_initial', '2022-11-05 09:09:34.523949'),
(27, 'edge_node', '0006_initial', '2022-11-05 10:17:17.487142'),
(28, 'edge_node', '0007_alter_devicemodel_datetime_created', '2022-11-05 10:37:47.776855'),
(29, 'edge_node', '0008_alter_devicemodel_device_ip_and_more', '2022-11-05 10:46:43.482944'),
(30, 'edge_node', '0009_alter_devicemodel_device_ip_and_more', '2022-11-05 10:55:38.013215'),
(31, 'edge_node', '0010_filemodel', '2022-11-05 11:38:24.490318'),
(32, 'edge_node', '0011_filemodel_file_type', '2022-11-05 11:58:10.762994'),
(33, 'edge_node', '0012_alter_filemodel_file_device', '2022-11-07 06:09:53.527000'),
(34, 'edge_node', '0013_alter_filemodel_file_size', '2022-11-08 09:29:46.161307'),
(35, 'edge_node', '0014_alter_filemodel_file_name', '2022-11-08 09:44:52.065637'),
(36, 'edge_node', '0015_devicemodel_device_status', '2022-11-09 06:23:25.013083'),
(37, 'edge_node', '0016_devicemodel_device_node_filemodel_file_node_and_more', '2022-11-09 08:09:12.848006'),
(38, 'edge_node', '0017_alter_devicemodel_device_node_and_more', '2022-11-09 08:16:19.624908'),
(39, 'mainapp', '0004_userdetailsmodel_user_server', '2022-11-11 06:35:18.926603'),
(40, 'edge_node', '0018_devicemodel_device_server', '2022-11-11 08:56:38.817214'),
(41, 'edge_node', '0019_alter_devicemodel_device_server', '2022-11-12 07:28:24.030224');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('od08skhtq4ny3xq2rbg2br2rwwbe6thi', 'eyJ1c2VyX2lkIjoxfQ:1otk5a:hnjG99sYGaOurscNUoBNjQtp704g2gG-LPK18c8XluU', '2022-11-26 06:34:02.087752'),
('elk63cmpou56vmahqcnmkg4zwg6yiht7', 'eyJ1c2VyX2lkIjoyfQ:1otmmO:3rAnPXiZfOoJ_wLX0swx22cmHHLNkAKx6MK0Fl06p1I', '2022-11-26 09:26:24.924209'),
('5rb5pkzcmed8pcmkfqzixm6grj4k2zu0', 'eyJ1c2VyX2lkIjoyfQ:1otqrQ:Y4YR9ICA957Osj7RO_8lDvjz4OT3Kc7sb8APLCGQSpc', '2022-11-26 13:47:52.833068');

-- --------------------------------------------------------

--
-- Table structure for table `file_details`
--

DROP TABLE IF EXISTS `file_details`;
CREATE TABLE IF NOT EXISTS `file_details` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `file-name` varchar(1000) NOT NULL,
  `file-size` int(11) NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  `file_device_id` int(11) DEFAULT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `file_user_id` int(11) DEFAULT NULL,
  `file-type` varchar(50) DEFAULT NULL,
  `file-node` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`file_id`),
  KEY `file_details_file_user_id_968db85c` (`file_user_id`),
  KEY `file_details_file_device_id_766b9830` (`file_device_id`)
) ENGINE=MyISAM AUTO_INCREMENT=85 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `file_details`
--

INSERT INTO `file_details` (`file_id`, `file-name`, `file-size`, `file`, `file_device_id`, `datetime_created`, `file_user_id`, `file-type`, `file-node`) VALUES
(55, 'RDBMS Record-1 (1).pdf', 15263862, 'Mobile/user-data/RDBMS_Record-1_1.pdf', 27, '2022-11-09 05:45:36.212832', 2, '.pdf', 'North America'),
(35, 'about1.png', 87269, 'Mobile/user-data/about1.png', 23, '2022-11-08 09:43:07.140753', 2, '.png', 'North America'),
(31, 'd.jpg', 14520, 'Mobile/user-data/d.jpg', 22, '2022-11-08 09:31:58.847554', 1, '.jpg', 'Asia'),
(38, 'learn_about_bg.png', 2054934, 'Mobile/user-data/learn_about_bg_TpZl81A.png', 24, '2022-11-08 09:47:26.100636', 2, '.png', 'North America'),
(53, 'cloud-data.png', 27749, 'Mobile/user-data/cloud-data.png', 25, '2022-11-08 13:01:05.045544', 2, '.png', 'North America'),
(78, 'about1.png', 87269, 'Mobile/user-data/about1_NeIHL1S.png', 32, '2022-11-12 07:12:45.280510', 1, '.png', 'Asia'),
(79, 'about2.png', 64155, 'Mobile/user-data/about2_AzeaSM3.png', 21, '2022-11-12 07:12:51.351132', 1, '.png', 'Asia'),
(81, 'about2.png', 64155, 'Mobile/user-data/about2_bYr56cH.png', 21, '2022-11-12 07:13:05.113278', 1, '.png', 'Asia');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
CREATE TABLE IF NOT EXISTS `user_details` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  `contact` bigint(20) NOT NULL,
  `user_region` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `user_status` varchar(50) DEFAULT NULL,
  `user_server` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `name`, `email`, `password`, `contact`, `user_region`, `image`, `datetime_created`, `user_status`, `user_server`) VALUES
(1, 'Jim helpert', 'mohd.hashwar552@gmail.com', 'Pass1234', 7878787876, 'Asia', 'Mobile/user-image/comment_2_8mGLwOf.png', '2022-11-05 13:52:43.055687', 'accepted', 'Europe (Frankfurt)'),
(2, 'tim', 'tim@gmail.com', 'Pass1234', 9898989898, 'North America', 'Mobile/user-image/comment_3.png', '2022-11-05 14:18:30.316499', 'accepted', 'none'),
(3, 'kit harington', 'kit@gmail.com', 'Pass1234', 7474747474, 'Europe', 'Mobile/user-image/g8.jpg', '2022-11-08 11:00:55.877327', 'accepted', 'none'),
(4, 'james', 'james@gmail.com', 'Pass1234', 7878787878, 'Europe', 'Mobile/user-image/cloud.png', '2022-11-10 12:57:16.833780', 'accepted', 'none'),
(5, 'tina lang', 'lang@gmail.com', 'Pass1234', 8888888888, 'Asia', 'Mobile/user-image/slide_thumb_1.png', '2022-11-10 16:28:53.774182', 'pending', 'none');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
