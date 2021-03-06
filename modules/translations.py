BULLET = u'\u2022'

maintenance_text = {
    'en': 'The tip bot is in maintenance.  Check @NanoTipBot on Twitter for more information.',
    'es': 'El tip bot está en mantenimiento. Revisa @NanoTipBot en Twitter para más información.',
    'nl': 'De Tip Bot is momenteel in onderhoud. Check @NanoTipBot op Twitter voor meer informatie.',
    'ja': '',
    'zh-t': '小費助手正在維修中。請觀看@NanoTipBot來獲得更多信息。',
    'zh-s': '小费助手正在维修中。请访问推特网上的@NanoTipBot来获得更多信息。',
    'fr': 'Le tip bot est en maintenance. Veuillez suivre @NanoTipBot sur Twitter pour plus d\'informations.',
    'pt': 'O tip bot encontra-se em manutenção. @NanoTipBot no Twitter para mais informações.',
    'th': '',
    'de': '',
    'id': 'Bot tip dalam pemeliharaan. Periksa @NanoTipBot di Twitter untuk informasi lebih lanjut.',
    'vt': '',
    'ru': 'Тип бот находится на обслуживании. Проверьте @NanoTipBot в Twitter для получения дополнительной '
          'информации.',
    'sv': '',
    'it': 'Il tip bot è in manutenzione. Controlla @NanoTipBot su Twitter per ulteriori informazioni.'
}
redirect_tip_text = {
    'en': 'Tips are processed through public messages now.  Please send in the format @NanoTipBot !tip 1 @user1.',
    'es': 'Los tips ahora están siendo procesados a través de mensajes públicos. Por favor, envíalos con el formato '
          '@NanoTipBot !tip 1 @usuario1.',
    'nl': 'Tips worden nu verwerkt via openbare berichten. Verstuur a.u.b. in dit formaat: @NanoTipBot !tip 1 '
          '@gebruikersnaam.',
    'ja': '',
    'zh-t': '現在小費只可以通過公開消息傳遞。請用這個格式 “@NanoTipBot ！賞 <金額> @<用戶名>”',
    'zh-s': '现在小费只可以通过公开消息传递。请用这个格式 “@NanoTipBot ！赏 <金额> @<用户名>”',
    'fr': 'Les tips sont dès à présent traités via message public. Veuillez les envoyer sous le format @NanoTipBot '
          '!tip 1 @utilisateur1',
    'pt': 'Agora, as tips são enviadas através de mensagens públicas. Por favor utiliza o seguinte formato '
          '@NanoTipBot !tip 1 @utilizador1',
    'th': '',
    'de': '',
    'id': 'Tip diproses melalui pesan publik sekarang. Silahkan kirim dalam format @NanoTipBot !tip 1 @user1.',
    'vt': '',
    'ru': 'Типы теперь обрабатываются через публичные сообщения. Пожалуйста, отправьте в формате @NanoTipBot '
          '!тип 1 @имя_пользователя1.',
    'sv': '',
    'it': 'Ora le mance vengono processate attraverso messaggi pubblici. Inviale nel formato @NanoTipBot '
          '!tip 1 @utente1.'
}
# TODO: Make Twitter into a dynamic system
self_tip_text = {
    'en': 'Self tipping is not allowed.  Please use this bot to spread the $NANO to other Twitter users!',
    'es': 'Enviarte tips a ti mismo no está permitido. Por favor, ¡usa este bot para difundir el $NANO a otros '
          'usuarios de Twitter!',
    'nl': 'Jezelf tippen is niet toegestaan. Gebruik deze bot om $NANO naar andere Twitter-gebruikers te verspreiden!',
    'ja': '',
    'zh-t': '不可以給自己小費。請用這個助手來轉發$NANO給其他人！',
    'zh-s': '不可以给自己小费哦。请用这个助手来转发$NANO给其他的推特用户们！',
    'fr': 'Les tips destinés à soi-même ne sont pas autorisés. Veuillez utiliser le bot pour introduire d\'autres '
          'utilisateurs Twitter à $NANO s.v.p!',
    'pt': 'Não é permitido enviar tips a si próprio. Por favor utiliza este bot para difundir e partilhar $NANO '
          'com outros usuários do Twitter!',
    'th': '',
    'de': '',
    'id': 'Tidak boleh self tipping. Silakan gunakan bot ini untuk menyebarkan $NANO ke pengguna Twitter lain!',
    'vt': '',
    'ru': 'Делать тип самому себе не допускаются. Пожалуйста, используйте этот бот, чтобы распространять '
          '$NANO другим пользователям Twitter!',
    'sv': '',
    'it': 'Non è permesso dare la mancia a se stessi. Usa il tip bot per inviare $NANO agli altri utenti Twitter!'
}

receiver_tip_text = {
    'en': '@{} just sent you a {} NANO tip! Reply to this DM with !balance to see your new balance.  '
          'If you have not registered an account, send a reply with !register to get started, or '
          '!help to see a list of commands!  Learn more about NANO at https://nano.org/',
    'es': '¡@{} acaba de enviarte un tip de {} NANO! Responde a este mensaje directo con !balance para revisar tu '
          'nuevo saldo. Si no has registrado una cuenta, responde con !register para comenzar, o con !help para ver '
          'una lista de comandos. Aprende más sobre NANO en https://nano.org/',
    'nl': '@{} heeft je zojuist een {} NANO tip gestuurd! Reageer op deze DM met !balance om jouw nieuwe saldo te '
          'zien. Als je nog geen account hebt geregistreerd, stuur dan een antwoord met !register om aan de slag te '
          'gaan, of !help om een lijst met opdrachten te bekijken! Meer informatie over NANO op https://nano.org/',
    'ja': '',
    'zh-t': '@{} 剛發給您 {} NANO 小費！在此回覆 “！餘額” 來查詢您賬戶的餘額。如果您還未註冊賬戶，在此回覆 “！註冊” 來註冊，'
            '或者回覆 “！幫助” 來看指令單。請拜訪 https://nano.org/ 來了解更多信息。',
    'zh-s': '@{} 刚发给您 {} NANO 小费！在此回复 “！余额” 来看您账户的余额。如果您还未注册账户，在此回复 “！注册” 来注册，或者回复 '
            '“！帮助” 来看指令单。请访问 https://nano.org/ 来了解更多信息。',
    'fr': '@{} vient de vous envoyer un tip de {} NANO! Veuillez répondre à ce message en envoyant !balance afin de '
          'voir votre solde. Si vous ne disposez pas encore de compte, veuillez répondre avec !register afin de vous '
          'inscrire, ou !help afin de recevoir une liste avec d\'autres fonctions! Voir https://nano.org afin d\'en '
          'savoir plus.',
    'pt': '@{} enviou-te uma tip de {} NANO agora mesmo! Responde a esta mensagem direta com !balance para '
          'verificares o teu saldo. Se ainda não estás registado, responde com !register para começar, ou !help '
          'para uma lista de comandos. Aprende mais sobre o NANO em https://nano.org/',
    'th': '',
    'de': '',
    'id': '@{} baru saja mengirimi Anda {} tip NANO! Balas DM ini dengan !balance untuk melihat saldo baru Anda. '
          'Jika Anda belum mendaftarkan akun, kirim balasan dengan !register untuk memulai, atau !help untuk melihat '
          'daftar perintah! Pelajari lebih lanjut tentang NANO di https://nano.org/',
    'vt': '',
    'ru': '@{} только что отправил вам {} NANO тип! Ответьте на этот DM с помощью  !баланс, чтобы увидеть '
          'ваш новый баланс. Если вы еще не зарегистрировали учетную запись, отправьте ответ с сообщением !регистрация '
          'для начала или !помощь, чтобы увидеть список команд! Узнайте больше о NANO на https://nano.org/',
    'sv': '',
    'it': '@{} ti ha inviato una mancia di {} NANO! Rispondi a questo DM con !balance per vedere il tuo saldo. '
          'Se non hai registrato un account, invia una risposta con !register per cominciare, o !help per vedere una '
          'lista dei comandi! Per saperne di più su NANO visita https://nano.org/'
}

private_tip_text = {
    'en': 'Private Tip is under maintenance.  To send your tip, use the !tip function in a tweet or reply!',
    'es': 'Los tips privados están en mantenimiento. Para poder enviar tu tip, usa la función '
          '!tip en un tweet o en una respuesta.',
    'nl': 'Privé tippen is momenteel in onderhoud. Gebruik de tipfunctie in een tweet of antwoord om '
          'jouw tip te verzenden!',
    'ja': '',
    'zh-t': '私賞正在維修中。請用 “！賞” 指令發推或回覆來發送小費！',
    'zh-s': '私赏正在维修中。请用 “！赏” 指令发推或回复来发送小费！',
    'fr': 'Les tips privés sont en maintenance. Afin d\'envoyer un tip, veuillez utiliser la fonction !tip dans '
          'un tweet ou une réponse!',
    'pt': 'A funcionalidade de tips privadas está em manutenção. Para enviar uma tip, utiliza o comando !tip num '
          'tweet ou numa resposta.',
    'th': '',
    'de': '',
    'id': 'Tip pribadi sedang dalam perbaikan. Untuk mengirim tip Anda, gunakan fungsi !tip dalam tweet atau balasan!',
    'vt': '',
    'ru': 'Приватный тип находится на обслуживании. Чтобы отправить свой тип, используйте функцию '
          '!тип в твите или ответе!',
    'sv': '',
    'it': 'Le mance private sono in manutenzione. Per inviare una mancia, usa la funzione !tip in un tweet o '
          'in una risposta!'
}

wrong_format_text = {
    'en': 'The command or syntax you sent is not recognized.  Please send !help for a list of '
          'commands and what they do.',
    'es': 'El comando o sintaxis que enviaste no fue reconocido. Por favor, envía !help para recibir una lista de '
          'comandos junto con sus funciones.',
    'nl': 'De opdracht of syntax die je hebt verzonden wordt niet herkend. Stuur a.u.b !help voor '
          'een lijst met opdrachten en wat ze doen.',
    'ja': '',
    'zh-t': '指令或格式無法被識別。請用 “！幫助” 來查詢指令單和它們的用途。',
    'zh-s': '指令或格式无法被识别。请用 “！帮助” 来查询指令单和它们的用途。',
    'fr': 'La fonction ou sa syntaxe n\'ont pas été reconnues. Veuillez envoyer !help pour obtenir une '
          'liste de fonctions et leurs effets.',
    'pt': 'Esse comando é desconhecido ou a sintaxe está errada. Responde !help para uma lista de comandos '
          'disponíveis e como utilizá-los.',
    'th': '',
    'de': '',
    'id': 'Perintah atau sintaks yang anda kirim tidak dikenali. Silakan kirim !help untuk daftar perintah dan apa '
          'saja fungsinya.',
    'vt': '',
    'ru': 'Отправленная вами команда или синтаксис не распознаются. Пожалуйста, отправьте !помощь для получения '
          'списка команд и того, что они делают.',
    'sv': '',
    'it': 'Il comando da te inviato non è stato riconosciuto. Invia !help per una lista dei comandi e per '
          'sapere cosa fanno.'
}

