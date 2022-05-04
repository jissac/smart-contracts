from brownie import accounts, config, SimpleStorage
import os

def deploy_simple_storage():
    # load account 3 ways, 
    # 1. test account 2. eth account thru cli 3. using venv

    account = accounts[0]
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {f"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

    # account = accounts.load("smart-contract-account")
    # print(account)

    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallet"]["from_key"]) # more secure version of above
    # print(account)


def main():
    deploy_simple_storage()
    print("Hello from brownie")