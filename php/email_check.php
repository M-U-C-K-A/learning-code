

<?php
session_start();

$code=$_SESSION['code'];
$civ=$_SESSION['civ'];
echo "<!-- si l'email ne fonctionne pas, voici le code $code-->";
echo "<!-- normalement aucun problème -->";
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
    <p>E-mail envoyé, regarder dans votre boite mail</p>
    <hr>
    <p>vérifier les spams</p>

    <fieldset>
    <h2>remplissez le code</h2>
    <form action="verif_code.php" method="post">
    <input type="number" name="code_remplis" id="code" min="100000" max="999999" placeholder="Code secret :">
    <input type="submit" value="code">
  </form>
    </fieldset>

<!--
    si le code est le bon alors remplir les informations dans la BDD
-->

</body>
</html>