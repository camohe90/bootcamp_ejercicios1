//SPDX-License_Identifier: MIT

pragma solidity ^0.8.7;

contract SaveNumber{

  uint256 public numero;

  function SetNumber(uint256 _numero) public{
    numero = _numero;
  }
  
}