no_users_text = {
    'en': 'Looks like you didn\'t enter in anyone to tip, or you mistyped someone\'s handle.  You can try '
          'to tip again using the format !tip 1234 @username',
    'es': 'Parece que no ingresaste a nadie para enviar un tip, o te equivocaste en la escritura de su nombre. '
          'Puedes intentar realizar un tip nuevamente usando el formato !tip 1234 @usuario',
    'nl': 'Het lijkt erop dat je niemand hebt genoemd om te ​​tippen, of dat je iemands naam verkeerd hebt '
          'getypt. Je kan proberen opnieuw een tip te versturen in het formaat: !tip 1234 @gebruikersnaam',
    'ja': '',
    'zh-t': '您似乎沒有輸入小費的接受人，或者誤輸了接受人的用戶名。您可以用此格式再試一次： “！賞 <金額> @<用戶名>”',
    'zh-s': '您似乎没有输入小费的接受人，或者误输了接受人的用户名。您可以用此格式再试一次： “！赏 <金额> @<用户名>”',
    'fr': 'Il semble que vous n\'ayez pas indiqué à qui envoyer un tip, ou que vous ayez fait une faute de frappe. '
          'Veuillez réessayer avec le format !tip 1234 @utilisateur',
    'pt': 'Parece que não especificaste nenhum utilizador na tip, ou esse utilizador não existe. Podes tentar '
          'enviar uma tip novamente com o seguinte formato !tip 1234 @utilizador',
    'th': '',
    'de': '',
    'id': 'Sepertinya Anda tidak memasukkan siapapun untuk memberi tip, atau Anda salah mengetik nama pengguna '
          'seseorang. Anda dapat mencoba memberi tip lagi menggunakan format !tip 1234 @username',
    'vt': '',
    'ru': 'Похоже, вы не отметили никого, чтобы сделать тип, или набрали неверно. Вы можете попробовать сделать '
          'тип снова, используя формат !тип 1234 @имя_пользователя',
    'sv': '',
    'it': 'Sembra che tu non abbia inserito nessuno cui dare la mancia, oppure abbia sbagliato a scrivere il suo nome '
          'utente. Puoi riprovare usando il formato !tip 1234 @nomeutente'
}

multi_tip_success = {
    'en': 'You have successfully sent your {} $NANO tips.  '
          'Check your account at https://nanocrawler.cc/explorer/account/{}',
    'es': 'Has enviado exitosamente tus tips de {} $NANO. Revisa tu cuenta en '
          'https://nanocrawler.cc/explorer/account/{}',
    'nl': 'Je hebt jouw {} $NANO tips met succes verzonden. Controleer jouw account op '
          'https://nanocrawler.cc/explorer/account/{}',
    'ja': '',
    'zh-t': '成功發送了{} $NANO 的小費。您可以在 https://nanocrawler.cc/explorer/account/{} 觀察您的賬戶。',
    'zh-s': '成功发送了{} $NANO 的小费。您可以在 https://nanocrawler.cc/explorer/account/{} 查看您的账户。',
    'fr': 'Vous avez envoyé vos tips de {} $NANO avec succès. Pour voir votre compte veuillez cliquer sur '
          'https://nanocrawler.cc/explorer/account/{}',
    'pt': 'As tuas tips de {} $NANO cada foram enviadas. Verifica a tua conta em '
          'https://nanocrawler.cc/explorer/account/{}',
    'th': '',
    'de': '',
    'id': 'Anda telah berhasil mengirim {} $NANO tips Anda. Periksa akun Anda di '
          'https://nanocrawler.cc/explorer/account/{}',
    'vt': '',
    'ru': 'Вы успешно отправили свои {} $NANO тип. Проверьте свой адрес на '
          'https://nanocrawler.cc/explorer/account/{} ',
    'sv': '',
    'it': 'Hai inviato con successo le tue mance di {} $NANO. Controlla il tuo account su '
          'https://nanocrawler.cc/explorer/account/{}'
}

tip_success = {
    'en': 'You have successfully sent your {} $NANO tip.  '
          'Check out this transaction at https://nanocrawler.cc/explorer/block/{}',
    'es': 'Has enviado exitosamente tu tip de {} $NANO. Verifica esta transacción en '
          'https://nanocrawler.cc/explorer/block/{}',
    'nl': 'Je hebt jouw {} $NANO tip succesvol verzonden. Bekijk deze transactie op '
          'https://nanocrawler.cc/explorer/block/{}',
    'ja': '',
    'zh-t': '成功發送了{} $NANO 的小費。您可以在 https://nanocrawler.cc/explorer/block/{} 查看這筆交易。',
    'zh-s': '成功发送了{} $NANO 的小费。您可以在 https://nanocrawler.cc/explorer/block/{} 查看这笔交易。',
    'fr': 'Vous avez envoyé votre tip de {} $NANO avec succès. Vous pouvez voir la transaction en cliquant sur '
          'https://nanocrawler.cc/explorer/block/{}',
    'pt': 'A tua tip de {} $NANO foi enviada com sucesso. Verifica esta transação em '
          'https://nanocrawler.cc/explorer/block/{}',
    'th': '',
    'de': '',
    'id': 'Anda telah berhasil mengirim tip {} $NANO Anda. Lihat transaksi ini di '
          'https://nanocrawler.cc/explorer/block/{}',
    'vt': '',
    'ru': 'Вы успешно отправили свой {} $NANO тип. Проверьте эту транзакцию на '
          'https://nanocrawler.cc/explorer/block/{}',
    'sv': '',
    'it': 'Hai inviato con successo la tua mancia di {} $NANO. Controlla questa transazione su '
          'https://nanocrawler.cc/explorer/block/{}'
}

not_a_number_text = {
    'en': 'Looks like the value you entered to tip was not a number.  You can try to tip '
          'again using the format !tip 1234 @username',
    'es': 'Parece que el valor que ingresaste para realizar un tip no fue un número. Puedes intentarlo nuevamente '
          'usando el formato !tip 1234 @usuario',
    'nl': 'Het lijkt erop dat de waarde die je hebt ingevoerd om een tip te geven geen getal was. '
          'Je kan proberen opnieuw een tip te geven in het formaat: !tip 1234 @gebruikersnaam',
    'ja': '',
    'zh-t': '您輸入的小費額度似乎不是個數字。您可以用此格式再試一次 “！賞 <金額> @<用戶名>”',
    'zh-s': '您输入的小费额度似乎不是个数字。您可以再试一次用此格式 “！赏 <金额> @<用户名>”',
    'fr': 'Il semble que le montant indiqué de votre tip se trouve ne pas être un nombre. Veuillez réessayer votre '
          'tip avec le format !tip 1234 @utilisateur',
    'pt': 'Parece que o valor da tip não é um número. Tenta novamente utilizando o formato !tip 1234 @utilizador',
    'th': '',
    'de': '',
    'id': 'Sepertinya nilai yang Anda masukkan ke tip bukan angka. Anda dapat mencoba memberi tip lagi menggunakan '
          'format !tip 1234 @username',
    'vt': '',
    'ru': 'Похоже, значение, которое вы ввели для тип, не было числом. Вы можете попробовать сделать снова '
          'тип, используя формат !тип 1234 @имя_пользователя',
    'sv': '',
    'it': 'Sembra che il valore della mancia inserito non sia un numero. Puoi riprovare usando il formato '
          '!tip 1234 @nomeutente'
}

min_tip_text = {
    'en': 'The minimum tip amount is {} NANO.  Please update your tip amount and try again.',
    'es': 'El monto mínimo para realizar un tip es de {} NANO. Por favor, actualiza el monto de tu tip e '
          'intenta nuevamente.',
    'nl': 'Het minimale tipbedrag is {} NANO. Pas je tipbedrag aan en probeer het opnieuw.',
    'ja': '',
    'zh-t': '最低小費額度是{} NANO。請更新您的小費額度後再試一次。',
    'zh-s': '最低小费额度是{} NANO。请更新您的小费额度并再试一次。',
    'fr': 'Le montant de tip minimum est {} NANO. Veuillez changer le montant de votre tip et réessayez.',
    'pt': 'O valor mínimo por cada tip é {} NANO. Por favor corrige o valor e tenta novamente.',
    'th': '',
    'de': '',
    'id': 'Jumlah tip minimum adalah {} NANO. Harap perbarui jumlah tip Anda dan coba lagi.',
    'vt': '',
    'ru': 'Минимальная сумма тип составляет {} NANO. Пожалуйста, обновите сумму тип и попробуйте снова.',
    'sv': '',
    'it': 'La mancia minima è di {} NANO. Aggiorna l\'importo della e riprova.'
}

missing_user_message = {
    'en': '{} not found in our records.  In order to tip them, they need to be a member of the channel.  If they are '
          'in the channel, please have them send a message in the chat so I can add them.',
    'es': '{} no se encontró en nuestros registros. Para poder realizarle un tip, el usuario debe ser miembro del '
          'grupo. Si está en el grupo, por favor que envíe un mensaje en el chat para poderlo agregar.',
    'nl': '{} wordt niet gevonden in onze administratie. Om personen een tip te geven, moeten ze lid zijn van het '
          'kanaal. Als ze deel uitmaken van het kanaal, stuur ze dan een bericht in de chat zodat ik ze kan toevoegen.',
    'ja': '',
    'zh-t': '{} 不在我們的記錄裏。被賞小費的人必須是此群組的成員，並要在群組裡發送過信息。',
    'zh-s': '{} 不在我们的记录里。若想给TA小费，TA需要成为此群的成员。如果TA在这个群，请让TA在聊天里冒个泡以让我来把TA加进来。',
    'fr': '{} introuvable. Afin de leur envoyer un tip, il faut qu\'ils soient membre de ce channel. S\'ils sont '
          'membre du channel, veuillez leur envoyer un message dans le chat afin que je puisse les inscrire.',
    'pt': 'O utilizador {} não se encontra na nossa lista. Para poder receber uma tip, ele tem de fazer parte do '
          'canal. Se ele já se encontra no canal, terá de enviar uma mensagem pública no chat para o bot '
          'poder adicioná-lo.',
    'th': '',
    'de': '',
    'id': '{} tidak ditemukan dalam catatan kami. Untuk memberi tip, mereka harus menjadi anggota saluran. Jika ada '
          'di saluran, minta mereka mengirim pesan di obrolan sehingga saya dapat menambahkannya.',
    'vt': '',
    'ru': '{} не найдено в наших записях. Чтобы дать им тип, им нужно быть участником канала. Если они '
          'находятся на канале, попросите их отправить сообщение в чат, чтобы я мог добавить их.',
    'sv': '',
    'it': '{} non trovato. Per dare loro una mancia, devono essere membri del gruppo. Se sono nel gruppo, dì '
          'loro di inviare un messaggio nella chat così potrò aggiungerli.'
}

no_account_text = {
    'en': 'You do not have an account with the bot.  Please send a DM to me with !register to set up an account.',
    'es': 'No tienes una cuenta registrada con el bot. Por favor, envíame un mensaje directo con !register para '
          'configurar una cuenta.',
    'nl': 'Je hebt nog geen account bij de bot. Stuur een DM naar mij met !register om een ​​account aan te maken.',
    'ja': '',
    'zh-t': '您沒有小費助手的賬戶。請向我發送私信 “！註冊” 來註冊一個新賬戶。',
    'zh-s': '您没有小费助手的账户。请向我发送私信 “！注册” 来注册一个新账户。',
    'fr': 'Vous ne disposez pas de compte avec le bot. Veuillez m\'envoyer un message privé contenant !register '
          'pour vous inscrire.',
    'pt': 'Ainda não tens uma conta registada com o tip bot. Envia-me uma mensagem direta com !register para começar.',
    'th': '',
    'de': '',
    'id': 'Anda tidak memiliki akun dengan bot. Silakan kirim DM kepada saya dengan !register untuk mengatur '
          'sebuah akun.',
    'vt': '',
    'ru': 'У вас нет аккаунта с ботом. Пожалуйста, пришлите мне Личное Сообщение с !регистрация, чтобы создать '
          'учетную запись.',
    'sv': '',
    'it': 'Non hai un account con il bot. Inviami un DM con !register per configurare un account.'
}

