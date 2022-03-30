# smart-contracts

## 0. intro
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

## 1. high level overview
**Ethereum Transaction On a Live Blockchain**
- Gas: unit of computational measure. Every transaction that happens on-chain pays a "gas fee" to node operators
  - any time you change state of the blockchain, pay gas
  - Wei is smallest denomination of Ether Wei -> Gwei -> Ether
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

**How Blockchain works/whats going on Inside the Blockchain**
- Blockchain Demo: 
  - https://andersbrownworth.com/blockchain/

**Signing and Verifying a Transaction**
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

**Concepts**
- In essence, the blockchain is a decentralized database. Enable smart contracts and the blockchain can do computations in a decentralized manner.

- Consensus: mechanism used to agree on the state of the blockchain
  - 1. Chain Selection rule (which blockchain is the true one)
    - Nakamoto Consensus: used by Bitcoin and Ethereum combination of proof-of-work and longest chain rule
  - 2. Sybil Resistance mechanism
    - proof-of-work: defines who is the block author
    - blockchains ability to defend against someone creating fake/malicious nodes 

- proof of work (PoW)
  - Mining: a single node has to go thru computational expensive process to figure out correct nonce, etc
    - no matter how many pseduo nodes you make, still have to go thru the computation
    - block time: how much time between blocks being mined
    - miners get paid in transaction fees and from the block rewards
      - gas fees are paid by whoever makes the transaction
  - uses a lot of energy

- Sybil Attack: a signle node or user creates pseudo accounts to try to influence a network, affect the decentrality by pretending to be many people/nodes 
- 51% attack: blockchains agree that the longest chain is the valid one, as long as it matches up with 51% of the network. If someone gains majority they can fork the longest chain and create new blockchain.
- Longest Chain Rule: the blockchain that's the longest is the one that's used 

- proof of stake (PoS)
  - proof of stake nodes put up collateral as a sybil resistance mechanism
  - validators (miners from proof of work)
  - nodes are randomly chosen to propose a new block.
    - validators then verify if proposal is honest
  - Pros: great Sybil resistance mechanism, much less computationally expensive
  - Cons: usually considered slightly less decentralized due to staking.
    - how decentralized is decentralized enough

- Scalability: how to prevent gas prices skyrocketing when more people are using the blockchain?
  - only certain number of transactions can be fit in a block
  - Sharding: a blockchain of blockchains
    - main chain coordinates everything, 
    - Layer 1: Base layer blockchain implementation (BTC, ETH, AVAX)
    - Layer 2: Any application built on top of Layer 1 (LINK)
    - Rollups: rollups that "rollup" their transactions into main chain
      - security of main chain, but fast transactions by freeing up blockchain computation

**Solidity**
Solidity: https://docs.soliditylang.org/en/v0.8.6/index.html
Remix: https://remix.ethereum.org/
1. Define solidity version
2. contract (like a class, defines functions of project)
3. Types and declaring variables
4. functions: self contained code that executes some task 
5. View and Pure are non-state changing functions
6. Structs
7. Arrays
8. memory vs storage
9. mappings
10. SPDX License
11. Injected Web3: taking sol source code and injecting metamask into browser

## 2. projects
**Storage Factory**
(Contract that stores and display strings and numbers)            
`SimpleStorage.sol`, `StorageFactory.sol`
- Can call a contract from another contract
- Anytime you do that you need
  - Address
  - ABI: Application Binary Interface

**Fund Me**
(Crowdsourcing contract that accepts payment from accounts and enables account owner to withdraw donated funds)           
`FundMe.sol`    
- payable enables payment on ETH
- msg.sender and msg.value are key words in every transaction
- blockchains are deterministic (all nodes have to agree on same value)
  - can't do API calls, random num gen bc each node will have a diff value (non-deterministic)
- Oracles allow data from the real world to be used by blockchains
- Decimals dont work in solidity
- Interfaces compile down to an ABI
- The ABI tells solidity and other programming languages how it can interact with another contract
  - always need an ABI to interact w a contract
- libraries are similar to contracts except that they are isolated code, their purpose is that they are deployed only once at a specific address and their code is reused
- Using keyword: using a for b - can be used to attach library functions (from library a) to any type (b) in the context of a contract
- https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol
- modifiers: https://medium.com/coinmonks/solidity-tutorial-all-about-modifiers-a86cf81c14cb


**Web3 python Simple Storage**
( Web3 python version of previous Simple Storage smart contract)          
`/web3_py_simple_storage`

- Limitations of Remix
  - Can't integrate other parts of a project
  - Can't save files locally w/out a plugin
  - doesn't have python :)

- web3.py and Brownie for smart contract dev in Python!
- 2 things you always need:
  - contract address
  - contract ABI
- Simulate and deploy contract to blockchain using Ganache or ganache-cli
- Deploy to a testnet using Infura RPC URL, Alchemy, etc
- Find out chain ids: https://chainlist.org/

**Brownie Simple Storage**


## references:
full stack blockchain development
- https://github.com/smartcontractkit/full-blockchain-solidity-course-py
- https://www.youtube.com/watch?v=M576WGiDBdQ
- https://www.youtube.com/watch?v=M576WGiDBdQ