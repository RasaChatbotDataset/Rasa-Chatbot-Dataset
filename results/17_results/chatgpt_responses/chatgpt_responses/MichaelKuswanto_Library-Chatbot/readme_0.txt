REQUEST
Problem: This is a README file from a Rasa chatbot repository ## Instalasi

- Download atau melakukan git clone terhadap file github yang ada
    ```
    git clone https://github.com/MichaelKuswanto/Library-Chatbot.git
    ```

- Masuk ke dalam project yang sudah di download atau di gitclone

- Buka terminal lalu melakukan instalasi requirements (disarankan menggunakan virtual environment)
    ```
    pip install -r requirements.txt
    ```

- Jika direktori "models" kosong maka anda bisa melakukan rasa train dan rasa train nlu, jika ada maka langkah ini adalah langkah opsional
    ```
    rasa train
    rasa train nlu
    ```

## Pemakaian

- Buka aplikasi ngrok dan lakukan login dan autentikasi

- Setelah itu ketik ngrok http 5005 untuk mendapatkan link forwarding
    ```
    ngrok http 5005
    ```

- Copy link forwarding tersebut untuk di paste dalam kode file credentials.yml
    ```
    webhook_url: "<ngrok link>/webhooks/telegram/webhook"
    ```

- Ketik rasa run actions di satu terminal untuk mengaktifkan cutom actions (virtual environment disarankan)
    ```
    rasa run actions
    ```

- setelah selesai/berjalan buka terminal baru (virtual environment disarankan) lalu ketik
    ```
    rasa run
    ```

- setelah selesai/berjalan maka anda bisa bercakap dengan chatbot melalui link telegram dibawah ini:
    ```
    t.me/nrp043739_bot
    ```



## License

Project ini mengambil template dari https://github.com/shamspias/The-Rasa-Answer-Machine-GPT3.git

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    None
ngrok, Telegram,,##
ngrok, Telegram,,##
None
Databases and external services:,- ngrok,- Telegram,,##
Databases and external services:,- ngrok,- Telegram,,##
None
Databases and services:,- ngrok,- Telegram,,##
- ngrok,- Telegram,,##
None
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
ngrok, Telegram

## Purpose of external services
- ngrok: ngrok is used to create a secure tunnel to the localhost, allowing the Rasa server to be accessible from the internet. This is necessary for testing the chatbot with external services like Telegram.
- Telegram: Telegram is used as the messaging platform where users can interact with the chatbot. The bot is deployed on Telegram and communicates with users through the Telegram API.