not_enough_text = {
    'en': 'You do not have enough NANO to cover this {} NANO tip.  '
          'Please check your balance by sending a DM to me with !balance and retry.',
    'es': 'No tienes suficiente NANO para cubrir este tip de {} NANO. Por favor verifica tu saldo enviándome un '
          'mensaje directo con !balance e intenta nuevamente.',
    'nl': 'Je hebt niet genoeg NANO om deze {} NANO tip te dekken. Controleer jouw saldo door een DM naar mij '
          'te sturen met !balance en probeer het opnieuw.',
    'ja': '',
    'zh-t': '您沒有足夠 NANO 去支付 {} NANO 的小費。請向我發送私信 “！餘額” 來查詢您的餘額，然後再嘗試。',
    'zh-s': '您没有足够 NANO 去支付 {} NANO 的小费。请向我发送私信 “！余额” 来查询您的余额，然后再尝试。',
    'fr': 'Vous n\'avez pas assez de NANO pour couvrir ce {} tip NANO. Veuillez vérifier votre solde en m\'envoyant '
          'un message privé contenant !balance et réessayez.',
    'pt': 'Não tens saldo suficiente para esta tip de {} NANO. Por favor verifica o teu saldo enviando-me uma '
          'mensagem com !balance e tenta novamente.',
    'th': '',
    'de': '',
    'id': 'Anda tidak memiliki cukup NANO untuk mengirim {} tip NANO ini. Silakan periksa saldo Anda dengan '
          'mengirimkan DM kepada saya dengan !balance dan coba lagi.',
    'vt': '',
    'ru': 'У вас недостаточно NANO, чтобы покрыть этот {} NANO тип. Пожалуйста, проверьте свой баланс, '
          'отправив мне Личное Сообщение с !баланс и повторите попытку.',
    'sv': '',
    'it': 'Non hai abbastanza NANO per coprire questa mancia di {} NANO. Controlla il tuo saldo inviandomi un '
          'DM con !balance e riprova.'
}

