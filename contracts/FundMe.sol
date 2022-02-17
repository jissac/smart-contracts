// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
// https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

// Crowdsourcing smart contract
// Users can fund, and the admin can withdraw the funds
contract FundMe {
    using SafeMathChainlink for uint256;
    // mapping to store which address deposited how much ETH
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    // address of owner who deployed contract
    address public owner;

    // first person to deploy contract is owner
    constructor() public {
        owner = msg.sender;
    }

    // funding
    function fund() public payable {
        uint256 minUSD = 5 * 10 ** 18; // min amount 
        require(getConversionRate(msg.value) >= minUSD, "You need to spend more ETH");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    // get version of the chainlink pricefeed
    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }

    // get description from the chainlink feed
    function getDescription() public view returns (string memory) {
        AggregatorV3Interface desc = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return desc.description();
    }

    // ETH/USD rate in gwei
    function getPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }

    // ETH to USD , 10^18 zeros
    function getConversionRate(uint256 ethAmount) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmountinUSD = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountinUSD; // 10^18
    }

    // who's the owner?
    function getOwner() public view returns (address) {
        return owner;
    }

    // modifiers used to change the behavior of a fn in a declarative way
    // modifier: https://medium.com/coinmonks/solidity-tutorial-all-about-modifiers-a86cf81c14cb
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    // onlyOwner modifer will first check the condition inside it 
    // and 
    // if true, withdraw function will be executed
    function withdraw() payable onlyOwner public {
        // only want the contract admin/owner to be able to transfer
        // msg.sender.transfer(address(this).balance);
        payable(msg.sender).transfer(address(this).balance);

        // iterate through all the mappings and make them 0
        // since all the deposited amount has been withdrawn
        for (uint256 funderIndex=0; funderIndex < funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }

        // funders array initialized to 0
        funders = new address[](0);

    }
}