<?php 
session_start();
include 'connect_bdd.php';

?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>inscription</title>
</head>
<body>
<h1>Formulaire d'inscription</h1>



<!--

Objectif créer une session TMP dans 
le but de conserver les infomations avant 
leur transfert dans la base de données

-->
<form action="register.php" method="post">
    <fieldset> 
  <div id="div_name">
    <label for="name">Nom :</label><input type="text" id="name" name="user_name" required/>
  
  </div><div id="div_prenom">
    <label for="prenom">Prenom :</label><input type="text" id="prenom" name="user_prenom" required/>

  </div><div id="div_email">
    <label>Email :</label><input type="email" id="email" name="email" required><br>

  </div><div id="div_civilité">
<label>Civilité :</label><select name="civ" required><option>Homme</option><option>Femme</option></select></div>
   
  <div id="div_password">
   <label for="pass">Mot de passe :</label>
   <input type="password" id="pass" name="password" placeholder="password" required><br>
  
  <label for="pass">confimation :</label>
  
  <input type="password" id="pass" name="passwordV" placeholder="password confirm" required></div> 
   <input type="submit" value="enter"></fieldset></form>
<?php
if(ISSET($_POST['password'])){
  //création du code secret:
  $min = 100000;
  $max = 999999;
  $code =rand($min,$max);
  //echo $code;
  $_SESSION['name']= $_POST['user_name'];
  $_SESSION['prenom']= $_POST['user_prenom'];
  $_SESSION['email']= $_POST['email'];
  $_SESSION['civ']=$_POST['civ'];
  $_SESSION['pass']=$_POST['password'];
  $_SESSION['code']=$code;
//envoie du code secret par mail
$headers="MIME-version: 1.0 \r\n";
$headers.="Content-type: text/html; charset='UTF-8' \r\n";
$headers.="From: hugo.delacour@univ-rouen.fr";
//vérification du mdp
if($_POST['password']==$_POST['passwordV']){
if( mail("hugo.delacour@univ-rouen.fr","reception code secret","voici ton code $code !",$headers)){
    echo "Mail bien envoyé !";
    header('Location: email_check.php');
}
else {
echo "<h1>mail non envoyé !</h1>";
}}}else{
  echo 'Veillez remplir les informations - Mot de Passe non valide';
}
?>
</body>
</html>