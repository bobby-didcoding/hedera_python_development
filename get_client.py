import os
from hedera import Client, AccountId, PrivateKey

OPERATOR_ID = AccountId.fromString(os.environ["OPERATOR_ID"])
OPERATOR_KEY = PrivateKey.fromString(os.environ["OPERATOR_KEY"])

client_dict = {
	"testnet": Client.forTestnet(),
	"previewnet": Client.forPreviewnet(),
	"testnet": Client.forMainnet(),
}

try:
	client = client_dict[os.environ["HEDERA_ENV"].lower()]
	client.setOperator(OPERATOR_ID, OPERATOR_KEY)
except KeyError:
	client = None

