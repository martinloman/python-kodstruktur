#
# Kommentarer
# --------------------------
# Kommentarer skapas med en hashtag (#)
# Kommentarer ignoreras när programmet körs.
#
# De används för att förklara komplicerad kod eller för
# att tillföra struktur i en fil.

variabel = "ett värde"  # Man kan kommentera på slutet av en rad.

# Vad en funktion gör kan med fördel kommenteras med en docstring.
# En docstring skapas med trippla enkel fnuttar på funktionens första rad.


def funktion_med_docstring(parameter_1):
    '''
    Denna kommentar visas av VSCode om man skriver kod som ska anropa funktionen
    eller om man "hovrar" funktionsnamnet med muspekaren.
    '''
    pass
