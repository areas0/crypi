from mpyc.runtime import mpc
from typing import List

secint = mpc.SecInt(32)

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(
                *args, **kwargs
            )

        return cls._instances[cls]

class Voter:
    def __init__(self) -> None:
        self.id = mpc.random.randint(secint, 0, 2**32)
        self.votee = -1

    def vote(self, vote: int):
        self.votee = vote

class VoteInstance(metaclass=Singleton):
    def __init__(self, n, candidates) -> None:
        self.votes :  List[secint] =  mpc.seclist([0] * candidates, secint)
        self.voters : List[(secint)]= [mpc.random_bits(secint, 32) for _ in range(n)]
        self.n : int = n # number of voters
        self.candidates : int= candidates # number of possibilities
        self.accept = True

    def add_vote(self, vote : Voter) -> None:
        # integrity check on number of votes and voters
        # sum the votes
        # s = mpc.seclist.count(self.votes, 0)
        # if not mpc.lt(s, self.n):
        #     return mpc.SecureInteger(0)
        # check that the voter is in the list
        # add the vote
        if not self.accept:
            return

        self.votes[vote.votee] += 1
        self.voters

    async def get_result(self) -> List[secint]:
        # get each total of vote per candidate in the vector
        # get the result
        result = []
        self.accept = False
        for i in range(len(self.votes)):
            result.append((i, await mpc.output(self.votes[i])))
        return result

global vote_instance
vote_instance = VoteInstance(8, 4)
