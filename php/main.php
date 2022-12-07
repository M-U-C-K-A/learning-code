<?php
//ajout de la Base De Donnée
include 'connect_bdd.php';
include 'deja_connecte.php';
//ajout de la table event + des differentes données
$bddevent = $bdd->prepare("SELECT * FROM sae203_event");
$bddevent->execute();
$bddevnt = $bddevent->fetchall();
//attribution des variables
foreach($bddevnt as $bd){
    $Id_event = $bd['Id_event'];
    $date = $bd['Date'];
    $time = $bd['Time'];
    $session = $bd['Session'];
}


/*
Nombres de places restante pour la séance du matin.
nombres de places total+restante
nombres de places total -> 50
*/
$bdd_matin = $bdd->prepare("SELECT NbPlaceTot,NbPlaceReste FROM sae203_event WHERE Session='matin' ");
$bdd_matin->execute();
$bdmat = $bdd_matin->fetchall();
foreach($bdmat as $bd){
    $nbPlace_tot_matin = $bd['NbPlaceTot'];
    $nbPlace_reste_matin = $bd['NbPlaceReste'];
}

/*
Nombres de places restante pour la séance de l'après midi.
nombres de places total+restante
après midi -> 'aprem'
nombres de places total -> 50
*/
$bdd_aprem = $bdd->prepare("SELECT NbPlaceTot,NbPlaceReste FROM sae203_event WHERE Session='aprem' ");
$bdd_aprem->execute();
$bdmat = $bdd_aprem->fetchall();
foreach($bdmat as $bd){
    $nbPlace_tot_aprem = $bd['NbPlaceTot'];
    $nbPlace_reste_aprem = $bd['NbPlaceReste'];
}

/*
Nombres de places restante pour la séance du soir.
nombres de places total+restante
nombres de places total -> 50
*/
$bdd_soir = $bdd->prepare("SELECT NbPlaceTot,NbPlaceReste FROM sae203_event WHERE Session='soir' ");
$bdd_soir->execute();
$bdmat = $bdd_soir->fetchall();
foreach($bdmat as $bd){
    $nbPlace_tot_soir = $bd['NbPlaceTot'];
    $nbPlace_reste_soir = $bd['NbPlaceReste'];
}

/*
Nombres de places restante pour la séance de la nuit.
nombres de places total+restante
nombres de places total -> 200
*/
$bdd_nuit = $bdd->prepare("SELECT NbPlaceTot,NbPlaceReste FROM sae203_event WHERE Session='nuit' ");
$bdd_nuit->execute();
$bdmat = $bdd_nuit->fetchall();
foreach($bdmat as $bd){
    $nbPlace_tot_nuit = $bd['NbPlaceTot'];
    $nbPlace_reste_nuit = $bd['NbPlaceReste'];
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

<h1>Nombres de places disponible</h1>
    <h2>jour :</h2>
    <h3>matin :</h3><p><?php 
    echo $nbPlace_reste_matin,"/",$nbPlace_tot_matin;
    ?></p>
    <h3>apres midi :</h3><p><?php 
    echo $nbPlace_reste_aprem,"/",$nbPlace_tot_aprem;
    ?></p>
    <h3>soir :</h3><p><?php 
    echo $nbPlace_reste_soir,"/",$nbPlace_tot_soir;
    ?></p>  

    
      
    <h2>nuit :</h2><p><?php 
    echo $nbPlace_reste_nuit,"/",$nbPlace_tot_nuit;
    ?></p><fieldset style="text-align:center; font-size:2rem;">
    
    <blockquote>Connexion : <a href="connect.php">Connexion</a></blockquote>

    <blockquote>réservation : <a href="reservation.php">reservation</a></blockquote>
    </fieldset>

</fieldset>
</body>
</html>