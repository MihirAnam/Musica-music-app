-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 03, 2024 at 07:05 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `musicapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

DROP TABLE IF EXISTS `adminlogin`;
CREATE TABLE IF NOT EXISTS `adminlogin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `reg_details`
--

DROP TABLE IF EXISTS `reg_details`;
CREATE TABLE IF NOT EXISTS `reg_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(30) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reg_details`
--

INSERT INTO `reg_details` (`id`, `username`, `email`, `password`, `date`) VALUES
(24, 'mayur', 'mayur@gmail.com', 'mayur1234', '2022-07-24 07:38:59'),
(25, 'kishor', 'kishor@gmail.com', 'kishor1234', '2022-07-24 07:40:02'),
(28, 'Kishor', 'kishoranam1234@gmail.com', 'kishor1234', '2024-01-30 14:59:09'),
(27, 'adesh', 'adesh@gmail.com', 'adesh1234', '2023-01-31 12:55:44'),
(23, 'manas', 'manas.sonatakke@gmail.com', 'manas1234', '2022-07-24 07:38:16'),
(26, 'Amol', 'amol@gmail.com', 'amol1234', '2022-07-27 06:06:39'),
(22, 'mihir', 'mihiranam1234@gmail.com', 'mihir1234', '2022-07-24 07:37:29');

-- --------------------------------------------------------

--
-- Table structure for table `watchlist`
--

DROP TABLE IF EXISTS `watchlist`;
CREATE TABLE IF NOT EXISTS `watchlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `song_name` text NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `watchlist`
--

INSERT INTO `watchlist` (`id`, `email`, `song_name`, `url`) VALUES
(28, 'amol@gmail.com', 'Badshah - Paani Paani | Jacqueline Fernandez | Official Music Video| Aastha Gill | Trending Songs', 'https://www.youtube.com/watch?v=nFjVlf2r9_Q'),
(23, 'mihiranam1234@gmail.com', 'Hawayein Lyric Video - Jab Harry Met Sejal|Shah Rukh Khan, Anushka|Arijit Singh|Pritam', 'https://www.youtube.com/watch?v=cYOB941gyXI'),
(22, 'mihiranam1234@gmail.com', 'Coke Studio | Season 14 | Pasoori | Ali Sethi x Shae Gill', 'https://www.youtube.com/watch?v=5Eqb_-j3FDA'),
(25, 'mihiranam1234@gmail.com', 'kesariya tera ishq hai piya (4k Official Video) | arijit singh new song | kesariya full song', 'https://www.youtube.com/watch?v=NlRoQpd9ZLk'),
(26, 'mihiranam1234@gmail.com', 'one direction ~ Baby, you light up my world like nobody else (lyrics) /\"what makes you beautiful \"', 'https://www.youtube.com/watch?v=H-4T0RLI7AY'),
(27, 'amol@gmail.com', 'Laree Choote  by Call | Lyrical Video', 'https://www.youtube.com/watch?v=cXPmrNwfSMg');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
