#
# Moduler
# --------------------------
# Moduler är filer med kod.
# Du kan lägga kod i en fil och sedan importera den modulen i en
# annan fil och anropa kod (variabler och ).
#
# Moduler är ett bra sätt att struktera kod. Det är lämpligt att
# skapa moduler för att inte ha all kod i samma fil, då blir det ofta
# svårt med överblicken.
#
# Att dela upp kod i moduler kan ibland kräva att man struktrerar om sin
# kod. Om så är fallet så är det ofta till det bättre. Det tvingar en att
# strukturera sin kod på ett bättre sätt.

# Här importeras den egenskapade modulen modul_exempel som ligger
# i filen modul_exempel.py
import modul_exempel

# Här anropas en funktion i den importerade modulen.
hypothenuse = modul_exempel.pythagoras(2, 3)

# Här används värdet på en variabel i en modul.
vinkelsumma = modul_exempel.TRIANGLE_ANGLE_SUM
