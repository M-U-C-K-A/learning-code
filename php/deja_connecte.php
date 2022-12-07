<?php 
/*
verification de la session, atribut connecte 
si atribut a 0:
-ne rien faire
si atribut a 1:
afficher "vous etes connecter" + Bonjour + $Civ

*/

session_start();
if(isset($_SESSION['name'])){
    $user_name= $_SESSION['name'];
    $user_prenom=$_SESSION['prenom'];
    echo "<br> Bonjour ",$user_prenom," ",$user_name,".";
}else {
    echo "<br> bonjour vous n'êtes pas connecté";
    //token d'authentification a 1
    $connect = 0;
    $_SESSION['connect']=$connect;

}



?>