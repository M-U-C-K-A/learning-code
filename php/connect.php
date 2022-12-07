<?php
include 'connect_bdd.php';
include 'deja_connecte.php';
$connect =$_SESSION['connect'];
if($connect==1){
  header('Location: reservation.php');
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
<h1>Formulaire de connexion</h1>
<form action="connect.php" method="post">
    <fieldset> 
  <div id="div_email">
        <label>Email :</label>
        <input type="email" id="email" name="email" required><br>
  </div>
  
  <div id="div_password">
  <label for="pass">Mot de passe :</label>
    <input type="password" id="pass" name="password" required>
  </div>

  <div id="connect/register">
  <input type="submit" value="enter">
  <blockquote>pas de compte ? <a href="register.php">inscription</a> </blockquote> </div>
    </fieldset>
</form>


<?php 
if(empty($_POST)){
  $email_test = 0;
  $password_test = 0;
}else{
  $email_test = $_POST['email'];
  $password_test =  $_POST['password'];
  $password_test = SHA1($password_test);
}
echo '<br>';

  try
  {   
      $reponse = $bdd->query("SELECT * FROM sae203_user WHERE Email='".$email_test."' AND Mdp='".$password_test."'");
      while($donnees=$reponse->fetch()){
      if ($donnees['Email']==$email_test && $donnees['Mdp']==$password_test) {
      $_SESSION['name']= $donnees['Nom'];
      $_SESSION['prenom']= $donnees['Prenom'];
      $_SESSION['email']= $donnees['Email'];
      $_SESSION['civ']=$donnees['Civ'];
      $_SESSION['pass']=$password_test;
      $_SESSION['Id']=$donnees['Id_user'];
      $_SESSION['connect']=1;
      header('Location: reservation.php');
      }
       
      else
      {
      echo 'informations non correctes';
      }
      }
       
  }
  catch(Exception $e)
  {
      die('Erreur : '.$e->getMessage());
  }
/*
remplir Email
remplir MDP
appui du bouton submit
'sinon lien vers l'inscription'

si non valide :
-renvoi sur la même page
-message annonce "échec de la connexion"

si la personne a un compte :
- vérification de l'Email
-> si l'Email est valide :
- vérification du MDP
- (son empreinte)
- renvoie sur la page reservation

*/
?>
</body>
</html>