help_message = {
    'en': 'Thank you for using the Nano Tip Bot!  Below is a list of commands, and a description of what they do:\n\n'
          + BULLET + '!help: The tip bot will respond to your DM with a list of commands and their functions. If you'
                     ' forget something, use this to get a hint of how to do it!\n\n'
          + BULLET + ' !register: Registers your user ID for an account that is tied to it.  This is used to store'
                     ' your tips. Make sure to withdraw to a private wallet, as the tip bot is not meant to be a '
                     'long term storage device for Nano.\n\n'
          + BULLET + '!balance: This returns the balance of the account linked with your user ID.\n\n'
          + BULLET + '!tip: Tips are sent through public tweets or in Telegram groups.\n'
                     ' On Twitter: Tag @NanoTipBot in a tweet and mention !tip <amount> <@username>.\n'
                     ' Example: @NanoTipBot !tip 1 @mitche50 would send a 1 Nano tip to user @mitche50.\n'
                     ' On Telegram send !tip <amount> <@username> to tip in the group.\n\n'
          + BULLET + ' !privatetip: Currently disabled.  This will send a tip to another user through DM.  If you '
                     'would like your tip amount to be private, use this function!  Proper usage is !privatetip '
                     '@username 1234\n\n'
          + BULLET + ' !account: Returns the account number that is tied to your user ID (currently unique to '
                     'platform).  You can use this to deposit more Nano to tip from your personal wallet.\n\n'
          + BULLET + ' !withdraw: Proper usage is !withdraw xrb_12345.  This will send the full balance of your tip '
                     'account to the provided Nano account.  Optional: You can include an amount to withdraw by '
                     'sending !withdraw <amount> <address>.  Example: !withdraw 1 xrb_iaoia83if221lodoepq would '
                     'withdraw 1 NANO to account xrb_iaoia83if221lodoepq.\n\n'
          + BULLET + ' !donate: Proper usage is !donate 1234.  This will send the requested donation to the Nano Tip '
                     'Bot donation account to help fund development efforts.\n\n'
          + BULLET + ' !setlanguage: Used to change the default language of the bot.  A list of available languages '
                     'is provided in the !languages command.  Proper use is "!setlanguage Russian" to change '
                     'your language to Russian.\n\n'
          + BULLET + ' !languages: Returns a list of languages available for translation.',
    'es': '¡Gracias por usar el Nano Tip Bot!\n'
          'Debajo hay una lista de comandos junto con una descripción de lo que cada uno hace.\n\n'
          + BULLET + ' !help o !ayuda: El tip bot va a responder a tu mensaje directo con una lista de comandos y sus '
                     'funciones. Si olvidas algo, usa esto para tener una pista de cómo hacerlo.\n\n'
          + BULLET + ' !register o !registro: Registra tu ID de usuario a una cuenta que esté vinculada a este. Esto '
                     'se utiliza para almacenar tus tips. Asegúrate de retirar tus fondos a una billetera privada, ya '
                     'que el tip bot no pretende ser un dispositivo de almacenamiento a largo plazo para NANO.\n\n'
          + BULLET + ' !balance: Te muestra el saldo de la cuenta vinculada con tu ID de usuario.\n\n'
          + BULLET + ' !tip: Los tips se envían a través de tweets públicos o en grupos de Telegram.\n'
                     'En Twitter: Etiqueta a @NanoTipBot en un tweet y menciona !tip <monto> <@usuario>. Ejemplo: '
                     '@NanoTipBot !tip 1 @mitche50 enviaría un tip de 1 NANO al usuario @mitche50.\n'
                     'En Telegram: Envía !tip <monto> <@usuario> para realizar un tip en el grupo.\n\n'
          + BULLET + ' !privatetip: Actualmente deshabilitado. Esto enviará un tip a otro usuario a través de un'
                     ' mensaje directo. Si deseas que la cantidad de tu tip sea privada, ¡usa esta función! El uso '
                     'correcto es: !privatetip @usuario 1234\n\n'
          + BULLET + ' !account o !cuenta: Recibirás el número de cuenta que está vinculado a tu ID de usuario '
                     '(actualmente exclusivo de la plataforma). Puedes usar esto para depositar más NANO para '
                     'realizar tips de tu billetera personal.\n\n'
          + BULLET + ' !withdraw o !retirar: El uso adecuado es !withdraw xrb_12345. Esto enviará el saldo completo '
                     'de tu cuenta de tips a la cuenta NANO provista. Opcional: Puedes incluir una cantidad para '
                     'retirar utilizando !withdraw <cantidad> <cuenta>. Ejemplo: !withdraw 1 xrb_iaoia83if221lodoepq '
                     'retiraría 1 NANO a la cuenta xrb_iaoia83if221lodoepq.\n\n'
          + BULLET + ' !donate o !donar: El uso adecuado es !donate 1234. Esto enviará la donación solicitada a '
                     'la cuenta de donación del Nano Tip Bot para ayudar a financiar los esfuerzos de desarrollo.\n\n'
          + BULLET + ' !setlanguage o !configuraridioma: Se usa para cambiar el idioma predeterminando del bot. El '
                     'uso correcto es: !setlanguage Russian, lo que cambiaría  tu idioma al ruso.\n\n'
          + BULLET + ' !languages o !idiomas: Te muestra una lista de idiomas disponibles para traducción.',
    'nl': 'Bedankt voor het gebruik van de Nano Tip Bot! Hieronder staat een lijst met opdrachten en een '
          'beschrijving van wat ze doen:\n\n'
          + BULLET + ' !help: De tipbot reageert op je DM met een lijst met opdrachten en hun functies. Als je iets '
                     'vergeet, gebruik dit dan om een ​​hint van hoe je het moet doen te krijgen!\n\n'
          + BULLET + ' !register: Gegistreert jouw gebruikers-ID voor een account dat hieraan is gekoppeld. Dit '
                     'wordt gebruikt om jouw tips op te slaan. Zorg ervoor dat je jouw saldo regelmatig naar een '
                     'privé-account verstuurt, want de Tip Bot is niet bedoeld als lange termijn opslag '
                     'voor jouw Nano.\n\n'
          + BULLET + ' !balance: Hiermee wordt het saldo van jouw persoonlijke Tip Bot account getoond.\n\n'
          + BULLET + ' !tip: Tips worden verzonden via openbare tweets of in Telegram-groepen.\n'
                     'Op Twitter: Tag @NanoTipBot in een tweet en vermeld !tip <aantal> <@gebruikersnaam>. '
                     'Voorbeeld: @NanoTipBot !tip 1 @mitche50 stuurt een 1 Nano-tip naar gebruiker @mitche50.\n'
                     'Op Telegram stuur !tip <aantal> <@gebruikersnaam> om iemand een ​​tip te geven in de groep.\n\n'
          + BULLET + ' !privatetip: Momenteel uitgeschakeld. Hiermee wordt via DM een tip naar een andere '
                     'gebruiker verzonden. Als je wilt dat jouw tipbedrag privé is, gebruik dan deze '
                     'functie! Correct gebruik is !privatetip @gebruikersnaam 1234\n\n'
          + BULLET + ' !account: Toont het accountnummer dat gekoppeld is aan jouw gebruikers-ID '
                     '(momenteel uniek voor het platform). Je kan dit adres gebruiken om er meer Nano op te '
                     'storten, zodat je een tip kan sturen vanuit jouw persoonlijke account.\n\n'
          + BULLET + ' !withdraw: Correct gebruik is !withdraw xrb_12345. Hiermee wordt het volledige saldo van '
                     'jouw tip-account naar het door jou opgegeven Nano-account verzonden. '
                     'Optioneel: je kan een specifiek bedrag opnemen door het verzenden van '
                     '!withdraw <bedrag> <adres>. Voorbeeld: !withdraw 1 xrb_iaoia83if221lodoepq zou 1 NANO '
                     'opnemen en versturen naar rekening xrb_iaoia83if221lodoepq.\n\n'
          + BULLET + ' !donate: correct gebruik is !donate 1234. Hiermee wordt de gevraagde donatie naar de '
                     'Nano Tip Bot-donatierekening verzonden om goede initiatieven te helpen financieren.\n\n'
          + BULLET + ' !setlanguage: wordt gebruikt om de standaardtaal van de bot te wijzigen. Een lijst met '
                     'beschikbare talen is beschikbaar in de! Talen-opdracht. Correct gebruik is '
                     '"!setlanguage Russian" om uw taal in het Russisch te veranderen.\n\n'
          + BULLET + ' !languages: retourneert een lijst met beschikbare talen voor vertaling.',
    'ja': '',
    'zh-t': '感謝您使用Nano小費助手！\n'
            '註意：所有“！”均爲中文輸入法的嘆號。若想用英文嘆號請用英文指令。\n'
            '以下是中文指令單以及它們功能的介紹：\n\n'
            + BULLET + ' ！幫助：小費助手會在您的私信裡回復指令單和每個指令的功能。如果您記不清指令，可以用這個回想起來！\n\n'
            + BULLET + ' ！註冊：註冊跟您用戶名相連的賬戶。這是用來儲存您的小費的。別忘了把小費提取到一個私人錢包裡，因為小費助手並不是一個用來長期保管Nano的設備。\n\n'
            + BULLET + ' ！餘額：此指令可匯報連著您用戶名的賬戶餘額。\n\n'
            + BULLET + ' ！賞：小費通過發推或電報群聊天傳送。\n'
                       '在推特上：發推時點名@NanoTipBot然後輸入 “！賞 <金額> @<用戶名>”。比如：“@NanoTipBot ！賞 1 @mitche50” 會給用戶 @mitche50 1 NANO的小費。\n'
                       '在電報上發 “！賞 <金額> @<用戶名>” 來在群裡賞小費。\n\n'
            + BULLET + ' ！私賞：目前不能使用。這會用私信給另一個用戶小費。如果您想私密地給小費，請用這個指令。正確用法是 “！私賞 @<用戶名> <金額>”。\n\n'
            + BULLET + ' ！賬戶：匯報和平台用戶名相連的賬戶號碼（目前每個平台的賬戶都不一樣）。您可以用個人錢包給此賬戶充值更多的NANO。\n\n'
            + BULLET + ' ！取款：正確用法是 “！取款 <目的地賬戶>” （別忘了“xrb_”的前綴）。這會把此賬戶裡的全部餘額發送到目的地的Nano賬戶。\n\n'
            + BULLET + ' ！捐款：正確用法是 “！捐款 <金額>”。這會把輸入的金額捐給Nano小費助手的捐款賬戶以便協助今後的軟件開發。\n\n'
            + BULLET + ' ！設語：用來改變小費助手的默認語言。現有語言單可以用 “！語言”來查詢。正確用法是 “！設語 English” 來把語言改為英語。\n\n'
            + BULLET + ' ！語言：提供現有的語言單以及它們能被系統識別的代名。',
    'zh-s': '感谢您使用Nano小费助手\n'
            '注意：所有“！”均为中文输入法的叹号。若想用英文叹号请用英文指令。\n'
            '以下是中文指令单以及它们功能的介绍：\n\n'
            + BULLET + ' ！帮助：小费助手会在您的私信里回复指令单和它们的功能。如果您记不清指令，可以用这个回想起来！\n\n'
            + BULLET + ' ！注册：注册跟您用户名相连的账户。这是用来储存您的小费的。别忘了把小费提取到一个私人钱包里，'
                       '因为小费助手并不是一个用来长期保管Nano的设备。\n\n'
            + BULLET + ' ！余额：此指令可汇报连着您用户名的账户余额。\n\n'
            + BULLET + ' ！赏：小费通过发推或电报群聊天传送。\n'
                       '在推特上：发推时点名@NanoTipBot然后输入 “！赏 <金额> @<用户名>”。\n'
                       '比如：“@NanoTipBot ！赏 1 @mitche50” 会给用户 @mitche50 1 NANO的小费。\n'
                       '在电报上发 “！赏 <金额> @<用户名>” 来在群里赏小费。\n\n'
            + BULLET + ' ！私赏：目前不能使用。这会用私信赏给另一个用户小费。如果您想私密地赏小费，请用这个指令。正确用法是 '
                       '“！私赏 @<用户名> <金额>”。\n\n'
            + BULLET + ' ！账户：汇报和平台用户名相连的账户号码（目前每个平台的账户都不一样）。'
                       '您可以用个人钱包给此账户充值更多的NANO。\n\n'
            + BULLET + ' ！取款：正确用法是 “！取款 <目的地账户>” （别忘了“xrb_”的前缀）。'
                       '这会把此账户里的全部余额发送到目的地的Nano账户。\n\n'
            + BULLET + ' ！捐款：正确用法是 “！捐款 <金额>”。这会把输入的金额捐给Nano小费助手的捐款账户以便协助今后的软件开发。\n\n'
            + BULLET + ' ！设语：用来改变小费助手的默认语言。现有语言单可以用 "！语言" 来查询。正确用法是 “！设语 English” '
                       '来把语言改为英语。\n\n'
            + BULLET + ' ！语言：提供现有的语言单和它们能被系统识别的代名。',
    'fr': 'Nous vous remercions d\'utiliser le Tip Bot de Nano! Ci-dessous se trouve une liste des fonctions, ainsi '
          'qu\'une description de ce qu\'elles effectuent:\n\n'
          + BULLET + ' !help: Le tip bot répondra à votre message avec une liste de commandes ainsi que leurs '
                     'fonctions. Si jamais vous oubliez l\'une d\'entre elles, n\'hésitez pas à demander un '
                     'coup de pouce!\n\n'
          + BULLET + ' !register: Inscrit votre identifiant utilisateur et le lie à un compte, afin de pouvoir '
                     'recevoir et enregistrer vos tips. Veuillez vous assurer de retirer vos fonds sur un '
                     'portefeuille privé, puisque le tip bot n\'est pas voué à être un outil de stockage à long '
                     'terme pour vos Nanos.\n\n'
          + BULLET + ' !balance: Vous indique le solde de votre compte lié à votre identifiant utilisateur.\n\n'
          + BULLET + '!tip: Les tips sont envoyés via les tweets publics ou au sein de groupes Telegram.\n'
                     'Sur Twitter: Taggez @NanoTipBot dans un tweet et indiquer !tip <montant> <@utilisateur>. '
                     'Exemple: @NanoTipBot !tip 1 @mitche50 enverrait un tip de 1 Nano à l\'utilisateur @mitche50.\n'
                     'Sur Telegram, envoyez !tip <montant> <@utilisateur> afin d\'envoyer un tip dans le groupe.\n\n'
          + BULLET + ' !privatetip: Désactivé pour l\'instant. Ceci enverra un tip à un autre utilisateur via message '
                     'privé. Si vous désirez que le montant de votre tip soit privé, utilisez cette fonction! '
                     'Sous ce format: !privatetip 1234 @utilisateur\n\n'
          + BULLET + ' !account: Vous indique le numéro de compte lié à votre identifiant utilisateur (unique à la '
                     'plate-forme utilisée). Vous pouvez l\'utiliser pour verser plus de Nano de votre compte '
                     'personnel vers votre compte tip.\n\n'
          + BULLET + ' !withdraw: La commande s\'utilise comme suit: !withdraw xrb_12345. Ceci enverra le montant '
                     'total de votre solde vers le compte Nano indiqué. Optionnel: Vous pouvez inclure un montant de '
                     'retrait en envoyant !withdraw <montant> <adresse>. Exemple: !withdraw 1 xrb_iaoia83if221lodoepq '
                     'retirerait 1 NANO vers le compte xrb_iaoia83if221lodoepq.\n\n'
          + BULLET + ' !donate: La commande s\'utilise comme suit: !donate 1234. Ceci enverra le montant indiqué de '
                     'donation vers le compte de donation du Tip Bot Nano afin d\'aider à financer les efforts de '
                     'développement.\n\n'
          + BULLET + ' !setlanguage: Vous permet de changer la langue du bot. Une liste de langues disponibles est à '
                     'disposition grâce à la commande !languages. Elle s\'utilise comme suit: " !setlanguage French " '
                     'afin de changer votre langue vers le Français.\n\n'
          + BULLET + ' !languages: Fournit une liste de langues disponibles.',
    'pt': 'Obrigado por utilizar o Nano Tip Bot! Os comandos disponíveis são:\n\n'
          + BULLET + ' !help: O tip bot irá responder a uma mensagem direta com esta lista de comandos e descrição de '
                     'utilização.\n\n'
          + BULLET + ' !register: Regista um utilizador com o tip bot. O bot passará a guardar o seu saldo. Por favor '
                     'faça levantamento das tips para uma carteira privada quando o objetivo for guardar Nano por '
                     'longos períodos de tempo. O tip bot não deve ser usado para guardar Nano.\n\n'
          + BULLET + ' !balance: Mostra o saldo do utilizador.\n\n'
          + BULLET + ' !tip: As tips são gorjetas enviadas através de tweets públicos ou em grupos do Telegram.\n'
                     'No Twitter, faz tag do @NanoTipBot num tweet e utiliza o comando !tip <valor> <@utilizador>. '
                     'Por exemplo: @NanoTipBot !tip 1 @mitche50.\n'
                     'No Telegram, envia !tip <valor> <@utilizador> no grupo.\n\n'
          + BULLET + ' !privatetip: De momento encontra-se desativado. Permite enviar uma tip a outro utilizador '
                     'através de mensagens privadas. Para utilizar, o formato é !privatetip <@utilizador> <valor>\n\n'
          + BULLET + ' !account: Devolve a conta associada ao teu utilizador. Envia Nano de uma carteira privada para '
                     'esta conta para poderes enviar mais tips.\n\n'
          + BULLET + ' !withdraw: Este comando serve para retirar o saldo do tip bot para outra conta à tua '
                     'escolha. !withdraw xrb_12345 envia todo o teu saldo para essa conta. Opcionalmente podes incluir '
                     'um montante para não enviar o saldo todo, da seguinte forma: !withdraw <valor> <conta>, '
                     'por exemplo, !withdraw 1 xrb_12345.\n\n'
          + BULLET + ' !donate: Este comando envia o valor pretendido para a conta de doações do Nano Tip Bot para '
                     'ajudar com os custos de desenvolvimento e manutenção. Para doar, !donate <valor>\n\n'
          + BULLET + ' !setlanguage: Usado para alterar o idioma padrão do bot. Uma lista de idiomas disponíveis é '
                     'fornecida no comando! Languages. O uso adequado é "!setlanguage Russian" para mudar seu '
                     'idioma para o russo.\n\n'
          + BULLET + ' !languages: retorna uma lista de idiomas disponíveis para tradução.',
    'th': '',
    'de': '',
    'id': 'Terima kasih telah menggunakan Nano Tip Bot! Di bawah ini adalah daftar perintah, dan deskripsi tentang apa '
          'yang akan Bot lakukan:\n\n'
          + BULLET + ' !help: Bot tip akan merespons DM Anda dengan daftar perintah dan fungsinya. Jika Anda lupa '
                     'sesuatu, gunakan ini untuk mendapatkan petunjuk bagaimana melakukannya!\n\n'
          + BULLET + ' !register: Mendaftarkan ID pengguna Anda untuk akun yang terkait dengannya. Ini digunakan '
                     'untuk menyimpan tips Anda. Pastikan untuk menarik ke dompet pribadi, karena bot tip tidak '
                     'dimaksudkan sebagai perangkat penyimpanan jangka panjang untuk Nano.\n\n'
          + BULLET + ' !balance: Ini mengembalikan/menunjukkan jumlah saldo akun yang ditautkan dengan ID '
                     'pengguna Anda.\n\n'
          + BULLET + ' !tip: Tip dikirim melalui tweet publik atau dalam grup Telegram.\n'
                     'Di Twitter: Beri tag @NanoTipBot dalam tweet dan sebutkan !tip <amount> <@username>. '
                     'Contoh: @NanoTipBot !tip 1 @mitche50 akan mengirim tip 1 Nano ke pengguna @mitche50.\n'
                     'Di Telegram, kirim !tip <amount> <@username> untuk memberi tip di grup.\n\n'
          + BULLET + ' !privatetip: Saat ini dinonaktifkan. Ini akan mengirim tip ke pengguna lain melalui DM. Jika '
                     'Anda ingin jumlah tip Anda menjadi pribadi, gunakan fungsi ini! Penggunaan yang benar '
                     'adalah !privatetip @username 1234\n\n'
          + BULLET + ' !account: Mengembalikan nomor akun / alamat dompet yang terkait dengan ID pengguna Anda (saat '
                     'ini unik untuk platform). Anda dapat menggunakan ini untuk menyimpan lebih banyak Nano dari '
                     'wallet personal anda.\n\n'
          + BULLET + ' !withdraw: Penggunaan yang benar adalah !withdraw xrb_12345. Ini akan mengirim saldo penuh '
                     'dari akun tip Anda ke akun Nano yang anda kirimkan. Opsional: Anda dapat memasukkan jumlah '
                     'yang akan ditarik dengan mengirimkan !withdraw <amount> <address>. Contoh: !withdraw 1 '
                     'xrb_iaoia83if221lodoepq akan menarik 1 NANO ke akun xrb_iaoia83if221lodoepq.\n\n'
          + BULLET + ' !donate: Penggunaan yang tepat adalah !donate 1234. Ini akan mengirimkan donasi yang '
                     'diminta ke akun donasi Nano Tip Bot untuk membantu upaya pengembangan bot kedepannya.\n\n'
          + BULLET + ' !setlanguage: Digunakan untuk mengubah bahasa default bot. Daftar bahasa yang tersedia '
                     'disediakan di perintah !languages. Penggunaan yang benar adalah "!setlanguage Russian" '
                     'untuk mengubah bahasa Anda ke Bahasa Rusia.\n\n'
          + BULLET + ' !languages: Melihat daftar bahasa yang tersedia untuk terjemahan / bahasa yang '
                     'digunakan oleh Bot.',
    'vt': '',
    'ru': 'Спасибо за использование Nano Tip Bot! Ниже приведен список команд и описание того, что они делают:\n\n'
          + BULLET + ' !помощь: Тип бот ответит на ваше Личное Сообщение со списком команд и их функций. Если вы '
                     'что-то забыли, используйте это, чтобы получить подсказку, как это сделать!\n\n'
          + BULLET + ' !регистрация: Регистрирует ваш идентификатор пользователя для учетной записи, которая связана с '
                     'ним. Это используется для хранения ваших тип. Обязательно выводите на собственный кошелек, '
                     'так как тип бот не предназначен для длительного хранения Nano.\n\n'
          + BULLET + ' !баланс: показывает баланс учетной записи, связанной с вашим идентификатором пользователя.\n\n'
          + BULLET + ' !тип: Тип отправляются через публичные твиты или в группах Telegram.\n'
                     'В Твиттере: Отметьте @NanoTipBot в твиттере и упомяните !тип <сумма> <@имя_пользователя>. '
                     'Пример: @NanoTipBot !тип 1 @mitche50 будет отправлено 1 Nano тип пользователю @mitche50.\n'
                     'В Telegram отправьте !тип <сумма> <@имя_пользователя> , чтобы сделать тип в группе.\n\n'
          + BULLET + ' !приватныйтип: В настоящее время отключен. Это отправит тип другому пользователю через DM. '
                     'Если вы хотите, чтобы сумма тип была конфиденциальной, используйте эту функцию! '
                     'Правильное использование  !приватныйтип @имя_пользователя 1234\n\n'
          + BULLET + ' !аккаунт: Возвращает счёт учетной записи, связанный с вашим идентификатором пользователя '
                     '(в настоящее время уникальным для платформы). Вы можете использовать это, чтобы пополнить '
                     'счет Nano для получения тип с вашего собственного кошелька.\n\n'
          + BULLET + ' !вывод: Правильное использование  !вывод xrb_12345. Это отправит весь баланс вашего '
                     'счета на предоставленный адрес Nano. Необязательно: Вы можете указать сумму для вывода, '
                     'отправив !вывод <сумма> <адрес>. Пример: !вывод 1 xrb_iaoia83if221lodoepq  выведет 1 '
                     'NANO на адрес xrb_iaoia83if221lodoepq.\n\n'
          + BULLET + ' !донат: Правильное использование  !донат 1234. Это отправит пожертвование '
                     'на адрес бота Nano Tip Bot, чтобы помочь в развитию его.\n\n'
          + BULLET + ' !выборязыка: Используется для изменения языка бота по умолчанию. Список доступных языков '
                     'представлен в команде !языки. Правильное использование "!выборязыка русский" для '
                     'изменения вашего языка на русский.\n\n'
          + BULLET + ' !языки: возвращает список языков, доступных для перевода.',
    'sv': '',
    'it': 'Grazie di utilizzare Nano Tip Bot! Qui sotto trovi una lista di comandi, e una '
          'descrizione di cosa fanno:\n\n'
          + BULLET + ' !help: Il tip bot risponderà al tuo DM con una lista di comandi e delle loro funzioni. Se ne '
                     'dimentichi qualcuno, usa questo per ottenere un suggerimento su come utilizzarlo!\n\n'
          + BULLET + ' !register: Registra il tuo ID utente per un account collegato ad esso. Viene utilizzato per '
                     'conservare le tue mance. Assicurati di prelevarle nel tuo portafoglio privato, in quanto il tip '
                     'bot non è destinato ad essere un mezzo per conservare i tuoi Nano nel lungo termine.\n\n'
          + BULLET + ' !balance: Mostra il saldo dell\'account collegato al tuo ID utente.\n\n'
          + BULLET + ' !tip: Le mance vengono inviate attraverso tweets pubblici o nei gruppi Telegram.\n'
                     'Su Twitter: Menziona @NanoTipBot in un tweet e usa !tip <importo> <@nomeutente>.\n'
                     'Esempio: @NanoTipBot !tip 1 @mitche50 invierà una mancia di 1 Nano all\'utente @mitche50.\n'
                     'Su Telegram invia !tip <importo> <@nomeutente> per dare una mancia nel gruppo.\n\n'
          + BULLET + ' !privatetip: Attualmente disabilitata. Questo invierà una mancia ad un altro utente tramite '
                     'DM. Se vuoi che l\'importo della tua mancia rimanga privato, usa questa funzione! L\'uso '
                     'corretto è !privatetip @nomeutente 1234\n\n'
          + BULLET + ' !account: Mostra il numero dell\'account collegato al tuo ID utente (unico sulla piattaforma). '
                     'Puoi utilizzarlo per depositare altri Nano dal tuo portafoglio personale.\n\n'
          + BULLET + ' !withdraw: L\'uso corretto è !withdraw xrb_12345. Questo invierà l\'intero saldo del tuo '
                     'account delle mance all\'indirizzo Nano fornito.Opzionale: Puoi includere l\'importo da '
                     'prelevare inviando !withdraw <importo> <indirizzo>. '
                     'Esemmpio: !withdraw 1 xrb_iaoia83if221lodoepq preleverà 1 NANO inviandolo '
                     'all\'indirizzo xrb_iaoia83if221lodoepq\n\n'
          + BULLET + ' !donate: L\'uso corretto è !donate 1234. Questo invierà la donazione richiesta all\'account '
                     'donazioni di Nano Tip Bot per finanziarne lo sviluppo.\n\n'
          + BULLET + ' !setlanguage: usato per cambiare la lingua predefinita del bot. Un elenco di lingue '
                     'disponibili è fornito nel comando! Languages. L\'uso corretto è "!setlanguage Russian" per '
                     'cambiare la lingua in russo.\n\n'
          + BULLET + ' !languages: restituisce un elenco di lingue disponibili per la traduzione.'
}
account_register_text = {
    'en': 'You have successfully registered for an account.  Your account number is:',
    'es': 'Te has registrado exitosamente para obtener una cuenta. Tu número de cuenta es:',
    'nl': 'Je bent succesvol geregistreerd voor een account. Jouw accountnummer is:',
    'ja': '',
    'zh-t': '您成功註冊了新賬戶。你的賬戶號碼是：',
    'zh-s': '您成功注册了新账户。你的账户号码是：',
    'fr': 'Vous vous êtes inscrit avec succès. Votre numéro de votre compte est:',
    'pt': 'Registaste uma conta com sucesso. A tua conta é:',
    'th': '',
    'de': '',
    'id': 'Anda telah berhasil membuat akun baru. Nomor akun Anda adalah:',
    'vt': '',
    'ru': 'Вы успешно зарегистрировались для учетной записи. Ваш адрес счета:',
    'sv': '',
    'it': 'Hai registrato un account con successo. Il numero del tuo account è:'
}

