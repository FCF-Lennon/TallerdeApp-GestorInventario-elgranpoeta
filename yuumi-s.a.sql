-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-01-2022 a las 19:43:59
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `yuumi_s.a.`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `categoriaID` int(11) NOT NULL,
  `nombre` varchar(254) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`categoriaID`, `nombre`) VALUES
(1, 'Shonen'),
(2, 'Seinen'),
(3, 'Kodomo'),
(4, 'Ecchi'),
(5, 'Shojo'),
(6, 'Josei'),
(7, 'Mecha'),
(8, 'Deportes'),
(9, 'Gore'),
(10, 'Fantasía'),
(11, 'Guerra'),
(12, 'Horror'),
(13, 'Lucha'),
(14, 'Magia'),
(15, 'Misterio'),
(16, 'Post Apocalíptico '),
(17, 'Samurai'),
(18, 'Shooter'),
(19, 'Shounen'),
(20, 'Shoujo'),
(21, 'Kemono');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `codigo` int(11) NOT NULL,
  `categoriaID` int(11) NOT NULL,
  `nombre` varchar(254) COLLATE utf8_spanish_ci DEFAULT NULL,
  `autor` varchar(254) COLLATE utf8_spanish_ci DEFAULT NULL,
  `stock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `libro`
--

INSERT INTO `libro` (`codigo`, `categoriaID`, `nombre`, `autor`, `stock`) VALUES
(1, 1, 'Antagonista', 'Saikomic', 10),
(2, 1, 'One Piece', 'Echiro Oda', 20),
(23, 2, 'Tokyo Ghoul', 'Sui Ishida', 30),
(24, 2, 'Death Note', 'Tsugumi Oba', 40),
(25, 3, 'Doraemon', 'Fujiko Fujio', 50),
(26, 3, 'Hamtaro', 'Ritsuko Kawai', 60),
(43, 2, 'Berserk', 'Kentaro Miura', 60),
(44, 7, 'Neon Genesis Evangelion', 'Yoshiyuki Sadamoto', 11),
(45, 1, 'Dragon Ball', 'Akira Toriyama', 12),
(46, 1, 'Naruto', 'Masashi Kishimoto', 22),
(47, 10, 'Fullmetal Alchemist', 'Hiromu Arakawa', 44),
(48, 1, 'Shingeki no Kyojin', 'Hajime Isayama', 66),
(50, 10, 'Los Caballeros del Zodiaco', 'Bau', 34),
(51, 21, 'Beastars', 'Paru Itagaki', 43),
(52, 1, 'One Punch-Man', 'One', 54),
(53, 9, 'Dororo', 'Yasuko Kobayashi', 34),
(54, 13, 'Fire Force', 'Atsushi Ōkubo', 68),
(55, 9, 'Devilman Crybaby ', ' Ichirō Ōkouchi', 56),
(56, 9, 'Akame ga Kill', 'Takahiro', 45),
(57, 10, 'Bleach', 'Tite Kubo', 65),
(58, 5, 'Kill la Kill', 'Kazuki Nakashima', 78),
(59, 15, 'The Promised Neverland', 'Kaiu Shirai', 89),
(60, 1, 'Nanatsu no Taizai ', 'Nakaba Suzuki', 98),
(61, 4, 'Shokugeki no Soma', 'Yūto Tsukuda', 67),
(62, 13, 'Kengan Ashura', 'Yabako Sandrovich', 49),
(63, 13, 'Baki', 'Keisuke Itagaki', 71),
(64, 1, 'Jujutsu Kaisen', 'Gege Akutami', 100),
(65, 10, 'Hunter × Hunter', 'Yoshihiro Togashi', 101),
(66, 9, 'Tokyo Ghoul', 'Sui ishida', 34),
(67, 13, 'Tokyo Revengers', 'Ken Wakui', 67),
(68, 16, 'Chainsaw Man', 'Tatsuki Fujimoto', 58),
(69, 10, 'Dorohedoro', 'Q Hayashida', 83),
(70, 8, 'Blue Lock', 'Muneyuki Kaneshiro', 74),
(71, 10, 'Black Clover ', 'Yūki Tabata', 39);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `nombre` varchar(254) COLLATE utf8_spanish_ci DEFAULT NULL,
  `correo` varchar(254) COLLATE utf8_spanish_ci DEFAULT NULL,
  `password` varchar(254) COLLATE utf8_spanish_ci DEFAULT NULL,
  `rut` varchar(254) COLLATE utf8_spanish_ci NOT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`nombre`, `correo`, `password`, `rut`, `estado`, `admin`) VALUES
('Ruben', 'RubenValencia@inacapmail.cl', '1111', '17239883-5', 1, 1),
('Felipe', 'FelipeCarrasco@inacapmail.cl', '1234', '17283634-k', 1, 0),
('Cristobal', 'CristobalCortes@inacapmail.cl', '1234', '19293984-9', 0, 0),
('Sebastian', 'SebastianRamirez@inacapmail.cl', '1111', '20133789-5', 1, 1),
('Maria Fernanda', 'MariaFernandaDiaz@inacapmail.cl', '1234', '20347383-1', 1, 0),
('Diego', 'DiegoEsquivel@inacapmail.cl', '1111', '20654838-6', 1, 1),
('Amit', 'AmitMartinez@inacapmail.cl', '1111', '21288571-1', 1, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`categoriaID`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `FK_association1` (`categoriaID`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`rut`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `categoriaID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `libro`
--
ALTER TABLE `libro`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `libro`
--
ALTER TABLE `libro`
  ADD CONSTRAINT `FK_association1` FOREIGN KEY (`categoriaID`) REFERENCES `categoria` (`categoriaID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
