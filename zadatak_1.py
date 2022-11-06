developers = { 

  'Marshal': ['Company website', 'Animal recognition', 'Fashion store website'],
  'Ted': ['Plants watering system', 'WHAT', 'Animal recognition', 'Food recognition'],
  'Monica': ['NEXT website', 'Fashion store website'], 
  'Phoebe': ['WHAT', 'Company website', 'NEXT website']

  }

# projects = {
#     'Company website' : ['Marshal, Phoebe'],
#     'Animal recognition' : ['Marshal', 'Ted'],
#     'Fashion store website' : ['Marshal', 'Monica'],
#     'Plants watering system' : ['Ted'],
#     'WHAT' : ['Ted', 'Phoebe'],  
#     'NEXT website' : ['Monica','Phoebe'],
# }


projektilista = []
for developer in developers:
    projektilista+= developers[developer]

projektiset = set(projektilista)

projects = {}

for project in projektiset:
  projects[project] = []
  for developer in developers:
    if project in developers[developer]:
      projects[project].append(developer)

print (projects)


# c) izmijeni ime svakog projekta u projektislista kao bixbix_ime

# def dodajpref (list, prefix):
#     newlist = []
#     for project in list:
#         newlist.append('_'.join([prefix,project]))
#     return newlist

# prefix = 'BIXBIT'
# dodaobixbix = dodajpref(projektiset, prefix)
# print(dodaobixbix)

# c) sa lambdom i map

print (list(map(lambda project:'BIXBIT_'+project,projektilista)))


# d) 

def dodajdev (developers, newdev):
  developers.update(newdev)
  devsum = len(developers)
  print (developers, 'OVO JE BROJ DEVELOPERA: ', devsum)


#driver code

dodajdev (developers, {'mark':['BIXBIT','3gProxy']})

# e) DODAJ ZARADU i vrijeme

# def alterdict(developers, newspecs):

def hmoney (pname,hours,money):
  for developer in developers:
    if pname in developers[developer]:
      developers[developer]= [(pname,hours,money)]
      # .........

hmoney ('Company website', '150', 3000)
print (developers)
 