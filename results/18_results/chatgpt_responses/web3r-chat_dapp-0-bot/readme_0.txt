REQUEST
Problem: This is a README file from a Rasa chatbot repository # dapp-0-bot

Our first Rasa chatbot for the Internet Computer.

The live deployment can be found at https://web3r.chat

The full application consists of 3 GitHub repositories:
1. [dapp-0](https://github.com/web3r-chat/dapp-0)
2. [dapp-0-django](https://github.com/web3r-chat/dapp-0-django)
3. [dapp-0-bot](https://github.com/web3r-chat/dapp-0-bot)

## Git

```bash
git clone git@github.com:web3r-chat/dapp-0-bot.git
cd dapp-0-bot
```

## Internet Identity

The action server makes authenticated calls to canister_motoko, using a dedicated internet identity.

- We used dfx to create the [dfx identity](https://smartcontracts.org/docs/developers-guide/cli-reference/dfx-identity.html) `dapp-0-bot-action-server`,  with the command:

  ```bash
  dfx identity new dapp-0-bot-action-server
  
  # The private key is stored in the file:
  # ~/.config/dfx/identity/dapp-0-bot-action-server/identity.pem
  ```

- We used dfx to specify that this identity uses our regular cycles wallet, with the commands:

  ```bash
  # Issue these commands from the web3r_chat repository
  dfx identity --network ic use dapp-0-bot-action-server
  dfx identity --network ic set-wallet aaaaa-aaaaa-aaaaa-aaaaa-aaa  # Replace with your wallet id !
  
  # Verify it is all ok
  dfx identity --network ic get-wallet 
  
  # Reset identity to default
  dfx identity --network ic use default
  ```

- We base64 encoded the pem file into a single line with the command:

  ```bash
  base64 -w 0 ~/.config/dfx/identity/dapp-0-bot-action-server/identity.pem
  ```

- We pass this value into our action server via the environment variable `BOT_0_ACTION_SERVER_IC_IDENTITY_PEM_ENCODED`

  - Locally, store it in `.env`

- We extract it in the file `actions/settings.py`

- We figured out the principal of this identity by calling the `whoami` method.

  - We updated the value for `_bot_0_action_server_principal` in the smart contract of the  `dapp-0` repository:

    ```javascript
    # file: dapp-0/src/backend/motoko/auth.mo
    
    public func is_django_server(p: Principal) : Result.Result<(), Http.StatusCode> {
        ...
        let _bot_0_action_server_principal : Principal = Principal.fromText("xxxx-xxxx-...");
    	...
    };
    ```

- Now we can use use [ic-py](https://github.com/rocklabs-io/ic-py) to make authenticated calls from the action server's python code to the protected APIs of the smart contract that is running in the motoko_canister on the Internet Computer.

## Secrets in `.env`

Create a `.env` file that looks like this:

```bash
#
# Only needed when deploying to Digital Ocean
# Access token is used to authenticate doctl with: make doctl-auth-init 
DIGITALOCEAN_ACCESS_TOKEN="..."

#
# JWT protection for socketio channel, using HS256
# Value must be equal to the SECRET_JWT_KEY value of the django_server
SECRET_JWT_KEY="..."
JWT_METHOD="HS256"

#
# Action server connection to local services
IC_NETWORK_URL="http://localhost:8000"
CANISTER_MOTOKO_ID="..."
CANISTER_MOTOKO_CANDID_UI="http://localhost:8000?canisterId=...&id=..."

#
# Action server internet identity
BOT_0_ACTION_SERVER_IC_IDENTITY_PEM_ENCODED="..."
```



To set the environment variables in your shell:

```bash
export $(cat .env | grep -v '#' | xargs)
```



## Conda

[Download MiniConda](https://docs.conda.io/en/latest/miniconda.html#linux-installers) and then install it:

```bash
bash Miniconda3-xxxxx.sh
```

Create a conda environment with Python:

Note: we use python 3.8, because the rasa-sdk is still at python 3.8

```bash
conda create --name dapp-0-bot python=3.8
conda activate dapp-0-bot

pip install --upgrade pip
pip install -r requirements-dev.txt
```



## Train the bot

```bash
rasa train --domain domain
```



## Test the bot

```bash
rasa test --domain domain
```

This will run [end-to-end testing](https://rasa.com/docs/rasa/user-guide/testing-your-assistant/#end-to-end-testing) on the conversations in `tests/test_stories.yml`. All tests must pass.



## Run the Rasa Server

```bash
# Set the environment variables in your shell
export $(cat .env | grep -v '#' | xargs)

# Run the rasa server
rasa run [--debug]
```



## Run the Action Server

```bash
# Set the environment variables in your shell
export $(cat .env | grep -v '#' | xargs)

# Run the action server
rasa run actions [--debug]
```



## Smoketest

```bash
make smoketest
```

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    dfx identity, Digital Ocean, JWT, ic-py, rasa-sdk,,##
- dfx identity, Digital Ocean, JWT, ic-py,,##
Databases and services:,- Internet Identity,- canister_motoko,- ic-py,- Digital Ocean,- JWT,- socketio,- rasa,- conda
Databases and services: ,- Internet Identity,- dfx,- ic-py,- Digital Ocean,- JWT,- socketio,- rasa,- conda,,##
- dfx identity, Digital Ocean, JWT, ic-py,,##
- dfx identity, Digital Ocean, JWT, ic-py,,##
- dfx identity, Digital Ocean, JWT, ic-py,,##
Databases and services:,- Internet Identity,- canister_motoko,- ic-py,- Digital Ocean,- JWT,,##
Databases and services: dfx identity, cycles wallet, ic-py, Digital Ocean, JWT, socketio, Internet Computer, MiniConda, rasa-sdk,,##
- canister_motoko,- Digital Ocean,- Internet Identity,- ic-py,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Internet Identity, canister_motoko, ic-py, Digital Ocean, JWT, socketio, rasa, conda

## Purpose of external services

- **Internet Identity**: Used for authenticated calls to canister_motoko.
- **canister_motoko**: A smart contract running on the Internet Computer.
- **ic-py**: A Python library to interact with the Internet Computer.
- **Digital Ocean**: Used for deployment.
- **JWT**: Used for JWT protection for the socketio channel.
- **socketio**: Used for real-time communication.
- **rasa**: The framework used to build the chatbot.
- **conda**: Used to manage the Python environment.