import modi_plus
bundle = modi_plus. MODIPlus()
bundle.modules

dial = bundle.dials[0]
print(dial.turn)
print(dial.turn)
turn = dial.turn
print("current turn:", turn)

while True:
    print(dial. turn, end="\r")
    if dial.turn < 1:
        break

turn = dial.turn
print("Current turn:", turn)