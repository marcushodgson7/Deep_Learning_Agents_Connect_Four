from simulate import simulate_both

"""
This project was done by myself (Marcus Hodgson, msh92) I am using MCTS and Alpha-Beta Pruning to simulate games between the two agents. The win percentage for MCTS is roughly 90%
while the win percentage for the Alpha Beta Pruning with a depth of 6 is 10%.
"""

def main():

    player1 = 0
    player2 = 0

    for iter in range(100):
        sim = simulate_both()
        if sim == 1:
            player1+=1
        elif sim == 2:
            player2+=1
    print('MCTS won ', player1, ' times out of 100\n')
    print('Alpha Beta Pruning won ', player2, ' times out of 100\n')


if __name__ == '__main__':
    main()