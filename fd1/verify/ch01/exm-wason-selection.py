"""exm-wason-selection (Section 1.4): exactly the 6 and the green card can falsify
"if a card shows an even number, its other side is red"."""
QUOTED = {"cards to turn": {"6", "green"}}

def falsifies(number, colour):
    return number % 2 == 0 and colour != "red"

hidden_numbers = range(0, 20)          # any whole number; parity is all that matters
colours = ("red", "green")
cards = {"6": [(6, c) for c in colours],
         "7": [(7, c) for c in colours],
         "red": [(n, "red") for n in hidden_numbers],
         "green": [(n, "green") for n in hidden_numbers]}
must_turn = {name for name, worlds in cards.items() if any(falsifies(n, c) for n, c in worlds)}
assert must_turn == QUOTED["cards to turn"], must_turn
print("exm-wason-selection: checks")
