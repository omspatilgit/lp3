// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint256) private balances;   // balance of each customer (in wei)

    function deposit() public payable {
        require(msg.value > 0, "Send some ether");
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) public {       // amount in wei
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;              // update first, then send
        payable(msg.sender).transfer(amount);
    }

    function showBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
