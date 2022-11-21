#
# Namngivning
# --------------------------
# "magic numbers" är tal som dyker upp i kod men som inte
# förklaras vad de betyder.
#


choice = int(input("Välj från menyn 1-3 -> "))

if choice == 1:  # vad betyer den här ettan?
    pass
elif choice == 2:
    pass
elif choice == 3:
    pass
else:
    pass

# För att undvika "magic numbers" så kan man använda konstanta
# variabler med beskrivande namn.
MENU_OPTION_CREATE_PLAYER = 1
MENU_OPTION_START_GAME = 2
MENU_OPTION_QUIT_GAME = 3

if choice == MENU_OPTION_CREATE_PLAYER:
    pass
elif choice == MENU_OPTION_START_GAME:
    pass
elif choice == MENU_OPTION_QUIT_GAME:
    pass
else:
    pass
