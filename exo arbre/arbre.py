data = [{ 'id': 1, 'nom': 'Philippe', 'age': 40, 'emploi': 'Coursier' },{ 'id': 2, 'nom': 'Sophie', 'age': 31, 'emploi': 'Ingénieur' },{ 'id': 3, 'nom': 'Antoine', 'age': 35, 'emploi': 'Avocat' },{ 'id': 4, 'nom': 'Emma', 'age': 24, 'emploi': 'Journaliste' },{ 'id': 5, 'nom': 'Jean', 'age': 52, 'emploi': 'Médecin' },{ 'id': 6, 'nom': 'Camille', 'age': 29, 'emploi': 'Professeur' },{ 'id': 7, 'nom': 'Lucie', 'age': 41, 'emploi': 'Designer' },{ 'id': 8, 'nom': 'Pierre', 'age': 45, 'emploi': 'Architecte' },{ 'id': 9, 'nom': 'Julie', 'age': 33, 'emploi': 'Acteur' },{ 'id': 10, 'nom': 'Maxime', 'age': 27, 'emploi': 'Comptable' },{ 'id': 11, 'nom': 'Marie', 'age': 48, 'emploi': 'Policier' },{ 'id': 12, 'nom': 'Thomas', 'age': 31, 'emploi': 'Étudiant' },{ 'id': 13, 'nom': 'Anne', 'age': 36, 'emploi': 'Jardinier' },{ 'id': 14, 'nom': 'Romain', 'age': 39, 'emploi': 'Vendeur' },{ 'id': 15, 'nom': 'Aurélie', 'age': 26, 'emploi': 'Infirmière' },{ 'id': 16, 'nom': 'Nicolas', 'age': 43, 'emploi': 'Entrepreneur' },{ 'id': 17, 'nom': 'Caroline', 'age': 30, 'emploi': 'Consultant' },{ 'id': 18, 'nom': 'Alexandre', 'age': 37, 'emploi': 'Pharmacien' },{ 'id': 19, 'nom': 'Élise', 'age': 25, 'emploi': 'Graphiste' },{ 'id': 20, 'nom': 'Vincent', 'age': 42, 'emploi': 'Ingénieur' }]
def selection_profil_sup_30(data):
    result = []
    for profil in data:
        if profil['age'] > 30:
            result.append(profil)
    return result

def selection_profil_techno(data):
    result=[]
    for profil in data:
        if profil['emploi']=='Ingénieur' or profil['emploi']=='Designer' or profil['emploi']=='Graphiste':
            result.append(profil)
    return result

def selection_profil_sup_30_techno(data):
    techno_profil = selection_profil_techno(data)
    sup_30_techno_profil = selection_profil_sup_30(techno_profil)
    return sup_30_techno_profil
  
result = selection_profil_sup_30_techno(data)
print(result)