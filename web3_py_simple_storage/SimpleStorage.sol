// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage {

    // type, visibility, variable name
    uint256 favNumber; // will get initialized to 0

    struct People {
        uint256 favNumber;
        string name;
    }

    People[] public people;

    // mapping dictionary like data structure, 1 value per key
    mapping(string => uint256) public nameToFavNumber;

    function store(uint256 _favNumber) public returns(uint256) {
        favNumber = _favNumber;
        return _favNumber;
    }
    // view - view some state off the blockchain
    function retrieve() public view returns(uint256) {
        return favNumber;
    }

    // memory: data will only be stored during the execution of the function
    // storage: data persists after execution
    // string is an array of bytes in solidity
    function addPerson(string memory _name, uint256 _favNumber) public {
        // adds to people array and to mapping
        people.push(People({favNumber: _favNumber, name: _name}));
        nameToFavNumber[_name] = _favNumber;
    }

}