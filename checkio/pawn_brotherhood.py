def safe_pawns(pawns):
    pawns_indexes = set([(int(p[1]) - 1, ord(p[0]) - 97) for p in pawns])

    count = 0
    print pawns_indexes
    for row, col in pawns_indexes:
        is_safe = ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
        if is_safe:
            count += 1

    return count

print 'Using safe_pawns:'

print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})

print safe_pawns({"a1","a2","a3","a4","h1","h2","h3","h4"})


def safe_pawns2(pawns):

    covered = set()

    for pawn in pawns:
        position = str(int(pawn[1])+1)
        covered.add((chr(ord(pawn[0])-1)) + position)
        covered.add((chr(ord(pawn[0])+1)) + position)

    print covered

    return int(len(covered & pawns))

print 'Using safe_pawns2:'

print safe_pawns2({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
print safe_pawns2({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})

print safe_pawns2({"a1","a2","a3","a4","h1","h2","h3","h4"})
