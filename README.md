# smart-contracts
full stack blockchain development
- https://github.com/smartcontractkit/full-blockchain-solidity-course-py
- https://www.youtube.com/watch?v=M576WGiDBdQ


## intro: 
Smart contracts and blockchains enable:
1. Decentralization
    - No single entity to control. Independent node operators run the network.
    - Node: single instance in a decentralized network

2. Transparency and Flexibility
    - Pseudo-anonymous

3. Speed and Efficiency
    - 10 min to couple of seconds

4. Security and Immutability
    - Blockchains can't be altered

5. Counterparty Risk Removal
    - Math based agreements remove conflict of interest in traditional contracts

6. Trust minimized agreements

7. DAOs - Decentralized Autonomous Organizations
    - Governance on chain, org that lives in the network

## high level overview:
- Gas: unit of computational measure. Every transaction that happens on-chain pays a "gas fee" to node operators
  - any time you change state of the blockchain, pay gas
  - Gas Price: how much it costs per unit of gas
  - Gas Limit: Max amount of gas in a transaction
  - Transaction Fee: Gas Used * Gas Price
  - Gas Price is based off the demand of the blockchain
    - The more people want to make transactions, the higher the gas price, and higher the transaction fee
  - Hash: a unique fixed length string, meant to identify a piece of data. They are created by placing said data into a "hash function"
    - Eth uses Keccak256 hashing algorithm
  - Genesis block: first block in blockchain
  - Mining: process of finding the "solution" to the blockchain "problem" (eg hash that starts w/ 4 zeros)
    - Nodes get paid for mining blocks, majority rules

- Blockchain Demo: 
  - https://andersbrownworth.com/blockchain/

- https://andersbrownworth.com/blockchain/public-private-keys/keys 
- Private key: secret password for transactions
  - use to digitally sign transactions
- Public key: Elliptic Curve Digital Signature Algorithm (used by Bitcoin and Ethereum) to generate a public key
  - derived from private key. Anyone can see it and use it to verify that a transaction came from you.

- Signatures:
  - Use private key to sign / generate a message signature
    - somone can't derive private key from message signature
    - can verify signature with public key

- Signing a transaction: a one way process. Someone with a private key signs a transaction by their private key being hashed with their transaction data. Anyone can verify this new transaction hash with your public key.

- Metamask address is actually a piece of the public key!
  - public + private key and take last 20 bytes



