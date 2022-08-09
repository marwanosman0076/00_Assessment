rounds_played = 0
rounds_won = 0
rounds_lost = 0

# ***** calculate game stats *****
percent_win = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100

print()

# displays game stats with % values to the nearest whole number
print("***** Game Statistics *****")
print("win: {}, ({:.0f}%)\nloss: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lost,))

# end of game statements
print()
print("***** END GAME SUMMARY *****")
print()
print("You choose {} as your operator".format(1, 2))
print()
print("You played {} rounds".format(rounds_played))
print()
print("Won: {} \t\t Lost: {}".format(rounds_won, rounds_lost))
print()
print("!!!Thanks for playing!!!")
