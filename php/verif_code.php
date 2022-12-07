<?php
session_start();
include 'connect_bdd.php';


$user_name= $_SESSION['name'];
$user_prenom=$_SESSION['prenom'];
$email=$_SESSION['email'];
$civ=$_SESSION['civ'];
$password=$_SESSION['pass'];
$code=$_SESSION['code'];
$vcode=$_POST['code_remplis'];
$print = SHA1($password);
if ($civ=='Homme'){
    $civ=1;

}else{
    $civ=0;
}
if($code==$vcode){
    $sqlInsertQuery = "INSERT INTO sae203_user(Civ, Nom, Prenom, Mdp, Email)
    VALUES (:civilite, :nom, :prenom, :lemdp, :email)";
    $insererUser = $bdd->prepare($sqlInsertQuery);
    
    $insererUser->execute(array(
    'civilite'=>$civ,
    'nom'=>$user_name,
    'prenom'=>$user_prenom,
    'lemdp'=>$print,
    'email'=>$email)
    );
  
  //token d'authentification a 1
  $connect = 1;
  $_SESSION['connect']=$connect;
  $_SESSION['id']=$donnees['Id_user'];

  header('Location: main.php');
}
$bdd->close();
?>