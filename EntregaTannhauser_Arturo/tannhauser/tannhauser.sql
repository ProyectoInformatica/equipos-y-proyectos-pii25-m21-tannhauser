-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-05-2026 a las 23:22:29
-- Versión del servidor: 8.0.45
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tannhauser`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `activity_log`
--

CREATE TABLE `activity_log` (
  `id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED DEFAULT NULL,
  `log_level` enum('INFO','WARNING','ERROR') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'INFO',
  `action` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `message` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `logged_at` datetime(6) NOT NULL,
  `metadata` json DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `activity_log`
--

INSERT INTO `activity_log` (`id`, `user_id`, `log_level`, `action`, `message`, `logged_at`, `metadata`) VALUES
(1, 2, 'INFO', 'login', 'Inicio de sesión correcto del administrador.', '2026-01-09 13:00:00.000000', '{\"archivo\": \"actividad.log\"}'),
(2, 7, 'INFO', 'inventario', 'Consulta del inventario desde la aplicación.', '2026-01-09 13:05:00.000000', '{\"modulo\": \"inventario\"}'),
(3, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-03-29 21:33:20.781372', '{\"origen\": \"app\"}'),
(4, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-03-29 21:33:44.000050', '{\"origen\": \"app\"}'),
(5, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-03-29 21:42:31.313449', '{\"origen\": \"app\"}'),
(6, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-21 17:20:35.691893', '{\"origen\": \"app\"}'),
(7, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-29 17:06:31.758014', '{\"origen\": \"app\"}'),
(8, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-29 17:08:11.647003', '{\"origen\": \"app\"}'),
(9, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-29 17:44:51.192705', '{\"origen\": \"app\"}'),
(10, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-29 17:48:47.874226', '{\"origen\": \"app\"}'),
(11, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-29 17:54:01.604339', '{\"origen\": \"app\"}'),
(12, NULL, 'INFO', 'start_simulacion', 'Acción registrada: START_SIMULACION', '2026-04-29 17:55:45.990151', '{\"origen\": \"app\"}'),
(13, NULL, 'INFO', 'stop_simulacion', 'Acción registrada: STOP_SIMULACION', '2026-04-29 17:55:50.093346', '{\"origen\": \"app\"}'),
(14, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-29 17:58:05.327325', '{\"origen\": \"app\"}'),
(15, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 11:08:00.318766', '{\"origen\": \"app\"}'),
(16, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 11:12:58.836358', '{\"origen\": \"app\"}'),
(17, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 11:26:40.942659', '{\"origen\": \"app\"}'),
(18, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 11:52:18.322936', '{\"origen\": \"app\"}'),
(19, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 12:04:08.277496', '{\"origen\": \"app\"}'),
(20, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 17:51:48.468724', '{\"origen\": \"app\"}'),
(21, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 17:57:57.788625', '{\"origen\": \"app\"}'),
(22, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 17:59:32.048202', '{\"origen\": \"app\"}'),
(23, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:08:49.336271', '{\"origen\": \"app\"}'),
(24, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:12:02.404326', '{\"origen\": \"app\"}'),
(25, NULL, 'INFO', 'start_simulacion', 'Acción registrada: START_SIMULACION', '2026-04-30 18:13:26.941185', '{\"origen\": \"app\"}'),
(26, NULL, 'INFO', 'stop_simulacion', 'Acción registrada: STOP_SIMULACION', '2026-04-30 18:13:29.731002', '{\"origen\": \"app\"}'),
(27, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:13:43.840852', '{\"origen\": \"app\"}'),
(28, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:16:54.482782', '{\"origen\": \"app\"}'),
(29, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:23:05.100731', '{\"origen\": \"app\"}'),
(30, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:24:25.944926', '{\"origen\": \"app\"}'),
(31, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:27:40.076489', '{\"origen\": \"app\"}'),
(32, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:31:19.538521', '{\"origen\": \"app\"}'),
(33, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:36:02.012448', '{\"origen\": \"app\"}'),
(34, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:36:54.083346', '{\"origen\": \"app\"}'),
(35, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:39:43.515538', '{\"origen\": \"app\"}'),
(36, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:40:59.702312', '{\"origen\": \"app\"}'),
(37, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 18:52:38.712894', '{\"origen\": \"app\"}'),
(38, 8, 'INFO', 'register', 'Acción registrada: REGISTER', '2026-04-30 20:22:01.141754', '{\"origen\": \"app\"}'),
(39, 9, 'INFO', 'register', 'Acción registrada: REGISTER', '2026-04-30 20:25:56.323383', '{\"origen\": \"app\"}'),
(40, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 20:32:04.585742', '{\"origen\": \"app\"}'),
(41, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 20:34:51.871465', '{\"origen\": \"app\"}'),
(42, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 20:35:49.050400', '{\"origen\": \"app\"}'),
(43, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 21:00:57.321164', '{\"origen\": \"app\"}'),
(44, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 21:02:13.348134', '{\"origen\": \"app\"}'),
(45, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 21:03:38.297446', '{\"origen\": \"app\"}'),
(46, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 21:05:32.261865', '{\"origen\": \"app\"}'),
(47, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-04-30 21:08:26.771205', '{\"origen\": \"app\"}'),
(48, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 13:55:28.326218', '{\"origen\": \"app\"}'),
(49, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 14:11:29.020324', '{\"origen\": \"app\"}'),
(50, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 14:31:50.573048', '{\"origen\": \"app\"}'),
(51, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 14:31:52.674537', '{\"origen\": \"app\"}'),
(52, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 14:32:25.298528', '{\"origen\": \"app\"}'),
(53, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 14:32:29.036251', '{\"origen\": \"app\"}'),
(54, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 14:35:40.708263', '{\"origen\": \"app\"}'),
(55, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 14:56:19.184615', '{\"origen\": \"app\"}'),
(56, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 15:00:17.775072', '{\"origen\": \"app\"}'),
(57, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 15:00:56.910845', '{\"origen\": \"app\"}'),
(58, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 15:05:56.702346', '{\"origen\": \"app\"}'),
(59, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 15:10:11.517630', '{\"origen\": \"app\"}'),
(60, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 17:34:13.181083', '{\"origen\": \"app\"}'),
(61, 7, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 17:42:18.519023', '{\"origen\": \"app\"}'),
(62, 7, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 17:59:02.203674', '{\"origen\": \"app\"}'),
(63, 7, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 18:00:27.157665', '{\"origen\": \"app\"}'),
(64, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 18:02:44.174734', '{\"origen\": \"app\"}'),
(65, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 18:03:12.260752', '{\"origen\": \"app\"}'),
(66, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 18:14:04.336418', '{\"origen\": \"app\"}'),
(67, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 18:14:24.595998', '{\"origen\": \"app\"}'),
(68, 7, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 18:17:15.738776', '{\"origen\": \"app\"}'),
(69, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 18:17:34.187489', '{\"origen\": \"app\"}'),
(70, 1, 'INFO', 'start_simulacion', 'Acción registrada: START_SIMULACION', '2026-05-03 18:17:56.361670', '{\"origen\": \"app\"}'),
(71, 1, 'INFO', 'stop_simulacion', 'Acción registrada: STOP_SIMULACION', '2026-05-03 18:18:01.476283', '{\"origen\": \"app\"}'),
(72, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:06:40.703595', '{\"origen\": \"app\"}'),
(73, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:07:44.483909', '{\"origen\": \"app\"}'),
(74, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:09:04.232587', '{\"origen\": \"app\"}'),
(75, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:09:15.561328', '{\"origen\": \"app\"}'),
(76, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:09:54.324232', '{\"origen\": \"app\"}'),
(77, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:10:11.739750', '{\"origen\": \"app\"}'),
(78, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:10:35.920712', '{\"origen\": \"app\"}'),
(79, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:35:07.617148', '{\"origen\": \"app\"}'),
(80, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:35:32.986374', '{\"origen\": \"app\"}'),
(81, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:35:58.909759', '{\"origen\": \"app\"}'),
(82, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:39:48.549586', '{\"origen\": \"app\"}'),
(83, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:45:03.423306', '{\"origen\": \"app\"}'),
(84, 2, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:45:41.653505', '{\"origen\": \"app\"}'),
(85, 7, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:45:51.581014', '{\"origen\": \"app\"}'),
(86, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:46:22.849249', '{\"origen\": \"app\"}'),
(87, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:58:30.760043', '{\"origen\": \"app\"}'),
(88, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-03 23:59:19.767217', '{\"origen\": \"app\"}'),
(89, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-04 00:06:10.860913', '{\"origen\": \"app\"}'),
(90, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-04 00:15:24.008492', '{\"origen\": \"app\"}'),
(91, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-04 00:20:09.867747', '{\"origen\": \"app\"}'),
(92, 9, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-04 18:37:41.347449', '{\"origen\": \"app\"}'),
(93, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-04 18:38:47.038598', '{\"origen\": \"app\"}'),
(94, 1, 'INFO', 'login', 'Acción registrada: LOGIN', '2026-05-04 18:39:43.551483', '{\"origen\": \"app\"}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alert_thresholds`
--

CREATE TABLE `alert_thresholds` (
  `id` int NOT NULL,
  `state_code` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `operator_type` enum('gt','lt') COLLATE utf8mb4_unicode_ci NOT NULL,
  `threshold_value` decimal(10,2) NOT NULL,
  `severity` enum('info','warning','critical') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'warning',
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description_template` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `alert_thresholds`
--

INSERT INTO `alert_thresholds` (`id`, `state_code`, `operator_type`, `threshold_value`, `severity`, `title`, `description_template`, `is_active`, `updated_at`) VALUES
(13, 'TEMP_AIR', 'gt', 0.00, 'critical', 'Nueva alerta', 'Descripción de la alerta', 1, '2026-04-30 21:02:46'),
(14, 'DISTANCE_CM', 'gt', 0.00, 'critical', 'Nueva alerta', 'Descripción de la alerta', 1, '2026-04-30 21:02:53');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camera_events`
--

CREATE TABLE `camera_events` (
  `id` bigint UNSIGNED NOT NULL,
  `device_id` bigint UNSIGNED NOT NULL,
  `event_type` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `file_path` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mime_type` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `captured_at` datetime(6) NOT NULL,
  `notes` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metadata` json DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `chat_messages`
--

CREATE TABLE `chat_messages` (
  `id` bigint UNSIGNED NOT NULL,
  `sender_id` bigint UNSIGNED NOT NULL,
  `receiver_id` bigint UNSIGNED NOT NULL,
  `message` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comments`
--

CREATE TABLE `comments` (
  `id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED DEFAULT NULL,
  `usuario_alias` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `texto` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `comments`
--

INSERT INTO `comments` (`id`, `user_id`, `usuario_alias`, `texto`, `is_active`, `created_at`) VALUES
(1, NULL, 'Anónimo', 'Tested', 1, '2026-01-09 14:04:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `current_state`
--

CREATE TABLE `current_state` (
  `id` bigint UNSIGNED NOT NULL,
  `device_id` bigint UNSIGNED NOT NULL,
  `state_code` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `state_value` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `numeric_value` decimal(10,2) DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `source` enum('simulado','esp32','manual','sistema','importado') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'simulado',
  `payload` json DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `current_state`
--

INSERT INTO `current_state` (`id`, `device_id`, `state_code`, `state_value`, `numeric_value`, `updated_at`, `source`, `payload`) VALUES
(1, 3, 'light_power', 'ON', 1.00, '2026-01-09 13:18:00.000000', 'simulado', '{\"archivo\": \"sensor_luz.json\"}'),
(2, 5, 'door_state', 'abierta', NULL, '2025-12-01 19:28:38.295094', 'importado', '{\"archivo\": \"sensor_puerta.json\"}'),
(3, 6, 'MQ135_AIR', '2141', 2141.00, '2026-04-30 21:10:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}'),
(6, 1, 'TEMP_AIR', '29.7', 29.70, '2026-04-30 21:10:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}'),
(7, 2, 'HUM_AIR', '17', 17.00, '2026-04-30 21:10:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}'),
(118, 8, 'lectura_actual', '20.85', 20.85, '2026-05-03 18:18:00.825355', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}'),
(119, 9, 'lectura_actual', '53', 53.00, '2026-05-03 18:18:00.846809', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}'),
(120, 10, 'lectura_actual', '39', 39.00, '2026-05-03 18:18:00.866271', 'simulado', '{\"sensor_name\": \"sensor_luz\"}'),
(121, 11, 'lectura_actual', '4.6', 4.60, '2026-05-03 18:18:00.885661', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}'),
(122, 12, 'estado', 'abierta', NULL, '2026-05-03 18:18:00.901311', 'simulado', '{\"sensor_name\": \"sensor_puerta\"}'),
(123, 8, 'consumo_24h', '12.01', 12.01, '2026-05-03 18:18:42.463783', 'sistema', '{\"tipo\": \"consumo_24h\", \"sensor_name\": \"sensor_temperatura\"}'),
(124, 9, 'consumo_24h', '7.21', 7.21, '2026-05-03 18:18:42.492324', 'sistema', '{\"tipo\": \"consumo_24h\", \"sensor_name\": \"sensor_humedad\"}'),
(125, 10, 'consumo_24h', '48.04', 48.04, '2026-05-03 18:18:42.518970', 'sistema', '{\"tipo\": \"consumo_24h\", \"sensor_name\": \"sensor_luz\"}'),
(126, 11, 'consumo_24h', '2402.06', 2402.06, '2026-05-03 18:18:42.544823', 'sistema', '{\"tipo\": \"consumo_24h\", \"sensor_name\": \"sensor_nevera\"}'),
(127, 12, 'consumo_24h', '2.4', 2.40, '2026-05-03 18:18:42.567893', 'sistema', '{\"tipo\": \"consumo_24h\", \"sensor_name\": \"sensor_puerta\"}'),
(131, 5, 'DISTANCE_CM', '16.69', 16.69, '2026-04-30 21:10:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devices`
--

CREATE TABLE `devices` (
  `id` bigint UNSIGNED NOT NULL,
  `device_code` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `device_name` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sensor_type_id` bigint UNSIGNED DEFAULT NULL,
  `location_name` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pin_or_channel` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` enum('activo','mantenimiento','inactivo') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'activo',
  `metadata` json DEFAULT NULL,
  `installed_at` datetime DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `deactivated_at` datetime DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `devices`
--

INSERT INTO `devices` (`id`, `device_code`, `device_name`, `sensor_type_id`, `location_name`, `pin_or_channel`, `status`, `metadata`, `installed_at`, `is_active`, `deactivated_at`, `created_at`, `updated_at`) VALUES
(1, 'temp_01', 'Sensor temperatura principal', 1, 'Zona general', 'GPIO-DHT', 'activo', '{\"origen\": \"json_actual\"}', NULL, 1, NULL, '2026-03-29 19:29:08', '2026-03-29 19:29:08'),
(2, 'hum_01', 'Sensor humedad principal', 2, 'Zona general', 'GPIO-DHT', 'activo', '{\"origen\": \"json_actual\"}', NULL, 1, NULL, '2026-03-29 19:29:08', '2026-03-29 19:29:08'),
(3, 'light_01', 'Control de luces', 3, 'Tienda', 'GPIO-LDR', 'activo', '{\"origen\": \"json_actual\"}', NULL, 1, NULL, '2026-03-29 19:29:08', '2026-03-29 19:29:08'),
(4, 'fridge_01', 'Sensor nevera', 4, 'Cámara frigorífica', 'GPIO-DHT22', 'activo', '{\"origen\": \"json_actual\"}', NULL, 1, NULL, '2026-03-29 19:29:08', '2026-03-29 19:29:08'),
(5, 'door_01', 'Sensor puerta acceso', 5, 'Entrada principal', 'GPIO-HCSR04', 'activo', '{\"origen\": \"json_actual\"}', NULL, 1, NULL, '2026-03-29 19:29:08', '2026-03-29 19:29:08'),
(6, 'mq135_01', 'Sensor calidad de aire', 6, 'Zona clientes', 'ADC1', 'activo', '{\"previsto_en_backlog\": true}', NULL, 1, NULL, '2026-03-29 19:29:08', '2026-03-29 19:29:08'),
(7, 'cam_01', 'ESP32-CAM vigilancia', 7, 'Entrada principal', 'CAM', 'activo', '{\"previsto_en_backlog\": true}', NULL, 1, NULL, '2026-03-29 19:29:08', '2026-03-29 19:29:08'),
(8, 'DEV-TEMP-001', 'Sensor Temperatura', 8, 'Supermercado', NULL, 'activo', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-04-29 17:06:41', 1, NULL, '2026-04-29 15:06:40', '2026-04-29 15:06:40'),
(9, 'DEV-HUM-001', 'Sensor Humedad', 9, 'Supermercado', NULL, 'activo', '{\"sensor_name\": \"sensor_humedad\"}', '2026-04-29 17:06:41', 1, NULL, '2026-04-29 15:06:40', '2026-04-29 15:06:40'),
(10, 'DEV-LUZ-001', 'Sensor Luz', 10, 'Supermercado', NULL, 'activo', '{\"sensor_name\": \"sensor_luz\"}', '2026-04-29 17:06:41', 1, NULL, '2026-04-29 15:06:40', '2026-04-29 15:06:40'),
(11, 'DEV-NEV-001', 'Sensor Nevera', 11, 'Zona refrigerada', NULL, 'activo', '{\"sensor_name\": \"sensor_nevera\"}', '2026-04-29 17:06:41', 1, NULL, '2026-04-29 15:06:41', '2026-04-29 15:06:41'),
(12, 'DEV-PUE-001', 'Sensor Puerta', 12, 'Entrada', NULL, 'activo', '{\"sensor_name\": \"sensor_puerta\"}', '2026-04-29 17:06:41', 1, NULL, '2026-04-29 15:06:41', '2026-04-29 15:06:41');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `events`
--

CREATE TABLE `events` (
  `id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED DEFAULT NULL,
  `device_id` bigint UNSIGNED DEFAULT NULL,
  `event_type` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `severity` enum('info','warning','critical') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'info',
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `event_time` datetime(6) NOT NULL,
  `payload` json DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_resolved` tinyint(1) NOT NULL DEFAULT '0',
  `resolved_at` datetime DEFAULT NULL,
  `resolved_by_user_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `events`
--

INSERT INTO `events` (`id`, `user_id`, `device_id`, `event_type`, `severity`, `title`, `description`, `event_time`, `payload`, `created_at`, `is_resolved`, `resolved_at`, `resolved_by_user_id`) VALUES
(1, 2, NULL, 'login_demo', 'info', 'Acceso de administrador', 'Evento de ejemplo alineado con la UI actual.', '2026-01-09 13:00:00.000000', '{\"origen\": \"actividad.log\"}', '2026-03-29 19:29:08', 0, NULL, NULL),
(2, NULL, 5, 'door_event', 'info', 'Movimiento en puerta', 'Apertura/cierre detectado desde sensor de puerta.', '2025-12-01 18:57:22.533696', '{\"evento\": \"entrada\"}', '2026-03-29 19:29:08', 0, NULL, NULL),
(3, NULL, 1, 'sensor_alert', 'critical', 'Sensor demasiado caliente', 'ENFRIAR LO ANTES POSIBLE', '2026-04-30 18:09:27.000000', '{\"valor\": 29.9, \"umbral\": 20, \"rule_id\": 9, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:27', 1, '2026-04-30 18:23:21', 1),
(4, NULL, 5, 'sensor_alert', 'critical', 'DEMASIADO CERCA', 'ALEJESE', '2026-04-30 18:13:51.000000', '{\"valor\": 2.97, \"umbral\": 5, \"rule_id\": 10, \"operador\": \"lt\", \"severity\": \"critical\", \"state_code\": \"DISTANCE_CM\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:51', 1, '2026-04-30 18:23:20', 1),
(5, NULL, 1, 'sensor_alert', 'critical', 'Sensor demasiado caliente', 'ENFRIAR LO ANTES POSIBLE', '2026-04-30 18:14:28.000000', '{\"valor\": 29.1, \"umbral\": 20, \"rule_id\": 9, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:28', 1, '2026-04-30 18:23:19', 1),
(6, NULL, 1, 'sensor_alert', 'critical', 'Sensor demasiado caliente', 'ENFRIAR LO ANTES POSIBLE', '2026-04-30 18:19:29.000000', '{\"valor\": 29.3, \"umbral\": 20, \"rule_id\": 9, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:29', 1, '2026-04-30 18:23:19', 1),
(7, NULL, 1, 'sensor_alert', 'critical', 'Sensor demasiado caliente', 'ENFRIAR LO ANTES POSIBLE', '2026-04-30 18:24:30.000000', '{\"valor\": 30, \"umbral\": 20, \"rule_id\": 9, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:30', 1, '2026-04-30 18:24:55', 1),
(8, NULL, 5, 'sensor_alert', 'critical', 'DEMASIADO CERCA', 'ALEJESE', '2026-04-30 18:24:45.000000', '{\"valor\": 3.29, \"umbral\": 4.99, \"rule_id\": 10, \"operador\": \"lt\", \"severity\": \"critical\", \"state_code\": \"DISTANCE_CM\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:45', 1, '2026-04-30 18:24:54', 1),
(9, NULL, 1, 'sensor_alert', 'critical', 'Sensor demasiado caliente', 'ENFRIAR LO ANTES POSIBLE', '2026-04-30 18:29:34.000000', '{\"valor\": 29.2, \"umbral\": 20, \"rule_id\": 9, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:34', 1, '2026-04-30 18:31:26', 1),
(10, NULL, 5, 'sensor_alert', 'critical', 'DEMASIADO CERCA', 'ALEJESE', '2026-04-30 18:31:51.000000', '{\"valor\": 1.66, \"umbral\": 4.99, \"rule_id\": 10, \"operador\": \"lt\", \"severity\": \"critical\", \"state_code\": \"DISTANCE_CM\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:51', 1, '2026-04-30 18:32:01', 1),
(11, NULL, 1, 'sensor_alert', 'warning', 'Nueva alerta', 'Descripción de la alerta', '2026-04-30 18:32:54.000000', '{\"valor\": 30.1, \"umbral\": 5, \"rule_id\": 11, \"operador\": \"gt\", \"severity\": \"warning\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:54', 1, '2026-04-30 18:36:24', 1),
(12, NULL, 1, 'sensor_alert', 'critical', 'Nueva alerta', 'Descripción de la alerta', '2026-04-30 18:32:59.000000', '{\"valor\": 30.2, \"umbral\": 0, \"rule_id\": 12, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:59', 1, '2026-04-30 18:36:24', 1),
(13, NULL, 1, 'sensor_alert', 'critical', 'Nueva alerta', 'Descripción de la alerta', '2026-04-30 18:38:03.000000', '{\"valor\": 29.7, \"umbral\": 0, \"rule_id\": 12, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:03', 1, '2026-04-30 18:43:23', 1),
(14, NULL, 5, 'sensor_alert', 'critical', 'DEMASIADO CERCA', 'ALEJESE', '2026-04-30 18:39:55.000000', '{\"valor\": 4.92, \"umbral\": 4.99, \"rule_id\": 10, \"operador\": \"lt\", \"severity\": \"critical\", \"state_code\": \"DISTANCE_CM\", \"device_code\": \"door_01\"}', '2026-04-30 16:39:55', 1, '2026-04-30 18:43:22', 1),
(15, NULL, 1, 'sensor_alert', 'critical', 'Nueva alerta', 'Descripción de la alerta', '2026-04-30 18:43:06.000000', '{\"valor\": 29.8, \"umbral\": 0, \"rule_id\": 12, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:06', 1, '2026-04-30 18:43:21', 1),
(16, NULL, 1, 'sensor_alert', 'critical', 'Nueva alerta', 'Descripción de la alerta', '2026-04-30 18:48:09.000000', '{\"valor\": 29.7, \"umbral\": 0, \"rule_id\": 12, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:09', 1, '2026-04-30 18:52:58', 1),
(17, NULL, 5, 'sensor_alert', 'critical', 'DEMASIADO CERCA', 'ALEJESE', '2026-04-30 18:53:03.000000', '{\"valor\": 2.97, \"umbral\": 4.99, \"rule_id\": 10, \"operador\": \"lt\", \"severity\": \"critical\", \"state_code\": \"DISTANCE_CM\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:03', 1, '2026-04-30 18:53:34', 1),
(18, NULL, 1, 'sensor_alert', 'critical', 'Nueva alerta', 'Descripción de la alerta', '2026-04-30 18:53:13.000000', '{\"valor\": 29.5, \"umbral\": 0, \"rule_id\": 12, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:13', 1, '2026-04-30 18:53:35', 1),
(19, NULL, 1, 'sensor_alert', 'critical', 'Nueva alerta', 'Descripción de la alerta', '2026-04-30 21:07:47.000000', '{\"valor\": 0.4, \"umbral\": 0, \"rule_id\": 13, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"TEMP_AIR\", \"device_code\": \"temp_01\"}', '2026-04-30 19:07:47', 1, '2026-04-30 21:08:56', 1),
(20, NULL, 5, 'sensor_alert', 'critical', 'Nueva alerta', 'Descripción de la alerta', '2026-04-30 21:07:47.000000', '{\"valor\": 16.04, \"umbral\": 0, \"rule_id\": 14, \"operador\": \"gt\", \"severity\": \"critical\", \"state_code\": \"DISTANCE_CM\", \"device_code\": \"door_01\"}', '2026-04-30 19:07:47', 1, '2026-04-30 21:08:57', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `loyalty_coupons`
--

CREATE TABLE `loyalty_coupons` (
  `id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED NOT NULL,
  `offer_id` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `coupon_code` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `points_cost` int NOT NULL DEFAULT '0',
  `status` enum('active','used','expired','cancelled') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'active',
  `redeemed_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `used_at` datetime DEFAULT NULL,
  `expires_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `loyalty_coupons`
--

INSERT INTO `loyalty_coupons` (`id`, `user_id`, `offer_id`, `coupon_code`, `title`, `description`, `points_cost`, `status`, `redeemed_at`, `used_at`, `expires_at`) VALUES
(1, 9, 'bebidas_10', 'TANN-9-BEBIDA-6XN3UI', '10% en bebidas frías', 'Descuento directo en refrescos, agua y bebidas isotónicas.', 80, 'used', '2026-05-04 18:37:54', '2026-05-04 18:38:20', '2026-06-03 18:37:54');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `loyalty_offers`
--

CREATE TABLE `loyalty_offers` (
  `id` bigint NOT NULL,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `points_required` int NOT NULL DEFAULT '0',
  `discount_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `loyalty_offers`
--

INSERT INTO `loyalty_offers` (`id`, `title`, `description`, `points_required`, `discount_label`, `is_active`, `created_at`) VALUES
(1, '10% en bebidas frías', 'Descuento directo en refrescos, agua y bebidas isotónicas.', 80, '10% DTO', 1, '2026-04-30 20:57:06'),
(2, '2x1 en snacks seleccionados', 'Promoción válida en productos marcados dentro del inventario.', 120, '2x1', 1, '2026-04-30 20:57:06'),
(3, '5 € en compras superiores a 40 €', 'Cupón de fidelidad para compras grandes.', 250, '5 € DTO', 1, '2026-04-30 20:57:06'),
(4, '15% en productos frescos', 'Aplicable a fruta, verdura y secciones seleccionadas.', 180, '15% DTO', 1, '2026-04-30 20:57:06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `loyalty_transactions`
--

CREATE TABLE `loyalty_transactions` (
  `id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED NOT NULL,
  `transaction_type` enum('purchase','redeem','adjustment') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'purchase',
  `purchase_amount` decimal(10,2) NOT NULL DEFAULT '0.00',
  `points_delta` int NOT NULL DEFAULT '0',
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reference_code` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `loyalty_transactions`
--

INSERT INTO `loyalty_transactions` (`id`, `user_id`, `transaction_type`, `purchase_amount`, `points_delta`, `description`, `reference_code`, `created_at`) VALUES
(1, 9, 'purchase', 25.50, 25, 'Compra registrada por 25.50 €', 'TICKET-001', '2026-05-03 13:57:16'),
(2, 9, 'purchase', 60.00, 60, 'Compra registrada por 60.00 €', 'TICKET-002', '2026-05-03 13:57:49'),
(3, 9, 'redeem', 0.00, -80, 'Canje de oferta: 10% en bebidas frías', 'OFFER-1', '2026-05-03 13:57:50'),
(4, 9, 'purchase', 90.00, 90, 'Compra registrada por 90.00 €', NULL, '2026-05-03 14:11:38'),
(5, 9, 'redeem', 0.00, -80, 'Canje de recompensa: 10% en bebidas frías', 'TANN-9-BEBIDA-6XN3UI', '2026-05-04 18:37:54'),
(6, 9, 'purchase', 90.00, 9, 'Compra registrada en supermercado', 'TICKET1', '2026-05-04 18:38:12');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `media_assets`
--

CREATE TABLE `media_assets` (
  `id` bigint UNSIGNED NOT NULL,
  `device_id` bigint UNSIGNED DEFAULT NULL,
  `product_id` bigint UNSIGNED DEFAULT NULL,
  `file_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mime_type` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `binary_data` longblob NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `media_assets`
--

INSERT INTO `media_assets` (`id`, `device_id`, `product_id`, `file_name`, `mime_type`, `binary_data`, `created_at`) VALUES
(1, 7, NULL, 'captura_demo.jpg', 'image/jpeg', 0xffd8ffe000104a46494600010100000100010000ffd9, '2026-03-29 19:29:08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `id` bigint UNSIGNED NOT NULL,
  `sku` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nombre` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cantidad` int NOT NULL DEFAULT '0',
  `precio` decimal(10,2) NOT NULL DEFAULT '0.00',
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deactivated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`id`, `sku`, `nombre`, `cantidad`, `precio`, `is_active`, `created_at`, `updated_at`, `deactivated_at`) VALUES
(1, 'PROD-001', 'Leche Entera 1L', 30, 1.25, 1, '2026-03-29 19:29:08', '2026-03-29 19:29:08', NULL),
(2, 'PROD-002', 'Pan Integral', 35, 0.90, 1, '2026-03-29 19:29:08', '2026-03-29 19:29:08', NULL),
(3, 'PROD-003', 'Huevos (docena)', 10, 2.50, 1, '2026-03-29 19:29:08', '2026-03-29 19:29:08', NULL),
(4, 'LAC-001', 'Leche Entera 1L', 30, 1.25, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(5, 'PAN-001', 'Pan Integral', 35, 0.90, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(6, 'HUE-001', 'Huevos (docena)', 10, 2.50, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(7, 'FRU-001', 'Plátanos 1kg', 24, 1.89, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(8, 'FRU-002', 'Manzanas 1kg', 18, 2.10, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(9, 'BEB-001', 'Agua Mineral 1.5L', 40, 0.65, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(10, 'BEB-002', 'Refresco Cola 2L', 22, 1.75, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(11, 'LAC-002', 'Yogur Natural Pack 4', 16, 2.20, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(12, 'CON-001', 'Arroz 1kg', 28, 1.45, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(13, 'CON-002', 'Pasta Espagueti 500g', 32, 1.10, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(14, 'SNK-001', 'Patatas Fritas', 20, 1.50, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL),
(15, 'CAF-001', 'Café Molido 250g', 12, 3.95, 1, '2026-05-03 12:25:02', '2026-05-03 12:25:02', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `readings`
--

CREATE TABLE `readings` (
  `id` bigint UNSIGNED NOT NULL,
  `device_id` bigint UNSIGNED NOT NULL,
  `sensor_type_id` bigint UNSIGNED NOT NULL,
  `reading_value` decimal(10,2) DEFAULT NULL,
  `reading_text` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `normalized_value` decimal(10,2) DEFAULT NULL,
  `consumption_w` decimal(10,4) DEFAULT NULL,
  `reading_unit` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recorded_at` datetime(6) NOT NULL,
  `source` enum('simulado','esp32','manual','importado') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'simulado',
  `payload` json DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `readings`
--

INSERT INTO `readings` (`id`, `device_id`, `sensor_type_id`, `reading_value`, `normalized_value`, `consumption_w`, `reading_unit`, `recorded_at`, `source`, `payload`, `created_at`) VALUES
(1, 1, 1, 20.18, NULL, 0.4036, 'C', '2025-12-01 19:28:35.432192', 'importado', '{\"archivo\": \"sensor_temperatura.json\"}', '2026-03-29 19:29:08'),
(2, 1, 1, 25.00, NULL, 0.5000, 'C', '2025-12-01 19:28:38.164948', 'importado', '{\"archivo\": \"sensor_temperatura.json\"}', '2026-03-29 19:29:08'),
(3, 1, 1, 25.50, NULL, 0.5100, 'C', '2026-01-09 13:18:02.735684', 'importado', '{\"archivo\": \"sensor_temperatura.json\"}', '2026-03-29 19:29:08'),
(4, 2, 2, 55.00, NULL, 1.1000, '%', '2025-11-29 11:04:15.393884', 'importado', '{\"archivo\": \"sensor_humedad.json\"}', '2026-03-29 19:29:08'),
(5, 2, 2, 40.00, NULL, 0.8000, '%', '2025-11-29 11:04:20.446125', 'importado', '{\"archivo\": \"sensor_humedad.json\"}', '2026-03-29 19:29:08'),
(6, 2, 2, 78.00, NULL, 1.5600, '%', '2025-11-29 11:04:25.517253', 'importado', '{\"archivo\": \"sensor_humedad.json\"}', '2026-03-29 19:29:08'),
(7, 4, 4, -18.00, NULL, 1.8000, 'C', '2025-12-01 19:28:35.000000', 'simulado', '{\"archivo\": \"sensor_nevera.json\"}', '2026-03-29 19:29:08'),
(8, 6, 6, 63.00, 63.00, NULL, 'indice', '2026-01-09 13:20:00.000000', 'simulado', '{\"nota\": \"dato de arranque para Sprint 2\"}', '2026-03-29 19:29:08'),
(9, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:31:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:31:17'),
(10, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:31:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:31:27'),
(11, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:31:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:31:37'),
(12, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:31:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:31:48'),
(13, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:31:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:31:58'),
(14, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:32:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:32:08'),
(15, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:32:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:32:19'),
(16, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:32:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:32:29'),
(17, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:32:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:32:39'),
(18, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:32:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:32:49'),
(19, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:32:59.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:32:59'),
(20, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:33:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:33:10'),
(21, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:33:20.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:33:20'),
(22, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:33:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:33:30'),
(23, 6, 6, 2043.00, NULL, NULL, 'raw', '2026-04-28 21:33:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:33:41'),
(24, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:33:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:33:51'),
(25, 6, 6, 2027.00, NULL, NULL, 'raw', '2026-04-28 21:34:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:34:01'),
(26, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:34:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:34:12'),
(27, 6, 6, 1079.00, NULL, NULL, 'raw', '2026-04-28 21:34:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:34:22'),
(28, 1, 1, 0.80, NULL, NULL, 'C', '2026-04-28 21:34:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:34:32'),
(29, 2, 2, 0.00, NULL, NULL, '%', '2026-04-28 21:34:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:34:32'),
(30, 6, 6, 119.00, NULL, NULL, 'raw', '2026-04-28 21:34:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:34:32'),
(31, 1, 1, 31.50, NULL, NULL, 'C', '2026-04-28 21:34:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:34:43'),
(32, 2, 2, 33.00, NULL, NULL, '%', '2026-04-28 21:34:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:34:43'),
(33, 6, 6, 154.00, NULL, NULL, 'raw', '2026-04-28 21:34:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:34:43'),
(34, 1, 1, 31.10, NULL, NULL, 'C', '2026-04-28 21:34:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:34:53'),
(35, 2, 2, 29.00, NULL, NULL, '%', '2026-04-28 21:34:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:34:53'),
(36, 6, 6, 1371.00, NULL, NULL, 'raw', '2026-04-28 21:34:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:34:53'),
(37, 1, 1, 31.90, NULL, NULL, 'C', '2026-04-28 21:35:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:35:03'),
(38, 2, 2, 25.00, NULL, NULL, '%', '2026-04-28 21:35:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:35:03'),
(39, 6, 6, 185.00, NULL, NULL, 'raw', '2026-04-28 21:35:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:35:03'),
(40, 1, 1, 31.70, NULL, NULL, 'C', '2026-04-28 21:35:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:35:13'),
(41, 2, 2, 23.00, NULL, NULL, '%', '2026-04-28 21:35:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:35:13'),
(42, 6, 6, 3664.00, NULL, NULL, 'raw', '2026-04-28 21:35:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:35:13'),
(43, 1, 1, 31.80, NULL, NULL, 'C', '2026-04-28 21:35:23.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:35:23'),
(44, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:35:23.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:35:23'),
(45, 6, 6, 3696.00, NULL, NULL, 'raw', '2026-04-28 21:35:23.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:35:23'),
(46, 1, 1, 31.50, NULL, NULL, 'C', '2026-04-28 21:35:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:35:34'),
(47, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:35:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:35:34'),
(48, 6, 6, 3657.00, NULL, NULL, 'raw', '2026-04-28 21:35:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:35:34'),
(49, 1, 1, 31.00, NULL, NULL, 'C', '2026-04-28 21:35:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:35:44'),
(50, 2, 2, 21.00, NULL, NULL, '%', '2026-04-28 21:35:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:35:44'),
(51, 6, 6, 3625.00, NULL, NULL, 'raw', '2026-04-28 21:35:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:35:44'),
(52, 1, 1, 30.00, NULL, NULL, 'C', '2026-04-28 21:35:54.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:35:54'),
(53, 2, 2, 21.00, NULL, NULL, '%', '2026-04-28 21:35:54.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:35:54'),
(54, 6, 6, 3614.00, NULL, NULL, 'raw', '2026-04-28 21:35:54.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:35:54'),
(55, 1, 1, 30.30, NULL, NULL, 'C', '2026-04-28 21:36:04.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:36:04'),
(56, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:36:04.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:36:04'),
(57, 6, 6, 3582.00, NULL, NULL, 'raw', '2026-04-28 21:36:04.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:36:04'),
(58, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-28 21:36:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:36:14'),
(59, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:36:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:36:14'),
(60, 6, 6, 3552.00, NULL, NULL, 'raw', '2026-04-28 21:36:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:36:14'),
(61, 1, 1, 30.30, NULL, NULL, 'C', '2026-04-28 21:36:25.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:36:25'),
(62, 2, 2, 21.00, NULL, NULL, '%', '2026-04-28 21:36:25.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:36:25'),
(63, 6, 6, 3542.00, NULL, NULL, 'raw', '2026-04-28 21:36:25.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:36:25'),
(64, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-28 21:36:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:36:35'),
(65, 2, 2, 21.00, NULL, NULL, '%', '2026-04-28 21:36:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:36:35'),
(66, 6, 6, 3515.00, NULL, NULL, 'raw', '2026-04-28 21:36:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:36:35'),
(67, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-28 21:36:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:36:45'),
(68, 2, 2, 21.00, NULL, NULL, '%', '2026-04-28 21:36:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:36:45'),
(69, 6, 6, 3511.00, NULL, NULL, 'raw', '2026-04-28 21:36:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:36:45'),
(70, 1, 1, 30.20, NULL, NULL, 'C', '2026-04-28 21:36:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:36:55'),
(71, 2, 2, 21.00, NULL, NULL, '%', '2026-04-28 21:36:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:36:55'),
(72, 6, 6, 3484.00, NULL, NULL, 'raw', '2026-04-28 21:36:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:36:55'),
(73, 1, 1, 30.40, NULL, NULL, 'C', '2026-04-28 21:37:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:37:06'),
(74, 2, 2, 21.00, NULL, NULL, '%', '2026-04-28 21:37:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:37:06'),
(75, 6, 6, 3467.00, NULL, NULL, 'raw', '2026-04-28 21:37:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:37:06'),
(76, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-28 21:38:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:38:01'),
(77, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:38:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:38:01'),
(78, 6, 6, 3411.00, NULL, NULL, 'raw', '2026-04-28 21:38:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:38:01'),
(79, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-28 21:38:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:38:11'),
(80, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:38:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:38:11'),
(81, 6, 6, 3390.00, NULL, NULL, 'raw', '2026-04-28 21:38:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:38:11'),
(82, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-28 21:38:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:38:21'),
(83, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:38:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:38:21'),
(84, 6, 6, 3400.00, NULL, NULL, 'raw', '2026-04-28 21:38:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:38:21'),
(85, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-28 21:38:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:38:31'),
(86, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:38:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:38:31'),
(87, 6, 6, 3369.00, NULL, NULL, 'raw', '2026-04-28 21:38:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:38:31'),
(88, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-28 21:38:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:38:42'),
(89, 2, 2, 22.00, NULL, NULL, '%', '2026-04-28 21:38:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:38:42'),
(90, 6, 6, 3362.00, NULL, NULL, 'raw', '2026-04-28 21:38:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:38:42'),
(91, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-28 21:38:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:38:52'),
(92, 2, 2, 23.00, NULL, NULL, '%', '2026-04-28 21:38:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:38:52'),
(93, 6, 6, 3363.00, NULL, NULL, 'raw', '2026-04-28 21:38:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:38:52'),
(94, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-28 21:39:02.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:39:02'),
(95, 2, 2, 23.00, NULL, NULL, '%', '2026-04-28 21:39:02.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:39:02'),
(96, 6, 6, 3354.00, NULL, NULL, 'raw', '2026-04-28 21:39:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:39:02'),
(97, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-28 21:39:12.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:39:12'),
(98, 2, 2, 23.00, NULL, NULL, '%', '2026-04-28 21:39:12.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:39:12'),
(99, 6, 6, 3338.00, NULL, NULL, 'raw', '2026-04-28 21:39:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:39:12'),
(100, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:40:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:40:11'),
(101, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:40:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:40:21'),
(102, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:40:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:40:31'),
(103, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:40:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:40:42'),
(104, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:40:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:40:52'),
(105, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:41:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:41:02'),
(106, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:41:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:41:12'),
(107, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:41:23.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:41:23'),
(108, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:41:33.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:41:33'),
(109, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:41:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:41:43'),
(110, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:41:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:41:53'),
(111, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:42:04.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:42:04'),
(112, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:42:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:42:14'),
(113, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:42:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:42:24'),
(114, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:42:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:42:35'),
(115, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:42:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:42:45'),
(116, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:42:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:42:55'),
(117, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:43:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:43:05'),
(118, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:43:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:43:16'),
(119, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:43:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:43:26'),
(120, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:43:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:43:39'),
(121, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:43:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:43:49'),
(122, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:44:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:44:00'),
(123, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:44:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:44:10'),
(124, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:44:20.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:44:20'),
(125, 6, 6, 4095.00, NULL, NULL, 'raw', '2026-04-28 21:44:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:44:30'),
(126, 1, 1, 0.50, NULL, NULL, 'C', '2026-04-28 21:44:41.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:44:41'),
(127, 2, 2, 0.00, NULL, NULL, '%', '2026-04-28 21:44:41.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:44:41'),
(128, 6, 6, 2414.00, NULL, NULL, 'raw', '2026-04-28 21:44:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:44:41'),
(129, 6, 6, 0.00, NULL, NULL, 'raw', '2026-04-28 21:44:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:44:51'),
(130, 1, 1, 0.50, NULL, NULL, 'C', '2026-04-28 21:45:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:45:01'),
(131, 2, 2, 0.00, NULL, NULL, '%', '2026-04-28 21:45:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:45:01'),
(132, 6, 6, 3275.00, NULL, NULL, 'raw', '2026-04-28 21:45:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:45:01'),
(133, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-28 21:45:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:45:11'),
(134, 2, 2, 25.00, NULL, NULL, '%', '2026-04-28 21:45:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:45:11'),
(135, 6, 6, 3340.00, NULL, NULL, 'raw', '2026-04-28 21:45:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:45:11'),
(136, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-28 21:45:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:45:21'),
(137, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:45:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:45:21'),
(138, 6, 6, 3331.00, NULL, NULL, 'raw', '2026-04-28 21:45:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:45:21'),
(139, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-28 21:45:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:45:32'),
(140, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:45:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:45:32'),
(141, 6, 6, 3355.00, NULL, NULL, 'raw', '2026-04-28 21:45:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:45:32'),
(142, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-28 21:45:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:45:42'),
(143, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:45:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:45:42'),
(144, 6, 6, 3344.00, NULL, NULL, 'raw', '2026-04-28 21:45:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:45:42'),
(145, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-28 21:45:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:45:52'),
(146, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:45:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:45:52'),
(147, 6, 6, 3306.00, NULL, NULL, 'raw', '2026-04-28 21:45:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:45:52'),
(148, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-28 21:46:02.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:46:02'),
(149, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:46:02.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:46:02'),
(150, 6, 6, 3319.00, NULL, NULL, 'raw', '2026-04-28 21:46:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:46:02'),
(151, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-28 21:46:12.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:46:12'),
(152, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:46:12.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:46:12'),
(153, 6, 6, 3303.00, NULL, NULL, 'raw', '2026-04-28 21:46:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:46:12'),
(154, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-28 21:46:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:46:22'),
(155, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:46:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:46:22'),
(156, 6, 6, 3306.00, NULL, NULL, 'raw', '2026-04-28 21:46:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:46:22'),
(157, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-28 21:46:33.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:46:33'),
(158, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:46:33.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:46:33'),
(159, 6, 6, 3280.00, NULL, NULL, 'raw', '2026-04-28 21:46:33.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:46:33'),
(160, 1, 1, 28.70, NULL, NULL, 'C', '2026-04-28 21:46:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:46:43'),
(161, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:46:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:46:43'),
(162, 6, 6, 3266.00, NULL, NULL, 'raw', '2026-04-28 21:46:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:46:43'),
(163, 1, 1, 28.80, NULL, NULL, 'C', '2026-04-28 21:46:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:46:53'),
(164, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:46:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:46:53'),
(165, 6, 6, 3267.00, NULL, NULL, 'raw', '2026-04-28 21:46:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:46:53'),
(166, 1, 1, 28.90, NULL, NULL, 'C', '2026-04-28 21:47:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:47:03'),
(167, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:47:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:47:03'),
(168, 6, 6, 3270.00, NULL, NULL, 'raw', '2026-04-28 21:47:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:47:03'),
(169, 1, 1, 28.60, NULL, NULL, 'C', '2026-04-28 21:47:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:47:14'),
(170, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:47:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:47:14'),
(171, 6, 6, 3265.00, NULL, NULL, 'raw', '2026-04-28 21:47:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:47:14'),
(172, 1, 1, 28.00, NULL, NULL, 'C', '2026-04-28 21:47:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:47:24'),
(173, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:47:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:47:24'),
(174, 6, 6, 3247.00, NULL, NULL, 'raw', '2026-04-28 21:47:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:47:24'),
(175, 1, 1, 28.60, NULL, NULL, 'C', '2026-04-28 21:47:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:47:34'),
(176, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:47:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:47:34'),
(177, 6, 6, 3248.00, NULL, NULL, 'raw', '2026-04-28 21:47:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:47:34'),
(178, 1, 1, 28.80, NULL, NULL, 'C', '2026-04-28 21:47:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:47:44'),
(179, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:47:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:47:44'),
(180, 6, 6, 3233.00, NULL, NULL, 'raw', '2026-04-28 21:47:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:47:44'),
(181, 1, 1, 28.70, NULL, NULL, 'C', '2026-04-28 21:47:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:47:55'),
(182, 2, 2, 25.00, NULL, NULL, '%', '2026-04-28 21:47:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:47:55'),
(183, 6, 6, 3223.00, NULL, NULL, 'raw', '2026-04-28 21:47:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:47:55'),
(184, 1, 1, 28.40, NULL, NULL, 'C', '2026-04-28 21:48:05.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:48:05'),
(185, 2, 2, 25.00, NULL, NULL, '%', '2026-04-28 21:48:05.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:48:05'),
(186, 6, 6, 3223.00, NULL, NULL, 'raw', '2026-04-28 21:48:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:48:05'),
(187, 1, 1, 28.60, NULL, NULL, 'C', '2026-04-28 21:48:15.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:48:15'),
(188, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:48:15.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:48:15'),
(189, 6, 6, 3216.00, NULL, NULL, 'raw', '2026-04-28 21:48:15.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:48:15'),
(190, 1, 1, 28.00, NULL, NULL, 'C', '2026-04-28 21:48:25.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:48:25'),
(191, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:48:25.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:48:25'),
(192, 6, 6, 3214.00, NULL, NULL, 'raw', '2026-04-28 21:48:25.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:48:25'),
(193, 1, 1, 28.50, NULL, NULL, 'C', '2026-04-28 21:48:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:48:35'),
(194, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:48:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:48:35'),
(195, 6, 6, 3199.00, NULL, NULL, 'raw', '2026-04-28 21:48:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:48:35'),
(196, 1, 1, 28.00, NULL, NULL, 'C', '2026-04-28 21:48:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:48:45'),
(197, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:48:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:48:45'),
(198, 6, 6, 3187.00, NULL, NULL, 'raw', '2026-04-28 21:48:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:48:45'),
(199, 1, 1, 28.60, NULL, NULL, 'C', '2026-04-28 21:48:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:48:56'),
(200, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:48:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:48:56'),
(201, 6, 6, 3184.00, NULL, NULL, 'raw', '2026-04-28 21:48:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:48:56'),
(202, 1, 1, 28.90, NULL, NULL, 'C', '2026-04-28 21:49:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:49:06'),
(203, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:49:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:49:06'),
(204, 6, 6, 3183.00, NULL, NULL, 'raw', '2026-04-28 21:49:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:49:06'),
(205, 1, 1, 28.40, NULL, NULL, 'C', '2026-04-28 21:49:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:49:17'),
(206, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:49:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:49:17'),
(207, 6, 6, 3190.00, NULL, NULL, 'raw', '2026-04-28 21:49:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:49:17'),
(208, 1, 1, 28.00, NULL, NULL, 'C', '2026-04-28 21:49:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:49:27'),
(209, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:49:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:49:27'),
(210, 6, 6, 3177.00, NULL, NULL, 'raw', '2026-04-28 21:49:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:49:27'),
(211, 1, 1, 28.40, NULL, NULL, 'C', '2026-04-28 21:49:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:49:37'),
(212, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:49:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:49:37'),
(213, 6, 6, 3157.00, NULL, NULL, 'raw', '2026-04-28 21:49:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:49:37'),
(214, 1, 1, 28.50, NULL, NULL, 'C', '2026-04-28 21:49:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:49:47'),
(215, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:49:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:49:47'),
(216, 6, 6, 3152.00, NULL, NULL, 'raw', '2026-04-28 21:49:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:49:47'),
(217, 1, 1, 28.90, NULL, NULL, 'C', '2026-04-28 21:50:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:50:00'),
(218, 2, 2, 25.00, NULL, NULL, '%', '2026-04-28 21:50:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:50:00'),
(219, 6, 6, 3161.00, NULL, NULL, 'raw', '2026-04-28 21:50:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:50:00'),
(220, 1, 1, 28.90, NULL, NULL, 'C', '2026-04-28 21:50:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:50:11'),
(221, 2, 2, 25.00, NULL, NULL, '%', '2026-04-28 21:50:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:50:11'),
(222, 6, 6, 3153.00, NULL, NULL, 'raw', '2026-04-28 21:50:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:50:11'),
(223, 1, 1, 28.60, NULL, NULL, 'C', '2026-04-28 21:50:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:50:21'),
(224, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:50:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:50:21'),
(225, 6, 6, 3163.00, NULL, NULL, 'raw', '2026-04-28 21:50:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:50:21'),
(226, 1, 1, 28.60, NULL, NULL, 'C', '2026-04-28 21:50:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:50:31'),
(227, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:50:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:50:31'),
(228, 6, 6, 3138.00, NULL, NULL, 'raw', '2026-04-28 21:50:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:50:31'),
(229, 1, 1, 28.60, NULL, NULL, 'C', '2026-04-28 21:50:41.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:50:41'),
(230, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:50:41.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:50:41'),
(231, 6, 6, 3136.00, NULL, NULL, 'raw', '2026-04-28 21:50:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:50:41'),
(232, 1, 1, 28.80, NULL, NULL, 'C', '2026-04-28 21:50:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:50:52'),
(233, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:50:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:50:52'),
(234, 6, 6, 3141.00, NULL, NULL, 'raw', '2026-04-28 21:50:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:50:52'),
(235, 1, 1, 28.60, NULL, NULL, 'C', '2026-04-28 21:51:02.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-28 19:51:02'),
(236, 2, 2, 24.00, NULL, NULL, '%', '2026-04-28 21:51:02.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-28 19:51:02'),
(237, 6, 6, 3125.00, NULL, NULL, 'raw', '2026-04-28 21:51:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-28 19:51:02'),
(238, 8, 8, 20.80, 20.80, NULL, 'C', '2026-04-29 17:06:40.903392', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-04-29 15:06:40'),
(239, 9, 9, 90.00, 90.00, NULL, '%', '2026-04-29 17:06:40.966671', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}', '2026-04-29 15:06:40'),
(240, 10, 10, 63.00, 63.00, NULL, '%', '2026-04-29 17:06:41.007220', 'simulado', '{\"sensor_name\": \"sensor_luz\"}', '2026-04-29 15:06:41'),
(241, 11, 11, 7.93, 7.93, NULL, 'C', '2026-04-29 17:06:41.043938', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}', '2026-04-29 15:06:41'),
(242, 8, 8, 22.74, 22.74, NULL, 'C', '2026-04-29 17:55:46.001066', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-04-29 15:55:46'),
(243, 9, 9, 65.00, 65.00, NULL, '%', '2026-04-29 17:55:46.029531', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}', '2026-04-29 15:55:46'),
(244, 10, 10, 25.00, 25.00, NULL, '%', '2026-04-29 17:55:46.058928', 'simulado', '{\"sensor_name\": \"sensor_luz\"}', '2026-04-29 15:55:46'),
(245, 11, 11, 4.35, 4.35, NULL, 'C', '2026-04-29 17:55:46.086521', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}', '2026-04-29 15:55:46'),
(246, 8, 8, 22.74, 22.74, NULL, 'C', '2026-04-29 17:55:47.972957', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-04-29 15:55:47'),
(247, 9, 9, 65.00, 65.00, NULL, '%', '2026-04-29 17:55:48.000662', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}', '2026-04-29 15:55:48'),
(248, 10, 10, 25.00, 25.00, NULL, '%', '2026-04-29 17:55:48.026611', 'simulado', '{\"sensor_name\": \"sensor_luz\"}', '2026-04-29 15:55:48'),
(249, 11, 11, 4.35, 4.35, NULL, 'C', '2026-04-29 17:55:48.052451', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}', '2026-04-29 15:55:48'),
(250, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:08:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:13'),
(251, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:08:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:13'),
(252, 6, 6, 2695.00, NULL, NULL, 'raw', '2026-04-30 18:08:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:13'),
(253, 5, 13, 59.17, NULL, NULL, 'cm', '2026-04-30 18:08:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:13'),
(254, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:08:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:18'),
(255, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:08:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:18'),
(256, 6, 6, 2691.00, NULL, NULL, 'raw', '2026-04-30 18:08:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:18'),
(257, 5, 13, 62.25, NULL, NULL, 'cm', '2026-04-30 18:08:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:18'),
(258, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:08:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:24'),
(259, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:08:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:24'),
(260, 6, 6, 2688.00, NULL, NULL, 'raw', '2026-04-30 18:08:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:24'),
(261, 5, 13, 49.65, NULL, NULL, 'cm', '2026-04-30 18:08:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:24'),
(262, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:08:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:29'),
(263, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:08:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:29'),
(264, 6, 6, 2701.00, NULL, NULL, 'raw', '2026-04-30 18:08:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:29'),
(265, 5, 13, 57.18, NULL, NULL, 'cm', '2026-04-30 18:08:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:29'),
(266, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:08:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:34'),
(267, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:08:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:34'),
(268, 6, 6, 2694.00, NULL, NULL, 'raw', '2026-04-30 18:08:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:34'),
(269, 5, 13, 65.65, NULL, NULL, 'cm', '2026-04-30 18:08:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:34'),
(270, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:08:39.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:39'),
(271, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:08:39.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:39'),
(272, 6, 6, 2678.00, NULL, NULL, 'raw', '2026-04-30 18:08:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:39'),
(273, 5, 13, 43.05, NULL, NULL, 'cm', '2026-04-30 18:08:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:39'),
(274, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:08:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:44'),
(275, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:08:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:44'),
(276, 6, 6, 2705.00, NULL, NULL, 'raw', '2026-04-30 18:08:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:44'),
(277, 5, 13, 17.63, NULL, NULL, 'cm', '2026-04-30 18:08:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:44'),
(278, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:08:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:50'),
(279, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:08:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:50'),
(280, 6, 6, 2689.00, NULL, NULL, 'raw', '2026-04-30 18:08:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:50'),
(281, 5, 13, 86.97, NULL, NULL, 'cm', '2026-04-30 18:08:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:50'),
(282, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:08:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:08:55'),
(283, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:08:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:08:55'),
(284, 6, 6, 2701.00, NULL, NULL, 'raw', '2026-04-30 18:08:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:08:55'),
(285, 5, 13, 71.14, NULL, NULL, 'cm', '2026-04-30 18:08:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:08:55'),
(286, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:09:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:00'),
(287, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:00'),
(288, 6, 6, 2692.00, NULL, NULL, 'raw', '2026-04-30 18:09:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:00'),
(289, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:09:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:00'),
(290, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:09:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:06'),
(291, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:06'),
(292, 6, 6, 2691.00, NULL, NULL, 'raw', '2026-04-30 18:09:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:06'),
(293, 5, 13, 43.25, NULL, NULL, 'cm', '2026-04-30 18:09:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:06'),
(294, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:09:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:11'),
(295, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:11'),
(296, 6, 6, 2694.00, NULL, NULL, 'raw', '2026-04-30 18:09:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:11'),
(297, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:09:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:11'),
(298, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:09:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:16'),
(299, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:16'),
(300, 6, 6, 2684.00, NULL, NULL, 'raw', '2026-04-30 18:09:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:16'),
(301, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:09:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:16'),
(302, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:09:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:21'),
(303, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:09:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:21'),
(304, 6, 6, 2683.00, NULL, NULL, 'raw', '2026-04-30 18:09:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:22'),
(305, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:09:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:22'),
(306, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:09:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:27'),
(307, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:09:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:27'),
(308, 6, 6, 2663.00, NULL, NULL, 'raw', '2026-04-30 18:09:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:27'),
(309, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:09:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:27'),
(310, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:09:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:32'),
(311, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:09:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:32'),
(312, 6, 6, 2706.00, NULL, NULL, 'raw', '2026-04-30 18:09:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:32'),
(313, 5, 13, 17.96, NULL, NULL, 'cm', '2026-04-30 18:09:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:32'),
(314, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:09:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:37'),
(315, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:37');
INSERT INTO `readings` (`id`, `device_id`, `sensor_type_id`, `reading_value`, `normalized_value`, `consumption_w`, `reading_unit`, `recorded_at`, `source`, `payload`, `created_at`) VALUES
(316, 6, 6, 2684.00, NULL, NULL, 'raw', '2026-04-30 18:09:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:37'),
(317, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:09:37.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:37'),
(318, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:09:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:42'),
(319, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:42'),
(320, 6, 6, 2667.00, NULL, NULL, 'raw', '2026-04-30 18:09:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:42'),
(321, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:09:42.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:42'),
(322, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:09:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:48'),
(323, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:48'),
(324, 6, 6, 2670.00, NULL, NULL, 'raw', '2026-04-30 18:09:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:48'),
(325, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:09:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:48'),
(326, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:09:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:53'),
(327, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:53'),
(328, 6, 6, 2688.00, NULL, NULL, 'raw', '2026-04-30 18:09:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:53'),
(329, 5, 13, 14.34, NULL, NULL, 'cm', '2026-04-30 18:09:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:53'),
(330, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:09:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:09:58'),
(331, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:09:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:09:58'),
(332, 6, 6, 2673.00, NULL, NULL, 'raw', '2026-04-30 18:09:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:09:58'),
(333, 5, 13, 14.68, NULL, NULL, 'cm', '2026-04-30 18:09:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:09:58'),
(334, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:10:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:03'),
(335, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:03'),
(336, 6, 6, 2682.00, NULL, NULL, 'raw', '2026-04-30 18:10:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:03'),
(337, 5, 13, 13.99, NULL, NULL, 'cm', '2026-04-30 18:10:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:03'),
(338, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:10:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:08'),
(339, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:08'),
(340, 6, 6, 2678.00, NULL, NULL, 'raw', '2026-04-30 18:10:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:08'),
(341, 5, 13, 12.62, NULL, NULL, 'cm', '2026-04-30 18:10:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:08'),
(342, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:10:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:14'),
(343, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:14'),
(344, 6, 6, 2673.00, NULL, NULL, 'raw', '2026-04-30 18:10:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:14'),
(345, 5, 13, 14.34, NULL, NULL, 'cm', '2026-04-30 18:10:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:14'),
(346, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:10:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:19'),
(347, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:19'),
(348, 6, 6, 2666.00, NULL, NULL, 'raw', '2026-04-30 18:10:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:19'),
(349, 5, 13, 15.02, NULL, NULL, 'cm', '2026-04-30 18:10:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:19'),
(350, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:10:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:24'),
(351, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:24'),
(352, 6, 6, 2682.00, NULL, NULL, 'raw', '2026-04-30 18:10:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:24'),
(353, 5, 13, 14.34, NULL, NULL, 'cm', '2026-04-30 18:10:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:24'),
(354, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:10:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:29'),
(355, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:29'),
(356, 6, 6, 2677.00, NULL, NULL, 'raw', '2026-04-30 18:10:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:29'),
(357, 5, 13, 15.37, NULL, NULL, 'cm', '2026-04-30 18:10:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:29'),
(358, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:10:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:35'),
(359, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:35'),
(360, 6, 6, 2672.00, NULL, NULL, 'raw', '2026-04-30 18:10:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:35'),
(361, 5, 13, 50.16, NULL, NULL, 'cm', '2026-04-30 18:10:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:35'),
(362, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:10:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:40'),
(363, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:40'),
(364, 6, 6, 2667.00, NULL, NULL, 'raw', '2026-04-30 18:10:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:40'),
(365, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:10:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:40'),
(366, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:10:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:45'),
(367, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:45'),
(368, 6, 6, 2661.00, NULL, NULL, 'raw', '2026-04-30 18:10:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:45'),
(369, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:10:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:10:45'),
(370, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:10:51.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:51'),
(371, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:51.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:51'),
(372, 6, 6, 2671.00, NULL, NULL, 'raw', '2026-04-30 18:10:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:51'),
(373, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:10:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:10:56'),
(374, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:10:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:10:56'),
(375, 6, 6, 2671.00, NULL, NULL, 'raw', '2026-04-30 18:10:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:10:56'),
(376, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:11:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:01'),
(377, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:01'),
(378, 6, 6, 2671.00, NULL, NULL, 'raw', '2026-04-30 18:11:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:01'),
(379, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:11:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:06'),
(380, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:06'),
(381, 6, 6, 2666.00, NULL, NULL, 'raw', '2026-04-30 18:11:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:06'),
(382, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:11:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:11'),
(383, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:11'),
(384, 6, 6, 2666.00, NULL, NULL, 'raw', '2026-04-30 18:11:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:11'),
(385, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:11:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:17'),
(386, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:17'),
(387, 6, 6, 2657.00, NULL, NULL, 'raw', '2026-04-30 18:11:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:17'),
(388, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:11:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:22'),
(389, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:22'),
(390, 6, 6, 2659.00, NULL, NULL, 'raw', '2026-04-30 18:11:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:22'),
(391, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:11:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:27'),
(392, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:27'),
(393, 6, 6, 2655.00, NULL, NULL, 'raw', '2026-04-30 18:11:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:27'),
(394, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:11:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:32'),
(395, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:32'),
(396, 6, 6, 2663.00, NULL, NULL, 'raw', '2026-04-30 18:11:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:32'),
(397, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:11:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:38'),
(398, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:38'),
(399, 6, 6, 2651.00, NULL, NULL, 'raw', '2026-04-30 18:11:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:38'),
(400, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:11:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:11:38'),
(401, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:11:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:43'),
(402, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:43'),
(403, 6, 6, 2672.00, NULL, NULL, 'raw', '2026-04-30 18:11:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:43'),
(404, 5, 13, 46.27, NULL, NULL, 'cm', '2026-04-30 18:11:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:11:43'),
(405, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:11:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:48'),
(406, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:11:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:48'),
(407, 6, 6, 2655.00, NULL, NULL, 'raw', '2026-04-30 18:11:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:48'),
(408, 5, 13, 17.97, NULL, NULL, 'cm', '2026-04-30 18:11:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:11:48'),
(409, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:11:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:53'),
(410, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:53'),
(411, 6, 6, 2647.00, NULL, NULL, 'raw', '2026-04-30 18:11:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:53'),
(412, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:11:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:11:53'),
(413, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:11:59.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:11:59'),
(414, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:11:59.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:11:59'),
(415, 6, 6, 2651.00, NULL, NULL, 'raw', '2026-04-30 18:11:59.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:11:59'),
(416, 5, 13, 12.28, NULL, NULL, 'cm', '2026-04-30 18:11:59.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:11:59'),
(417, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:12:04.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:04'),
(418, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:04.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:04'),
(419, 6, 6, 2661.00, NULL, NULL, 'raw', '2026-04-30 18:12:04.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:04'),
(420, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:12:04.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:04'),
(421, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:12:09.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:09'),
(422, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:09.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:09'),
(423, 6, 6, 2646.00, NULL, NULL, 'raw', '2026-04-30 18:12:09.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:09'),
(424, 5, 13, 56.46, NULL, NULL, 'cm', '2026-04-30 18:12:09.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:09'),
(425, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:12:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:14'),
(426, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:14'),
(427, 6, 6, 2649.00, NULL, NULL, 'raw', '2026-04-30 18:12:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:14'),
(428, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:12:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:14'),
(429, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:12:20.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:20'),
(430, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:20.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:20'),
(431, 6, 6, 2657.00, NULL, NULL, 'raw', '2026-04-30 18:12:20.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:20'),
(432, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:12:20.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:20'),
(433, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:12:25.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:25'),
(434, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:25.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:25'),
(435, 6, 6, 2645.00, NULL, NULL, 'raw', '2026-04-30 18:12:25.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:25'),
(436, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:12:25.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:25'),
(437, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:12:30.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:30'),
(438, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:30.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:30'),
(439, 6, 6, 2643.00, NULL, NULL, 'raw', '2026-04-30 18:12:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:30'),
(440, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:12:30.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:30'),
(441, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:12:36.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:36'),
(442, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:36.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:36'),
(443, 6, 6, 2641.00, NULL, NULL, 'raw', '2026-04-30 18:12:36.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:36'),
(444, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:12:36.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:36'),
(445, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:12:41.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:41'),
(446, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:41.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:41'),
(447, 6, 6, 2640.00, NULL, NULL, 'raw', '2026-04-30 18:12:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:41'),
(448, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:12:41.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:41'),
(449, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:12:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:47'),
(450, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:47'),
(451, 6, 6, 2641.00, NULL, NULL, 'raw', '2026-04-30 18:12:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:47'),
(452, 5, 13, 42.84, NULL, NULL, 'cm', '2026-04-30 18:12:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:47'),
(453, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:12:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:52'),
(454, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:52'),
(455, 6, 6, 2656.00, NULL, NULL, 'raw', '2026-04-30 18:12:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:52'),
(456, 5, 13, 15.71, NULL, NULL, 'cm', '2026-04-30 18:12:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:52'),
(457, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:12:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:12:57'),
(458, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:12:57.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:12:57'),
(459, 6, 6, 2657.00, NULL, NULL, 'raw', '2026-04-30 18:12:57.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:12:57'),
(460, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:12:57.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:12:57'),
(461, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:13:02.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:02'),
(462, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:02.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:02'),
(463, 6, 6, 2649.00, NULL, NULL, 'raw', '2026-04-30 18:13:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:02'),
(464, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:13:02.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:02'),
(465, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:13:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:08'),
(466, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:08'),
(467, 6, 6, 2653.00, NULL, NULL, 'raw', '2026-04-30 18:13:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:08'),
(468, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:13:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:08'),
(469, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:13:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:13'),
(470, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:13'),
(471, 6, 6, 2642.00, NULL, NULL, 'raw', '2026-04-30 18:13:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:13'),
(472, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:13:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:13'),
(473, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:13:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:18'),
(474, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:18'),
(475, 6, 6, 2638.00, NULL, NULL, 'raw', '2026-04-30 18:13:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:18'),
(476, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:13:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:18'),
(477, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:13:25.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:25'),
(478, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:25.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:25'),
(479, 6, 6, 2645.00, NULL, NULL, 'raw', '2026-04-30 18:13:25.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:25'),
(480, 5, 13, 49.67, NULL, NULL, 'cm', '2026-04-30 18:13:25.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:25'),
(481, 8, 8, 19.63, 19.63, NULL, 'C', '2026-04-30 18:13:26.956094', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-04-30 16:13:26'),
(482, 9, 9, 70.00, 70.00, NULL, '%', '2026-04-30 18:13:26.991055', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}', '2026-04-30 16:13:26'),
(483, 10, 10, 73.00, 73.00, NULL, '%', '2026-04-30 18:13:27.021620', 'simulado', '{\"sensor_name\": \"sensor_luz\"}', '2026-04-30 16:13:27'),
(484, 11, 11, 3.27, 3.27, NULL, 'C', '2026-04-30 18:13:27.052449', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}', '2026-04-30 16:13:27'),
(485, 8, 8, 19.63, 19.63, NULL, 'C', '2026-04-30 18:13:27.114099', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-04-30 16:13:27'),
(486, 9, 9, 70.00, 70.00, NULL, '%', '2026-04-30 18:13:27.144823', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}', '2026-04-30 16:13:27'),
(487, 10, 10, 73.00, 73.00, NULL, '%', '2026-04-30 18:13:27.175811', 'simulado', '{\"sensor_name\": \"sensor_luz\"}', '2026-04-30 16:13:27'),
(488, 11, 11, 3.27, 3.27, NULL, 'C', '2026-04-30 18:13:27.205648', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}', '2026-04-30 16:13:27'),
(489, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:13:30.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:30'),
(490, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:30.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:30'),
(491, 6, 6, 2624.00, NULL, NULL, 'raw', '2026-04-30 18:13:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:30'),
(492, 5, 13, 64.09, NULL, NULL, 'cm', '2026-04-30 18:13:30.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:30'),
(493, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:13:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:35'),
(494, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:35'),
(495, 6, 6, 2634.00, NULL, NULL, 'raw', '2026-04-30 18:13:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:35'),
(496, 5, 13, 17.96, NULL, NULL, 'cm', '2026-04-30 18:13:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:35'),
(497, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:13:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:40'),
(498, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:40'),
(499, 6, 6, 2641.00, NULL, NULL, 'raw', '2026-04-30 18:13:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:40'),
(500, 5, 13, 12.28, NULL, NULL, 'cm', '2026-04-30 18:13:41.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:41'),
(501, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:13:46.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:46'),
(502, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:46.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:46'),
(503, 6, 6, 2634.00, NULL, NULL, 'raw', '2026-04-30 18:13:46.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:46'),
(504, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:13:46.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:46'),
(505, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:13:51.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:51'),
(506, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:51.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:51'),
(507, 6, 6, 2635.00, NULL, NULL, 'raw', '2026-04-30 18:13:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:51'),
(508, 5, 13, 2.97, NULL, NULL, 'cm', '2026-04-30 18:13:51.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:51'),
(509, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:13:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:13:56'),
(510, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:13:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:13:56'),
(511, 6, 6, 2640.00, NULL, NULL, 'raw', '2026-04-30 18:13:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:13:56'),
(512, 5, 13, 5.90, NULL, NULL, 'cm', '2026-04-30 18:13:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:13:56'),
(513, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:14:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:01'),
(514, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:14:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:01'),
(515, 6, 6, 2637.00, NULL, NULL, 'raw', '2026-04-30 18:14:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:01'),
(516, 5, 13, 8.18, NULL, NULL, 'cm', '2026-04-30 18:14:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:01'),
(517, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:14:07.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:07'),
(518, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:07.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:07'),
(519, 6, 6, 2618.00, NULL, NULL, 'raw', '2026-04-30 18:14:07.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:07'),
(520, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:14:07.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:07'),
(521, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:14:12.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:12'),
(522, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:14:12.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:12'),
(523, 6, 6, 2631.00, NULL, NULL, 'raw', '2026-04-30 18:14:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:12'),
(524, 5, 13, 15.37, NULL, NULL, 'cm', '2026-04-30 18:14:12.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:12'),
(525, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:14:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:17'),
(526, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:14:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:17'),
(527, 6, 6, 2619.00, NULL, NULL, 'raw', '2026-04-30 18:14:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:17'),
(528, 5, 13, 15.37, NULL, NULL, 'cm', '2026-04-30 18:14:17.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:17'),
(529, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:14:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:22'),
(530, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:22'),
(531, 6, 6, 2629.00, NULL, NULL, 'raw', '2026-04-30 18:14:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:22'),
(532, 5, 13, 13.65, NULL, NULL, 'cm', '2026-04-30 18:14:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:22'),
(533, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:14:28.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:28'),
(534, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:28.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:28'),
(535, 6, 6, 2624.00, NULL, NULL, 'raw', '2026-04-30 18:14:28.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:28'),
(536, 5, 13, 13.65, NULL, NULL, 'cm', '2026-04-30 18:14:28.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:28'),
(537, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:14:33.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:33'),
(538, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:33.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:33'),
(539, 6, 6, 2623.00, NULL, NULL, 'raw', '2026-04-30 18:14:33.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:33'),
(540, 5, 13, 36.15, NULL, NULL, 'cm', '2026-04-30 18:14:33.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:33'),
(541, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:14:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:38'),
(542, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:38'),
(543, 6, 6, 2634.00, NULL, NULL, 'raw', '2026-04-30 18:14:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:38'),
(544, 5, 13, 23.03, NULL, NULL, 'cm', '2026-04-30 18:14:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:38'),
(545, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:14:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:44'),
(546, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:44'),
(547, 6, 6, 2624.00, NULL, NULL, 'raw', '2026-04-30 18:14:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:44'),
(548, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:14:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:44'),
(549, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:14:49.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:49'),
(550, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:49.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:49'),
(551, 6, 6, 2617.00, NULL, NULL, 'raw', '2026-04-30 18:14:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:49'),
(552, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:14:49.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:49'),
(553, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:14:54.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:54'),
(554, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:54.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:54'),
(555, 6, 6, 2631.00, NULL, NULL, 'raw', '2026-04-30 18:14:54.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:54'),
(556, 5, 13, 64.93, NULL, NULL, 'cm', '2026-04-30 18:14:54.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:54'),
(557, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:14:59.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:14:59'),
(558, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:14:59.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:14:59'),
(559, 6, 6, 2618.00, NULL, NULL, 'raw', '2026-04-30 18:14:59.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:14:59'),
(560, 5, 13, 61.26, NULL, NULL, 'cm', '2026-04-30 18:14:59.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:14:59'),
(561, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:15:04.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:04'),
(562, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:04.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:04'),
(563, 6, 6, 2619.00, NULL, NULL, 'raw', '2026-04-30 18:15:04.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:04'),
(564, 5, 13, 18.28, NULL, NULL, 'cm', '2026-04-30 18:15:04.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:04'),
(565, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:15:10.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:10'),
(566, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:10.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:10'),
(567, 6, 6, 2613.00, NULL, NULL, 'raw', '2026-04-30 18:15:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:10'),
(568, 5, 13, 60.97, NULL, NULL, 'cm', '2026-04-30 18:15:10.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:10'),
(569, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:15:15.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:15'),
(570, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:15.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:15'),
(571, 6, 6, 2618.00, NULL, NULL, 'raw', '2026-04-30 18:15:15.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:15'),
(572, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:15:15.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:15'),
(573, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:15:20.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:20'),
(574, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:20.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:20'),
(575, 6, 6, 2633.00, NULL, NULL, 'raw', '2026-04-30 18:15:20.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:20'),
(576, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:15:20.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:20'),
(577, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:15:25.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:25'),
(578, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:25.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:25'),
(579, 6, 6, 2621.00, NULL, NULL, 'raw', '2026-04-30 18:15:25.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:25'),
(580, 5, 13, 13.65, NULL, NULL, 'cm', '2026-04-30 18:15:25.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:25'),
(581, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:15:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:31'),
(582, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:31'),
(583, 6, 6, 2610.00, NULL, NULL, 'raw', '2026-04-30 18:15:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:31'),
(584, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:15:31.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:31'),
(585, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:15:36.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:36'),
(586, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:36.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:36'),
(587, 6, 6, 2624.00, NULL, NULL, 'raw', '2026-04-30 18:15:36.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:36'),
(588, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:15:36.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:36'),
(589, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:15:41.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:41'),
(590, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:41.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:41'),
(591, 6, 6, 2618.00, NULL, NULL, 'raw', '2026-04-30 18:15:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:41'),
(592, 5, 13, 18.28, NULL, NULL, 'cm', '2026-04-30 18:15:41.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:41'),
(593, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:15:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:47'),
(594, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:47'),
(595, 6, 6, 2622.00, NULL, NULL, 'raw', '2026-04-30 18:15:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:47'),
(596, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:15:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:47'),
(597, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:15:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:52'),
(598, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:52'),
(599, 6, 6, 2608.00, NULL, NULL, 'raw', '2026-04-30 18:15:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:52'),
(600, 5, 13, 14.34, NULL, NULL, 'cm', '2026-04-30 18:15:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:52'),
(601, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:15:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:15:57'),
(602, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:15:57.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:15:57'),
(603, 6, 6, 2614.00, NULL, NULL, 'raw', '2026-04-30 18:15:57.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:15:57'),
(604, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:15:57.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:15:57'),
(605, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:16:02.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:02'),
(606, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:02.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:02'),
(607, 6, 6, 2602.00, NULL, NULL, 'raw', '2026-04-30 18:16:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:02'),
(608, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:16:02.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:02'),
(609, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:16:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:08'),
(610, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:08'),
(611, 6, 6, 2623.00, NULL, NULL, 'raw', '2026-04-30 18:16:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:08'),
(612, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:16:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:08'),
(613, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:16:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:13'),
(614, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:13'),
(615, 6, 6, 2618.00, NULL, NULL, 'raw', '2026-04-30 18:16:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:13'),
(616, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:16:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:13'),
(617, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:16:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:18'),
(618, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:18'),
(619, 6, 6, 2609.00, NULL, NULL, 'raw', '2026-04-30 18:16:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:18'),
(620, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:16:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:18'),
(621, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:16:23.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:23'),
(622, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:23.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:23'),
(623, 6, 6, 2613.00, NULL, NULL, 'raw', '2026-04-30 18:16:23.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:23'),
(624, 5, 13, 37.54, NULL, NULL, 'cm', '2026-04-30 18:16:23.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:23'),
(625, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:16:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:29'),
(626, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:29'),
(627, 6, 6, 2604.00, NULL, NULL, 'raw', '2026-04-30 18:16:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:29'),
(628, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:16:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:29'),
(629, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:16:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:34');
INSERT INTO `readings` (`id`, `device_id`, `sensor_type_id`, `reading_value`, `normalized_value`, `consumption_w`, `reading_unit`, `recorded_at`, `source`, `payload`, `created_at`) VALUES
(630, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:34'),
(631, 6, 6, 2592.00, NULL, NULL, 'raw', '2026-04-30 18:16:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:34'),
(632, 5, 13, 56.47, NULL, NULL, 'cm', '2026-04-30 18:16:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:34'),
(633, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:16:39.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:39'),
(634, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:39.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:39'),
(635, 6, 6, 2613.00, NULL, NULL, 'raw', '2026-04-30 18:16:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:39'),
(636, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:16:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:39'),
(637, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:16:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:45'),
(638, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:45'),
(639, 6, 6, 2605.00, NULL, NULL, 'raw', '2026-04-30 18:16:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:45'),
(640, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:16:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:45'),
(641, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:16:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:50'),
(642, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:50'),
(643, 6, 6, 2605.00, NULL, NULL, 'raw', '2026-04-30 18:16:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:50'),
(644, 5, 13, 12.97, NULL, NULL, 'cm', '2026-04-30 18:16:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:50'),
(645, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:16:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:16:55'),
(646, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:16:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:16:55'),
(647, 6, 6, 2606.00, NULL, NULL, 'raw', '2026-04-30 18:16:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:16:55'),
(648, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:16:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:16:55'),
(649, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:17:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:01'),
(650, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:17:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:01'),
(651, 6, 6, 2603.00, NULL, NULL, 'raw', '2026-04-30 18:17:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:01'),
(652, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:17:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:01'),
(653, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:17:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:06'),
(654, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:17:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:06'),
(655, 6, 6, 2597.00, NULL, NULL, 'raw', '2026-04-30 18:17:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:06'),
(656, 5, 13, 5.90, NULL, NULL, 'cm', '2026-04-30 18:17:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:06'),
(657, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:17:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:11'),
(658, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:17:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:11'),
(659, 6, 6, 2607.00, NULL, NULL, 'raw', '2026-04-30 18:17:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:11'),
(660, 5, 13, 3.29, NULL, NULL, 'cm', '2026-04-30 18:17:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:11'),
(661, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:17:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:16'),
(662, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:17:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:16'),
(663, 6, 6, 2594.00, NULL, NULL, 'raw', '2026-04-30 18:17:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:16'),
(664, 5, 13, 16.34, NULL, NULL, 'cm', '2026-04-30 18:17:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:16'),
(665, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:17:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:22'),
(666, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:17:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:22'),
(667, 6, 6, 2607.00, NULL, NULL, 'raw', '2026-04-30 18:17:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:22'),
(668, 5, 13, 4.60, NULL, NULL, 'cm', '2026-04-30 18:17:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:22'),
(669, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:17:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:27'),
(670, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:17:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:27'),
(671, 6, 6, 2607.00, NULL, NULL, 'raw', '2026-04-30 18:17:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:27'),
(672, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:17:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:27'),
(673, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:17:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:32'),
(674, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:17:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:32'),
(675, 6, 6, 2599.00, NULL, NULL, 'raw', '2026-04-30 18:17:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:32'),
(676, 5, 13, 46.08, NULL, NULL, 'cm', '2026-04-30 18:17:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:32'),
(677, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:17:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:38'),
(678, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:17:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:38'),
(679, 6, 6, 2608.00, NULL, NULL, 'raw', '2026-04-30 18:17:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:38'),
(680, 5, 13, 45.67, NULL, NULL, 'cm', '2026-04-30 18:17:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:38'),
(681, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:17:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:43'),
(682, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:17:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:43'),
(683, 6, 6, 2608.00, NULL, NULL, 'raw', '2026-04-30 18:17:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:43'),
(684, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:17:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:43'),
(685, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:17:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:48'),
(686, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:17:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:48'),
(687, 6, 6, 2608.00, NULL, NULL, 'raw', '2026-04-30 18:17:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:49'),
(688, 5, 13, 56.61, NULL, NULL, 'cm', '2026-04-30 18:17:49.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:49'),
(689, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:17:54.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:54'),
(690, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:17:54.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:54'),
(691, 6, 6, 2598.00, NULL, NULL, 'raw', '2026-04-30 18:17:54.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:54'),
(692, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:17:59.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:17:59'),
(693, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:17:59.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:17:59'),
(694, 6, 6, 2608.00, NULL, NULL, 'raw', '2026-04-30 18:17:59.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:17:59'),
(695, 5, 13, 57.32, NULL, NULL, 'cm', '2026-04-30 18:17:59.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:17:59'),
(696, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:18:05.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:05'),
(697, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:18:05.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:05'),
(698, 6, 6, 2607.00, NULL, NULL, 'raw', '2026-04-30 18:18:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:05'),
(699, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:18:05.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:05'),
(700, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:18:10.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:10'),
(701, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:18:10.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:10'),
(702, 6, 6, 2595.00, NULL, NULL, 'raw', '2026-04-30 18:18:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:10'),
(703, 5, 13, 4.60, NULL, NULL, 'cm', '2026-04-30 18:18:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:11'),
(704, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:18:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:16'),
(705, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:18:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:16'),
(706, 6, 6, 2598.00, NULL, NULL, 'raw', '2026-04-30 18:18:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:16'),
(707, 5, 13, 5.90, NULL, NULL, 'cm', '2026-04-30 18:18:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:16'),
(708, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:18:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:21'),
(709, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:18:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:21'),
(710, 6, 6, 2586.00, NULL, NULL, 'raw', '2026-04-30 18:18:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:21'),
(711, 5, 13, 19.57, NULL, NULL, 'cm', '2026-04-30 18:18:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:21'),
(712, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:18:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:26'),
(713, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:18:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:26'),
(714, 6, 6, 2604.00, NULL, NULL, 'raw', '2026-04-30 18:18:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:26'),
(715, 5, 13, 69.97, NULL, NULL, 'cm', '2026-04-30 18:18:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:26'),
(716, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:18:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:32'),
(717, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:18:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:32'),
(718, 6, 6, 2601.00, NULL, NULL, 'raw', '2026-04-30 18:18:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:32'),
(719, 5, 13, 14.34, NULL, NULL, 'cm', '2026-04-30 18:18:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:32'),
(720, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:18:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:37'),
(721, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:18:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:37'),
(722, 6, 6, 2592.00, NULL, NULL, 'raw', '2026-04-30 18:18:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:37'),
(723, 5, 13, 15.71, NULL, NULL, 'cm', '2026-04-30 18:18:37.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:37'),
(724, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:18:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:42'),
(725, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:18:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:42'),
(726, 6, 6, 2587.00, NULL, NULL, 'raw', '2026-04-30 18:18:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:42'),
(727, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:18:42.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:42'),
(728, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:18:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:47'),
(729, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:18:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:47'),
(730, 6, 6, 2606.00, NULL, NULL, 'raw', '2026-04-30 18:18:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:47'),
(731, 5, 13, 16.34, NULL, NULL, 'cm', '2026-04-30 18:18:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:47'),
(732, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:18:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:52'),
(733, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:18:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:52'),
(734, 6, 6, 2593.00, NULL, NULL, 'raw', '2026-04-30 18:18:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:52'),
(735, 5, 13, 15.71, NULL, NULL, 'cm', '2026-04-30 18:18:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:52'),
(736, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:18:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:18:58'),
(737, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:18:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:18:58'),
(738, 6, 6, 2586.00, NULL, NULL, 'raw', '2026-04-30 18:18:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:18:58'),
(739, 5, 13, 14.68, NULL, NULL, 'cm', '2026-04-30 18:18:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:18:58'),
(740, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:19:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:03'),
(741, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:03'),
(742, 6, 6, 2595.00, NULL, NULL, 'raw', '2026-04-30 18:19:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:03'),
(743, 5, 13, 15.71, NULL, NULL, 'cm', '2026-04-30 18:19:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:03'),
(744, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:19:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:08'),
(745, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:08'),
(746, 6, 6, 2604.00, NULL, NULL, 'raw', '2026-04-30 18:19:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:08'),
(747, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:19:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:08'),
(748, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:19:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:14'),
(749, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:14'),
(750, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:19:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:14'),
(751, 5, 13, 15.71, NULL, NULL, 'cm', '2026-04-30 18:19:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:14'),
(752, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:19:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:19'),
(753, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:19'),
(754, 6, 6, 2590.00, NULL, NULL, 'raw', '2026-04-30 18:19:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:19'),
(755, 5, 13, 20.84, NULL, NULL, 'cm', '2026-04-30 18:19:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:19'),
(756, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:19:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:24'),
(757, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:24'),
(758, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:19:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:24'),
(759, 5, 13, 14.68, NULL, NULL, 'cm', '2026-04-30 18:19:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:24'),
(760, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:19:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:29'),
(761, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:29'),
(762, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:19:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:29'),
(763, 5, 13, 20.85, NULL, NULL, 'cm', '2026-04-30 18:19:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:29'),
(764, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:19:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:35'),
(765, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:35'),
(766, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:19:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:35'),
(767, 5, 13, 20.84, NULL, NULL, 'cm', '2026-04-30 18:19:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:35'),
(768, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:19:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:40'),
(769, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:40'),
(770, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:19:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:40'),
(771, 5, 13, 19.55, NULL, NULL, 'cm', '2026-04-30 18:19:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:40'),
(772, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:19:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:45'),
(773, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:45'),
(774, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:19:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:45'),
(775, 5, 13, 19.57, NULL, NULL, 'cm', '2026-04-30 18:19:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:45'),
(776, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:19:51.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:51'),
(777, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:51.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:51'),
(778, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:19:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:51'),
(779, 5, 13, 49.82, NULL, NULL, 'cm', '2026-04-30 18:19:51.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:51'),
(780, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:19:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:19:56'),
(781, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:19:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:19:56'),
(782, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:19:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:19:56'),
(783, 5, 13, 19.57, NULL, NULL, 'cm', '2026-04-30 18:19:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:19:56'),
(784, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:20:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:01'),
(785, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:01'),
(786, 6, 6, 2579.00, NULL, NULL, 'raw', '2026-04-30 18:20:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:01'),
(787, 5, 13, 19.55, NULL, NULL, 'cm', '2026-04-30 18:20:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:01'),
(788, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:20:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:06'),
(789, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:06'),
(790, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:20:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:06'),
(791, 5, 13, 19.57, NULL, NULL, 'cm', '2026-04-30 18:20:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:06'),
(792, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:20:12.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:12'),
(793, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:12.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:12'),
(794, 6, 6, 2586.00, NULL, NULL, 'raw', '2026-04-30 18:20:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:12'),
(795, 5, 13, 20.84, NULL, NULL, 'cm', '2026-04-30 18:20:12.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:12'),
(796, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:20:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:17'),
(797, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:17'),
(798, 6, 6, 2577.00, NULL, NULL, 'raw', '2026-04-30 18:20:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:17'),
(799, 5, 13, 64.38, NULL, NULL, 'cm', '2026-04-30 18:20:17.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:17'),
(800, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:20:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:22'),
(801, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:22'),
(802, 6, 6, 2587.00, NULL, NULL, 'raw', '2026-04-30 18:20:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:22'),
(803, 5, 13, 49.98, NULL, NULL, 'cm', '2026-04-30 18:20:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:22'),
(804, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:20:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:27'),
(805, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:27'),
(806, 6, 6, 2585.00, NULL, NULL, 'raw', '2026-04-30 18:20:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:27'),
(807, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:20:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:27'),
(808, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:20:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:32'),
(809, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:32'),
(810, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:20:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:32'),
(811, 5, 13, 19.55, NULL, NULL, 'cm', '2026-04-30 18:20:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:32'),
(812, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:20:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:38'),
(813, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:38'),
(814, 6, 6, 2582.00, NULL, NULL, 'raw', '2026-04-30 18:20:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:38'),
(815, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:20:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:38'),
(816, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:20:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:44'),
(817, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:44'),
(818, 6, 6, 2550.00, NULL, NULL, 'raw', '2026-04-30 18:20:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:44'),
(819, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:20:49.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:49'),
(820, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:49.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:49'),
(821, 6, 6, 2555.00, NULL, NULL, 'raw', '2026-04-30 18:20:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:49'),
(822, 5, 13, 18.28, NULL, NULL, 'cm', '2026-04-30 18:20:49.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:49'),
(823, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:20:54.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:20:54'),
(824, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:20:54.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:20:54'),
(825, 6, 6, 2550.00, NULL, NULL, 'raw', '2026-04-30 18:20:54.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:20:54'),
(826, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:20:54.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:20:54'),
(827, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:21:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:00'),
(828, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:00'),
(829, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:21:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:00'),
(830, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:21:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:00'),
(831, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:21:05.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:05'),
(832, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:05.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:05'),
(833, 6, 6, 2558.00, NULL, NULL, 'raw', '2026-04-30 18:21:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:05'),
(834, 5, 13, 79.15, NULL, NULL, 'cm', '2026-04-30 18:21:05.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:05'),
(835, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:21:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:11'),
(836, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:11'),
(837, 6, 6, 2546.00, NULL, NULL, 'raw', '2026-04-30 18:21:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:11'),
(838, 5, 13, 18.28, NULL, NULL, 'cm', '2026-04-30 18:21:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:11'),
(839, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:21:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:16'),
(840, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:16'),
(841, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:21:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:16'),
(842, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 18:21:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:16'),
(843, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:21:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:21'),
(844, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:21'),
(845, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:21:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:21'),
(846, 5, 13, 19.55, NULL, NULL, 'cm', '2026-04-30 18:21:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:21'),
(847, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:21:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:26'),
(848, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:26'),
(849, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:21:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:26'),
(850, 5, 13, 20.85, NULL, NULL, 'cm', '2026-04-30 18:21:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:26'),
(851, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:21:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:31'),
(852, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:31'),
(853, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:21:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:31'),
(854, 5, 13, 44.68, NULL, NULL, 'cm', '2026-04-30 18:21:31.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:31'),
(855, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:21:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:37'),
(856, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:37'),
(857, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:21:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:37'),
(858, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:21:37.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:37'),
(859, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:21:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:42'),
(860, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:42'),
(861, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:21:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:42'),
(862, 5, 13, 20.84, NULL, NULL, 'cm', '2026-04-30 18:21:42.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:42'),
(863, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:21:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:47'),
(864, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:47'),
(865, 6, 6, 2544.00, NULL, NULL, 'raw', '2026-04-30 18:21:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:47'),
(866, 5, 13, 19.57, NULL, NULL, 'cm', '2026-04-30 18:21:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:47'),
(867, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:21:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:52'),
(868, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:52'),
(869, 6, 6, 2547.00, NULL, NULL, 'raw', '2026-04-30 18:21:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:52'),
(870, 5, 13, 19.57, NULL, NULL, 'cm', '2026-04-30 18:21:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:52'),
(871, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:21:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:21:57'),
(872, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:21:57.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:21:57'),
(873, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:21:57.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:21:57'),
(874, 5, 13, 64.81, NULL, NULL, 'cm', '2026-04-30 18:21:57.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:21:57'),
(875, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:22:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:03'),
(876, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:22:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:03'),
(877, 6, 6, 2551.00, NULL, NULL, 'raw', '2026-04-30 18:22:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:03'),
(878, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:22:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:03'),
(879, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:22:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:08'),
(880, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:22:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:08'),
(881, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:22:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:08'),
(882, 5, 13, 18.28, NULL, NULL, 'cm', '2026-04-30 18:22:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:08'),
(883, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:22:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:13'),
(884, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:22:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:13'),
(885, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:22:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:13'),
(886, 5, 13, 44.25, NULL, NULL, 'cm', '2026-04-30 18:22:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:13'),
(887, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:22:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:18'),
(888, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:22:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:18'),
(889, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:22:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:18'),
(890, 5, 13, 18.59, NULL, NULL, 'cm', '2026-04-30 18:22:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:18'),
(891, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:22:23.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:23'),
(892, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:22:23.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:23'),
(893, 6, 6, 2553.00, NULL, NULL, 'raw', '2026-04-30 18:22:23.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:23'),
(894, 5, 13, 47.47, NULL, NULL, 'cm', '2026-04-30 18:22:23.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:23'),
(895, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:22:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:29'),
(896, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:22:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:29'),
(897, 6, 6, 2545.00, NULL, NULL, 'raw', '2026-04-30 18:22:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:29'),
(898, 5, 13, 58.16, NULL, NULL, 'cm', '2026-04-30 18:22:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:29'),
(899, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:22:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:34'),
(900, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:22:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:34'),
(901, 6, 6, 2535.00, NULL, NULL, 'raw', '2026-04-30 18:22:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:34'),
(902, 5, 13, 18.28, NULL, NULL, 'cm', '2026-04-30 18:22:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:34'),
(903, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:22:39.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:39'),
(904, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:22:39.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:39'),
(905, 6, 6, 2550.00, NULL, NULL, 'raw', '2026-04-30 18:22:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:39'),
(906, 5, 13, 44.86, NULL, NULL, 'cm', '2026-04-30 18:22:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:39'),
(907, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:22:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:44'),
(908, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:22:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:44'),
(909, 6, 6, 2559.00, NULL, NULL, 'raw', '2026-04-30 18:22:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:44'),
(910, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:22:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:44'),
(911, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:22:49.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:49'),
(912, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:22:49.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:49'),
(913, 6, 6, 2544.00, NULL, NULL, 'raw', '2026-04-30 18:22:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:49'),
(914, 5, 13, 45.28, NULL, NULL, 'cm', '2026-04-30 18:22:49.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:49'),
(915, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:22:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:22:57'),
(916, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:22:57.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:22:57'),
(917, 6, 6, 2556.00, NULL, NULL, 'raw', '2026-04-30 18:22:57.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:22:57'),
(918, 5, 13, 51.02, NULL, NULL, 'cm', '2026-04-30 18:22:57.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:22:57'),
(919, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:23:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:23:03'),
(920, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:23:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:23:03'),
(921, 6, 6, 2543.00, NULL, NULL, 'raw', '2026-04-30 18:23:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:23:03'),
(922, 5, 13, 12.97, NULL, NULL, 'cm', '2026-04-30 18:23:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:23:03'),
(923, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:23:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:23:08'),
(924, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:23:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:23:08'),
(925, 6, 6, 2554.00, NULL, NULL, 'raw', '2026-04-30 18:23:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:23:08'),
(926, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:23:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:23:08'),
(927, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:23:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:23:13'),
(928, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:23:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:23:13'),
(929, 6, 6, 2545.00, NULL, NULL, 'raw', '2026-04-30 18:23:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:23:13'),
(930, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:23:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:23:13'),
(931, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:24:09.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:09'),
(932, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:09.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:09'),
(933, 6, 6, 2532.00, NULL, NULL, 'raw', '2026-04-30 18:24:09.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:09'),
(934, 5, 13, 42.86, NULL, NULL, 'cm', '2026-04-30 18:24:09.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:09'),
(935, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:24:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:14'),
(936, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:14'),
(937, 6, 6, 2539.00, NULL, NULL, 'raw', '2026-04-30 18:24:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:14'),
(938, 5, 13, 53.92, NULL, NULL, 'cm', '2026-04-30 18:24:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:14'),
(939, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:24:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:19'),
(940, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:19'),
(941, 6, 6, 2542.00, NULL, NULL, 'raw', '2026-04-30 18:24:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:19'),
(942, 5, 13, 12.97, NULL, NULL, 'cm', '2026-04-30 18:24:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:19');
INSERT INTO `readings` (`id`, `device_id`, `sensor_type_id`, `reading_value`, `normalized_value`, `consumption_w`, `reading_unit`, `recorded_at`, `source`, `payload`, `created_at`) VALUES
(943, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:24:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:24'),
(944, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:24'),
(945, 6, 6, 2533.00, NULL, NULL, 'raw', '2026-04-30 18:24:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:24'),
(946, 5, 13, 13.99, NULL, NULL, 'cm', '2026-04-30 18:24:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:24'),
(947, 1, 1, 30.00, NULL, NULL, 'C', '2026-04-30 18:24:30.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:30'),
(948, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:30.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:30'),
(949, 6, 6, 2537.00, NULL, NULL, 'raw', '2026-04-30 18:24:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:30'),
(950, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:24:30.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:30'),
(951, 1, 1, 30.40, NULL, NULL, 'C', '2026-04-30 18:24:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:35'),
(952, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:35'),
(953, 6, 6, 2530.00, NULL, NULL, 'raw', '2026-04-30 18:24:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:35'),
(954, 5, 13, 22.74, NULL, NULL, 'cm', '2026-04-30 18:24:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:35'),
(955, 1, 1, 30.50, NULL, NULL, 'C', '2026-04-30 18:24:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:40'),
(956, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:40'),
(957, 6, 6, 2529.00, NULL, NULL, 'raw', '2026-04-30 18:24:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:40'),
(958, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:24:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:40'),
(959, 1, 1, 30.50, NULL, NULL, 'C', '2026-04-30 18:24:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:45'),
(960, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:45'),
(961, 6, 6, 2534.00, NULL, NULL, 'raw', '2026-04-30 18:24:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:45'),
(962, 5, 13, 3.29, NULL, NULL, 'cm', '2026-04-30 18:24:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:45'),
(963, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-30 18:24:51.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:51'),
(964, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:51.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:51'),
(965, 6, 6, 2543.00, NULL, NULL, 'raw', '2026-04-30 18:24:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:51'),
(966, 5, 13, 56.73, NULL, NULL, 'cm', '2026-04-30 18:24:51.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:51'),
(967, 1, 1, 30.10, NULL, NULL, 'C', '2026-04-30 18:24:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:24:56'),
(968, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:24:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:24:56'),
(969, 6, 6, 2523.00, NULL, NULL, 'raw', '2026-04-30 18:24:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:24:56'),
(970, 5, 13, 16.98, NULL, NULL, 'cm', '2026-04-30 18:24:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:24:56'),
(971, 1, 1, 30.20, NULL, NULL, 'C', '2026-04-30 18:25:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:01'),
(972, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:01'),
(973, 6, 6, 2538.00, NULL, NULL, 'raw', '2026-04-30 18:25:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:01'),
(974, 5, 13, 13.99, NULL, NULL, 'cm', '2026-04-30 18:25:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:01'),
(975, 1, 1, 30.40, NULL, NULL, 'C', '2026-04-30 18:25:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:06'),
(976, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:06'),
(977, 6, 6, 2529.00, NULL, NULL, 'raw', '2026-04-30 18:25:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:06'),
(978, 5, 13, 15.37, NULL, NULL, 'cm', '2026-04-30 18:25:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:06'),
(979, 1, 1, 30.40, NULL, NULL, 'C', '2026-04-30 18:25:12.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:12'),
(980, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:12.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:12'),
(981, 6, 6, 2527.00, NULL, NULL, 'raw', '2026-04-30 18:25:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:12'),
(982, 5, 13, 19.89, NULL, NULL, 'cm', '2026-04-30 18:25:12.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:12'),
(983, 1, 1, 30.50, NULL, NULL, 'C', '2026-04-30 18:25:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:17'),
(984, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:17'),
(985, 6, 6, 2526.00, NULL, NULL, 'raw', '2026-04-30 18:25:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:17'),
(986, 5, 13, 16.34, NULL, NULL, 'cm', '2026-04-30 18:25:17.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:17'),
(987, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-30 18:25:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:22'),
(988, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:22'),
(989, 6, 6, 2519.00, NULL, NULL, 'raw', '2026-04-30 18:25:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:22'),
(990, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 18:25:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:22'),
(991, 1, 1, 30.50, NULL, NULL, 'C', '2026-04-30 18:25:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:27'),
(992, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:27'),
(993, 6, 6, 2523.00, NULL, NULL, 'raw', '2026-04-30 18:25:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:27'),
(994, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:25:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:27'),
(995, 1, 1, 30.00, NULL, NULL, 'C', '2026-04-30 18:25:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:32'),
(996, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:32'),
(997, 6, 6, 2530.00, NULL, NULL, 'raw', '2026-04-30 18:25:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:32'),
(998, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:25:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:32'),
(999, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-30 18:25:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:38'),
(1000, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:38'),
(1001, 6, 6, 2525.00, NULL, NULL, 'raw', '2026-04-30 18:25:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:38'),
(1002, 5, 13, 15.71, NULL, NULL, 'cm', '2026-04-30 18:25:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:38'),
(1003, 1, 1, 30.70, NULL, NULL, 'C', '2026-04-30 18:25:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:43'),
(1004, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:43'),
(1005, 6, 6, 2518.00, NULL, NULL, 'raw', '2026-04-30 18:25:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:43'),
(1006, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:25:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:43'),
(1007, 1, 1, 30.20, NULL, NULL, 'C', '2026-04-30 18:25:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:48'),
(1008, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:48'),
(1009, 6, 6, 2522.00, NULL, NULL, 'raw', '2026-04-30 18:25:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:48'),
(1010, 5, 13, 70.86, NULL, NULL, 'cm', '2026-04-30 18:25:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:48'),
(1011, 1, 1, 30.60, NULL, NULL, 'C', '2026-04-30 18:25:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:53'),
(1012, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:53'),
(1013, 6, 6, 2514.00, NULL, NULL, 'raw', '2026-04-30 18:25:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:53'),
(1014, 5, 13, 20.53, NULL, NULL, 'cm', '2026-04-30 18:25:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:53'),
(1015, 1, 1, 30.70, NULL, NULL, 'C', '2026-04-30 18:25:59.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:25:59'),
(1016, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:25:59.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:25:59'),
(1017, 6, 6, 2531.00, NULL, NULL, 'raw', '2026-04-30 18:25:59.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:25:59'),
(1018, 5, 13, 72.85, NULL, NULL, 'cm', '2026-04-30 18:25:59.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:25:59'),
(1019, 1, 1, 30.10, NULL, NULL, 'C', '2026-04-30 18:26:04.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:04'),
(1020, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:04.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:04'),
(1021, 6, 6, 2513.00, NULL, NULL, 'raw', '2026-04-30 18:26:04.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:04'),
(1022, 5, 13, 50.85, NULL, NULL, 'cm', '2026-04-30 18:26:04.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:04'),
(1023, 1, 1, 30.70, NULL, NULL, 'C', '2026-04-30 18:26:09.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:09'),
(1024, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:09.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:09'),
(1025, 6, 6, 2517.00, NULL, NULL, 'raw', '2026-04-30 18:26:09.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:09'),
(1026, 5, 13, 20.53, NULL, NULL, 'cm', '2026-04-30 18:26:09.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:09'),
(1027, 1, 1, 30.40, NULL, NULL, 'C', '2026-04-30 18:26:15.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:15'),
(1028, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:15.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:15'),
(1029, 6, 6, 2529.00, NULL, NULL, 'raw', '2026-04-30 18:26:15.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:15'),
(1030, 5, 13, 20.53, NULL, NULL, 'cm', '2026-04-30 18:26:15.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:15'),
(1031, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:26:20.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:20'),
(1032, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:20.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:20'),
(1033, 6, 6, 2528.00, NULL, NULL, 'raw', '2026-04-30 18:26:20.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:20'),
(1034, 5, 13, 20.53, NULL, NULL, 'cm', '2026-04-30 18:26:20.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:20'),
(1035, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-30 18:26:25.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:25'),
(1036, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:25.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:25'),
(1037, 6, 6, 2523.00, NULL, NULL, 'raw', '2026-04-30 18:26:25.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:25'),
(1038, 5, 13, 19.24, NULL, NULL, 'cm', '2026-04-30 18:26:25.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:25'),
(1039, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:26:30.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:30'),
(1040, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:30.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:30'),
(1041, 6, 6, 2513.00, NULL, NULL, 'raw', '2026-04-30 18:26:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:30'),
(1042, 5, 13, 20.53, NULL, NULL, 'cm', '2026-04-30 18:26:30.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:30'),
(1043, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-30 18:26:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:35'),
(1044, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:35'),
(1045, 6, 6, 2516.00, NULL, NULL, 'raw', '2026-04-30 18:26:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:35'),
(1046, 5, 13, 19.24, NULL, NULL, 'cm', '2026-04-30 18:26:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:35'),
(1047, 1, 1, 30.70, NULL, NULL, 'C', '2026-04-30 18:26:41.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:41'),
(1048, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:41.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:41'),
(1049, 6, 6, 2515.00, NULL, NULL, 'raw', '2026-04-30 18:26:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:41'),
(1050, 5, 13, 19.23, NULL, NULL, 'cm', '2026-04-30 18:26:41.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:41'),
(1051, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:26:46.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:46'),
(1052, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:46.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:46'),
(1053, 6, 6, 2523.00, NULL, NULL, 'raw', '2026-04-30 18:26:46.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:46'),
(1054, 5, 13, 19.26, NULL, NULL, 'cm', '2026-04-30 18:26:46.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:46'),
(1055, 1, 1, 30.40, NULL, NULL, 'C', '2026-04-30 18:26:51.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:51'),
(1056, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:51.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:51'),
(1057, 6, 6, 2512.00, NULL, NULL, 'raw', '2026-04-30 18:26:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:51'),
(1058, 5, 13, 19.24, NULL, NULL, 'cm', '2026-04-30 18:26:51.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:51'),
(1059, 1, 1, 30.40, NULL, NULL, 'C', '2026-04-30 18:26:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:26:56'),
(1060, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:26:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:26:56'),
(1061, 6, 6, 2531.00, NULL, NULL, 'raw', '2026-04-30 18:26:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:26:56'),
(1062, 5, 13, 19.24, NULL, NULL, 'cm', '2026-04-30 18:26:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:26:56'),
(1063, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:27:02.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:02'),
(1064, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:02.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:02'),
(1065, 6, 6, 2499.00, NULL, NULL, 'raw', '2026-04-30 18:27:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:02'),
(1066, 5, 13, 19.24, NULL, NULL, 'cm', '2026-04-30 18:27:02.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:02'),
(1067, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:27:07.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:07'),
(1068, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:07.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:07'),
(1069, 6, 6, 2511.00, NULL, NULL, 'raw', '2026-04-30 18:27:07.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:07'),
(1070, 5, 13, 20.53, NULL, NULL, 'cm', '2026-04-30 18:27:07.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:07'),
(1071, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:27:12.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:12'),
(1072, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:12.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:12'),
(1073, 6, 6, 2525.00, NULL, NULL, 'raw', '2026-04-30 18:27:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:12'),
(1074, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:27:12.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:12'),
(1075, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:27:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:18'),
(1076, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:18'),
(1077, 6, 6, 2524.00, NULL, NULL, 'raw', '2026-04-30 18:27:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:18'),
(1078, 5, 13, 67.47, NULL, NULL, 'cm', '2026-04-30 18:27:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:18'),
(1079, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:27:23.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:23'),
(1080, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:23.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:23'),
(1081, 6, 6, 2515.00, NULL, NULL, 'raw', '2026-04-30 18:27:23.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:23'),
(1082, 5, 13, 49.99, NULL, NULL, 'cm', '2026-04-30 18:27:23.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:23'),
(1083, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:27:28.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:28'),
(1084, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:28.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:28'),
(1085, 6, 6, 2521.00, NULL, NULL, 'raw', '2026-04-30 18:27:28.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:28'),
(1086, 5, 13, 19.24, NULL, NULL, 'cm', '2026-04-30 18:27:28.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:28'),
(1087, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:27:33.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:33'),
(1088, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:33.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:33'),
(1089, 6, 6, 2508.00, NULL, NULL, 'raw', '2026-04-30 18:27:33.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:33'),
(1090, 5, 13, 15.02, NULL, NULL, 'cm', '2026-04-30 18:27:33.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:33'),
(1091, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:27:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:38'),
(1092, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:38'),
(1093, 6, 6, 2514.00, NULL, NULL, 'raw', '2026-04-30 18:27:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:38'),
(1094, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:27:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:39'),
(1095, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:27:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:44'),
(1096, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:27:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:44'),
(1097, 6, 6, 2512.00, NULL, NULL, 'raw', '2026-04-30 18:27:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:44'),
(1098, 5, 13, 53.42, NULL, NULL, 'cm', '2026-04-30 18:27:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:44'),
(1099, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:27:49.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:49'),
(1100, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:27:49.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:49'),
(1101, 6, 6, 2525.00, NULL, NULL, 'raw', '2026-04-30 18:27:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:49'),
(1102, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:27:54.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:54'),
(1103, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:27:54.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:54'),
(1104, 6, 6, 2527.00, NULL, NULL, 'raw', '2026-04-30 18:27:54.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:54'),
(1105, 5, 13, 3.29, NULL, NULL, 'cm', '2026-04-30 18:27:54.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:54'),
(1106, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:27:59.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:27:59'),
(1107, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:27:59.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:27:59'),
(1108, 6, 6, 2512.00, NULL, NULL, 'raw', '2026-04-30 18:27:59.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:27:59'),
(1109, 5, 13, 49.27, NULL, NULL, 'cm', '2026-04-30 18:27:59.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:27:59'),
(1110, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:28:05.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:05'),
(1111, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:05.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:05'),
(1112, 6, 6, 2511.00, NULL, NULL, 'raw', '2026-04-30 18:28:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:05'),
(1113, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:28:05.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:05'),
(1114, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:28:10.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:10'),
(1115, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:10.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:10'),
(1116, 6, 6, 2512.00, NULL, NULL, 'raw', '2026-04-30 18:28:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:10'),
(1117, 5, 13, 6.55, NULL, NULL, 'cm', '2026-04-30 18:28:10.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:10'),
(1118, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:28:15.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:15'),
(1119, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:15.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:15'),
(1120, 6, 6, 2512.00, NULL, NULL, 'raw', '2026-04-30 18:28:15.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:15'),
(1121, 5, 13, 58.00, NULL, NULL, 'cm', '2026-04-30 18:28:15.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:15'),
(1122, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:28:20.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:20'),
(1123, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:20.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:20'),
(1124, 6, 6, 2512.00, NULL, NULL, 'raw', '2026-04-30 18:28:20.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:20'),
(1125, 5, 13, 57.04, NULL, NULL, 'cm', '2026-04-30 18:28:20.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:20'),
(1126, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:28:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:26'),
(1127, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:26'),
(1128, 6, 6, 2500.00, NULL, NULL, 'raw', '2026-04-30 18:28:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:26'),
(1129, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:28:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:26'),
(1130, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:28:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:31'),
(1131, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:31'),
(1132, 6, 6, 2501.00, NULL, NULL, 'raw', '2026-04-30 18:28:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:31'),
(1133, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:28:31.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:31'),
(1134, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:28:36.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:36'),
(1135, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:36.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:36'),
(1136, 6, 6, 2503.00, NULL, NULL, 'raw', '2026-04-30 18:28:36.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:36'),
(1137, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:28:36.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:36'),
(1138, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:28:41.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:41'),
(1139, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:41.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:41'),
(1140, 6, 6, 2507.00, NULL, NULL, 'raw', '2026-04-30 18:28:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:41'),
(1141, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:28:41.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:41'),
(1142, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:28:46.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:46'),
(1143, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:46.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:46'),
(1144, 6, 6, 2499.00, NULL, NULL, 'raw', '2026-04-30 18:28:46.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:46'),
(1145, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:28:46.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:46'),
(1146, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:28:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:52'),
(1147, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:28:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:52'),
(1148, 6, 6, 2514.00, NULL, NULL, 'raw', '2026-04-30 18:28:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:52'),
(1149, 5, 13, 72.32, NULL, NULL, 'cm', '2026-04-30 18:28:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:52'),
(1150, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:28:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:28:57'),
(1151, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:28:57.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:28:57'),
(1152, 6, 6, 2506.00, NULL, NULL, 'raw', '2026-04-30 18:28:57.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:28:57'),
(1153, 5, 13, 22.74, NULL, NULL, 'cm', '2026-04-30 18:28:57.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:28:57'),
(1154, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:29:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:03'),
(1155, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:29:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:03'),
(1156, 6, 6, 2501.00, NULL, NULL, 'raw', '2026-04-30 18:29:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:03'),
(1157, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:29:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:08'),
(1158, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:29:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:08'),
(1159, 6, 6, 2485.00, NULL, NULL, 'raw', '2026-04-30 18:29:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:08'),
(1160, 5, 13, 21.47, NULL, NULL, 'cm', '2026-04-30 18:29:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:08'),
(1161, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:29:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:13'),
(1162, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:29:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:13'),
(1163, 6, 6, 2511.00, NULL, NULL, 'raw', '2026-04-30 18:29:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:13'),
(1164, 5, 13, 21.51, NULL, NULL, 'cm', '2026-04-30 18:29:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:13'),
(1165, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:29:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:19'),
(1166, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:29:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:19'),
(1167, 6, 6, 2500.00, NULL, NULL, 'raw', '2026-04-30 18:29:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:19'),
(1168, 5, 13, 62.10, NULL, NULL, 'cm', '2026-04-30 18:29:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:19'),
(1169, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:29:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:24'),
(1170, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:29:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:24'),
(1171, 6, 6, 2494.00, NULL, NULL, 'raw', '2026-04-30 18:29:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:24'),
(1172, 5, 13, 57.02, NULL, NULL, 'cm', '2026-04-30 18:29:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:24'),
(1173, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:29:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:29'),
(1174, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:29:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:29'),
(1175, 6, 6, 2500.00, NULL, NULL, 'raw', '2026-04-30 18:29:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:29'),
(1176, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:29:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:29'),
(1177, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:29:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:34'),
(1178, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:29:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:34'),
(1179, 6, 6, 2495.00, NULL, NULL, 'raw', '2026-04-30 18:29:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:34'),
(1180, 5, 13, 71.58, NULL, NULL, 'cm', '2026-04-30 18:29:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:34'),
(1181, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:29:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:40'),
(1182, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:29:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:40'),
(1183, 6, 6, 2495.00, NULL, NULL, 'raw', '2026-04-30 18:29:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:40'),
(1184, 5, 13, 118.33, NULL, NULL, 'cm', '2026-04-30 18:29:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:40'),
(1185, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:29:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:45'),
(1186, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:29:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:45'),
(1187, 6, 6, 2497.00, NULL, NULL, 'raw', '2026-04-30 18:29:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:45'),
(1188, 5, 13, 119.21, NULL, NULL, 'cm', '2026-04-30 18:29:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:45'),
(1189, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:29:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:50'),
(1190, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:29:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:50'),
(1191, 6, 6, 2496.00, NULL, NULL, 'raw', '2026-04-30 18:29:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:50'),
(1192, 5, 13, 22.74, NULL, NULL, 'cm', '2026-04-30 18:29:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:50'),
(1193, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:29:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:29:55'),
(1194, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:29:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:29:55'),
(1195, 6, 6, 2490.00, NULL, NULL, 'raw', '2026-04-30 18:29:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:29:55'),
(1196, 5, 13, 56.61, NULL, NULL, 'cm', '2026-04-30 18:29:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:29:55'),
(1197, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:30:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:01'),
(1198, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:01'),
(1199, 6, 6, 2493.00, NULL, NULL, 'raw', '2026-04-30 18:30:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:01'),
(1200, 5, 13, 58.86, NULL, NULL, 'cm', '2026-04-30 18:30:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:01'),
(1201, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:30:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:06'),
(1202, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:06'),
(1203, 6, 6, 2489.00, NULL, NULL, 'raw', '2026-04-30 18:30:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:06'),
(1204, 5, 13, 78.43, NULL, NULL, 'cm', '2026-04-30 18:30:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:06'),
(1205, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:30:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:11'),
(1206, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:11'),
(1207, 6, 6, 2494.00, NULL, NULL, 'raw', '2026-04-30 18:30:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:11'),
(1208, 5, 13, 22.74, NULL, NULL, 'cm', '2026-04-30 18:30:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:11'),
(1209, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:30:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:16'),
(1210, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:16'),
(1211, 6, 6, 2490.00, NULL, NULL, 'raw', '2026-04-30 18:30:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:16'),
(1212, 5, 13, 22.74, NULL, NULL, 'cm', '2026-04-30 18:30:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:16'),
(1213, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:30:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:21'),
(1214, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:21'),
(1215, 6, 6, 2495.00, NULL, NULL, 'raw', '2026-04-30 18:30:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:21'),
(1216, 5, 13, 22.74, NULL, NULL, 'cm', '2026-04-30 18:30:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:21'),
(1217, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:30:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:27'),
(1218, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:27'),
(1219, 6, 6, 2490.00, NULL, NULL, 'raw', '2026-04-30 18:30:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:27'),
(1220, 5, 13, 62.12, NULL, NULL, 'cm', '2026-04-30 18:30:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:27'),
(1221, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:30:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:32'),
(1222, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:32'),
(1223, 6, 6, 2491.00, NULL, NULL, 'raw', '2026-04-30 18:30:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:32'),
(1224, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:30:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:32'),
(1225, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:30:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:37'),
(1226, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:37'),
(1227, 6, 6, 2502.00, NULL, NULL, 'raw', '2026-04-30 18:30:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:37'),
(1228, 5, 13, 14.66, NULL, NULL, 'cm', '2026-04-30 18:30:37.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:37'),
(1229, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:30:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:43'),
(1230, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:43'),
(1231, 6, 6, 2480.00, NULL, NULL, 'raw', '2026-04-30 18:30:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:43'),
(1232, 5, 13, 60.42, NULL, NULL, 'cm', '2026-04-30 18:30:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:43'),
(1233, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:30:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:48'),
(1234, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:30:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:48'),
(1235, 6, 6, 2485.00, NULL, NULL, 'raw', '2026-04-30 18:30:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:48'),
(1236, 5, 13, 13.99, NULL, NULL, 'cm', '2026-04-30 18:30:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:48'),
(1237, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:30:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:53'),
(1238, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:30:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:53'),
(1239, 6, 6, 2496.00, NULL, NULL, 'raw', '2026-04-30 18:30:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:53'),
(1240, 5, 13, 20.22, NULL, NULL, 'cm', '2026-04-30 18:30:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:53'),
(1241, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:30:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:30:58'),
(1242, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:30:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:30:58'),
(1243, 6, 6, 2484.00, NULL, NULL, 'raw', '2026-04-30 18:30:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:30:58'),
(1244, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:30:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:30:58'),
(1245, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:31:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:03'),
(1246, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:31:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:03'),
(1247, 6, 6, 2487.00, NULL, NULL, 'raw', '2026-04-30 18:31:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:03'),
(1248, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:31:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:03'),
(1249, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:31:09.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:09'),
(1250, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:31:09.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:09'),
(1251, 6, 6, 2485.00, NULL, NULL, 'raw', '2026-04-30 18:31:09.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:09'),
(1252, 5, 13, 76.35, NULL, NULL, 'cm', '2026-04-30 18:31:09.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:09'),
(1253, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:31:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:14');
INSERT INTO `readings` (`id`, `device_id`, `sensor_type_id`, `reading_value`, `normalized_value`, `consumption_w`, `reading_unit`, `recorded_at`, `source`, `payload`, `created_at`) VALUES
(1254, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:31:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:14'),
(1255, 6, 6, 2490.00, NULL, NULL, 'raw', '2026-04-30 18:31:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:14'),
(1256, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:31:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:14'),
(1257, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:31:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:19'),
(1258, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:31:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:19'),
(1259, 6, 6, 2492.00, NULL, NULL, 'raw', '2026-04-30 18:31:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:19'),
(1260, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:31:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:19'),
(1261, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:31:25.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:25'),
(1262, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:31:25.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:25'),
(1263, 6, 6, 2477.00, NULL, NULL, 'raw', '2026-04-30 18:31:25.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:25'),
(1264, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:31:25.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:25'),
(1265, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:31:30.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:30'),
(1266, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:31:30.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:30'),
(1267, 6, 6, 2473.00, NULL, NULL, 'raw', '2026-04-30 18:31:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:30'),
(1268, 5, 13, 8.85, NULL, NULL, 'cm', '2026-04-30 18:31:30.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:30'),
(1269, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:31:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:35'),
(1270, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:31:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:35'),
(1271, 6, 6, 2480.00, NULL, NULL, 'raw', '2026-04-30 18:31:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:35'),
(1272, 5, 13, 5.57, NULL, NULL, 'cm', '2026-04-30 18:31:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:35'),
(1273, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:31:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:40'),
(1274, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:31:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:40'),
(1275, 6, 6, 2491.00, NULL, NULL, 'raw', '2026-04-30 18:31:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:40'),
(1276, 5, 13, 56.34, NULL, NULL, 'cm', '2026-04-30 18:31:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:40'),
(1277, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:31:46.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:46'),
(1278, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:31:46.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:46'),
(1279, 6, 6, 2490.00, NULL, NULL, 'raw', '2026-04-30 18:31:46.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:46'),
(1280, 5, 13, 56.46, NULL, NULL, 'cm', '2026-04-30 18:31:46.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:46'),
(1281, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:31:51.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:51'),
(1282, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:31:51.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:51'),
(1283, 6, 6, 2482.00, NULL, NULL, 'raw', '2026-04-30 18:31:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:51'),
(1284, 5, 13, 1.66, NULL, NULL, 'cm', '2026-04-30 18:31:51.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:51'),
(1285, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:31:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:31:56'),
(1286, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:31:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:31:56'),
(1287, 6, 6, 2480.00, NULL, NULL, 'raw', '2026-04-30 18:31:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:31:56'),
(1288, 5, 13, 49.82, NULL, NULL, 'cm', '2026-04-30 18:31:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:31:56'),
(1289, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:32:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:01'),
(1290, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:32:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:01'),
(1291, 6, 6, 2471.00, NULL, NULL, 'raw', '2026-04-30 18:32:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:01'),
(1292, 5, 13, 47.47, NULL, NULL, 'cm', '2026-04-30 18:32:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:01'),
(1293, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:32:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:06'),
(1294, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:32:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:06'),
(1295, 6, 6, 2481.00, NULL, NULL, 'raw', '2026-04-30 18:32:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:06'),
(1296, 5, 13, 6.53, NULL, NULL, 'cm', '2026-04-30 18:32:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:06'),
(1297, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:32:12.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:12'),
(1298, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:32:12.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:12'),
(1299, 6, 6, 2479.00, NULL, NULL, 'raw', '2026-04-30 18:32:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:12'),
(1300, 5, 13, 45.67, NULL, NULL, 'cm', '2026-04-30 18:32:12.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:12'),
(1301, 1, 1, 30.70, NULL, NULL, 'C', '2026-04-30 18:32:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:17'),
(1302, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:32:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:17'),
(1303, 6, 6, 2496.00, NULL, NULL, 'raw', '2026-04-30 18:32:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:17'),
(1304, 5, 13, 2.97, NULL, NULL, 'cm', '2026-04-30 18:32:17.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:17'),
(1305, 1, 1, 30.50, NULL, NULL, 'C', '2026-04-30 18:32:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:22'),
(1306, 2, 2, 31.00, NULL, NULL, '%', '2026-04-30 18:32:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:22'),
(1307, 6, 6, 2470.00, NULL, NULL, 'raw', '2026-04-30 18:32:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:22'),
(1308, 5, 13, 3.94, NULL, NULL, 'cm', '2026-04-30 18:32:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:22'),
(1309, 1, 1, 30.20, NULL, NULL, 'C', '2026-04-30 18:32:28.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:28'),
(1310, 2, 2, 32.00, NULL, NULL, '%', '2026-04-30 18:32:28.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:28'),
(1311, 6, 6, 2480.00, NULL, NULL, 'raw', '2026-04-30 18:32:28.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:28'),
(1312, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:32:28.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:28'),
(1313, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:32:33.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:33'),
(1314, 2, 2, 31.00, NULL, NULL, '%', '2026-04-30 18:32:33.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:33'),
(1315, 6, 6, 2481.00, NULL, NULL, 'raw', '2026-04-30 18:32:33.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:33'),
(1316, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:32:33.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:33'),
(1317, 1, 1, 30.30, NULL, NULL, 'C', '2026-04-30 18:32:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:38'),
(1318, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:32:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:38'),
(1319, 6, 6, 2481.00, NULL, NULL, 'raw', '2026-04-30 18:32:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:38'),
(1320, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:32:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:38'),
(1321, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:32:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:43'),
(1322, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:32:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:43'),
(1323, 6, 6, 2482.00, NULL, NULL, 'raw', '2026-04-30 18:32:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:43'),
(1324, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:32:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:43'),
(1325, 1, 1, 30.30, NULL, NULL, 'C', '2026-04-30 18:32:49.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:49'),
(1326, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:32:49.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:49'),
(1327, 6, 6, 2475.00, NULL, NULL, 'raw', '2026-04-30 18:32:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:49'),
(1328, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:32:49.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:49'),
(1329, 1, 1, 30.10, NULL, NULL, 'C', '2026-04-30 18:32:54.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:54'),
(1330, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:32:54.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:54'),
(1331, 6, 6, 2477.00, NULL, NULL, 'raw', '2026-04-30 18:32:54.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:54'),
(1332, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:32:54.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:54'),
(1333, 1, 1, 30.20, NULL, NULL, 'C', '2026-04-30 18:32:59.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:32:59'),
(1334, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:32:59.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:32:59'),
(1335, 6, 6, 2467.00, NULL, NULL, 'raw', '2026-04-30 18:32:59.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:32:59'),
(1336, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:32:59.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:32:59'),
(1337, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:33:05.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:05'),
(1338, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:05.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:05'),
(1339, 6, 6, 2477.00, NULL, NULL, 'raw', '2026-04-30 18:33:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:05'),
(1340, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:33:05.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:05'),
(1341, 1, 1, 30.40, NULL, NULL, 'C', '2026-04-30 18:33:10.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:10'),
(1342, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:10.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:10'),
(1343, 6, 6, 2476.00, NULL, NULL, 'raw', '2026-04-30 18:33:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:10'),
(1344, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:33:10.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:10'),
(1345, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:33:15.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:15'),
(1346, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:15.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:15'),
(1347, 6, 6, 2481.00, NULL, NULL, 'raw', '2026-04-30 18:33:15.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:15'),
(1348, 5, 13, 18.92, NULL, NULL, 'cm', '2026-04-30 18:33:15.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:15'),
(1349, 1, 1, 30.20, NULL, NULL, 'C', '2026-04-30 18:33:20.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:20'),
(1350, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:20.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:20'),
(1351, 6, 6, 2494.00, NULL, NULL, 'raw', '2026-04-30 18:33:20.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:20'),
(1352, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:33:20.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:20'),
(1353, 1, 1, 30.70, NULL, NULL, 'C', '2026-04-30 18:33:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:26'),
(1354, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:26'),
(1355, 6, 6, 2480.00, NULL, NULL, 'raw', '2026-04-30 18:33:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:26'),
(1356, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:33:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:26'),
(1357, 1, 1, 30.00, NULL, NULL, 'C', '2026-04-30 18:33:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:31'),
(1358, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:31'),
(1359, 6, 6, 2480.00, NULL, NULL, 'raw', '2026-04-30 18:33:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:31'),
(1360, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:33:31.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:31'),
(1361, 1, 1, 30.00, NULL, NULL, 'C', '2026-04-30 18:33:36.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:36'),
(1362, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:36.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:36'),
(1363, 6, 6, 2471.00, NULL, NULL, 'raw', '2026-04-30 18:33:36.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:36'),
(1364, 5, 13, 18.93, NULL, NULL, 'cm', '2026-04-30 18:33:36.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:36'),
(1365, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-30 18:33:41.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:41'),
(1366, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:41.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:41'),
(1367, 6, 6, 2475.00, NULL, NULL, 'raw', '2026-04-30 18:33:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:41'),
(1368, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:33:41.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:41'),
(1369, 1, 1, 30.60, NULL, NULL, 'C', '2026-04-30 18:33:46.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:46'),
(1370, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:46.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:46'),
(1371, 6, 6, 2469.00, NULL, NULL, 'raw', '2026-04-30 18:33:46.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:46'),
(1372, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:33:46.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:46'),
(1373, 1, 1, 30.70, NULL, NULL, 'C', '2026-04-30 18:33:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:52'),
(1374, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:52'),
(1375, 6, 6, 2463.00, NULL, NULL, 'raw', '2026-04-30 18:33:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:52'),
(1376, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:33:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:52'),
(1377, 1, 1, 30.60, NULL, NULL, 'C', '2026-04-30 18:33:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:33:57'),
(1378, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:33:57.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:33:57'),
(1379, 6, 6, 2479.00, NULL, NULL, 'raw', '2026-04-30 18:33:57.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:33:57'),
(1380, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:33:57.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:33:57'),
(1381, 1, 1, 30.30, NULL, NULL, 'C', '2026-04-30 18:34:02.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:02'),
(1382, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:02.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:02'),
(1383, 6, 6, 2465.00, NULL, NULL, 'raw', '2026-04-30 18:34:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:02'),
(1384, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:02.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:02'),
(1385, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:34:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:08'),
(1386, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:08'),
(1387, 6, 6, 2466.00, NULL, NULL, 'raw', '2026-04-30 18:34:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:08'),
(1388, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:08'),
(1389, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:34:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:13'),
(1390, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:13'),
(1391, 6, 6, 2474.00, NULL, NULL, 'raw', '2026-04-30 18:34:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:13'),
(1392, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:13'),
(1393, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:34:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:18'),
(1394, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:18'),
(1395, 6, 6, 2467.00, NULL, NULL, 'raw', '2026-04-30 18:34:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:18'),
(1396, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:18'),
(1397, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:34:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:24'),
(1398, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:24'),
(1399, 6, 6, 2466.00, NULL, NULL, 'raw', '2026-04-30 18:34:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:24'),
(1400, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:24'),
(1401, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:34:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:29'),
(1402, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:29'),
(1403, 6, 6, 2464.00, NULL, NULL, 'raw', '2026-04-30 18:34:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:29'),
(1404, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:29'),
(1405, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:34:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:34'),
(1406, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:34'),
(1407, 6, 6, 2470.00, NULL, NULL, 'raw', '2026-04-30 18:34:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:34'),
(1408, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:34'),
(1409, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:34:39.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:39'),
(1410, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:39.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:39'),
(1411, 6, 6, 2471.00, NULL, NULL, 'raw', '2026-04-30 18:34:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:39'),
(1412, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:39'),
(1413, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:34:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:45'),
(1414, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:45'),
(1415, 6, 6, 2461.00, NULL, NULL, 'raw', '2026-04-30 18:34:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:45'),
(1416, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:45'),
(1417, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:34:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:50'),
(1418, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:50'),
(1419, 6, 6, 2471.00, NULL, NULL, 'raw', '2026-04-30 18:34:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:50'),
(1420, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:50'),
(1421, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:34:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:34:55'),
(1422, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:34:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:34:55'),
(1423, 6, 6, 2458.00, NULL, NULL, 'raw', '2026-04-30 18:34:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:34:55'),
(1424, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:34:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:34:55'),
(1425, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:35:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:00'),
(1426, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:00'),
(1427, 6, 6, 2458.00, NULL, NULL, 'raw', '2026-04-30 18:35:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:00'),
(1428, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:35:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:00'),
(1429, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:35:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:06'),
(1430, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:06'),
(1431, 6, 6, 2451.00, NULL, NULL, 'raw', '2026-04-30 18:35:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:06'),
(1432, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:35:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:06'),
(1433, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:35:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:11'),
(1434, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:11'),
(1435, 6, 6, 2462.00, NULL, NULL, 'raw', '2026-04-30 18:35:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:11'),
(1436, 5, 13, 21.47, NULL, NULL, 'cm', '2026-04-30 18:35:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:11'),
(1437, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:35:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:16'),
(1438, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:35:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:16'),
(1439, 6, 6, 2462.00, NULL, NULL, 'raw', '2026-04-30 18:35:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:16'),
(1440, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:35:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:16'),
(1441, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:35:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:21'),
(1442, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:35:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:21'),
(1443, 6, 6, 2477.00, NULL, NULL, 'raw', '2026-04-30 18:35:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:21'),
(1444, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:35:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:21'),
(1445, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:35:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:26'),
(1446, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:26'),
(1447, 6, 6, 2462.00, NULL, NULL, 'raw', '2026-04-30 18:35:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:26'),
(1448, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:35:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:26'),
(1449, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:35:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:32'),
(1450, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:32'),
(1451, 6, 6, 2461.00, NULL, NULL, 'raw', '2026-04-30 18:35:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:32'),
(1452, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:35:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:32'),
(1453, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:35:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:37'),
(1454, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:37'),
(1455, 6, 6, 2458.00, NULL, NULL, 'raw', '2026-04-30 18:35:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:37'),
(1456, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:35:37.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:37'),
(1457, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:35:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:42'),
(1458, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:42'),
(1459, 6, 6, 2463.00, NULL, NULL, 'raw', '2026-04-30 18:35:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:42'),
(1460, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:35:42.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:42'),
(1461, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:35:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:47'),
(1462, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:47'),
(1463, 6, 6, 2464.00, NULL, NULL, 'raw', '2026-04-30 18:35:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:47'),
(1464, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:35:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:47'),
(1465, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:35:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:52'),
(1466, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:52'),
(1467, 6, 6, 2448.00, NULL, NULL, 'raw', '2026-04-30 18:35:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:52'),
(1468, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:35:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:52'),
(1469, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:35:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:35:58'),
(1470, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:35:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:35:58'),
(1471, 6, 6, 2438.00, NULL, NULL, 'raw', '2026-04-30 18:35:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:35:58'),
(1472, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:35:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:35:58'),
(1473, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:36:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:03'),
(1474, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:03'),
(1475, 6, 6, 2463.00, NULL, NULL, 'raw', '2026-04-30 18:36:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:03'),
(1476, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:36:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:03'),
(1477, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:36:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:08'),
(1478, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:08'),
(1479, 6, 6, 2448.00, NULL, NULL, 'raw', '2026-04-30 18:36:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:08'),
(1480, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:36:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:08'),
(1481, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:36:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:13'),
(1482, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:13'),
(1483, 6, 6, 2453.00, NULL, NULL, 'raw', '2026-04-30 18:36:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:13'),
(1484, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:36:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:13'),
(1485, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:36:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:18'),
(1486, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:18'),
(1487, 6, 6, 2452.00, NULL, NULL, 'raw', '2026-04-30 18:36:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:18'),
(1488, 5, 13, 20.22, NULL, NULL, 'cm', '2026-04-30 18:36:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:18'),
(1489, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:36:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:24'),
(1490, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:24'),
(1491, 6, 6, 2441.00, NULL, NULL, 'raw', '2026-04-30 18:36:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:24'),
(1492, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:36:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:24'),
(1493, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:36:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:29'),
(1494, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:29'),
(1495, 6, 6, 2458.00, NULL, NULL, 'raw', '2026-04-30 18:36:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:29'),
(1496, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:36:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:29'),
(1497, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:36:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:34'),
(1498, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:34'),
(1499, 6, 6, 2450.00, NULL, NULL, 'raw', '2026-04-30 18:36:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:34'),
(1500, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:36:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:34'),
(1501, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:36:39.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:39'),
(1502, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:39.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:39'),
(1503, 6, 6, 2438.00, NULL, NULL, 'raw', '2026-04-30 18:36:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:39'),
(1504, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:36:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:39'),
(1505, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:36:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:44'),
(1506, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:44'),
(1507, 6, 6, 2450.00, NULL, NULL, 'raw', '2026-04-30 18:36:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:44'),
(1508, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:36:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:44'),
(1509, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:36:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:50'),
(1510, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:50'),
(1511, 6, 6, 2448.00, NULL, NULL, 'raw', '2026-04-30 18:36:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:50'),
(1512, 5, 13, 17.96, NULL, NULL, 'cm', '2026-04-30 18:36:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:50'),
(1513, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:36:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:36:55'),
(1514, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:36:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:36:55'),
(1515, 6, 6, 2437.00, NULL, NULL, 'raw', '2026-04-30 18:36:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:36:55'),
(1516, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:36:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:36:55'),
(1517, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:37:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:00'),
(1518, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:00'),
(1519, 6, 6, 2447.00, NULL, NULL, 'raw', '2026-04-30 18:37:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:00'),
(1520, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:37:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:00'),
(1521, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:37:05.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:05'),
(1522, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:05.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:05'),
(1523, 6, 6, 2448.00, NULL, NULL, 'raw', '2026-04-30 18:37:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:05'),
(1524, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:37:05.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:05'),
(1525, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:37:10.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:10'),
(1526, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:10.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:10'),
(1527, 6, 6, 2435.00, NULL, NULL, 'raw', '2026-04-30 18:37:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:10'),
(1528, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:37:10.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:10'),
(1529, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:37:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:16'),
(1530, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:16'),
(1531, 6, 6, 2458.00, NULL, NULL, 'raw', '2026-04-30 18:37:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:16'),
(1532, 5, 13, 18.28, NULL, NULL, 'cm', '2026-04-30 18:37:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:16'),
(1533, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:37:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:21'),
(1534, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:21'),
(1535, 6, 6, 2437.00, NULL, NULL, 'raw', '2026-04-30 18:37:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:21'),
(1536, 5, 13, 19.24, NULL, NULL, 'cm', '2026-04-30 18:37:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:21'),
(1537, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:37:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:26'),
(1538, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:26'),
(1539, 6, 6, 2449.00, NULL, NULL, 'raw', '2026-04-30 18:37:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:26'),
(1540, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:37:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:26'),
(1541, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:37:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:31'),
(1542, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:31'),
(1543, 6, 6, 2447.00, NULL, NULL, 'raw', '2026-04-30 18:37:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:31'),
(1544, 5, 13, 24.47, NULL, NULL, 'cm', '2026-04-30 18:37:31.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:31'),
(1545, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:37:36.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:36'),
(1546, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:36.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:36'),
(1547, 6, 6, 2442.00, NULL, NULL, 'raw', '2026-04-30 18:37:36.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:36'),
(1548, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:37:36.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:36'),
(1549, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:37:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:42'),
(1550, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:42'),
(1551, 6, 6, 2447.00, NULL, NULL, 'raw', '2026-04-30 18:37:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:42'),
(1552, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:37:42.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:42'),
(1553, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:37:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:47'),
(1554, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:47'),
(1555, 6, 6, 2448.00, NULL, NULL, 'raw', '2026-04-30 18:37:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:47'),
(1556, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:37:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:47'),
(1557, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:37:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:52'),
(1558, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:52'),
(1559, 6, 6, 2445.00, NULL, NULL, 'raw', '2026-04-30 18:37:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:52'),
(1560, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:37:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:52'),
(1561, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:37:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:37:57'),
(1562, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:37:57.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:37:57'),
(1563, 6, 6, 2433.00, NULL, NULL, 'raw', '2026-04-30 18:37:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:37:58'),
(1564, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:37:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:37:58');
INSERT INTO `readings` (`id`, `device_id`, `sensor_type_id`, `reading_value`, `normalized_value`, `consumption_w`, `reading_unit`, `recorded_at`, `source`, `payload`, `created_at`) VALUES
(1565, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:38:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:03'),
(1566, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:38:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:03'),
(1567, 6, 6, 2442.00, NULL, NULL, 'raw', '2026-04-30 18:38:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:03'),
(1568, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:38:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:03'),
(1569, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:38:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:08'),
(1570, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:38:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:08'),
(1571, 6, 6, 2448.00, NULL, NULL, 'raw', '2026-04-30 18:38:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:08'),
(1572, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:38:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:08'),
(1573, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:38:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:13'),
(1574, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:38:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:13'),
(1575, 6, 6, 2445.00, NULL, NULL, 'raw', '2026-04-30 18:38:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:13'),
(1576, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:38:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:13'),
(1577, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:38:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:18'),
(1578, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:38:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:18'),
(1579, 6, 6, 2437.00, NULL, NULL, 'raw', '2026-04-30 18:38:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:18'),
(1580, 5, 13, 18.59, NULL, NULL, 'cm', '2026-04-30 18:38:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:18'),
(1581, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:38:23.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:23'),
(1582, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:38:23.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:23'),
(1583, 6, 6, 2439.00, NULL, NULL, 'raw', '2026-04-30 18:38:23.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:23'),
(1584, 5, 13, 21.49, NULL, NULL, 'cm', '2026-04-30 18:38:23.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:23'),
(1585, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:38:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:29'),
(1586, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:38:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:29'),
(1587, 6, 6, 2437.00, NULL, NULL, 'raw', '2026-04-30 18:38:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:29'),
(1588, 5, 13, 18.92, NULL, NULL, 'cm', '2026-04-30 18:38:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:29'),
(1589, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:38:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:34'),
(1590, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:38:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:34'),
(1591, 6, 6, 2448.00, NULL, NULL, 'raw', '2026-04-30 18:38:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:34'),
(1592, 5, 13, 18.92, NULL, NULL, 'cm', '2026-04-30 18:38:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:34'),
(1593, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:38:39.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:39'),
(1594, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:38:39.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:39'),
(1595, 6, 6, 2435.00, NULL, NULL, 'raw', '2026-04-30 18:38:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:39'),
(1596, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 18:38:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:39'),
(1597, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:38:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:38:44'),
(1598, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:38:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:38:44'),
(1599, 6, 6, 2433.00, NULL, NULL, 'raw', '2026-04-30 18:38:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:38:44'),
(1600, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:38:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:38:44'),
(1601, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:39:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:39:44'),
(1602, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:39:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:39:44'),
(1603, 6, 6, 2432.00, NULL, NULL, 'raw', '2026-04-30 18:39:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:39:44'),
(1604, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:39:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:39:44'),
(1605, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:39:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:39:50'),
(1606, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:39:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:39:50'),
(1607, 6, 6, 2426.00, NULL, NULL, 'raw', '2026-04-30 18:39:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:39:50'),
(1608, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:39:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:39:50'),
(1609, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:39:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:39:55'),
(1610, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:39:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:39:55'),
(1611, 6, 6, 2442.00, NULL, NULL, 'raw', '2026-04-30 18:39:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:39:55'),
(1612, 5, 13, 4.92, NULL, NULL, 'cm', '2026-04-30 18:39:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:39:55'),
(1613, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:40:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:00'),
(1614, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:40:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:00'),
(1615, 6, 6, 2432.00, NULL, NULL, 'raw', '2026-04-30 18:40:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:00'),
(1616, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:00'),
(1617, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:40:05.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:05'),
(1618, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:40:05.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:05'),
(1619, 6, 6, 2445.00, NULL, NULL, 'raw', '2026-04-30 18:40:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:05'),
(1620, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:05.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:05'),
(1621, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:40:10.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:10'),
(1622, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:40:10.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:10'),
(1623, 6, 6, 2432.00, NULL, NULL, 'raw', '2026-04-30 18:40:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:10'),
(1624, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:10.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:10'),
(1625, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:40:15.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:15'),
(1626, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:40:15.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:15'),
(1627, 6, 6, 2435.00, NULL, NULL, 'raw', '2026-04-30 18:40:15.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:15'),
(1628, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:15.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:15'),
(1629, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:40:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:21'),
(1630, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:40:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:21'),
(1631, 6, 6, 2423.00, NULL, NULL, 'raw', '2026-04-30 18:40:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:21'),
(1632, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:21'),
(1633, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:40:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:26'),
(1634, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:40:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:26'),
(1635, 6, 6, 2419.00, NULL, NULL, 'raw', '2026-04-30 18:40:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:26'),
(1636, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:40:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:26'),
(1637, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:40:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:31'),
(1638, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:40:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:31'),
(1639, 6, 6, 2429.00, NULL, NULL, 'raw', '2026-04-30 18:40:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:31'),
(1640, 5, 13, 19.88, NULL, NULL, 'cm', '2026-04-30 18:40:31.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:31'),
(1641, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:40:36.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:36'),
(1642, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:40:36.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:36'),
(1643, 6, 6, 2427.00, NULL, NULL, 'raw', '2026-04-30 18:40:36.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:36'),
(1644, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:36.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:36'),
(1645, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:40:41.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:41'),
(1646, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:40:41.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:41'),
(1647, 6, 6, 2432.00, NULL, NULL, 'raw', '2026-04-30 18:40:41.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:41'),
(1648, 5, 13, 19.89, NULL, NULL, 'cm', '2026-04-30 18:40:41.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:41'),
(1649, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:40:46.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:46'),
(1650, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:40:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:47'),
(1651, 6, 6, 2421.00, NULL, NULL, 'raw', '2026-04-30 18:40:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:47'),
(1652, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:47'),
(1653, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:40:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:52'),
(1654, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:40:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:52'),
(1655, 6, 6, 2417.00, NULL, NULL, 'raw', '2026-04-30 18:40:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:52'),
(1656, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:52'),
(1657, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:40:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:40:57'),
(1658, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:40:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:40:58'),
(1659, 6, 6, 2425.00, NULL, NULL, 'raw', '2026-04-30 18:40:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:40:58'),
(1660, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:40:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:40:58'),
(1661, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:41:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:03'),
(1662, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:03'),
(1663, 6, 6, 2422.00, NULL, NULL, 'raw', '2026-04-30 18:41:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:03'),
(1664, 5, 13, 19.89, NULL, NULL, 'cm', '2026-04-30 18:41:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:03'),
(1665, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:41:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:08'),
(1666, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:08'),
(1667, 6, 6, 2422.00, NULL, NULL, 'raw', '2026-04-30 18:41:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:08'),
(1668, 5, 13, 21.18, NULL, NULL, 'cm', '2026-04-30 18:41:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:08'),
(1669, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:41:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:13'),
(1670, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:13'),
(1671, 6, 6, 2410.00, NULL, NULL, 'raw', '2026-04-30 18:41:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:13'),
(1672, 5, 13, 19.89, NULL, NULL, 'cm', '2026-04-30 18:41:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:13'),
(1673, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:41:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:19'),
(1674, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:19'),
(1675, 6, 6, 2407.00, NULL, NULL, 'raw', '2026-04-30 18:41:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:19'),
(1676, 5, 13, 19.88, NULL, NULL, 'cm', '2026-04-30 18:41:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:19'),
(1677, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:41:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:24'),
(1678, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:24'),
(1679, 6, 6, 2416.00, NULL, NULL, 'raw', '2026-04-30 18:41:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:24'),
(1680, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:41:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:24'),
(1681, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:41:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:29'),
(1682, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:29'),
(1683, 6, 6, 2423.00, NULL, NULL, 'raw', '2026-04-30 18:41:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:29'),
(1684, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:41:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:29'),
(1685, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:41:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:34'),
(1686, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:34'),
(1687, 6, 6, 2416.00, NULL, NULL, 'raw', '2026-04-30 18:41:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:34'),
(1688, 5, 13, 19.89, NULL, NULL, 'cm', '2026-04-30 18:41:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:34'),
(1689, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:41:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:40'),
(1690, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:40'),
(1691, 6, 6, 2419.00, NULL, NULL, 'raw', '2026-04-30 18:41:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:40'),
(1692, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:41:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:40'),
(1693, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:41:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:45'),
(1694, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:45'),
(1695, 6, 6, 2421.00, NULL, NULL, 'raw', '2026-04-30 18:41:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:45'),
(1696, 5, 13, 21.18, NULL, NULL, 'cm', '2026-04-30 18:41:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:45'),
(1697, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:41:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:50'),
(1698, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:50'),
(1699, 6, 6, 2405.00, NULL, NULL, 'raw', '2026-04-30 18:41:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:50'),
(1700, 5, 13, 21.18, NULL, NULL, 'cm', '2026-04-30 18:41:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:50'),
(1701, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:41:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:41:55'),
(1702, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:41:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:41:55'),
(1703, 6, 6, 2415.00, NULL, NULL, 'raw', '2026-04-30 18:41:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:41:55'),
(1704, 5, 13, 21.18, NULL, NULL, 'cm', '2026-04-30 18:41:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:41:55'),
(1705, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:42:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:00'),
(1706, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:00'),
(1707, 6, 6, 2409.00, NULL, NULL, 'raw', '2026-04-30 18:42:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:00'),
(1708, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:42:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:00'),
(1709, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:42:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:06'),
(1710, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:06'),
(1711, 6, 6, 2416.00, NULL, NULL, 'raw', '2026-04-30 18:42:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:06'),
(1712, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:42:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:06'),
(1713, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:42:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:11'),
(1714, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:11'),
(1715, 6, 6, 2416.00, NULL, NULL, 'raw', '2026-04-30 18:42:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:11'),
(1716, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:42:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:11'),
(1717, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:42:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:16'),
(1718, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:16'),
(1719, 6, 6, 2422.00, NULL, NULL, 'raw', '2026-04-30 18:42:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:16'),
(1720, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:42:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:16'),
(1721, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:42:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:21'),
(1722, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:21'),
(1723, 6, 6, 2407.00, NULL, NULL, 'raw', '2026-04-30 18:42:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:21'),
(1724, 5, 13, 21.18, NULL, NULL, 'cm', '2026-04-30 18:42:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:21'),
(1725, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:42:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:26'),
(1726, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:26'),
(1727, 6, 6, 2425.00, NULL, NULL, 'raw', '2026-04-30 18:42:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:26'),
(1728, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:42:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:26'),
(1729, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:42:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:32'),
(1730, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:32'),
(1731, 6, 6, 2415.00, NULL, NULL, 'raw', '2026-04-30 18:42:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:32'),
(1732, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:42:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:32'),
(1733, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:42:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:37'),
(1734, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:37'),
(1735, 6, 6, 2427.00, NULL, NULL, 'raw', '2026-04-30 18:42:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:37'),
(1736, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:42:37.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:37'),
(1737, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:42:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:42'),
(1738, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:42'),
(1739, 6, 6, 2397.00, NULL, NULL, 'raw', '2026-04-30 18:42:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:42'),
(1740, 5, 13, 20.20, NULL, NULL, 'cm', '2026-04-30 18:42:42.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:42'),
(1741, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:42:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:50'),
(1742, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:50'),
(1743, 6, 6, 2410.00, NULL, NULL, 'raw', '2026-04-30 18:42:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:50'),
(1744, 5, 13, 22.45, NULL, NULL, 'cm', '2026-04-30 18:42:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:50'),
(1745, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:42:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:42:55'),
(1746, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:42:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:42:55'),
(1747, 6, 6, 2406.00, NULL, NULL, 'raw', '2026-04-30 18:42:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:42:55'),
(1748, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:42:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:42:55'),
(1749, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:43:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:00'),
(1750, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:43:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:00'),
(1751, 6, 6, 2411.00, NULL, NULL, 'raw', '2026-04-30 18:43:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:00'),
(1752, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:00'),
(1753, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:43:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:06'),
(1754, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:43:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:06'),
(1755, 6, 6, 2411.00, NULL, NULL, 'raw', '2026-04-30 18:43:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:06'),
(1756, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:06'),
(1757, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:43:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:11'),
(1758, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:43:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:11'),
(1759, 6, 6, 2414.00, NULL, NULL, 'raw', '2026-04-30 18:43:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:11'),
(1760, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:11'),
(1761, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:43:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:16'),
(1762, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:16'),
(1763, 6, 6, 2414.00, NULL, NULL, 'raw', '2026-04-30 18:43:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:16'),
(1764, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:16'),
(1765, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:43:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:21'),
(1766, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:21'),
(1767, 6, 6, 2407.00, NULL, NULL, 'raw', '2026-04-30 18:43:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:21'),
(1768, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:21'),
(1769, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:43:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:26'),
(1770, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:27'),
(1771, 6, 6, 2410.00, NULL, NULL, 'raw', '2026-04-30 18:43:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:27'),
(1772, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:27'),
(1773, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:43:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:32'),
(1774, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:32'),
(1775, 6, 6, 2403.00, NULL, NULL, 'raw', '2026-04-30 18:43:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:32'),
(1776, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:32'),
(1777, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:43:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:37'),
(1778, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:37'),
(1779, 6, 6, 2401.00, NULL, NULL, 'raw', '2026-04-30 18:43:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:37'),
(1780, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:37.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:37'),
(1781, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:43:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:42'),
(1782, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:42'),
(1783, 6, 6, 2410.00, NULL, NULL, 'raw', '2026-04-30 18:43:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:42'),
(1784, 5, 13, 21.16, NULL, NULL, 'cm', '2026-04-30 18:43:42.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:42'),
(1785, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:43:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:47'),
(1786, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:48'),
(1787, 6, 6, 2416.00, NULL, NULL, 'raw', '2026-04-30 18:43:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:48'),
(1788, 5, 13, 21.18, NULL, NULL, 'cm', '2026-04-30 18:43:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:48'),
(1789, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:43:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:53'),
(1790, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:53'),
(1791, 6, 6, 2405.00, NULL, NULL, 'raw', '2026-04-30 18:43:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:53'),
(1792, 5, 13, 3.62, NULL, NULL, 'cm', '2026-04-30 18:43:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:53'),
(1793, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:43:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:43:58'),
(1794, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:43:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:43:58'),
(1795, 6, 6, 2411.00, NULL, NULL, 'raw', '2026-04-30 18:43:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:43:58'),
(1796, 5, 13, 57.45, NULL, NULL, 'cm', '2026-04-30 18:43:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:43:58'),
(1797, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:44:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:03'),
(1798, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:44:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:03'),
(1799, 6, 6, 2410.00, NULL, NULL, 'raw', '2026-04-30 18:44:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:03'),
(1800, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:03'),
(1801, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:44:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:08'),
(1802, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:44:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:08'),
(1803, 6, 6, 2406.00, NULL, NULL, 'raw', '2026-04-30 18:44:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:08'),
(1804, 5, 13, 3.29, NULL, NULL, 'cm', '2026-04-30 18:44:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:08'),
(1805, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:44:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:14'),
(1806, 2, 2, 33.00, NULL, NULL, '%', '2026-04-30 18:44:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:14'),
(1807, 6, 6, 2406.00, NULL, NULL, 'raw', '2026-04-30 18:44:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:14'),
(1808, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:14'),
(1809, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:44:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:19'),
(1810, 2, 2, 31.00, NULL, NULL, '%', '2026-04-30 18:44:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:19'),
(1811, 6, 6, 2409.00, NULL, NULL, 'raw', '2026-04-30 18:44:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:19'),
(1812, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:19'),
(1813, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:44:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:24'),
(1814, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:44:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:24'),
(1815, 6, 6, 2406.00, NULL, NULL, 'raw', '2026-04-30 18:44:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:24'),
(1816, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:24'),
(1817, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:44:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:29'),
(1818, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:44:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:29'),
(1819, 6, 6, 2414.00, NULL, NULL, 'raw', '2026-04-30 18:44:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:29'),
(1820, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:29'),
(1821, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:44:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:35'),
(1822, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:44:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:35'),
(1823, 6, 6, 2406.00, NULL, NULL, 'raw', '2026-04-30 18:44:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:35'),
(1824, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:35'),
(1825, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:44:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:40'),
(1826, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:44:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:40'),
(1827, 6, 6, 2405.00, NULL, NULL, 'raw', '2026-04-30 18:44:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:40'),
(1828, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:40'),
(1829, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:44:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:45'),
(1830, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:44:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:45'),
(1831, 6, 6, 2410.00, NULL, NULL, 'raw', '2026-04-30 18:44:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:45'),
(1832, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:45'),
(1833, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:44:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:50'),
(1834, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:44:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:50'),
(1835, 6, 6, 2403.00, NULL, NULL, 'raw', '2026-04-30 18:44:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:50'),
(1836, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:50'),
(1837, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:44:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:44:55'),
(1838, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:44:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:44:55'),
(1839, 6, 6, 2403.00, NULL, NULL, 'raw', '2026-04-30 18:44:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:44:55'),
(1840, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:44:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:44:55'),
(1841, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:45:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:01'),
(1842, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:01'),
(1843, 6, 6, 2403.00, NULL, NULL, 'raw', '2026-04-30 18:45:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:01'),
(1844, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:01'),
(1845, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:45:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:06'),
(1846, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:06'),
(1847, 6, 6, 2403.00, NULL, NULL, 'raw', '2026-04-30 18:45:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:06'),
(1848, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:06'),
(1849, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:45:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:11'),
(1850, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:11'),
(1851, 6, 6, 2414.00, NULL, NULL, 'raw', '2026-04-30 18:45:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:11'),
(1852, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:11'),
(1853, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:45:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:17'),
(1854, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:17'),
(1855, 6, 6, 2403.00, NULL, NULL, 'raw', '2026-04-30 18:45:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:17'),
(1856, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:17.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:17'),
(1857, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:45:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:22'),
(1858, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:22'),
(1859, 6, 6, 2397.00, NULL, NULL, 'raw', '2026-04-30 18:45:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:22'),
(1860, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:22'),
(1861, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:45:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:27'),
(1862, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:27'),
(1863, 6, 6, 2395.00, NULL, NULL, 'raw', '2026-04-30 18:45:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:27'),
(1864, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:27'),
(1865, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:45:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:32'),
(1866, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:32'),
(1867, 6, 6, 2396.00, NULL, NULL, 'raw', '2026-04-30 18:45:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:32'),
(1868, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:45:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:32'),
(1869, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:45:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:38'),
(1870, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:38'),
(1871, 6, 6, 2401.00, NULL, NULL, 'raw', '2026-04-30 18:45:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:38'),
(1872, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:38'),
(1873, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:45:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:43'),
(1874, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:43'),
(1875, 6, 6, 2392.00, NULL, NULL, 'raw', '2026-04-30 18:45:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:43');
INSERT INTO `readings` (`id`, `device_id`, `sensor_type_id`, `reading_value`, `normalized_value`, `consumption_w`, `reading_unit`, `recorded_at`, `source`, `payload`, `created_at`) VALUES
(1876, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:43'),
(1877, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:45:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:48'),
(1878, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:48'),
(1879, 6, 6, 2400.00, NULL, NULL, 'raw', '2026-04-30 18:45:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:48'),
(1880, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:45:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:48'),
(1881, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:45:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:53'),
(1882, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:45:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:53'),
(1883, 6, 6, 2401.00, NULL, NULL, 'raw', '2026-04-30 18:45:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:53'),
(1884, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:45:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:53'),
(1885, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:45:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:45:58'),
(1886, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:45:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:45:58'),
(1887, 6, 6, 2397.00, NULL, NULL, 'raw', '2026-04-30 18:45:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:45:58'),
(1888, 5, 13, 17.30, NULL, NULL, 'cm', '2026-04-30 18:45:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:45:58'),
(1889, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:46:04.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:04'),
(1890, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:04.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:04'),
(1891, 6, 6, 2395.00, NULL, NULL, 'raw', '2026-04-30 18:46:04.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:04'),
(1892, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:46:04.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:04'),
(1893, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:46:09.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:09'),
(1894, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:09.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:09'),
(1895, 6, 6, 2391.00, NULL, NULL, 'raw', '2026-04-30 18:46:09.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:09'),
(1896, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:09.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:09'),
(1897, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:46:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:14'),
(1898, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:14'),
(1899, 6, 6, 2399.00, NULL, NULL, 'raw', '2026-04-30 18:46:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:14'),
(1900, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:14'),
(1901, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:46:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:19'),
(1902, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:19'),
(1903, 6, 6, 2384.00, NULL, NULL, 'raw', '2026-04-30 18:46:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:19'),
(1904, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:19'),
(1905, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:46:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:24'),
(1906, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:24'),
(1907, 6, 6, 2390.00, NULL, NULL, 'raw', '2026-04-30 18:46:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:24'),
(1908, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:24'),
(1909, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:46:30.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:30'),
(1910, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:30.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:30'),
(1911, 6, 6, 2399.00, NULL, NULL, 'raw', '2026-04-30 18:46:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:30'),
(1912, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:30.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:30'),
(1913, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:46:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:35'),
(1914, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:35'),
(1915, 6, 6, 2390.00, NULL, NULL, 'raw', '2026-04-30 18:46:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:35'),
(1916, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:35'),
(1917, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:46:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:40'),
(1918, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:40'),
(1919, 6, 6, 2401.00, NULL, NULL, 'raw', '2026-04-30 18:46:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:40'),
(1920, 5, 13, 30.68, NULL, NULL, 'cm', '2026-04-30 18:46:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:40'),
(1921, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:46:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:45'),
(1922, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:45'),
(1923, 6, 6, 2385.00, NULL, NULL, 'raw', '2026-04-30 18:46:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:45'),
(1924, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:45'),
(1925, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:46:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:50'),
(1926, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:50'),
(1927, 6, 6, 2400.00, NULL, NULL, 'raw', '2026-04-30 18:46:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:50'),
(1928, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:50'),
(1929, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:46:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:46:56'),
(1930, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:46:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:46:56'),
(1931, 6, 6, 2390.00, NULL, NULL, 'raw', '2026-04-30 18:46:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:46:56'),
(1932, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:46:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:46:56'),
(1933, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:47:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:01'),
(1934, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:01'),
(1935, 6, 6, 2384.00, NULL, NULL, 'raw', '2026-04-30 18:47:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:01'),
(1936, 5, 13, 31.49, NULL, NULL, 'cm', '2026-04-30 18:47:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:01'),
(1937, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:47:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:06'),
(1938, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:06'),
(1939, 6, 6, 2390.00, NULL, NULL, 'raw', '2026-04-30 18:47:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:06'),
(1940, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:47:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:06'),
(1941, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:47:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:11'),
(1942, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:11'),
(1943, 6, 6, 2381.00, NULL, NULL, 'raw', '2026-04-30 18:47:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:11'),
(1944, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:11'),
(1945, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:47:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:16'),
(1946, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:16'),
(1947, 6, 6, 2389.00, NULL, NULL, 'raw', '2026-04-30 18:47:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:16'),
(1948, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:16'),
(1949, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:47:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:22'),
(1950, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:22'),
(1951, 6, 6, 2393.00, NULL, NULL, 'raw', '2026-04-30 18:47:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:22'),
(1952, 5, 13, 17.30, NULL, NULL, 'cm', '2026-04-30 18:47:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:22'),
(1953, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:47:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:27'),
(1954, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:27'),
(1955, 6, 6, 2391.00, NULL, NULL, 'raw', '2026-04-30 18:47:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:27'),
(1956, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:27'),
(1957, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:47:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:32'),
(1958, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:32'),
(1959, 6, 6, 2382.00, NULL, NULL, 'raw', '2026-04-30 18:47:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:32'),
(1960, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:32'),
(1961, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:47:37.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:37'),
(1962, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:37.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:37'),
(1963, 6, 6, 2383.00, NULL, NULL, 'raw', '2026-04-30 18:47:37.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:37'),
(1964, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:37.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:37'),
(1965, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:47:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:43'),
(1966, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:43'),
(1967, 6, 6, 2387.00, NULL, NULL, 'raw', '2026-04-30 18:47:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:43'),
(1968, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:43'),
(1969, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:47:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:48'),
(1970, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:48'),
(1971, 6, 6, 2393.00, NULL, NULL, 'raw', '2026-04-30 18:47:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:48'),
(1972, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:48'),
(1973, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:47:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:53'),
(1974, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:53'),
(1975, 6, 6, 2391.00, NULL, NULL, 'raw', '2026-04-30 18:47:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:53'),
(1976, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:53'),
(1977, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:47:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:47:58'),
(1978, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:47:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:47:58'),
(1979, 6, 6, 2395.00, NULL, NULL, 'raw', '2026-04-30 18:47:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:47:58'),
(1980, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:47:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:47:58'),
(1981, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:48:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:03'),
(1982, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:03'),
(1983, 6, 6, 2374.00, NULL, NULL, 'raw', '2026-04-30 18:48:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:03'),
(1984, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:48:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:03'),
(1985, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:48:09.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:09'),
(1986, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:09.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:09'),
(1987, 6, 6, 2383.00, NULL, NULL, 'raw', '2026-04-30 18:48:09.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:09'),
(1988, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:48:09.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:09'),
(1989, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:48:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:14'),
(1990, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:14'),
(1991, 6, 6, 2389.00, NULL, NULL, 'raw', '2026-04-30 18:48:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:14'),
(1992, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:48:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:14'),
(1993, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:48:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:19'),
(1994, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:19'),
(1995, 6, 6, 2384.00, NULL, NULL, 'raw', '2026-04-30 18:48:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:19'),
(1996, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:48:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:19'),
(1997, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:48:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:24'),
(1998, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:24'),
(1999, 6, 6, 2391.00, NULL, NULL, 'raw', '2026-04-30 18:48:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:24'),
(2000, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:48:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:24'),
(2001, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:48:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:29'),
(2002, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:29'),
(2003, 6, 6, 2390.00, NULL, NULL, 'raw', '2026-04-30 18:48:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:29'),
(2004, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:48:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:29'),
(2005, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:48:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:35'),
(2006, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:35'),
(2007, 6, 6, 2381.00, NULL, NULL, 'raw', '2026-04-30 18:48:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:35'),
(2008, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:48:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:35'),
(2009, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:48:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:40'),
(2010, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:40'),
(2011, 6, 6, 2382.00, NULL, NULL, 'raw', '2026-04-30 18:48:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:40'),
(2012, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:48:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:40'),
(2013, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:48:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:45'),
(2014, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:45'),
(2015, 6, 6, 2381.00, NULL, NULL, 'raw', '2026-04-30 18:48:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:45'),
(2016, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:48:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:45'),
(2017, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:48:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:50'),
(2018, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:50'),
(2019, 6, 6, 2383.00, NULL, NULL, 'raw', '2026-04-30 18:48:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:50'),
(2020, 5, 13, 17.30, NULL, NULL, 'cm', '2026-04-30 18:48:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:50'),
(2021, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:48:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:48:56'),
(2022, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:48:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:48:56'),
(2023, 6, 6, 2384.00, NULL, NULL, 'raw', '2026-04-30 18:48:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:48:56'),
(2024, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:48:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:48:56'),
(2025, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:49:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:01'),
(2026, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:49:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:01'),
(2027, 6, 6, 2388.00, NULL, NULL, 'raw', '2026-04-30 18:49:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:01'),
(2028, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:01'),
(2029, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:49:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:06'),
(2030, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:49:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:06'),
(2031, 6, 6, 2382.00, NULL, NULL, 'raw', '2026-04-30 18:49:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:06'),
(2032, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:06'),
(2033, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:49:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:11'),
(2034, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:49:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:11'),
(2035, 6, 6, 2382.00, NULL, NULL, 'raw', '2026-04-30 18:49:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:11'),
(2036, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:11'),
(2037, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:49:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:17'),
(2038, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:49:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:17'),
(2039, 6, 6, 2378.00, NULL, NULL, 'raw', '2026-04-30 18:49:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:17'),
(2040, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:17.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:17'),
(2041, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:49:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:22'),
(2042, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:49:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:22'),
(2043, 6, 6, 2375.00, NULL, NULL, 'raw', '2026-04-30 18:49:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:22'),
(2044, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:49:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:22'),
(2045, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:49:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:27'),
(2046, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:49:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:27'),
(2047, 6, 6, 2382.00, NULL, NULL, 'raw', '2026-04-30 18:49:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:27'),
(2048, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:27'),
(2049, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:49:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:32'),
(2050, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:49:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:32'),
(2051, 6, 6, 2370.00, NULL, NULL, 'raw', '2026-04-30 18:49:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:32'),
(2052, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:32.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:32'),
(2053, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:49:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:38'),
(2054, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:49:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:38'),
(2055, 6, 6, 2384.00, NULL, NULL, 'raw', '2026-04-30 18:49:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:38'),
(2056, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:38'),
(2057, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:49:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:43'),
(2058, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:49:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:43'),
(2059, 6, 6, 2384.00, NULL, NULL, 'raw', '2026-04-30 18:49:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:43'),
(2060, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:43'),
(2061, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:49:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:48'),
(2062, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:49:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:48'),
(2063, 6, 6, 2373.00, NULL, NULL, 'raw', '2026-04-30 18:49:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:48'),
(2064, 5, 13, 31.49, NULL, NULL, 'cm', '2026-04-30 18:49:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:48'),
(2065, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:49:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:53'),
(2066, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:49:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:53'),
(2067, 6, 6, 2379.00, NULL, NULL, 'raw', '2026-04-30 18:49:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:53'),
(2068, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:49:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:53'),
(2069, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:49:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:49:58'),
(2070, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:49:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:49:58'),
(2071, 6, 6, 2370.00, NULL, NULL, 'raw', '2026-04-30 18:49:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:49:58'),
(2072, 5, 13, 17.30, NULL, NULL, 'cm', '2026-04-30 18:49:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:49:58'),
(2073, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:50:04.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:04'),
(2074, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:50:04.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:04'),
(2075, 6, 6, 2378.00, NULL, NULL, 'raw', '2026-04-30 18:50:04.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:04'),
(2076, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:50:04.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:04'),
(2077, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:50:09.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:09'),
(2078, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:50:09.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:09'),
(2079, 6, 6, 2379.00, NULL, NULL, 'raw', '2026-04-30 18:50:09.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:09'),
(2080, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:50:09.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:09'),
(2081, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:50:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:14'),
(2082, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:50:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:14'),
(2083, 6, 6, 2375.00, NULL, NULL, 'raw', '2026-04-30 18:50:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:14'),
(2084, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:50:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:14'),
(2085, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:50:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:19'),
(2086, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:50:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:19'),
(2087, 6, 6, 2382.00, NULL, NULL, 'raw', '2026-04-30 18:50:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:19'),
(2088, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:50:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:19'),
(2089, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:50:25.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:25'),
(2090, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:50:25.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:25'),
(2091, 6, 6, 2368.00, NULL, NULL, 'raw', '2026-04-30 18:50:25.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:25'),
(2092, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:50:25.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:25'),
(2093, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:50:30.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:30'),
(2094, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:50:30.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:30'),
(2095, 6, 6, 2369.00, NULL, NULL, 'raw', '2026-04-30 18:50:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:30'),
(2096, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:50:30.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:30'),
(2097, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:50:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:35'),
(2098, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:50:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:35'),
(2099, 6, 6, 2372.00, NULL, NULL, 'raw', '2026-04-30 18:50:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:35'),
(2100, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:50:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:35'),
(2101, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:50:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:40'),
(2102, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:50:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:40'),
(2103, 6, 6, 2363.00, NULL, NULL, 'raw', '2026-04-30 18:50:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:40'),
(2104, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:50:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:40'),
(2105, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:50:46.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:46'),
(2106, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:50:46.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:46'),
(2107, 6, 6, 2375.00, NULL, NULL, 'raw', '2026-04-30 18:50:46.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:46'),
(2108, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:50:46.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:46'),
(2109, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:50:51.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:51'),
(2110, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:50:51.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:51'),
(2111, 6, 6, 2369.00, NULL, NULL, 'raw', '2026-04-30 18:50:51.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:51'),
(2112, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:50:51.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:51'),
(2113, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:50:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:50:56'),
(2114, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:50:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:50:56'),
(2115, 6, 6, 2364.00, NULL, NULL, 'raw', '2026-04-30 18:50:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:50:56'),
(2116, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:50:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:50:56'),
(2117, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:51:02.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:02'),
(2118, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:51:02.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:02'),
(2119, 6, 6, 2368.00, NULL, NULL, 'raw', '2026-04-30 18:51:02.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:02'),
(2120, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:02.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:02'),
(2121, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:51:07.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:07'),
(2122, 2, 2, 28.00, NULL, NULL, '%', '2026-04-30 18:51:07.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:07'),
(2123, 6, 6, 2377.00, NULL, NULL, 'raw', '2026-04-30 18:51:07.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:07'),
(2124, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:07.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:07'),
(2125, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:51:12.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:12'),
(2126, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:12.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:12'),
(2127, 6, 6, 2363.00, NULL, NULL, 'raw', '2026-04-30 18:51:12.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:12'),
(2128, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:51:12.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:12'),
(2129, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:51:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:17'),
(2130, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:17'),
(2131, 6, 6, 2353.00, NULL, NULL, 'raw', '2026-04-30 18:51:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:17'),
(2132, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:51:17.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:17'),
(2133, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:51:23.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:23'),
(2134, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:23.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:23'),
(2135, 6, 6, 2368.00, NULL, NULL, 'raw', '2026-04-30 18:51:23.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:23'),
(2136, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:23.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:23'),
(2137, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 18:51:28.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:28'),
(2138, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:28.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:28'),
(2139, 6, 6, 2368.00, NULL, NULL, 'raw', '2026-04-30 18:51:28.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:28'),
(2140, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:28.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:28'),
(2141, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:51:33.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:33'),
(2142, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:33.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:33'),
(2143, 6, 6, 2374.00, NULL, NULL, 'raw', '2026-04-30 18:51:33.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:33'),
(2144, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:33.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:33'),
(2145, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:51:39.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:39'),
(2146, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:39.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:39'),
(2147, 6, 6, 2373.00, NULL, NULL, 'raw', '2026-04-30 18:51:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:39'),
(2148, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:39'),
(2149, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:51:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:44'),
(2150, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:44'),
(2151, 6, 6, 2362.00, NULL, NULL, 'raw', '2026-04-30 18:51:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:44'),
(2152, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:44'),
(2153, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 18:51:49.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:49'),
(2154, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:49.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:49'),
(2155, 6, 6, 2377.00, NULL, NULL, 'raw', '2026-04-30 18:51:49.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:49'),
(2156, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:49.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:49'),
(2157, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:51:54.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:51:54'),
(2158, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:51:54.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:51:54'),
(2159, 6, 6, 2355.00, NULL, NULL, 'raw', '2026-04-30 18:51:54.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:51:54'),
(2160, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:51:54.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:51:54'),
(2161, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:52:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:00'),
(2162, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:00'),
(2163, 6, 6, 2358.00, NULL, NULL, 'raw', '2026-04-30 18:52:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:00'),
(2164, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:52:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:00'),
(2165, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:52:05.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:05'),
(2166, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:05.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:05'),
(2167, 6, 6, 2354.00, NULL, NULL, 'raw', '2026-04-30 18:52:05.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:05'),
(2168, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:52:05.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:05'),
(2169, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:52:10.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:10'),
(2170, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:10.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:10'),
(2171, 6, 6, 2352.00, NULL, NULL, 'raw', '2026-04-30 18:52:10.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:10'),
(2172, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:52:10.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:10'),
(2173, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:52:15.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:15'),
(2174, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:15.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:15'),
(2175, 6, 6, 2357.00, NULL, NULL, 'raw', '2026-04-30 18:52:15.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:15'),
(2176, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:52:15.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:15'),
(2177, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:52:20.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:20'),
(2178, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:20.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:20'),
(2179, 6, 6, 2370.00, NULL, NULL, 'raw', '2026-04-30 18:52:20.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:20'),
(2180, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:52:20.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:20'),
(2181, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 18:52:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:26'),
(2182, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:26'),
(2183, 6, 6, 2368.00, NULL, NULL, 'raw', '2026-04-30 18:52:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:26'),
(2184, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:52:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:26'),
(2185, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:52:31.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:31'),
(2186, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:31.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:31');
INSERT INTO `readings` (`id`, `device_id`, `sensor_type_id`, `reading_value`, `normalized_value`, `consumption_w`, `reading_unit`, `recorded_at`, `source`, `payload`, `created_at`) VALUES
(2187, 6, 6, 2365.00, NULL, NULL, 'raw', '2026-04-30 18:52:31.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:31'),
(2188, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:52:31.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:31'),
(2189, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:52:36.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:36'),
(2190, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:36.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:36'),
(2191, 6, 6, 2366.00, NULL, NULL, 'raw', '2026-04-30 18:52:36.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:36'),
(2192, 5, 13, 18.28, NULL, NULL, 'cm', '2026-04-30 18:52:36.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:36'),
(2193, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:52:42.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:42'),
(2194, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:42.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:42'),
(2195, 6, 6, 2358.00, NULL, NULL, 'raw', '2026-04-30 18:52:42.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:42'),
(2196, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 18:52:42.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:42'),
(2197, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 18:52:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:47'),
(2198, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:47'),
(2199, 6, 6, 2369.00, NULL, NULL, 'raw', '2026-04-30 18:52:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:47'),
(2200, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:52:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:47'),
(2201, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 18:52:52.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:52'),
(2202, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:52.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:52'),
(2203, 6, 6, 2365.00, NULL, NULL, 'raw', '2026-04-30 18:52:52.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:52'),
(2204, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:52:52.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:52'),
(2205, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:52:57.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:52:57'),
(2206, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:52:57.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:52:57'),
(2207, 6, 6, 2356.00, NULL, NULL, 'raw', '2026-04-30 18:52:57.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:52:57'),
(2208, 5, 13, 31.49, NULL, NULL, 'cm', '2026-04-30 18:52:57.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:52:57'),
(2209, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 18:53:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:03'),
(2210, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:53:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:03'),
(2211, 6, 6, 2352.00, NULL, NULL, 'raw', '2026-04-30 18:53:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:03'),
(2212, 5, 13, 2.97, NULL, NULL, 'cm', '2026-04-30 18:53:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:03'),
(2213, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 18:53:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:08'),
(2214, 2, 2, 27.00, NULL, NULL, '%', '2026-04-30 18:53:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:08'),
(2215, 6, 6, 2362.00, NULL, NULL, 'raw', '2026-04-30 18:53:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:08'),
(2216, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 18:53:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:08'),
(2217, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 18:53:13.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:13'),
(2218, 2, 2, 29.00, NULL, NULL, '%', '2026-04-30 18:53:13.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:13'),
(2219, 6, 6, 2372.00, NULL, NULL, 'raw', '2026-04-30 18:53:13.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:13'),
(2220, 5, 13, 4.27, NULL, NULL, 'cm', '2026-04-30 18:53:13.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:13'),
(2221, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:53:18.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:18'),
(2222, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:53:18.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:18'),
(2223, 6, 6, 2380.00, NULL, NULL, 'raw', '2026-04-30 18:53:18.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:18'),
(2224, 5, 13, 17.65, NULL, NULL, 'cm', '2026-04-30 18:53:18.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:18'),
(2225, 1, 1, 29.20, NULL, NULL, 'C', '2026-04-30 18:53:23.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:23'),
(2226, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:53:23.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:23'),
(2227, 6, 6, 2352.00, NULL, NULL, 'raw', '2026-04-30 18:53:23.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:23'),
(2228, 5, 13, 1.66, NULL, NULL, 'cm', '2026-04-30 18:53:23.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:23'),
(2229, 1, 1, 29.00, NULL, NULL, 'C', '2026-04-30 18:53:29.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:29'),
(2230, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:53:29.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:29'),
(2231, 6, 6, 2369.00, NULL, NULL, 'raw', '2026-04-30 18:53:29.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:29'),
(2232, 5, 13, 4.27, NULL, NULL, 'cm', '2026-04-30 18:53:29.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:29'),
(2233, 1, 1, 30.10, NULL, NULL, 'C', '2026-04-30 18:53:34.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:34'),
(2234, 2, 2, 30.00, NULL, NULL, '%', '2026-04-30 18:53:34.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:34'),
(2235, 6, 6, 2368.00, NULL, NULL, 'raw', '2026-04-30 18:53:34.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:34'),
(2236, 5, 13, 18.59, NULL, NULL, 'cm', '2026-04-30 18:53:34.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:34'),
(2237, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:53:39.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:39'),
(2238, 2, 2, 33.00, NULL, NULL, '%', '2026-04-30 18:53:39.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:39'),
(2239, 6, 6, 2364.00, NULL, NULL, 'raw', '2026-04-30 18:53:39.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:39'),
(2240, 5, 13, 3.29, NULL, NULL, 'cm', '2026-04-30 18:53:39.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:39'),
(2241, 1, 1, 30.90, NULL, NULL, 'C', '2026-04-30 18:53:44.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:44'),
(2242, 2, 2, 31.00, NULL, NULL, '%', '2026-04-30 18:53:44.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:44'),
(2243, 6, 6, 2368.00, NULL, NULL, 'raw', '2026-04-30 18:53:44.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:44'),
(2244, 5, 13, 3.94, NULL, NULL, 'cm', '2026-04-30 18:53:44.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:44'),
(2245, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 18:53:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:50'),
(2246, 2, 2, 39.00, NULL, NULL, '%', '2026-04-30 18:53:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:50'),
(2247, 6, 6, 2373.00, NULL, NULL, 'raw', '2026-04-30 18:53:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:50'),
(2248, 5, 13, 3.94, NULL, NULL, 'cm', '2026-04-30 18:53:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:50'),
(2249, 1, 1, 30.50, NULL, NULL, 'C', '2026-04-30 18:53:55.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:53:55'),
(2250, 2, 2, 38.00, NULL, NULL, '%', '2026-04-30 18:53:55.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:53:55'),
(2251, 6, 6, 2369.00, NULL, NULL, 'raw', '2026-04-30 18:53:55.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:53:55'),
(2252, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:53:55.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:53:55'),
(2253, 1, 1, 30.30, NULL, NULL, 'C', '2026-04-30 18:54:00.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 16:54:00'),
(2254, 2, 2, 33.00, NULL, NULL, '%', '2026-04-30 18:54:00.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 16:54:00'),
(2255, 6, 6, 2367.00, NULL, NULL, 'raw', '2026-04-30 18:54:00.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 16:54:00'),
(2256, 5, 13, 17.32, NULL, NULL, 'cm', '2026-04-30 18:54:00.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 16:54:00'),
(2257, 1, 1, 0.40, NULL, NULL, 'C', '2026-04-30 21:07:47.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:07:47'),
(2258, 2, 2, 0.00, NULL, NULL, '%', '2026-04-30 21:07:47.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:07:47'),
(2259, 6, 6, 2173.00, NULL, NULL, 'raw', '2026-04-30 21:07:47.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:07:47'),
(2260, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 21:07:47.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:07:47'),
(2261, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 21:07:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:07:53'),
(2262, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:07:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:07:53'),
(2263, 6, 6, 2164.00, NULL, NULL, 'raw', '2026-04-30 21:07:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:07:53'),
(2264, 5, 13, 17.00, NULL, NULL, 'cm', '2026-04-30 21:07:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:07:53'),
(2265, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 21:07:58.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:07:58'),
(2266, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:07:58.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:07:58'),
(2267, 6, 6, 2166.00, NULL, NULL, 'raw', '2026-04-30 21:07:58.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:07:58'),
(2268, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 21:07:58.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:07:58'),
(2269, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 21:08:03.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:03'),
(2270, 2, 2, 17.00, NULL, NULL, '%', '2026-04-30 21:08:03.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:03'),
(2271, 6, 6, 2161.00, NULL, NULL, 'raw', '2026-04-30 21:08:03.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:03'),
(2272, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 21:08:03.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:03'),
(2273, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 21:08:08.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:08'),
(2274, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:08:08.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:08'),
(2275, 6, 6, 2159.00, NULL, NULL, 'raw', '2026-04-30 21:08:08.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:08'),
(2276, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 21:08:08.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:08'),
(2277, 1, 1, 29.80, NULL, NULL, 'C', '2026-04-30 21:08:14.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:14'),
(2278, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:08:14.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:14'),
(2279, 6, 6, 2160.00, NULL, NULL, 'raw', '2026-04-30 21:08:14.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:14'),
(2280, 5, 13, 16.69, NULL, NULL, 'cm', '2026-04-30 21:08:14.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:14'),
(2281, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 21:08:19.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:19'),
(2282, 2, 2, 19.00, NULL, NULL, '%', '2026-04-30 21:08:19.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:19'),
(2283, 6, 6, 2179.00, NULL, NULL, 'raw', '2026-04-30 21:08:19.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:19'),
(2284, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:08:19.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:19'),
(2285, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 21:08:24.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:24'),
(2286, 2, 2, 20.00, NULL, NULL, '%', '2026-04-30 21:08:24.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:24'),
(2287, 6, 6, 2162.00, NULL, NULL, 'raw', '2026-04-30 21:08:24.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:24'),
(2288, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:08:24.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:24'),
(2289, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 21:08:30.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:30'),
(2290, 2, 2, 19.00, NULL, NULL, '%', '2026-04-30 21:08:30.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:30'),
(2291, 6, 6, 2175.00, NULL, NULL, 'raw', '2026-04-30 21:08:30.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:30'),
(2292, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:08:30.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:30'),
(2293, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 21:08:35.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:35'),
(2294, 2, 2, 19.00, NULL, NULL, '%', '2026-04-30 21:08:35.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:35'),
(2295, 6, 6, 2154.00, NULL, NULL, 'raw', '2026-04-30 21:08:35.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:35'),
(2296, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:08:35.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:35'),
(2297, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 21:08:40.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:40'),
(2298, 2, 2, 19.00, NULL, NULL, '%', '2026-04-30 21:08:40.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:40'),
(2299, 6, 6, 2150.00, NULL, NULL, 'raw', '2026-04-30 21:08:40.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:40'),
(2300, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:08:40.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:40'),
(2301, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 21:08:45.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:45'),
(2302, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:08:45.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:45'),
(2303, 6, 6, 2170.00, NULL, NULL, 'raw', '2026-04-30 21:08:45.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:45'),
(2304, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:08:45.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:45'),
(2305, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 21:08:50.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:50'),
(2306, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:08:50.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:50'),
(2307, 6, 6, 2145.00, NULL, NULL, 'raw', '2026-04-30 21:08:50.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:50'),
(2308, 5, 13, 6.23, NULL, NULL, 'cm', '2026-04-30 21:08:50.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:50'),
(2309, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 21:08:56.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:08:56'),
(2310, 2, 2, 20.00, NULL, NULL, '%', '2026-04-30 21:08:56.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:08:56'),
(2311, 6, 6, 2160.00, NULL, NULL, 'raw', '2026-04-30 21:08:56.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:08:56'),
(2312, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:08:56.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:08:56'),
(2313, 1, 1, 30.20, NULL, NULL, 'C', '2026-04-30 21:09:01.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:01'),
(2314, 2, 2, 17.00, NULL, NULL, '%', '2026-04-30 21:09:01.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:01'),
(2315, 6, 6, 2133.00, NULL, NULL, 'raw', '2026-04-30 21:09:01.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:01'),
(2316, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 21:09:01.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:01'),
(2317, 1, 1, 30.60, NULL, NULL, 'C', '2026-04-30 21:09:06.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:06'),
(2318, 2, 2, 16.00, NULL, NULL, '%', '2026-04-30 21:09:06.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:06'),
(2319, 6, 6, 2160.00, NULL, NULL, 'raw', '2026-04-30 21:09:06.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:06'),
(2320, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 21:09:06.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:06'),
(2321, 1, 1, 30.00, NULL, NULL, 'C', '2026-04-30 21:09:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:11'),
(2322, 2, 2, 16.00, NULL, NULL, '%', '2026-04-30 21:09:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:11'),
(2323, 6, 6, 2151.00, NULL, NULL, 'raw', '2026-04-30 21:09:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:11'),
(2324, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 21:09:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:11'),
(2325, 1, 1, 30.80, NULL, NULL, 'C', '2026-04-30 21:09:17.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:17'),
(2326, 2, 2, 15.00, NULL, NULL, '%', '2026-04-30 21:09:17.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:17'),
(2327, 6, 6, 2151.00, NULL, NULL, 'raw', '2026-04-30 21:09:17.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:17'),
(2328, 5, 13, 16.04, NULL, NULL, 'cm', '2026-04-30 21:09:17.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:17'),
(2329, 1, 1, 30.70, NULL, NULL, 'C', '2026-04-30 21:09:22.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:22'),
(2330, 2, 2, 15.00, NULL, NULL, '%', '2026-04-30 21:09:22.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:22'),
(2331, 6, 6, 2162.00, NULL, NULL, 'raw', '2026-04-30 21:09:22.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:22'),
(2332, 5, 13, 7.20, NULL, NULL, 'cm', '2026-04-30 21:09:22.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:22'),
(2333, 1, 1, 30.20, NULL, NULL, 'C', '2026-04-30 21:09:27.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:27'),
(2334, 2, 2, 22.00, NULL, NULL, '%', '2026-04-30 21:09:27.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:27'),
(2335, 6, 6, 2150.00, NULL, NULL, 'raw', '2026-04-30 21:09:27.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:27'),
(2336, 5, 13, 2.32, NULL, NULL, 'cm', '2026-04-30 21:09:27.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:27'),
(2337, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 21:09:32.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:32'),
(2338, 2, 2, 22.00, NULL, NULL, '%', '2026-04-30 21:09:32.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:32'),
(2339, 6, 6, 2135.00, NULL, NULL, 'raw', '2026-04-30 21:09:32.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:32'),
(2340, 5, 13, 16.67, NULL, NULL, 'cm', '2026-04-30 21:09:33.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:33'),
(2341, 1, 1, 29.50, NULL, NULL, 'C', '2026-04-30 21:09:38.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:38'),
(2342, 2, 2, 21.00, NULL, NULL, '%', '2026-04-30 21:09:38.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:38'),
(2343, 6, 6, 2151.00, NULL, NULL, 'raw', '2026-04-30 21:09:38.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:38'),
(2344, 5, 13, 1.99, NULL, NULL, 'cm', '2026-04-30 21:09:38.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:38'),
(2345, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 21:09:43.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:43'),
(2346, 2, 2, 23.00, NULL, NULL, '%', '2026-04-30 21:09:43.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:43'),
(2347, 6, 6, 2140.00, NULL, NULL, 'raw', '2026-04-30 21:09:43.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:43'),
(2348, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:09:43.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:43'),
(2349, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 21:09:48.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:48'),
(2350, 2, 2, 21.00, NULL, NULL, '%', '2026-04-30 21:09:48.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:48'),
(2351, 6, 6, 2125.00, NULL, NULL, 'raw', '2026-04-30 21:09:48.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:48'),
(2352, 5, 13, 16.69, NULL, NULL, 'cm', '2026-04-30 21:09:48.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:48'),
(2353, 1, 1, 29.90, NULL, NULL, 'C', '2026-04-30 21:09:53.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:53'),
(2354, 2, 2, 20.00, NULL, NULL, '%', '2026-04-30 21:09:53.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:53'),
(2355, 6, 6, 2134.00, NULL, NULL, 'raw', '2026-04-30 21:09:53.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:53'),
(2356, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:09:53.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:53'),
(2357, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 21:09:59.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:09:59'),
(2358, 2, 2, 19.00, NULL, NULL, '%', '2026-04-30 21:09:59.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:09:59'),
(2359, 6, 6, 2144.00, NULL, NULL, 'raw', '2026-04-30 21:09:59.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:09:59'),
(2360, 5, 13, 16.69, NULL, NULL, 'cm', '2026-04-30 21:09:59.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:09:59'),
(2361, 1, 1, 29.40, NULL, NULL, 'C', '2026-04-30 21:10:04.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:10:04'),
(2362, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:10:04.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:10:04'),
(2363, 6, 6, 2121.00, NULL, NULL, 'raw', '2026-04-30 21:10:04.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:10:04'),
(2364, 5, 13, 15.73, NULL, NULL, 'cm', '2026-04-30 21:10:04.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:10:04'),
(2365, 1, 1, 29.60, NULL, NULL, 'C', '2026-04-30 21:10:11.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:10:11'),
(2366, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:10:11.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:10:11'),
(2367, 6, 6, 2141.00, NULL, NULL, 'raw', '2026-04-30 21:10:11.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:10:11'),
(2368, 5, 13, 15.73, NULL, NULL, 'cm', '2026-04-30 21:10:11.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:10:11'),
(2369, 1, 1, 29.10, NULL, NULL, 'C', '2026-04-30 21:10:16.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:10:16'),
(2370, 2, 2, 18.00, NULL, NULL, '%', '2026-04-30 21:10:16.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:10:16'),
(2371, 6, 6, 2130.00, NULL, NULL, 'raw', '2026-04-30 21:10:16.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:10:16'),
(2372, 5, 13, 16.36, NULL, NULL, 'cm', '2026-04-30 21:10:16.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:10:16'),
(2373, 1, 1, 29.30, NULL, NULL, 'C', '2026-04-30 21:10:21.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:10:21'),
(2374, 2, 2, 17.00, NULL, NULL, '%', '2026-04-30 21:10:21.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:10:21'),
(2375, 6, 6, 2109.00, NULL, NULL, 'raw', '2026-04-30 21:10:21.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:10:21'),
(2376, 5, 13, 16.69, NULL, NULL, 'cm', '2026-04-30 21:10:21.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:10:21'),
(2377, 1, 1, 29.70, NULL, NULL, 'C', '2026-04-30 21:10:26.000000', 'esp32', '{\"tipo\": \"temperatura\", \"device_code\": \"temp_01\"}', '2026-04-30 19:10:26'),
(2378, 2, 2, 17.00, NULL, NULL, '%', '2026-04-30 21:10:26.000000', 'esp32', '{\"tipo\": \"humedad\", \"device_code\": \"hum_01\"}', '2026-04-30 19:10:26'),
(2379, 6, 6, 2141.00, NULL, NULL, 'raw', '2026-04-30 21:10:26.000000', 'esp32', '{\"tipo\": \"calidad_aire\", \"device_code\": \"mq135_01\"}', '2026-04-30 19:10:26'),
(2380, 5, 13, 16.69, NULL, NULL, 'cm', '2026-04-30 21:10:26.000000', 'esp32', '{\"tipo\": \"distancia_cm\", \"device_code\": \"door_01\"}', '2026-04-30 19:10:26'),
(2381, 8, 8, 21.09, 21.09, NULL, 'C', '2026-05-03 17:44:48.710462', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-05-03 15:44:48'),
(2382, 9, 9, 57.00, 57.00, NULL, '%', '2026-05-03 17:44:48.737728', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}', '2026-05-03 15:44:48'),
(2383, 10, 10, 30.00, 30.00, NULL, '%', '2026-05-03 17:44:48.759691', 'simulado', '{\"sensor_name\": \"sensor_luz\"}', '2026-05-03 15:44:48'),
(2384, 11, 11, 2.36, 2.36, NULL, 'C', '2026-05-03 17:44:48.780592', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}', '2026-05-03 15:44:48'),
(2385, 8, 8, 20.85, 20.85, NULL, 'C', '2026-05-03 18:17:56.380784', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-05-03 16:17:56'),
(2386, 9, 9, 53.00, 53.00, NULL, '%', '2026-05-03 18:17:56.402905', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}', '2026-05-03 16:17:56'),
(2387, 10, 10, 39.00, 39.00, NULL, '%', '2026-05-03 18:17:56.423529', 'simulado', '{\"sensor_name\": \"sensor_luz\"}', '2026-05-03 16:17:56'),
(2388, 11, 11, 4.60, 4.60, NULL, 'C', '2026-05-03 18:17:56.444931', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}', '2026-05-03 16:17:56'),
(2389, 8, 8, 20.85, 20.85, NULL, 'C', '2026-05-03 18:18:00.817522', 'simulado', '{\"sensor_name\": \"sensor_temperatura\"}', '2026-05-03 16:18:00'),
(2390, 9, 9, 53.00, 53.00, NULL, '%', '2026-05-03 18:18:00.842649', 'simulado', '{\"sensor_name\": \"sensor_humedad\"}', '2026-05-03 16:18:00'),
(2391, 10, 10, 39.00, 39.00, NULL, '%', '2026-05-03 18:18:00.861983', 'simulado', '{\"sensor_name\": \"sensor_luz\"}', '2026-05-03 16:18:00'),
(2392, 11, 11, 4.60, 4.60, NULL, 'C', '2026-05-03 18:18:00.882103', 'simulado', '{\"sensor_name\": \"sensor_nevera\"}', '2026-05-03 16:18:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reviews`
--

CREATE TABLE `reviews` (
  `id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED NOT NULL,
  `rating` tinyint NOT NULL,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `comment` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `reviews`
--

INSERT INTO `reviews` (`id`, `user_id`, `rating`, `title`, `comment`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 8, 5, 'Muy contento', 'Muy bueno', 1, '2026-05-03 17:38:17', '2026-05-03 17:38:17'),
(2, 8, 5, 'jdwjoed', 'joedjoeojd', 1, '2026-05-03 17:38:34', '2026-05-03 17:38:34'),
(3, 9, 5, 'Hola', 'Adios', 1, '2026-05-04 00:21:31', '2026-05-04 00:21:31');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `review_images`
--

CREATE TABLE `review_images` (
  `id` bigint UNSIGNED NOT NULL,
  `review_id` bigint UNSIGNED NOT NULL,
  `image_path` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `review_responses`
--

CREATE TABLE `review_responses` (
  `id` bigint UNSIGNED NOT NULL,
  `review_id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED NOT NULL,
  `response_text` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` bigint UNSIGNED NOT NULL,
  `code` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `code`, `name`, `description`, `created_at`) VALUES
(1, 'superusuario', 'Superusuario', 'Acceso total al sistema', '2026-03-29 19:29:08'),
(2, 'administrador', 'Administrador', 'Gestión operativa y administrativa', '2026-03-29 19:29:08'),
(3, 'cliente', 'Cliente', 'Usuario final del supermercado', '2026-03-29 19:29:08'),
(4, 'empleado', 'Empleado', 'Operación diaria e inventario', '2026-03-29 19:29:08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sensor_types`
--

CREATE TABLE `sensor_types` (
  `id` bigint UNSIGNED NOT NULL,
  `code` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `unit` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` enum('ambiental','seguridad','consumo','estado','camara','otro') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'otro',
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `sensor_types`
--

INSERT INTO `sensor_types` (`id`, `code`, `name`, `unit`, `category`, `description`, `created_at`) VALUES
(1, 'TEMP_AIR', 'Temperatura ambiente', 'C', 'ambiental', 'Lectura de temperatura del supermercado', '2026-03-29 19:29:08'),
(2, 'HUM_AIR', 'Humedad ambiente', '%', 'ambiental', 'Lectura de humedad relativa', '2026-03-29 19:29:08'),
(3, 'LIGHT_STATE', 'Estado de luz', 'ON/OFF', 'estado', 'Estado de iluminación', '2026-03-29 19:29:08'),
(4, 'FRIDGE_TEMP', 'Temperatura de nevera', 'C', 'ambiental', 'Temperatura en cámara frigorífica', '2026-03-29 19:29:08'),
(5, 'DOOR_STATE', 'Estado de puerta', 'abierta/cerrada', 'estado', 'Estado de la puerta de acceso', '2026-03-29 19:29:08'),
(6, 'MQ135_AIR', 'Calidad de aire MQ-135', 'indice', 'ambiental', 'Índice de calidad de aire', '2026-03-29 19:29:08'),
(7, 'CAM_EVENT', 'Evento de cámara', NULL, 'camara', 'Captura y eventos de cámara', '2026-03-29 19:29:08'),
(8, 'temperatura', 'Temperatura', 'C', 'ambiental', 'Sensor de temperatura ambiental', '2026-04-29 15:06:40'),
(9, 'humedad', 'Humedad', '%', 'ambiental', 'Sensor de humedad ambiental', '2026-04-29 15:06:40'),
(10, 'luz', 'Luz', '%', 'ambiental', 'Sensor de luz', '2026-04-29 15:06:40'),
(11, 'nevera', 'Nevera', 'C', 'consumo', 'Sensor de temperatura de nevera', '2026-04-29 15:06:41'),
(12, 'puerta', 'Puerta', NULL, 'estado', 'Sensor de estado de puerta', '2026-04-29 15:06:41'),
(13, 'DISTANCE_CM', 'Distancia ultrasónica', 'cm', 'estado', 'Distancia medida por sensor HC-SR04', '2026-04-30 08:55:28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `state_history`
--

CREATE TABLE `state_history` (
  `id` bigint UNSIGNED NOT NULL,
  `device_id` bigint UNSIGNED NOT NULL,
  `state_code` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `old_value` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `new_value` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `changed_at` datetime(6) NOT NULL,
  `event_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `source` enum('simulado','esp32','manual','sistema','importado') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'simulado',
  `payload` json DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `state_history`
--

INSERT INTO `state_history` (`id`, `device_id`, `state_code`, `old_value`, `new_value`, `changed_at`, `event_type`, `source`, `payload`) VALUES
(1, 5, 'door_state', 'cerrada', 'abierta', '2025-12-01 18:57:22.533696', 'entrada', 'importado', '{\"archivo\": \"sensor_puerta.json\"}'),
(2, 5, 'door_state', 'abierta', 'cerrada', '2025-12-01 18:57:23.680742', 'salida', 'importado', '{\"archivo\": \"sensor_puerta.json\"}'),
(3, 5, 'door_state', 'cerrada', 'abierta', '2025-12-01 19:28:35.545664', 'entrada', 'importado', '{\"archivo\": \"sensor_puerta.json\"}'),
(4, 12, 'estado', NULL, 'abierta', '2026-04-29 17:06:41.075301', 'cambio_estado', 'simulado', '{\"sensor_name\": \"sensor_puerta\"}'),
(5, 12, 'estado', 'abierta', 'cerrada', '2026-04-29 17:55:46.118265', 'cambio_estado', 'simulado', '{\"sensor_name\": \"sensor_puerta\"}'),
(6, 12, 'estado', 'cerrada', 'abierta', '2026-04-30 18:13:24.349868', 'cambio_estado', 'simulado', '{\"sensor_name\": \"sensor_puerta\"}'),
(7, 12, 'estado', 'abierta', 'cerrada', '2026-04-30 18:13:27.084990', 'cambio_estado', 'simulado', '{\"sensor_name\": \"sensor_puerta\"}'),
(8, 12, 'estado', 'cerrada', 'abierta', '2026-05-03 17:44:48.802298', 'cambio_estado', 'simulado', '{\"sensor_name\": \"sensor_puerta\"}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` bigint UNSIGNED NOT NULL,
  `role_id` bigint UNSIGNED NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `profile_image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deactivated_at` datetime DEFAULT NULL,
  `last_login_at` datetime DEFAULT NULL,
  `loyalty_points` int NOT NULL DEFAULT '0',
  `total_spent` decimal(10,2) NOT NULL DEFAULT '0.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `role_id`, `nombre`, `email`, `password_hash`, `profile_image`, `is_active`, `created_at`, `updated_at`, `deactivated_at`, `last_login_at`, `loyalty_points`, `total_spent`) VALUES
(1, 1, 'Superusuario', 'root@supermercado.com', 'e14cb9e5c0eeee0ea313a4e04fbd10aa17ac17aa33a3cad4bdfe74b87ca18ef8', NULL, 1, '2026-03-29 19:29:08', '2026-05-04 16:39:43', NULL, '2026-05-04 18:39:43', 0, 0.00),
(2, 2, 'Administrador', 'admin@supermercado.com', '3b612c75a7b5048a435fb6ec81e52ff92d6d795a8b5a9c17070f6a63c97a53b2', NULL, 1, '2026-03-29 19:29:08', '2026-05-03 21:45:41', NULL, '2026-05-03 23:45:41', 0, 0.00),
(3, 3, 'Cliente', 'cliente@supermercado.com', '09a31a7001e261ab1e056182a71d3cf57f582ca9a29cff5eb83be0f0549730a9', NULL, 1, '2026-03-29 19:29:08', '2026-03-29 19:47:06', NULL, NULL, 0, 0.00),
(5, 3, 'Arturo', 'arturo@clubpenguin.com', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', NULL, 1, '2026-03-29 19:29:08', '2026-03-29 19:29:08', NULL, NULL, 0, 0.00),
(6, 3, 'Jesus', 'jesus@panda.com', '68ed251400d644dbca42c908cf6835a3aeeb8e857d3141829a65ef3fb9b2d156', NULL, 1, '2026-03-29 19:29:08', '2026-03-29 19:29:08', NULL, NULL, 0, 0.00),
(7, 4, 'Empleado', 'empleado@supermercado.com', 'd90ca2b319506bc8dd4dc77b7484226d5e7524c397e1d9d419be7a2d84b30098', NULL, 1, '2026-03-29 19:29:08', '2026-05-03 21:45:51', NULL, '2026-05-03 23:45:51', 0, 0.00),
(8, 3, 'Miguel Prueba Foto', 'miguelpruebafoto@fakemail.com', '0f7f8eec62dfbd1df0ffbe6f93a575730f1e8befed475f3e682d653f8a00d1c8', 'assets/profile_pics/profile_1777573316785.png', 1, '2026-04-30 18:22:01', '2026-05-03 15:38:17', NULL, '2026-05-03 17:38:17', 0, 0.00),
(9, 3, 'Miguel Angel Prueba Foto', 'miguelpruebafoo@fakemail.com', '0f7f8eec62dfbd1df0ffbe6f93a575730f1e8befed475f3e682d653f8a00d1c8', 'profile_images/profile_1777846906030.png', 1, '2026-04-30 18:25:56', '2026-05-04 16:38:12', NULL, '2026-05-04 18:37:41', 24, 265.50);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vw_estado_actual`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vw_estado_actual` (
`device_code` varchar(50)
,`device_name` varchar(120)
,`state_code` varchar(50)
,`state_value` varchar(100)
,`numeric_value` decimal(10,2)
,`updated_at` datetime(6)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vw_ultimas_lecturas`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vw_ultimas_lecturas` (
`device_code` varchar(50)
,`device_name` varchar(120)
,`sensor_code` varchar(40)
,`sensor_name` varchar(100)
,`reading_value` decimal(10,2)
,`reading_unit` varchar(20)
,`consumption_w` decimal(10,4)
,`recorded_at` datetime(6)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vw_estado_actual`
--
DROP TABLE IF EXISTS `vw_estado_actual`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_estado_actual`  AS SELECT `d`.`device_code` AS `device_code`, `d`.`device_name` AS `device_name`, `cs`.`state_code` AS `state_code`, `cs`.`state_value` AS `state_value`, `cs`.`numeric_value` AS `numeric_value`, `cs`.`updated_at` AS `updated_at` FROM (`current_state` `cs` join `devices` `d` on((`d`.`id` = `cs`.`device_id`))) ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vw_ultimas_lecturas`
--
DROP TABLE IF EXISTS `vw_ultimas_lecturas`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_ultimas_lecturas`  AS SELECT `d`.`device_code` AS `device_code`, `d`.`device_name` AS `device_name`, `st`.`code` AS `sensor_code`, `st`.`name` AS `sensor_name`, `r`.`reading_value` AS `reading_value`, `r`.`reading_unit` AS `reading_unit`, `r`.`consumption_w` AS `consumption_w`, `r`.`recorded_at` AS `recorded_at` FROM (((`readings` `r` join `devices` `d` on((`d`.`id` = `r`.`device_id`))) join `sensor_types` `st` on((`st`.`id` = `r`.`sensor_type_id`))) join (select `readings`.`device_id` AS `device_id`,max(`readings`.`recorded_at`) AS `max_recorded_at` from `readings` group by `readings`.`device_id`) `last_r` on(((`last_r`.`device_id` = `r`.`device_id`) and (`last_r`.`max_recorded_at` = `r`.`recorded_at`)))) ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `activity_log`
--
ALTER TABLE `activity_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_activity_log_user` (`user_id`),
  ADD KEY `idx_activity_log_logged_at` (`logged_at`),
  ADD KEY `idx_activity_log_action_logged_at` (`action`,`logged_at`);

--
-- Indices de la tabla `alert_thresholds`
--
ALTER TABLE `alert_thresholds`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_alert_thresholds_state_code` (`state_code`),
  ADD KEY `idx_alert_thresholds_active` (`is_active`);

--
-- Indices de la tabla `camera_events`
--
ALTER TABLE `camera_events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_camera_events_captured_at` (`captured_at`),
  ADD KEY `idx_camera_events_device_captured_at` (`device_id`,`captured_at`);

--
-- Indices de la tabla `chat_messages`
--
ALTER TABLE `chat_messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_chat_receiver` (`receiver_id`),
  ADD KEY `idx_chat_participants` (`sender_id`,`receiver_id`);

--
-- Indices de la tabla `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_comments_user` (`user_id`),
  ADD KEY `idx_comments_created_at` (`created_at`);

--
-- Indices de la tabla `current_state`
--
ALTER TABLE `current_state`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_current_state_device_state` (`device_id`,`state_code`),
  ADD KEY `idx_current_state_updated_at` (`updated_at`);

--
-- Indices de la tabla `devices`
--
ALTER TABLE `devices`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `device_code` (`device_code`),
  ADD KEY `fk_devices_sensor_type` (`sensor_type_id`);

--
-- Indices de la tabla `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_events_user` (`user_id`),
  ADD KEY `fk_events_device` (`device_id`),
  ADD KEY `idx_events_time` (`event_time`),
  ADD KEY `idx_events_type_time` (`event_type`,`event_time`);

--
-- Indices de la tabla `loyalty_coupons`
--
ALTER TABLE `loyalty_coupons`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `coupon_code` (`coupon_code`),
  ADD KEY `fk_loyalty_coupons_user` (`user_id`);

--
-- Indices de la tabla `loyalty_offers`
--
ALTER TABLE `loyalty_offers`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `loyalty_transactions`
--
ALTER TABLE `loyalty_transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_loyalty_transactions_user` (`user_id`);

--
-- Indices de la tabla `media_assets`
--
ALTER TABLE `media_assets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_media_device` (`device_id`),
  ADD KEY `fk_media_product` (`product_id`);

--
-- Indices de la tabla `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sku` (`sku`);

--
-- Indices de la tabla `readings`
--
ALTER TABLE `readings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_readings_recorded_at` (`recorded_at`),
  ADD KEY `idx_readings_device_recorded_at` (`device_id`,`recorded_at`),
  ADD KEY `idx_readings_sensor_recorded_at` (`sensor_type_id`,`recorded_at`);

--
-- Indices de la tabla `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reviews_user` (`user_id`);

--
-- Indices de la tabla `review_images`
--
ALTER TABLE `review_images`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_review_images_review` (`review_id`);

--
-- Indices de la tabla `review_responses`
--
ALTER TABLE `review_responses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_review_responses_review` (`review_id`),
  ADD KEY `fk_review_responses_user` (`user_id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indices de la tabla `sensor_types`
--
ALTER TABLE `sensor_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indices de la tabla `state_history`
--
ALTER TABLE `state_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_state_history_changed_at` (`changed_at`),
  ADD KEY `idx_state_history_device_changed_at` (`device_id`,`changed_at`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `fk_users_role` (`role_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `activity_log`
--
ALTER TABLE `activity_log`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=95;

--
-- AUTO_INCREMENT de la tabla `alert_thresholds`
--
ALTER TABLE `alert_thresholds`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `camera_events`
--
ALTER TABLE `camera_events`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `chat_messages`
--
ALTER TABLE `chat_messages`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `comments`
--
ALTER TABLE `comments`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `current_state`
--
ALTER TABLE `current_state`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2251;

--
-- AUTO_INCREMENT de la tabla `devices`
--
ALTER TABLE `devices`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `events`
--
ALTER TABLE `events`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `loyalty_coupons`
--
ALTER TABLE `loyalty_coupons`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `loyalty_offers`
--
ALTER TABLE `loyalty_offers`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `loyalty_transactions`
--
ALTER TABLE `loyalty_transactions`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `media_assets`
--
ALTER TABLE `media_assets`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `products`
--
ALTER TABLE `products`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `readings`
--
ALTER TABLE `readings`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2393;

--
-- AUTO_INCREMENT de la tabla `reviews`
--
ALTER TABLE `reviews`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `review_images`
--
ALTER TABLE `review_images`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `review_responses`
--
ALTER TABLE `review_responses`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `sensor_types`
--
ALTER TABLE `sensor_types`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `state_history`
--
ALTER TABLE `state_history`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `activity_log`
--
ALTER TABLE `activity_log`
  ADD CONSTRAINT `fk_activity_log_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `camera_events`
--
ALTER TABLE `camera_events`
  ADD CONSTRAINT `fk_camera_events_device` FOREIGN KEY (`device_id`) REFERENCES `devices` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Filtros para la tabla `chat_messages`
--
ALTER TABLE `chat_messages`
  ADD CONSTRAINT `fk_chat_receiver` FOREIGN KEY (`receiver_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_chat_sender` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `fk_comments_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `current_state`
--
ALTER TABLE `current_state`
  ADD CONSTRAINT `fk_current_state_device` FOREIGN KEY (`device_id`) REFERENCES `devices` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Filtros para la tabla `devices`
--
ALTER TABLE `devices`
  ADD CONSTRAINT `fk_devices_sensor_type` FOREIGN KEY (`sensor_type_id`) REFERENCES `sensor_types` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `fk_events_device` FOREIGN KEY (`device_id`) REFERENCES `devices` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_events_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `loyalty_coupons`
--
ALTER TABLE `loyalty_coupons`
  ADD CONSTRAINT `fk_loyalty_coupons_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `loyalty_transactions`
--
ALTER TABLE `loyalty_transactions`
  ADD CONSTRAINT `fk_loyalty_transactions_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `media_assets`
--
ALTER TABLE `media_assets`
  ADD CONSTRAINT `fk_media_device` FOREIGN KEY (`device_id`) REFERENCES `devices` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_media_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `readings`
--
ALTER TABLE `readings`
  ADD CONSTRAINT `fk_readings_device` FOREIGN KEY (`device_id`) REFERENCES `devices` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_readings_sensor_type` FOREIGN KEY (`sensor_type_id`) REFERENCES `sensor_types` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Filtros para la tabla `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `fk_reviews_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `review_images`
--
ALTER TABLE `review_images`
  ADD CONSTRAINT `fk_review_images_review` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `review_responses`
--
ALTER TABLE `review_responses`
  ADD CONSTRAINT `fk_review_responses_review` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_review_responses_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `state_history`
--
ALTER TABLE `state_history`
  ADD CONSTRAINT `fk_state_history_device` FOREIGN KEY (`device_id`) REFERENCES `devices` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
