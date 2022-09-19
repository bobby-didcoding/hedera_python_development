from  get_client import client, OPERATOR_ID
from hedera import AccountBalanceQuery

def check_balance():
	return AccountBalanceQuery().setAccountId(OPERATOR_ID).execute(client).hbars.toString()