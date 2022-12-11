<?php
  session_start(); // démarre la session

  // récupère les variables de session 'code' et 'civ'
  $code = $_SESSION['code'];
  $civ = $_SESSION['civ'];
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
    <p>E-mail envoyé, regardez dans votre boîte mail</p>
    <hr>
    <p>Vérifiez les spams</p>

    <fieldset>
      <h2>Remplissez le code</h2>
      <form action="verif_code.php" method="post">
        <input type="number" name="code_remplis" id="code" min="100000" max="999999" placeholder="Code secret :">
        <input type="submit" value="Code">
      </form>
    </fieldset>

    <!--
      si le code est le bon, alors remplir les informations dans la base de données
    -->

</body>
</html>