account_already_registered = {
    'en': 'You already have registered your account.  Your account number is:',
    'es': 'Ya habías registrado tu cuenta. Tu número de cuenta es:',
    'nl': 'Je hebt al een account geregistreerd. Jouw accountnummer is:',
    'ja': '',
    'zh-t': '您已經有賬戶了。你的賬戶號碼是：',
    'zh-s': '您已经有账户了。你的账户号码是：',
    'fr': 'Vous êtes déjà inscrit. Votre numéro de votre compte est:',
    'pt': 'Já te encontras registado. A tua conta é:',
    'th': '',
    'de': '',
    'id': 'Anda sudah mendaftarkan akun Anda. Nomor akun Anda adalah:',
    'vt': '',
    'ru': 'Вы уже зарегистрировали свой аккаунт. Ваш адрес счета:',
    'sv': '',
    'it': 'Hai già registrato un account. Il numero del tuo account è:'
}

account_create_text = {
    'en': 'You didn\'t have an account set up, so I set one up for you.  Your account number is:',
    'es': 'No tenías una cuenta configurada, así que he configurado una para ti. Tu número de cuenta es:',
    'nl': 'Je had nog geen account ingesteld, dus ik heb er één voor je aangemaakt. Jouw accountnummer is:',
    'ja': '',
    'zh-t': '您還沒有賬戶，所以我幫您註冊了新賬戶。您的賬戶號碼是：',
    'zh-s': '您还没有账户，所以我帮您注册了新账户。您的账户号码是：',
    'fr': 'Vous êtes déjà inscrit. Votre numéro de votre compte est:',
    'pt': 'Ainda não tinhas uma conta, por isso criei uma para ti. A conta é:',
    'th': '',
    'de': '',
    'id': 'Anda belum memiliki akun yang diatur, jadi saya mengaturnya untuk Anda. Nomor akun Anda adalah:',
    'vt': '',
    'ru': 'У вас не было учетной записи, поэтому я создал ее для вас. Ваш адрес счета:',
    'sv': '',
    'it': 'Non hai ancora configurato un account, quindi ne ho fatto uno per te. Il numero del tuo account è:'
}

account_text = {
    'en': 'Your account number is:',
    'es': 'Tu número de cuenta es:',
    'nl': 'Jouw accountnummer is:',
    'ja': '',
    'zh-t': '您的賬戶號碼是：',
    'zh-s': '您的账户号码是：',
    'fr': 'Le numéro de votre compte est:',
    'pt': 'A tua conta é:',
    'th': '',
    'de': '',
    'id': 'Nomor akun Anda adalah:',
    'vt': '',
    'ru': 'Ваш адрес счета:',
    'sv': '',
    'it': 'Il numero del tuo account è:'
}

withdraw_no_account_text = {
    'en': 'You do not have an account with the bot.  Please send a DM to me with !register to set up an account.',
    'es': 'No tienes una cuenta registrada con el bot. Por favor, envíame un mensaje directo con !register para '
          'configurar una cuenta.',
    'nl': 'Je hebt nog geen account bij de bot. Stuur een DM naar mij met !register om een ​​account aan te maken.',
    'ja': '',
    'zh-t': '您沒有小費助手的賬戶。請向我發送私信 “！註冊” 來註冊一個新賬戶。',
    'zh-s': '您没有小费助手的账户。请向我发送私信 “！注册” 来注册一个新账户。',
    'fr': 'Vous ne disposez pas de compte avec le bot. Veuillez m\'envoyer un message privé contenant '
          '!register pour vous inscrire.',
    'pt': 'Ainda não tens uma conta registada com o tip bot. Envia-me uma mensagem direta com !register para começar.',
    'th': '',
    'de': '',
    'id': 'Anda tidak memiliki akun dengan bot. Silakan kirim DM kepada saya dengan !register untuk mengatur '
          'sebuah akun.',
    'vt': '',
    'ru': 'У вас нет учетной записи. Ответьте !регистрация для создания учетной записи.',
    'sv': '',
    'it': 'Non hai un account con il bot. Inviami un DM con !register per configurare un account.'
}

