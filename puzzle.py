from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Rules of game states a person is a knight or knave
    Or(AKnight, AKnave),

    # A says "I am both a knight and a knave."
    # the person is a knight if and only if what they said was true
    Biconditional(AKnight, And(AKnight, AKnave)),
    # the person is a knave if and only if what they said was not true
    Biconditional(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Rules of game states a person is a knight or knave
    Or(AKnight, AKnave), Or(BKnight, BKnave),

    # A says "We are both knaves."
    # the person is a knight if and only if what they said was true
    Biconditional(AKnight, And(AKnave, BKnave)),
    # the person is a knave if and only if what they said was not true
    Biconditional(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Rules of game states a person is a knight or knave
    Or(AKnight, AKnave), Or(BKnight, BKnave),

    # A says "We are the same kind."
    # the person is a knight if and only if what they said was true
    Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    # the person is a knave if and only if what they said was not true
    Biconditional(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),

    # B says "We are of different kinds."
    # the person is a knight if and only if what they said was true
    Biconditional(BKnight, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    # the person is a knave if and only if what they said was not true
    Biconditional(BKnave, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Rules of game states a person is a knight or knave
    Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Or(
        # If A said "I am a knight"
        And(
            Biconditional(AKnight, AKnight),
            Biconditional(AKnave, Not(AKnight))
        ),
        # If A said "I am a knave"
        And(
            Biconditional(AKnight, AKnave),
            Biconditional(AKnave, Not(AKnave))
        )
    ),

    # B says "A said 'I am a knave'."
    # the person is a knight if and only if what they said was true
    Biconditional(BKnight, And(Biconditional(AKnight, AKnave), Biconditional(AKnave, Not(AKnave)))),
    # the person is a knave if and only if what they said was not true
    Biconditional(BKnave, Not(And(Biconditional(AKnight, AKnave), Biconditional(AKnave, Not(AKnave))))),

    # B says "C is a knave."
    # the person is a knight if and only if what they said was true
    Biconditional(BKnight, CKnave),
    # the person is a knave if and only if what they said was not true
    Biconditional(BKnave, Not(CKnave)),

    # C says "A is a knight."
    # the person is a knight if and only if what they said was true
    Biconditional(CKnight, AKnight),
    # the person is a knave if and only if what they said was not true
    Biconditional(CKnave, Not(AKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
