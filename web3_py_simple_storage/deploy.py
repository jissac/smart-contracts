from solcx import compile_standard, install_solc
install_solc("0.6.0")

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
solc
)
print(compiled_sol)
