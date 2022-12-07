<?php
// Vérification de la validité de l'email et du mot de passe
if (email_valide($_POST['email']) && mdp_valide($_POST['mdp'])) {
  // Si l'email et le mot de passe sont valides, on redirige vers main.php
  header('Location: main.php');
  // On met la valeur de la variable $connecte à 1
  $connecte = 1;
} else {
  // Si l'email ou le mot de passe sont non valides, on redirige vers connect.php
  header('Location: connect.php');
}
//Note : ceci n'est qu'un exemple de code, et il est possible qu'il contienne des erreurs ou des omissions. 
//Il est important de toujours vérifier le code avant de l'utiliser.
// voici par exemple une autre possibilité
?>
<?php
// vérification des données d'identification
$email = $_POST['email'];
$mdp = $_POST['mdp'];
// vérification de la validité de l'email et du mot de passe
if (validEmail($email) && validMdp($mdp)) {
  // l'email et le mot de passe sont valides
  // on redirige l'utilisateur vers la page principale
  header('Location: main.php');
  // on met la valeur "$connecte" à 1
  $connecte = 1;
} else {
  // l'email ou le mot de passe n'est pas valide
  // on redirige l'utilisateur vers la page de connexion
  header('Location: connect.php');
}

?>
