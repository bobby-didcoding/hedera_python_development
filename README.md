# [Hedera](https://hedera.com/) [Python](https://python.org) Development
This project has been developed to help you create and mint NFT's on the [Hedera](https://hedera.com/) network.

This is a [Dockerized](https://www.docker.com/) app that uses the [Hedera](https://hedera.com/) [JAVA SDK](https://docs.hedera.com/guides/docs/sdks) with a [Python wrapper](https://pypi.org/project/hedera-sdk-py/). The aim is to get you up & running with [Python](https://python.org) with minimal effort.

***
***

## Prerequisites
* [Hedera](https://hedera.com/) credentials. You can sign up [here](https://portal.hedera.com/register).
> Please use testnet credentials!
* [Docker & Docker Compose](https://docs.docker.com/desktop/)

***
***

## Repository
Clone or pull from the main branch before you begin coding. Download the zip file if you do not have a GitHub Account.
```
#option 1 - SSH
git clone git@github.com:bobby-didcoding/hedera_python_development.git .

#option 2 - Github CLI
gh repo clone bobby-didcoding/hedera_python_development .

#option 3 - HTTPS
git clone https://github.com/bobby-didcoding/hedera_python_development.git .
```

***
***

## Environment variable and secrets
1. Create a .env file from .env.template
```
copy .env.template .env
```

2. Update your new .env file with OPERATOR_ID (Public key), OPERATOR_KEY (Secret key), and HEDERA_END (testnet, previewnet or mainnet)
```
#!/usr/bin/env bash
export OPERATOR_ID=***User your credentials***
export OPERATOR_KEY=***User your credentials***
##HEDERA_ENV can be testnet, previewnet or mainnet
export HEDERA_ENV=***User your credentials***
```

***
***

## Fire up Docker:

>Note: You will need to make sure Docker is running on your machine!

Use the following command to build the docker images:
> Note: this command will create the Docker containers and configure everything you need to get started.
```
docker-compose up -d --build
```

### Access
You should now be up and running!

We are using Flask as we can run it without the need to configure components.
* The web app is running on  [http://localhost:5000](http://localhost:5000)

You can fire up a [Python](https://python.org) interpreter in your terminal with the following code.
```
docker exec -it python_app bash
python
```
Alternatively, You can open the cli using Docker desktop.

### Testing the app
Add the following into your interpreter. You should see your account HBAR balance.

```
from balance import check_balance
check_balance()
```