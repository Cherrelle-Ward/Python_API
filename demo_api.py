import requests


def api_call():
    
    # user enters the name of character they wish to search about.
    user_input = str(input('Pick a name?\n'))
   
    # API call
    url = 'https://rickandmortyapi.com/api/character/'
    request = requests.get(url)
    json = request.json()
    results = json.get('results')

# stores all character names
    character_list = []
    
# loops through the json character info based on the user input. 
    for character_info in results:
            
        character_name = character_info.get('name')
        character_list.append(character_name)
            
        if user_input == character_name:
                
            character_name = character_info.get('name')
            print('Character', character_name)
            species = character_info.get('species')
            print(species, 'i am species')            
            status = character_info.get('status')
                
            # adds to demo_file.txt
            f = open('demo_file.txt', 'a')
            f.write('Character: '+character_name+'\nSpecies: '+species+'\nStatus: '+status)
            f.close()
                
            
    if user_input not in character_list:
        print('\nCharacter unknown')
        print('\nAll Characters: \n', character_list)
    
   

    
api_call()



# Character names:
# Rick Sanchez
# Morty Smith
# Summer Smith
# Beth Smith
# Jerry Smit