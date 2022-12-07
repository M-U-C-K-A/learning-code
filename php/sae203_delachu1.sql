-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 10 juin 2022 à 20:19
-- Version du serveur :  10.4.17-MariaDB
-- Version de PHP : 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sae203_delachu1`
--

-- --------------------------------------------------------

--
-- Structure de la table `sae203_event`
--

CREATE TABLE `sae203_event` (
  `Id_event` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Session` varchar(50) NOT NULL,
  `NbPlaceTot` int(11) NOT NULL,
  `NbPlaceReste` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `sae203_event`
--

INSERT INTO `sae203_event` (`Id_event`, `Date`, `Time`, `Session`, `NbPlaceTot`, `NbPlaceReste`) VALUES
(1, '2022-06-30', '09:00:00', 'matin', 50, 50),
(2, '2022-06-30', '13:00:00', 'aprem', 50, 50),
(3, '2022-06-30', '16:00:00', 'soir', 50, 50),
(4, '2022-06-30', '19:00:00', 'nuit', 200, 200);

-- --------------------------------------------------------

--
-- Structure de la table `sae203_reservation`
--

CREATE TABLE `sae203_reservation` (
  `Id` int(11) NOT NULL,
  `Id_event` int(11) NOT NULL,
  `Id_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `sae203_user`
--

CREATE TABLE `sae203_user` (
  `Id_user` int(11) NOT NULL,
  `Civ` varchar(50) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Prenom` varchar(50) NOT NULL,
  `Mdp` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `sae203_event`
--
ALTER TABLE `sae203_event`
  ADD PRIMARY KEY (`Id_event`),
  ADD UNIQUE KEY `Id_event` (`Id_event`);

--
-- Index pour la table `sae203_reservation`
--
ALTER TABLE `sae203_reservation`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `sae203_reservation_Id_user` (`Id_user`),
  ADD KEY `Id_event` (`Id_event`);

--
-- Index pour la table `sae203_user`
--
ALTER TABLE `sae203_user`
  ADD PRIMARY KEY (`Id_user`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `sae203_event`
--
ALTER TABLE `sae203_event`
  MODIFY `Id_event` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `sae203_reservation`
--
ALTER TABLE `sae203_reservation`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `sae203_user`
--
ALTER TABLE `sae203_user`
  MODIFY `Id_user` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `sae203_reservation`
--
ALTER TABLE `sae203_reservation`
  ADD CONSTRAINT `sae203_reservation_Id_user` FOREIGN KEY (`Id_user`) REFERENCES `sae203_user` (`Id_user`),
  ADD CONSTRAINT `sae203_reservation_ibfk_1` FOREIGN KEY (`Id_event`) REFERENCES `sae203_event` (`Id_event`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
