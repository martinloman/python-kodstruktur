#
# Type hints
# --------------------------
# Python har stöd för "type hints". Det är ett sätt att ange i koden
# vilken typ av datatyper den förväntar sig.
#
# Om man använder type hints så får man mer hjälp av VSCode eftersom
# det talar om för VSCode vilka datatyper som förväntas.
#

# parameter: int talar om att parametern förväntas vara en int (ett heltal)
# -> int talar om att funktionen kommer retunera en int (ett heltal)
def square(parameter: int) -> int:
    return parameter**2


varibel = square(3)  # Nu vet VSCode att variabel är en int
