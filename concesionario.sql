-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-03-2024 a las 20:26:31
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `concesionario`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `activarmarca` (IN `idmarca` INT)   BEGIN
UPDATE marcas set estado = 1 WHERE id = idmarca;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `activarproveedor` (IN `idproveedor` INT)   BEGIN
UPDATE proveedor set estado = 1 WHERE id = idproveedor;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `activarvehiculo` (IN `idvehiculo` INT)   BEGIN
UPDATE vehiculos set estado = 1 WHERE id = idvehiculo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizarvehiculo` (IN `idvehiculo` INT, IN `nombre` VARCHAR(100), IN `color` VARCHAR(50), IN `modelo` VARCHAR(50), IN `capacidad` INT, IN `cilindraje` INT, IN `capacidad_de_vehiculo` INT, IN `precio` INT, IN `foto` VARCHAR(250), IN `proveedor_id` INT, IN `marcas_id` INT)   BEGIN
INSERT INTO vehiculos (nombre, color, modelo, capacidad, cilindraje, cantidad_de_vehiculos, precio, foto, proveedor_id, marcas_id, estado) VALUES (nombre, color, modelo, capacidad, cilindraje, cantidad_de_vehiculos, precio, foto, proveedor_id, marcas_id, 1);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `inactivarmarca` (IN `idmarca` INT)   BEGIN
UPDATE marcas set estado = 0 WHERE id = idmarca;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `inactivarproveedor` (IN `idproveedor` INT)   BEGIN
UPDATE proveedor set estado = 0 WHERE id = idproveedor;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `inactivarvehiculo` (IN `idvehiculo` INT)   BEGIN
UPDATE vehiculos set estado = 0 WHERE id = idvehiculo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarvehiculo` (IN `nombre` VARCHAR(100), IN `color` VARCHAR(50), IN `modelo` VARCHAR(50), IN `capacidad` INT, IN `cilindraje` INT, IN `cantidad_de_vehiculos` INT, IN `precio` INT, IN `foto` VARCHAR(250), IN `proveedor_id` INT, IN `marcas_id` INT, IN `estado` INT)   BEGIN 
INSERT INTO vehiculos (nombre, color, modelo, capacidad, cilindraje, cantidad_de_vehiculos, precio, foto, proveedor_id, marcas_id, estado) VALUES (nombre, color, modelo, capacidad, cilindraje, cantidad_de_vehiculos, precio, foto, proveedor_id, marcas_id, 1);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marcas`
--

CREATE TABLE `marcas` (
  `id` int(11) NOT NULL,
  `nombre_marca` varchar(100) NOT NULL,
  `pais_origen` varchar(100) NOT NULL,
  `fecha_fundacion` date NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `marcas`
--

INSERT INTO `marcas` (`id`, `nombre_marca`, `pais_origen`, `fecha_fundacion`, `descripcion`, `estado`) VALUES
(10, 'Toyota', 'Japon', '2024-03-01', 'Toyota Yokomotor', 1),
(11, 'Ford', 'Estados Unidos', '2024-03-14', 'Ford ', 0),
(12, 'Chevrolet', 'Estados Unidos', '2024-03-20', 'Chevrolet-Camaro', 1),
(13, 'koenigsegg', 'Suecia', '2023-08-10', 'Christian von Koenigsegg', 0),
(14, 'Dodge', 'Estados Unidos', '2024-03-27', 'dodge', 0),
(15, 'jeep', 'Estados Unidos', '2023-10-12', 'jeep', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `cedula` int(20) NOT NULL,
  `celular` int(20) NOT NULL,
  `pais` varchar(100) NOT NULL,
  `estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`id`, `nombre`, `cedula`, `celular`, `pais`, `estado`) VALUES
(1, 'Alejandro', 1025885963, 2147483647, 'Colombia', 1),
(2, 'Cristian Cardona', 102030, 3020100, 'Brasil', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `color` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `capacidad` int(11) NOT NULL,
  `cilindraje` int(11) NOT NULL,
  `cantidad_de_vehiculos` int(11) NOT NULL,
  `precio` int(11) NOT NULL,
  `foto` varchar(250) NOT NULL,
  `proveedor_id` int(11) NOT NULL,
  `marcas_id` int(11) NOT NULL,
  `estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`id`, `nombre`, `color`, `modelo`, `capacidad`, `cilindraje`, `cantidad_de_vehiculos`, `precio`, `foto`, `proveedor_id`, `marcas_id`, `estado`) VALUES
(2, '4Runner', 'negro', '2023', 7, 4000, 100, 12, 'FB_IMG_1711232621912.jpg', 1, 10, 0),
(3, '4Runner', 'Gris', '2018', 7, 4000, 10, 12, 'FB_IMG_1711232621912.jpg', 2, 10, 1),
(4, 'Hilux', 'Gris', '2003', 5, 2400, 5, 800000, 'FB_IMG_1711501692491.jpg', 1, 10, 1),
(7, 'Fortuner', 'Amarillo', '2018', 5, 1, 1, 1, 'FB_IMG_1711501692491.jpg', 2, 12, 1),
(8, 'a', 'Gris', 'a', 5, 5, 5, 5, 'FB_IMG_1711501682658.jpg', 2, 12, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `marcas`
--
ALTER TABLE `marcas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `proveedor_id` (`proveedor_id`),
  ADD KEY `marca_id` (`marcas_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `marcas`
--
ALTER TABLE `marcas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `vehiculos_ibfk_1` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`),
  ADD CONSTRAINT `vehiculos_ibfk_2` FOREIGN KEY (`marcas_id`) REFERENCES `marcas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