invalid_account_text = {
    'en': 'The account number you provided is invalid.  Please double check and resend your request.',
    'es': 'El número de cuenta que proveíste no es válido. Por favor revisa nuevamente y vuelve a enviar tu solicitud.',
    'nl': 'Het accountnummer dat je hebt opgegeven is ongeldig. Controleer het nogmaals en verzend je verzoek opnieuw.',
    'ja': '',
    'zh-t': '您所提供的帳戶號碼無效。請檢查一遍後再嘗試。',
    'zh-s': '您所提供的帐户号码无效。请检查一遍后再尝试。',
    'fr': 'Le numéro de compte que vous avez fourni n\'est pas valable. Veuillez le vérifier et '
          'réessayer votre requête.',
    'pt': 'A conta especificada não é válida. Por favor verifica e volta a enviar.',
    'th': '',
    'de': '',
    'id': 'Nomor akun yang Anda berikan tidak valid. Periksa ulang dan kirim ulang permintaan Anda.',
    'vt': '',
    'ru': 'Указанный вами номер счета недействителен. Пожалуйста, проверьте еще раз и отправьте запрос.',
    'sv': '',
    'it': 'Il numero dell\'account da te fornito non è valido. Controllalo di nuovo e rinvia la tua richiesta.'
}

no_balance_text = {
    'en': 'You have 0 balance in your account.  Please deposit to your address {} to send more tips!',
    'es': 'Tienes 0 saldo en tu cuenta. ¡Por favor deposita en tu cuenta {} para enviar más tips!',
    'nl': 'Je hebt 0 saldo in jouw account. Stort extra NANO naar je adres {} om meer tips te kunnen sturen!',
    'ja': '',
    'zh-t': '您的賬戶沒有任何餘額。請在 {} 存款後再發送小費！',
    'zh-s': '您的账户没有任何余额。请在 {} 存款再发送小费！',
    'fr': 'Le solde de votre compte est de 0. Veuillez déposer des fonds sur votre adresse {} pour '
          'pouvoir envoyer plus de tips!',
    'pt': 'Não tens saldo na tua conta, por favor deposita na conta {} para enviar mais tips!',
    'th': '',
    'de': '',
    'id': 'Anda memiliki saldo 0 di akun Anda. Harap setorkan ke alamat Anda {} untuk mengirim tip lainnya!',
    'vt': '',
    'ru': 'У вас 0 баланса на вашем счету. Пожалуйста, внесите депозит на ваш адрес {}, '
          'чтобы отправить больше тип!',
    'sv': '',
    'it': 'Hai un saldo di 0 nel tuo account. Deposita nel tuo indirizzo {} per inviare altre mance!'
}

invalid_amount_text = {
    'en': 'You did not send a number to withdraw.  Please resend with the format !withdraw <account> or '
          '!withdraw <amount> <account>',
    'es': 'No enviaste un número para retirar. Por favor vuelve a enviar con el formato !withdraw <cuenta> o '
          '!withdraw <monto> <cuenta>',
    'nl': 'Je hebt geen bedrag genoemd om op te nemen. Gelieve opnieuw te verzenden in het formaat: !withdraw '
          '<account>, of: !withdraw <bedrag> <account>',
    'ja': '',
    'zh-t': '您沒有輸入提款金額。請用格式 “！取款 <地址>” 或 “！取款 <金額> <地址>”',
    'zh-s': '您没有输入提款金额。请用格式 “！取款 <地址>” 或 “！取款 <金额> <地址>”',
    'fr': 'Vous n\'avez pas indiqué de montant pour votre retrait. Veuillez réessayer en suivant le format '
          '!withdraw <compte> ou !withdraw <montant> <compte>',
    'pt': 'Não especificaste uma conta, volta a tentar com o formato !withdraw <conta> ou !withdraw <valor> <conta>',
    'th': '',
    'de': '',
    'id': 'Anda tidak mengirim alamat wallet untuk menarik saldo. Harap kirim ulang dengan format '
          '!withdraw <account> atau !withdraw <amount> <account>',
    'vt': '',
    'ru': 'Вы не отправили адрес для вывода. Пожалуйста, повторите отправку в формате  '
          '!вывод <адрес> или !вывод <сумма> <адрес>;',
    'sv': '',
    'it': 'Non hai inviato un numero da prelevare. Rinvia con il formato !withdraw <account> o '
          '!withdraw <importo> <account>'
}

not_enough_balance_text = {
    'en': 'You do not have that much NANO in your account.  To withdraw your full amount, send !withdraw <account>',
    'es': 'No tienes esa cantidad de NANO en tu cuenta. Para retirar el monto total, envía !withdraw <cuenta>',
    'nl': 'Je hebt niet zoveel NANO in jouw account. Om het volledige bedrag op te nemen, verzendt '
          'je !withdraw <account>',
    'ja': '',
    'zh-t': '您的賬戶沒有那麼多的NANO。發送 “！取款 <目的地賬戶>” 來提款你所有的NANO。',
    'zh-s': '您的账户没有那么多的NANO。发送 “！取款 <目的地账户>” 来提款你所有的NANO。',
    'fr': 'Vous ne disposez pas d\'assez de NANO dans votre compte. Pour retirer le montant total, veuillez '
          'envoyer !withdraw <compte>',
    'pt': 'Não tens NANO suficiente. Para enviar todo o saldo, usa !withdraw <conta>',
    'th': '',
    'de': '',
    'id': 'Anda tidak memiliki NANO sebanyak itu di akun Anda. Untuk menarik jumlah penuh Anda, kirim '
          '!withdraw <account>',
    'vt': '',
    'ru': 'У вас не так много NANO на вашем аккаунте. Чтобы вывести всю сумму, отправьте !вывод <адрес>',
    'sv': '',
    'it': 'Non hai così tanti NANO nel tuo account. Per prelevarne l\'intero importo, invia !withdraw <account>'
}

withdraw_text = {
    'en': 'You have successfully withdrawn {} NANO!  You can check the transaction at '
          'https://nanocrawler.cc/explorer/block/{}',
    'es': '¡Has retirado con éxito {} NANO! Puedes verificar la transacción en '
          'https://nanocrawler.cc/explorer/block/{}',
    'nl': 'Je hebt met succes {} NANO opgenomen! Je kan de transactie bekijken op '
          'https://nanocrawler.cc/explorer/block/{}',
    'ja': '',
    'zh-t': '您已成功提取{} NANO！您可以在 https://nanocrawler.cc/explorer/block/{} 查看交易記錄。',
    'zh-s': '您已成功提取{} NANO！您可以在 https://nanocrawler.cc/explorer/block/{} 查看交易记录。',
    'fr': 'Vous avez retiré {} NANO avec succès! Vous pouvez consulter la transaction à partir de '
          'https://nanocrawler.cc/explorer/block/{}',
    'pt': 'Enviaste {} NANO com sucesso! Verifica a transação em https://nanocrawler.cc/explorer/block/{}',
    'th': '',
    'de': '',
    'id': 'Anda telah berhasil menarik {} NANO! Anda dapat memeriksa transaksi di '
          'https://nanocrawler.cc/explorer/block/{}',
    'vt': '',
    'ru': 'Вы успешно отправили {} NANO! Вы можете проверить транзакцию по адресу '
          'https://nanocrawler.cc/explorer/block/{}',
    'sv': '',
    'it': 'Hai prelevato con successo {} NANO! Puoi controllare la transazione su '
          'https://nanocrawler.cc/explorer/block/{}'
}

incorrect_withdraw_text = {
    'en': 'I didn\'t understand your withdraw request.  Please resend with !withdraw <optional:amount> <account>.  '
          'Example, !withdraw 1 xrb_aigakjkfa343tm3h1kj would withdraw 1 NANO to account xrb_aigakjkfa343tm3h1kj.  '
          'Also, !withdraw xrb_aigakjkfa343tm3h1kj would withdraw your entire balance to account '
          'xrb_aigakjkfa343tm3h1kj.',
    'es': 'No comprendí tu solicitud de retiro. Por favor, vuelve a enviarla con !withdraw <opcional:cantidad> '
          '<cuenta>. Por ejemplo, !withdraw 1 xrb_aigakjkfa343tm3h1kj retiraría 1 NANO a la cuenta '
          'xrb_aigakjkfa343tm3h1kj. Además, !withdraw xrb_aigakjkfa343tm3h1kj retiraría tu saldo completo a la cuenta '
          'xrb_aigakjkfa343tm3h1kj.',
    'nl': 'Ik heb jouw opnameverzoek niet begrepen. Stuur opnieuw met !withdraw <optioneel: bedrag> <account>. '
          'Voorbeeld: !withdraw 1 xrb_aigakjkfa343tm3h1kj zou 1 NANO opnemen en versturen naar rekening '
          'xrb_aigakjkfa343tm3h1kj. Ook !withdraw xrb_aigakjkfa343tm3h1kj stuurt je gehele saldo naar account '
          'xrb_aigakjkfa343tm3h1kj.',
    'ja': '',
    'zh-t': '我沒看懂您的取款命令。請重發 “！取款 <金額（非必填）> <目的地賬戶>”。比如：“！取款 1 xrb_aigakjkfa343tm3h1kj” '
            '會提取 1 NANO 到賬戶 xrb_aigakjkfa343tm3h1kj。另外，“！取款 xrb_aigakjkfa343tm3h1kj" 會把您全部餘額轉到賬戶 '
            'xrb_aigakjkfa343tm3h1kj 裏。',
    'zh-s': '我没看懂您的取款命令。请重发 “！取款 <金额（非必填）> <目的地账户>”。比如：“！取款 1 xrb_aigakjkfa343tm3h1kj” '
            '会提取1 NANO到账户 xrb_aigakjkfa343tm3h1kj。另外，“！取款 xrb_aigakjkfa343tm3h1kj” 会把您全部余额转到账户 '
            'xrb_aigakjkfa343tm3h1kj 里。',
    'fr': 'Je n\'ai pas compris votre requête de retrait. Veuillez s.v.p. réessayer avec !withdraw '
          '<montant:optionnel> <compte>. Exemple: !withdraw 1 xrb_aigakjkfa343tm3h1kj retirerait 1 NANO vers le '
          'compte xrb_aigakjkfa343tm3h1kj. Aussi, !withdraw xrb_aigakjkfa343tm3h1kj retirerait le montant total du '
          'solde de votre compte vers le compte xrb_aigakjkfa343tm3h1kj.',
    'pt': 'Não compreendi o comando. Por favor, volta a tentar com !withdraw <valor> <conta>.  O valor é '
          'opcional. Se não for especificado, todo o saldo é enviado.',
    'th': '',
    'de': '',
    'id': 'Saya tidak mengerti permintaan penarikan Anda. Harap kirim ulang dengan !withdraw <opsional: amount> '
          '<account>. Contoh, !withdraw 1 xrb_aigakjkfa343tm3h1kj akan menarik 1 NANO ke akun '
          'xrb_aigakjkfa343tm3h1kj. Juga, !withdraw xrb_aigakjkfa343tm3h1kj akan menarik seluruh saldo Anda ke '
          'akun xrb_aigakjkfa343tm3h1kj.',
    'vt': '',
    'ru': 'Я не понял ваш запрос на снятие средств. Пожалуйста, повторно отправьте с помощью !withdraw '
          '<необязательно: сумма> <адрес>. Например,  !вывод 1 xrb_aigakjkfa343tm3h1kj выведет 1 NANO на '
          'адрес xrb_aigakjkfa343tm3h1kj. Также, !вывод xrb_aigakjkfa343tm3h1kj выведет весь ваш баланс на '
          'адрес xrb_aigakjkfa343tm3h1kj.',
    'sv': '',
    'it': 'Non ho capito la tua richiesta di prelievo. Rinvia con !withdraw <opzionale:importo> <account>. '
          'Esempio, !withdraw 1 xrb_aigakjkfa343tm3h1kj preleverà 1 NANO inviandolo all\'account '
          'xrb_aigakjkfa343tm3h1kj. Inoltre, !withdraw xrb_aigakjkfa343tm3h1kj preleverà l\'intero saldo '
          'inviandolo all\'account xrb_aigakjkfa343tm3h1kj.'
}

