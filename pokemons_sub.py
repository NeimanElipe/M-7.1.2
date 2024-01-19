# a)
function getUnitatMesuraAltura (pokemon):
    return pokemon["pes"]["mesura"]

# b

function isSegonMovimentDeContacte (pokemon):
    if pokemon["moviment"]["contacte"] == true:
        return True
    else:
        return False

#c

function getSumaEstadistiques (pokemon):
    poder_total = pokemon["estadistiques"]["velocitat"] + pokemon["estadistiques"]["fortalesa"] + pokemon["estadistiques"]["precisio"] + pokemon["estadistiques"]["resistencia"]
    return poder_total

#d

function getMitjanaEstadistiques (pokemon):
    mitjana_estadistiques = pokemon["estadistiques"]["velocitat"] + pokemon["estadistiques"]["fortalesa"] + pokemon["estadistiques"]["precisio"] + pokemon["estadistiques"]["resistencia"]) / 5
    return mitjana_estadistiques

#e

function getPes (llista3Pokemon):
    pes_total = pokemons[0]["pes"][pesatge] + pokemons[1]["pes"][pesatge] + pokemons[2]["pes"][pesatge]
    return pes_total

#f

function isEvolucioPossible (pokemon, nivell):

    pokemon = int(input("Introdueix nivell pokemon: "))
    if pokemon >= nivell
        return True
    else:
        return False

#g

function getPotenciaMesAlta (pokemonsList)

