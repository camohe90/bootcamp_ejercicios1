from brownie import config, network, accounts, SaveNumber

def main():
    account = accounts.add(config["wallets"]["from_key"])
    print(f"Vamos a desplegar usando la cuenta {account}")

    savenumber = SaveNumber.deploy({"from":account})
    return savenumber

