// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.0;

contract Election{
    uint public AwlVoteCount;
    uint public BnpVoteCount;
    uint public Neutral;
    uint public TotalVotes;

    function placeVote(uint vote) public {
        if(vote == 1){
            AwlVoteCount = AwlVoteCount + 1;
        }
        if(vote== 2){
            BnpVoteCount = BnpVoteCount + 1;
        }

        else{
            Neutral = Neutral + 1;
        }
    }

    function viewVoteStatus() public view returns(uint,uint, uint,uint){
        return (AwlVoteCount,BnpVoteCount,Neutral,TotalVotes);
    }

}