wrong_donate_text = {
    'en': 'Only number amounts are accepted.  Please resend as !donate 1234',
    'es': 'Solo se aceptan cantidades en números. Por favor vuelve a intentar con !donate 1234',
    'nl': 'Alleen bedragen met genoemde aantallen worden geaccepteerd. Gelieve opnieuw te verzenden als !donate 1234',
    'ja': '',
    'zh-t': '金額只能輸入數字。請重發 "！捐款 <金額>"。',
    'zh-s': '金额只能输入数字。请重发 “！捐款 <金额>”。',
    'fr': 'Seuls les montants en nombres sont acceptés. Veuillez réessayer avec !donate 1234',
    'pt': 'Só são aceites quantidades numéricas. Por favor volta a tentar como !donate 1234',
    'th': '',
    'de': '',
    'id': 'Hanya jumlah angka yang diterima. Harap kirim ulang sebagai !donate 1234',
    'vt': '',
    'ru': 'Принимаются только цифровые суммы. Пожалуйста, отправьте как !донат 1234',
    'sv': '',
    'it': 'Sono accettati solo importi numerici. Rinvia tramite !donate 1234'
}

large_donate_text = {
    'en': 'Your balance is only {} NANO and you tried to send {}.  Please add more NANO to your account, or lower '
          'your donation amount.',
    'es': 'Tu saldo es de solo {} NANO e intentaste enviar {}. Agrega más NANO a tu cuenta, o reduce el monto de '
          'tu donación.',
    'nl': 'Jouw saldo is slechts {} NANO en je hebt geprobeerd {} te verzenden. Voeg meer NANO toe aan '
          'jouw account of verlaag je donatiebedrag.',
    'ja': '',
    'zh-t': '您的餘額只有{} NANO，可您在嘗試發送{} NANO。請給賬戶充值，或降低您的捐款額。',
    'zh-s': '您的余额只有{} NANO，可您在尝试发送{} NANO。请给账户充值，或降低您的捐款额。',
    'fr': 'Votre solde est de {} NANO seulement, alors que vous avez essayé d\'envoyer {}. Veuillez ajouter plus '
          'de NANO à votre compte, ou diminuez le montant de votre donation. ',
    'pt': 'O teu saldo é apenas {} NANO e tentaste enviar {}. Deposita mais NANO na tua conta, '
          'ou reduz o montante da doação.',
    'th': '',
    'de': '',
    'id': 'Saldo Anda hanya {} NANO dan Anda mencoba mengirim {}. Silakan tambahkan lebih banyak NANO ke '
          'akun Anda, atau turunkan jumlah donasi Anda.',
    'vt': '',
    'ru': 'Ваш баланс только {} NANO, и вы пытались отправить {}. Пожалуйста, добавьте больше NANO в свой аккаунт '
          'или уменьшите сумму тип.',
    'sv': '',
    'it': 'Il tuo saldo è di soli {} NANO e hai provato a inviare {}. Aggiungi altri NANO al tuo '
          'account, o diminuisci l\'importo della donazione.'
}

small_donate_text = {
    'en': 'The minimum donation amount is {}.  Please update your donation amount and resend.',
    'es': 'La cantidad mínima de donación es de {} NANO. Por favor actualiza el monto de tu donación e '
          'intenta nuevamente.',
    'nl': 'Het minimale donatiebedrag is {}. Pas je donatiebedrag aan en verzend het opnieuw.',
    'ja': '',
    'zh-t': '最低捐款是{}。請改變捐款額後再嘗試。',
    'zh-s': '最低捐款是{}。请改变捐款额后再尝试。',
    'fr': 'Le montant de donation minimum est de {}. Veuillez changer le montant de votre donation et réessayer.',
    'pt': 'A quantidade mínima de doação é {}. Por favor corrige o momante e tenta novamente.',
    'th': '',
    'de': '',
    'id': 'Jumlah donasi minimum adalah {}. Harap perbarui jumlah donasi Anda dan kirim kembali.',
    'vt': '',
    'ru': 'Минимальная сумма тип составляет {}. Пожалуйста, обновите сумму тип и '
          'отправьте повторно.',
    'sv': '',
    'it': 'L\'importo minimo per la donazione è {}. Aggiorna l\'importo della donazione e rinvia.'
}

donate_text = {
    'en': 'Thank you for your generosity!  You have successfully donated {} NANO!  You can check the '
          'transaction at https://nanocrawler.cc/explorer/block/{}',
    'es': '¡Gracias por tu generosidad! Has donado {} NANO de manera exitosa. Puedes verificar esta transacción en '
          'https://nanocrawler.cc/explorer/block/{}',
    'nl': 'Bedankt voor jouw vrijgevigheid! Je hebt met succes {} NANO gedoneerd! Je kan de transactie '
          'bekijken op https://nanocrawler.cc/explorer/block/{}',
    'ja': '',
    'zh-t': '謝謝您慷慨的捐款！您成功捐款了 {} NANO！可以在https://nanocrawler.cc/explorer/block/{} 審核捐款記錄。',
    'zh-s': '谢谢您慷慨的捐款！您成功捐款了 {} NANO！可以在https://nanocrawler.cc/explorer/block/{} 审核捐款记录。',
    'fr': 'Merci beaucoup pour votre générosité! Vous avez donné {} NANO avec succès! Vous pouvez consulter la '
          'transaction à partir de https://nanocrawler.cc/explorer/block/{}',
    'pt': 'Obrigado pela tua generosidade, doaste {} NANO com sucesso! Verifica a transação em '
          'https://nanocrawler.cc/explorer/block/{}',
    'th': '',
    'de': '',
    'id': 'Terima kasih atas kedermawanan Anda! Anda telah berhasil menyumbang {} NANO! Anda dapat memeriksa '
          'transaksi di https://nanocrawler.cc/explorer/block/ {}',
    'vt': '',
    'ru': 'Благодарим вас за щедрость! Вы успешно пожертвовали {} NANO! Вы можете проверить '
          'транзакцию по адресу https://nanocrawler.cc/explorer/block/{}',
    'sv': '',
    'it': 'Grazie della tua generosità! Hai inviato con successo {} NANO! Puoi controllare la transazione su '
          'https://nanocrawler.cc/explorer/block/{}'
}

incorrect_donate_text = {
    'en': 'Incorrect syntax.  Please use the format !donate 1234',
    'es': 'Sintaxis incorrecta. Por favor usa el formato !donate 1234',
    'nl': 'Onjuiste syntax. Gebruik het formaat !donate 1234',
    'ja': '',
    'zh-t': '無效語法。請用格式 “！捐款 1234”',
    'zh-s': '无效语法。请用格式 “！捐款 1234”',
    'fr': 'Syntaxe érronée. Veuillez utiliser le format !donate 1234',
    'pt': 'A sintaxe está incorreta. Por favor utiliza o formato !donate <valor>, por exemplo: !donate 1234',
    'th': '',
    'de': '',
    'id': 'Sintaks salah. Silakan gunakan format !donate 1234',
    'vt': '',
    'ru': 'Неверный синтаксис. Пожалуйста, используйте формат !донат 1234',
    'sv': '',
    'it': 'Sintassi incorretta. Usa il formato !donate 1234'
}

balance_text = {
    'en': 'Available: {} NANO\n'
          'Pending: {} NANO',
    'es': 'Disponible: {} NANO\n'
          'Pendiente: {} NANO',
    'nl': 'Beschikbaar: {} NANO\n'
          'In afwachting: {} NANO',
    'ja': '',
    'zh-t': '現有金額： {} NANO\n'
            '等候金額： {} NANO',
    'zh-s': '现有金额： {} NANO\n'
            '等候金额： {} NANO',
    'fr': 'Disponible: {} NANO\n'
          'En attente: {} NANO',
    'pt': 'Disponível: {} NANO\n'
          'Pendente: {} NANO',
    'th': '',
    'de': '',
    'id': 'Tersedia: {} NANO\n'
          'Tertunda: {} NANO',
    'vt': '',
    'ru': 'Имеется в наличии: {} NANO\n'
          'В ожидании: {} NANO',
    'sv': '',
    'it': 'Disponibile: {} NANO\n'
          'In sospeso: {} NANO'
}

language_change_success = {
    'en': 'You have successfully updated your language.  Message you receive from the bot will now be in your new '
          'language.  If you\'d like to change back, resend the !setlanguage command with your new language!',
    'es': 'Has actualizado exitosamente tu idioma. Los mensajes que recibas del bot ahora estarán en tu nuevo idioma. '
          'Si deseas cambiarlo nuevamente, vuelve a enviar el comando !setlanguage con tu nuevo lenguaje.',
    'nl': 'U hebt uw taal met succes bijgewerkt. Het bericht dat u van de bot ontvangt, is nu in uw nieuwe taal. '
          'Als je terug wilt veranderen, stuur dan !setlanguage met je nieuwe taal!',
    'ja': '',
    'zh-t': '您成功地更新了您的語言。現在來自小費助手的信息會用您新設的語言。如果您想再改變語言，請重發 "！設語" 命令加上您的語言代名。',
    'zh-s': '您成功地更新了您的语言。现在来自小费助手的信息会用您新设的语言。如果您想改回去，请重发 “！设语” 命令加上您语言的代名。',
    'fr': 'Vous avez changé la langue avec succès. Les messages que vous recevrez du bot sont dès à présent dans '
          'votre langue. Si vous souhaitez changer de nouveau, réenvoyez la commande !setlanguage pour '
          'amender votre choix!',
    'pt': 'Atualizaste as preferências com sucesso. As mensagens que receberes de agora em diante serão na língua '
          'escolhida. Para voltar a alterar, envia novamente o comando !setlanguage com a nova língua.',
    'th': '',
    'de': '',
    'id': 'Anda telah berhasil memperbarui bahasa Anda. Pesan yang Anda terima dari bot sekarang akan dalam bahasa '
          'baru Anda. Jika Anda ingin mengubah kembali, kirim ulang perintah !setlanguage dengan bahasa baru '
          'yang Anda inginkan!',
    'vt': '',
    'ru': 'Вы успешно обновили свой язык. Сообщение, которое вы получите от бота, теперь будет на вашем новом языке. '
          'Если вы хотите вернуться обратно, отправьте команду !выборязыка с новым языком!',
    'sv': '',
    'it': 'Hai aggiornato la lingua con successo. Ora i messaggi che riceverai dal bot saranno nella tua '
          'nuova lingua. Nel caso volessi cambiarla di nuovo, rinvia il comando !setlanguage con la tua nuova lingua!'
}

