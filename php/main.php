<?php
  // inclut les fichiers de connection à la base de données et de vérification de la connexion
  require_once 'connect_bdd.php';
  require_once 'deja_connecte.php';

  // récupère toutes les entrées de la table 'sae203_event'
  $bddevent = $bdd->prepare("SELECT * FROM sae203_event");
  $bddevent->execute();
  $bddevnt = $bddevent->fetchall();

  // initialise les variables pour les différentes sessions
  $nbPlace_tot_matin = 0;
  $nbPlace_reste_matin = 0;
  $nbPlace_tot_aprem = 0;
  $nbPlace_reste_aprem = 0;
  $nbPlace_tot_soir = 0;
  $nbPlace_reste_soir = 0;
  $nbPlace_tot_nuit = 0;
  $nbPlace_reste_nuit = 0;

  // parcourt les entrées de la table et met à jour les variables pour chaque session
  foreach ($bddevnt as $bd) {
    $session = $bd['Session'];
    switch ($session) {
      case 'matin':
        $nbPlace_tot_matin = $bd['NbPlaceTot'];
        $nbPlace_reste_matin = $bd['NbPlaceReste'];
        break;
      case 'aprem':
        $nbPlace_tot_aprem = $bd['NbPlaceTot'];
        $nbPlace_reste_aprem = $bd['NbPlaceReste'];
        break;
      case 'soir':
        $nbPlace_tot_soir = $bd['NbPlaceTot'];
        $nbPlace_reste_soir = $bd['NbPlaceReste'];
        break;
      case 'nuit':
        $nbPlace_tot_nuit = $bd['NbPlaceTot'];
        $nbPlace_reste_nuit = $bd['NbPlaceReste'];
        break;
    }
  }
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Page principale</title>
</head>
<body>
<fieldset>

<h1>Nombres de places disponibles</h1>
    <h2>Jour :</h2>
    <h3>Matin :</h3><p><?php 
    echo $nbPlace_reste_matin,"/",$nbPlace_tot_matin;
    ?></p>

    <h3>Après-midi :</h3><p><?php 
    echo $nbPlace_reste_aprem,"/",$nbPlace_tot_aprem;
    ?></p>

    <h3>Soir :</h3><p><?php 
    echo $nbPlace_reste_soir,"/",$nbPlace_tot_soir;
    ?></p>

    <h3>Nuit :</h3><p><?php 
    echo $nbPlace_reste_nuit,"/",$nbPlace_tot_nuit;
    ?></p>

</fieldset>

</body>
</html>
