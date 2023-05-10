
async def main():
    votes = [1, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    n = 10
    candidates = 2
    vote_instance = VoteInstance(n, candidates)
    for i in range(n):
        await vote_instance.add_vote(Voter(votes[i]))
    await vote_instance.add_vote(Voter(1))
    result = await vote_instance.get_result()
    print(result)

mpc.start()
mpc.run(main())
