# Decentralized_Voting_Application_Dapp
This is a decentralized voting application built using web3.py, flask, tinydb and solidity

## Blockchain Voting Dapp using Flask,web3.py,solidity,ganache and Tinydb

High Level Architecture:

![image](https://github.com/shaikat010/Decentralized_Voting_Application_Dapp/assets/68814937/a889818f-637a-48e0-b8fe-0a9ab83d9580)

Abstract:
This is a voting web application built using flask web framework. It utilizes the ganache blockchain to deploy the solidity smart contract using the web3 deployment scripts. The app.py is the main flask application file that is connected to all the other endpoints. TinyDB is used here for storing the voter data when they are going to place their votes. 

There is a list called OTP that keeps all the accepted otp that are going to be given by the user when they will be giving their vote and this will work as their authentication data. On the successful submission of the votes, it will recorded in the blockchain and the otp will be appended in another list that will let the application know that the otp has already been used once. 


![image](https://github.com/shaikat010/Decentralized_Voting_Application_Dapp/assets/68814937/fdaba27e-9c6d-4ce9-b7ec-d83df07451b6)

![image](https://github.com/shaikat010/Decentralized_Voting_Application_Dapp/assets/68814937/52857e9a-7383-4dc5-98c3-02dd9dc0a7dd)