missing_language = {
    'en': 'This language is not available for translations, please send !languagelist for a '
          'list of languages and codes.',
    'es': 'Este idioma no está disponible para traducciones, por favor envía !languagelist para obtener una lista '
          'de lenguajes y códigos.',
    'nl': 'Deze taal is niet beschikbaar voor vertalingen, stuur aub !languagelist voor een lijst met talen en codes.',
    'ja': '',
    'zh-t': '這個語言還沒有被翻譯，請用 "！語言" 來查看現有語言單。',
    'zh-s': '这个语言还没有被翻译，请用 “！语言” 来查看现有语言单。',
    'fr': 'Cette langue n\'est pas disponible, veuillez envoyer !languagelist pour une liste des '
          'langues et de leurs codes associés.',
    'pt': 'Essa língua não está disponível, por favor envia !languagelist para uma lista das opções e os códigos.',
    'th': '',
    'de': '',
    'id': 'Bahasa ini tidak tersedia untuk terjemahan, silakan kirim !languagelist untuk daftar bahasa dan '
          'kode yang tersedia.',
    'vt': '',
    'ru': 'Этот язык не доступен для переводов, отправьте !списокязыков для списка языков и кодов.',
    'sv': '',
    'it': 'Questa lingua non è disponibile per le traduzioni, invia !languagelist per una lista delle '
          'lingue e dei codici.'
}

language_list = (
    'Chinese Simplified - 简体中文\n'
    'Chinese Traditional - 繁體中文\n'
    'Dutch - Nederlands\n'
    'English\n'
    'French - Français\n'
    # 'German - Deutsche\n'
    'Indonesian - Indonesia\n'
    'Italian - Italiano\n'
    # 'Japanese - 日本語\n'
    'Portuguese - Português\n'
    'Russian - русский\n'
    'Spanish - Español\n'
    # 'Swedish - Svenska\n'
    # 'Thai - ไทย\n'
    # 'Vietnamese - Tiếng Việt\n'
)

balance_commands = {
    'en': ['!balance', '!bal', '!b', '/balance', '/bal', '/b'],
    'es': [
        # Users said they would prefer english commands
    ],
    'nl': [
        # Users said they would prefer english commands
    ],
    'ja': [],
    'zh-t': ['！餘額', '！餘', '！餘', '/餘額', '/餘', '/餘'],
    'zh-s': ['！余额', '！余', '/余额', '/余'],
    'fr': [
        # Users said they would prefer english commands
    ],
    'pt': ['!saldo', '/saldo'],
    'th': [],
    'de': [],
    'id': [
        # Users said they would prefer english commands
    ],
    'vt': [],
    'ru': ['!баланс', '!бал', '!б', '/баланс', '/бал', '/б'],
    'sv': [],
    'it': ['!saldo', '!sal', '!s', '/saldo', '/sal', '/s']
}

account_commands = {
    'en': ['!account', '!acc', '!a', '!deposit', '/account', '/acc', '/a', '/deposit'],
    'es': ['!cuenta', '!depósito', '/cuenta', '/depósito'],
    'nl': [
        # Users said they would prefer english commands
    ],
    'ja': [],
    'zh-t': ['！賬戶', '！賬', '！賬', '！存款', '/賬戶', '/賬', '/賬', '/存款'],
    'zh-s': ['！账户', '！账', '！存款', '/账户', '/账', '/存款'],
    'fr': [
        # Users said they would prefer english commands
    ],
    'pt': ['!conta', '/conta'],
    'th': [],
    'de': [],
    'id': [
        # Users said they would prefer english commands
    ],
    'vt': [],
    'ru': ['!аккаунт', '!акк', '!а', '!депозит', '/аккаунт', '/акк', '/а', '/депозит'],
    'sv': [],
    'it': ['!conto', '!con', '!c', '!deposita', '/conto', '/con', '/c', '/deposita']
}

help_commands = {
    'en': ['!help', '!h', '/help', '/h', '/start'],
    'es': ['!ayuda', '/ayuda', '/iniciar'],
    'nl': [
        # Users said they would prefer english commands
    ],
    'ja': [],
    'zh-t': ['！幫助', '！幫', '/幫助', '/幫', '/開始'],
    'zh-s': ['！帮助', '！帮', '/帮助', '/帮', '/开始'],
    'fr': [
        # Users said they would prefer english commands
    ],
    'pt': ['!ajuda', '/ajuda'],
    'th': [],
    'de': [],
    'id': [
        # Users said they would prefer english commands
    ],
    'vt': [],
    'ru': ['!помощь', '!п', '/помощь', '/п', '/старт'],
    'sv': [],
    'it': ['!aiuto', '/aiuto', '/inizia']
}

register_commands = {
    'en': ['!register', '!reg', '!r', '/register', '/reg', '/r'],
    'es': ['!registro', '/registro'],
    'nl': [
        # Users said they would prefer english commands
    ],
    'ja': [],
    'zh-t': ['！註冊', '！註', '！註', '/註冊', '/註', '/註'],
    'zh-s': ['！注册', '！注', '/注册', '/注'],
    'fr': [
        # Users said they would prefer english commands
    ],
    'pt': ['!registar', '/registar'],
    'th': [],
    'de': [],
    'id': [
        # Users said they would prefer english commands
    ],
    'vt': [],
    'ru': ['!регистрация', '!рег', '!р', '/регистрация', '/рег', '/р'],
    'sv': [],
    'it': ['!registra', '!reg', '/registra', '/reg']
}

withdraw_commands = {
    'en': ['!withdraw', '!w', '/withdraw', '/w'],
    'es': ['!retiro', '/retiro'],
    'nl': [
        # Users said they would prefer english commands
    ],
    'ja': [],
    'zh-t': ['！取款', '！取', '/取款', '/取'],
    'zh-s': ['！取款', '！取', '/取款', '/取'],
    'fr': [
        # Users said they would prefer english commands
    ],
    'pt': ['!retirar', '/retirar'],
    'th': [],
    'de': [],
    'id': [
        # Users said they would prefer english commands
    ],
    'vt': [],
    'ru': ['!вывод', '!в', '/вывод', '/в'],
    'sv': [],
    'it': ['!preleva', '!p', '/preleva', '/p']
}

donate_commands = {
    'en': ['!donate', '!d', '/donate', '/d'],
    'es': ['!donar', '/donar'],
    'nl': [
        # Users said they would prefer english commands
    ],
    'ja': [],
    'zh-t': ['！捐款', '！捐', '/捐款', '/捐'],
    'zh-s': ['！捐款', '！捐', '/捐款', '/捐'],
    'fr': [
        # Users said they would prefer english commands
    ],
    'pt': ['!doar', '/doar'],
    'th': [],
    'de': [],
    'id': [
        # Users said they would prefer english commands
    ],
    'vt': [],
    'ru': ['!донат', '!д', '/донат', '/д'],
    'sv': [],
    'it': ['!dona', '!d', '/dona', '/d']
}

tip_commands = {
    'en': ['!tip', '!t', '/tip', '/t'],
    'es': [
        # Users said they would prefer english commands
    ],
    'nl': [
        # Users said they would prefer english commands
    ],
    'ja': [],
    'zh-t': ['！賞', '！給小費', '/賞', '/給小費'],
    'zh-s': ['！给小费', '！赏', '/给小费', '/赏'],
    'fr': [
        # Users said they would prefer english commands
    ],
    'pt': ['!tip', '/tip'],
    'th': [],
    'de': [],
    'id': [
        # Users said they would prefer english commands
    ],
    'vt': [],
    'ru': ['!тип', '!т', '/тип', '/т'],
    'sv': [],
    'it': ['!mancia', '!m', '/mancia', '/m']
}

private_tip_commands = {
    'en': ['!privatetip', '!private', '!pt', '/privatetip', '/private', '/pt'],
    'es': [
        # Users said they would prefer english commands
    ],
    'nl': [
        # Users said they would prefer english commands
    ],
    'ja': [],
    'zh-t': ['！私賞', '！隱私', '！私', '/私賞', '/隱私', '/私'],
    'zh-s': ['！隐私小费', '！隐私', '！私', '/隐私小费', '/隐私', '/私'],
    'fr': [
        # Users said they would prefer english commands
    ],
    'pt': ['!tipprivada', '/tipprivada'],
    'th': [],
    'de': [],
    'id': [
        # Users said they would prefer english commands
    ],
    'vt': [],
    'ru': ['!приватныйтип', '!приват', '!пт', '/приватныйтип', '/приват', '/пт'],
    'sv': [],
    'it': ['!manciaprivata', '!privata', '!pt', '/manciaprivata', '/privata', '/pt']
}

language_commands = [
    '!setlanguage', '!setlang', '!sl', '/setlanguage', '/setlang', '/sl',
    '!configuraridioma', '/configuraridioma',
    '!выборязыка', '!выборязыка', '!вя', '/выборязыка', '/выборязыка', '/вя',
    '！設置語言', '！設語', '！設', '/設置語言', '/設語', '/設',
    '！设置语言', '！设语', '！设', '/设置语言', '/设语', '/设',
    '!impostalingua', '!lingua', '!il', '/impostalingua', '/lingua', '/il'
]

language_list_commands = [
    '!languages', '!langs', '!languagelist', '!l', '/languages', '/langs', '/languagelist', '/l',
    '!idiomas', '/idiomas',
    '!языки', '!языки', '!списокязыков', '!я', '/языки', '/языки', '/списокязыков', '/я',
    '！語言', '！語', '！語言單', '！語', '/語言', '/語', '/語言單', '/語',
    '！语言', '！语', '！语言单', '！语', '/语言', '/语', '/语言单', '/语',
    '!lingue', '!lingue', '!listalingue', '!l', '/lingue', '/lingue', '/listalingue', '/l'
]

language_dict = {
    'english': 'en',
    'en': 'en',
    'dutch': 'nl',
    'nederlands': 'nl',
    'nl': 'nl',
    # 'japanese': 'ja',
    # '日本語': 'ja',
    # 'ja': 'ja',
    'chinese traditional': 'zh-t',
    '繁體中文': 'zh-t',
    'zh-t': 'zh-t',
    'zh-hant': 'zh-t',
    'chinese simplified': 'zh-s',
    '简体中文': 'zh-s',
    'zh-s': 'zh-s',
    'zh-hans': 'zh-s',
    'fr': 'fr',
    'french': 'fr',
    'français': 'fr',
    # 'th': 'th',
    # 'thai': 'th',
    # 'ไทย': 'th',
    # 'de': 'de',
    # 'german': 'de',
    # 'deutsche': 'de',
    'id': 'id',
    'indonesian': 'id',
    'indonesia': 'id',
    # 'vt': 'vt',
    # 'vietnamese': 'vt',
    # 'tiếng việt': 'vt',
    'ru': 'ru',
    'russian': 'ru',
    'русский': 'ru',
    # 'sv': 'sv',
    # 'swedish': 'sv',
    # 'svenska': 'sv',
    'it': 'it',
    'italian': 'it',
    'italiano': 'it',
    'pt': 'pt',
    'portuguese': 'pt',
    'português': 'pt',
    'spanish': 'es',
    'es': 'es',
    'español': 'es'
}
