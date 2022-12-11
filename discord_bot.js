/*
Le code ci-dessus est utilisé dans un programme de chat pour exécuter une commande "LONG". 
Cette commande permet à l'utilisateur d'ouvrir une position "LONG" sur une crypto-monnaie en spécifiant divers arguments 
tels que la monnaie, le stop-loss, le take-profit et le levier. 
Le code utilise également l'API Binance pour obtenir le prix actuel de la crypto-monnaie en question et l'affiche dans un message dans le chat. 
Enfin, les détails de la transaction sont enregistrés dans une base de données en utilisant l'objet "Calls".

Le code ci-dessus semble être une implémentation d'un événement pour un client Discord qui gère les messages reçus. Lorsqu'un message est reçu, 
le code vérifie si le message commence par "LONG". 
Si c'est le cas, il extrait les arguments du message et envoie un message d'embed dans le salon avec les informations sur le LONG, 
enregistre ces informations dans la base de données et envoie un message de confirmation.
*/
client.on('message', message => {
  // Si l'auteur du message est un bot, on arrête l'exécution de la fonction.
  //console.log([${message.author.tag}]: ${message.content});
  if (message.author.bot) return;

  // Si le message commence par "LONG", on exécute la suite du code.
  if (message.content.startsWith("LONG")) {
    // On extrait les arguments de la commande en divisant le message par les espaces.
    const [CMD_NAME, ...args] = message.content
        .trim()
        //.substring(PREFIX.length)
        .split(/\s+/);

    // On initialise un tableau pour stocker les informations de prix de la crypto-monnaie et une variable pour le prix actuel.
    var arrayPrice = [];
    var price = 0;

    // On utilise l'API Binance pour obtenir le prix actuel de la crypto-monnaie spécifiée dans les arguments.
    var url = 'https://api.binance.com/api/v3/ticker/price?symbol=' + args[0] + 'USDT';

    // On utilise une fonction asynchrone pour récupérer le prix de la crypto-monnaie.
    (async function _iife() {
      try {
        // On récupère les valeurs de l'objet retourné par l'API Binance et on les stocke dans le tableau "arrayPrice".
        arrayPrice = Object.values(await tiny.get({ url }));

        // On récupère le prix de la crypto-monnaie à partir des informations stockées dans le tableau "arrayPrice" et on le stocke dans la variable "price".
        price = arrayPrice[0]['price'];

        // On envoie un message dans le chat
