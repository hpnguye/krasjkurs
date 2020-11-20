
poengstatus = {}
hendelseslog = [{}]


"""
poengstatus = {"Vegard" : 100, "Mathias" : 50}
hendelseslog = [{Vegard : [("holdt kræsjkurs", 50), ("var slem", - 10)]}, {"Mathias" : [("holdt kræsjkurs", 50)]}]
"""

def reg_incident(navn, beskrivelse, poeng):
    """
    Oppdaterer poengstatusen og hendelsesloggen. 
    """

    if navn in poengstatus:
        poengstatus[navn] += poeng
    else:
        poengstatus[navn] = poeng
    for i, hendelse in enumerate(hendelseslog):
        if navn in hendelse:
            hendelseslog[i][navn].append((beskrivelse, poeng))
        else:
            hendelseslog[i][navn] = [(beskrivelse, poeng)]


def is_nice(navn):
    """
    Returnerer om en person er nice (har mer enn 0 poeng).
    """
    try:
        return poengstatus[navn] > 0
    except:
        return None
    
def status_all():
    """
    Returnerer en dictionary med navn og om de er snille eller ikke
    {"Mathias" : True, "Vegard" : True}
    """
    status = {}
    for key, value in poengstatus.items():
        status[key] = value > 0
    return status


def assign_presents(gaveliste, available_coal):
    presanger = {}
    slemme = []
    slemme_count = 0
    for name, nice in status_all().items():
        if nice:
            presanger[name] = gaveliste.pop()
        else:
            slemme.append(navn)
            slemme_count += 1
    vekt_kull = available_coal / slemme_count
    for name in slemme:
        presanger[name] = (0,'Kull', vekt_kull, '')

    return presanger

def person_log(navn):
    for hendelse in hendelseslog:
        if navn in hendelse:
            return hendelse[navn]

def delete_person(navn):
    status_all[navn] = None
    for i, hendelse in enumerate(hendelseslog):
        if navn in hendelse:
            hendelseslog[i] = None


def check_assignment():
    presents = False
    reg_person = True
    kull = True
    gaver = assign_presents()
    if len(gaver) == len(hendelseslog):
        presents = True

    for navn in status_all.keys():
        if navn not in gaver:
            reg_person = False
            break

    for name, gift in gaver.items():
        if not (gaver[name][1] == "Kull" and is_nice(name)):
            kull = False
            break
    if not presents and reg_person and kull:
        raise ValueError
    


