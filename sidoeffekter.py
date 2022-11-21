#
# Sidoeffekter
# --------------------------
# Sidoeffekter är saker som händer (ändras) utanför en funktions
# lokala scope. Exempel kan vara att att värden på globala variabler ändras,
# eller att information hämtas eller skrivs från en fil.
#
# Sidoeffekter behöver inte vara dåliga MEN, om man har kod med
# många sidoeffekter så kan det bli svårt att förstå alla
# och hålla alla sidoeffekter i huvudet. Då blir det svårt att
# första, felsöka och vidareutveckla sin kod.
player_health = 10

# Den här funktionen ändrar värdet på den globala variabeln player_health.
# Det kan vara ok men om det sker på många ställen kan det bli svårt att ha
# översikt.


def trap():
    trap_damage = 2
    global player_health
    player_health = player_health - trap_damage


def poison():
    poison_damage = 3
    global player_health
    player_health = player_health - poison_damage


def virus():
    virus_damage = 3
    global player_health
    player_health = player_health - virus_damage


def starvation():
    starvation_damage = 8
    global player_health
    player_health = player_health - starvation_damage


# -------------------------------------------------
# Ett bättre sätt
#
# Försök att bara ändra på den globala variabeln
# på ett ställe. T.ex. genom att införa en funktion
# som gör just det.
#
# Det här gör det också enklare att i framtiden ändra
# på hur player_health modelleras.
# -------------------------------------------------

def reduce_player_health(damage):
    global player_health
    player_health = player_health - damage


def trap():
    trap_damage = 2
    reduce_player_health(trap_damage)


def poison():
    poison_damage = 3
    reduce_player_health(poison_damage)


def virus():
    virus_damage = 3
    reduce_player_health(virus_damage)


def starvation():
    starvation_damage = 8
    reduce_player_health(starvation_damage)
