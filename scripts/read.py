from brownie import SaveNumber

def read():
    savenumber = SaveNumber[-1]
    print(f"El numero almacenado en el contrato inteligente es {savenumber.numero()}")

def main():
    read()