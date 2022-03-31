-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 25 Mar 2022, 10:24
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `strava2gl`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `statistics`
--

CREATE TABLE `statistics` (
  `id` int(2) NOT NULL,
  `lastname` varchar(35) DEFAULT NULL,
  `birth` date DEFAULT NULL,
  `miles` float(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `statistics`
--

INSERT INTO `statistics` (`id`, `lastname`, `birth`, `miles`) VALUES
(1, 'Kacperczyk', '1987-05-23', 123.23),
(2, 'Kowalski', '1992-08-12', 87.69),
(3, 'Podolski', '1998-11-07', 54.30),
(4, 'Kapala', '1989-02-18', 101.82),
(5, 'Zawolski', '1982-05-20', 68.43);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `statistics`
--
ALTER TABLE `statistics`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `statistics`
--
ALTER TABLE `statistics`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
