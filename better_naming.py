#
# Namngivning
# --------------------------
# Den här filen innehåller kod som är bättre namngiven
# förhoppningsvis blir det lättare att förstå koden.
#

SPEED_OF_LIGHT = 299792458


def fraction_of_lightspeed(speed):
    return speed / SPEED_OF_LIGHT


speed_of_sound = 320
fraction = fraction_of_lightspeed(speed_of_sound)

print(fraction)
