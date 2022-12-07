<?php
echo $_SESSION['connecte'];
/*
création de la session
------------------------------------------------
si la session n'existe pas :
-créer une session et mettre le compteur a zero

si la session existe + personne non log :
-garder la session et mettre le compteur a zero

si la session existe déjà + personne log :
-garder la valeur connecte a 1

Ce code permet de vérifier si l'utilisateur est connecté ou non à une session. Si l'utilisateur n'est pas connecté, 
la variable $_SESSION['connecte'] est initialisée à 0. Si l'utilisateur est déjà connecté, 
la variable $_SESSION['connecte'] est mise à jour avec la valeur 1. 
Des messages sont ensuite affichés pour indiquer dans quel cas l'utilisateur se trouve (cas 0 pour non connecté, cas 1 pour déjà connecté).
*/
echo "<!--Session ✔️";
if (empty($_SESSION['connecte'])){
    $connecte = 0;
    $_SESSION['connecte']=$connecte;
    echo "-->";
    echo " cas numero 0";
}else if($_SESSION['connecte']==0) {
    $connecte = 0;
    $_SESSION['connecte']=$connecte;
    echo " + la personne n'est pas connecte-->";
    echo " cas numero 1";
}else {
    $connecte =1;
    $_SESSION['connecte']=$connecte;
    echo " + la personne est connecte-->";
    echo " cas numero 2";
}
?>