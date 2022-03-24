from openpyxl import Workbook
from datetime import datetime


def simplePrint(arrayEquipes, arrayColleges):
    for equipe in arrayEquipes:
        print(equipe.effectifs)

    # On calcule la répartition du point de vue des collèges
    for college in arrayColleges:
        for equipe in arrayEquipes:
            college.repartition[equipe.nom] = equipe.effectifs[college.nom]
        print(f"{college.nom} : {college.repartition}")


def writeResultsInExcel(arrayEquipes, arrayColleges):
    wb = Workbook()

    """ Première page : par équipe """
    ws = wb.active
    ws.title = "Répartition par équipe"

    for equipe in arrayEquipes:
        ws.append([equipe.nom])
        for key, value in equipe.effectifs.items():
            if value > 0:
                ws.append([key, value])
        ws.append([])

    """ Deuxième page : par équipe """
    ws = wb.create_sheet(title="Répartition par collège")
    ws.title = "Répartition par collège"

    for college in arrayColleges:
        # D'abord calcul python
        for equipe in arrayEquipes:
            college.repartition[equipe.nom] = equipe.effectifs[college.nom]
        # Puis on enregistre
        ws.append([college.nom])
        for key, value in college.repartition.items():
            if value > 0:
                ws.append([key, value])
        # Une petite ligne vide pour que ce soit plus propre
        ws.append([])

    """ Enregistrer """
    timestamp = datetime.now().strftime("%H%M%S")
    dest_filename = f"results_{timestamp}.xlsx"
    wb.save(filename=dest_filename)