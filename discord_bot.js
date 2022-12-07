client.on('message', message => {
            //if (message.author.bot) return;
            //console.log([${message.author.tag}]: ${message.content});
            /////////////////////////////////////////////////////////////////////////
            /////////////////////////////////////////////////////////////////////////
            /////////////////////////   LONG COMMAND   //////////////////////////////
            /////////////////////////////////////////////////////////////////////////
            /////////////////////////////////////////////////////////////////////////
            if (message.content.startsWith("LONG")) {
                const [CMD_NAME, ...args] = message.content
                    .trim()
                    //.substring(PREFIX.length)
                    .split(/\s+/);
                //console.log(args);
                //console.log(message.author.id + ' // ' + message.author.username);
                var arrayPrice = [];
                var price = 0;
                var url = 'https://api.binance.com/api/v3/ticker/price?symbol=' + args[0] + 'USDT';
                (async function _iife() {
                    try {
                        arrayPrice = Object.values(await tiny.get({ url }));
                        //console.log(arrayPrice[0]['price']);
                        price = arrayPrice[0]['price'];

                        message.channel.send({
                            embed: {
                                color: 3447003,
                                author: {
                                    name: message.author.username,
                                    icon_url: message.author.displayAvatarURL()
                                },
                                description: message.author.username + " a ouvert un LONG " + args[0],
                                fields: [
                                    { name: "Entry", value: price + "$", inline: false },
                                    { name: "SL", value: args[4] + "$", inline: true },
                                    { name: "TP", value: args[6] + "$", inline: true },
                                    { name: "Leverage", value: args[7], inline: true }
                                ],
                            }
                        });
                        const calls = new Calls({
                            username: message.author.username,
                            userID: message.author.id,
                            callType: 'LONG',
                            coin: args[0],
                            valueEntry: price,
                            entryTime: message.createdAt,
                            tp: args[6],
                            sl: args[4],
                            closeTime: '',
                            valueClose: ''
                        });
                        calls.save()
                            .then(result => console.log(result))
                            .catch(err => console.log(err));
                    } catch (err) {
                        console.log('ruh roh!', err)
                    }
                })();
            }