<?php
  session_start(); // démarre la session

  // vérifie si l'utilisateur est connecté
  if (isset($_SESSION['name']) && isset($_SESSION['prenom'])) {
    // affiche un message de bienvenue à l'utilisateur
    echo "<br> Bonjour ",$_SESSION['prenom']," ",$_SESSION['name'],".";
  } else {
    // affiche un message indiquant que l'utilisateur n'est pas connecté
    echo "<br> Bonjour, vous n'êtes pas connecté.";
    // définit le token d'authentification à 0
    $_SESSION['connect'] = 0;
  }
?>
