print ("jste ve válce s alkarani co máme aktivovat")
valkarani = 2
lalkarani = 12
alkobrana = 0
lidvojsko = 5
lolidi = 1
obrana = 4
print ("chcete aktivovat kasárny mariňáků")
vovos = input("ano nebo ne\n")
if vovos == "ano":
    print("dobře, máte plus 5 bodů vojska")
    lidvojsko += 5
else:
    print("škoda, dostáváte 4 body obrany")
    obrana += 4
    alkobrana += 5
print("máme aktivovat autolab, ale obětujete 2 body vojska")
lab = input("ano nebo ne\n")
if lab == "ano":
    print("dobře pane")
    lolidi += 5
    valkarani += 1
    lidvojsko -= 2
else:
    print("škoda")
print("máme pustit planetární štít, ale ztratíte 2 body vojska")
sus = input("ano nebo ne\n")
if sus == "ano":
    print("dobře pane")
    lidvojsko -= 2
    obrana += 1
else:
    print("škoda")
    alkobrana += 1
body = lidvojsko + obrana + lolidi
print(f"Vy máte {body} bodů.")
body_alkarani = alkobrana + valkarani * lalkarani
print(f"Alkarani mají {body_alkarani} bodů.")
print("Pojďme na zápas!")
print("--- Shrnutí bodů ---")
print(f"Vaše body: {body}")
print(f"Body alkaranů: {body_alkarani}")
if body > body_alkarani:
    print("Výhra! Zotročili jste alkarany a získali jejich kolonii.")
elif body < body_alkarani:
    print("Prohra! Alkarani ovládli vaši kolonii.")
else:
    print("Remíza! Nikdo nezvítězil, válka pokračuje.")
