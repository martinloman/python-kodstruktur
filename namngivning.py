#
# Namngivning
# --------------------------
# Namngivning är inte alltid lätt men gör din kod lättare att:
#   - förstå (för både dig och andra)
#   - underhålla, kod som är lätt att förstå har färre buggar
#   - felsöka, med tydliga namn blir det tydligare om något blir fel
#

# variabler namnges med små bokstäver
variabel = 1337

# om variabler ska innehålla flera ord, för att vara
# beskrivande, delar man va dem med _ (understreck).
# Denna metod kallas "snake case" för att det ser ut som en ringlande orm.
en_variabel_med_längre_namn = "ok"

# en variabel som innehåller ett boolskt värde namnges med inledande is_
is_player_alive = True

# konstanta värden man vill använda i sin kod bör få
# beskrivande namn. Då använder man bara stora bokstäver.
KONSTANT = 7
EN_LÄNGRE_KONSTANT = 8

# funktioner namnges som variabler,
# även inparametrar namnges som variabler.


def funktion(parameter_1, parameter_2):
    return


def funktion_med_långt_namn(parameter_1, parameter_2):
    return
