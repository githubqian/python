There is a file containing a listing of Basketball Players, position and their strongest statistic they record during games.

Positions = [PG, SG, SF, PF, C]
Stats = [PTS, AST, DRB, ORB, STL, BLK]

For example, the file players.txt contains these four lines:
PG - James Tyler - STL
PF - Harold Ennis - DRB
C - Hal Monroe - BLK
SF - Gerry Valdez - PTS
PF - Ferris Samuel - STL

Write a script or program that scans the file and returns the most common position amongst the players listed.

For example, if you run your program
./most_common_positions players.txt
it would print the position, most common:
PF

In the case that there are two positions which have an equal amount of players listed, return both positions.

------------

def find_most_common_position:
    fh = open ('players.txt', 'r')
    alist = []
    fh.read a newline
    \n to space
    alist.append() =[PG, PF, C,.....]
    cnt=0
    for item in alist:
        pg_count=alist.count('PG')
        Do the same for each
        ...
    Take each count and do a comparison on which is largest. Print the correct position based on this.
 