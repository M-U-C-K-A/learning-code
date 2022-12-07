<?php 
session_start();
/*
création de la session
------------------------------------------------
si la session n'existe pas :
-créer une session et mettre le compteur a zero

si la session existe + personne non log :
-garder la session et mettre le compteur a zero

si la session existe déjà + personne log :
-garder la valeur connecte a 1


*/
echo "<!--Session ✔️";
if (empty($_SESSION['connecte'])){
    $connecte = 0;
    $_SESSION['connecte']=$connecte;
    echo "-->";
    echo " 1";
}else if($_SESSION['connecte']==0) {
    $connecte = 0;
    $_SESSION['connecte']=$connecte;
    echo " + la personne n'est pas connecte-->";
    echo " 2";
}else {
    $connecte =1;
    $_SESSION['connecte']=$connecte;
    echo " + la personne est connecte-->";
    echo " 3";
}
?>