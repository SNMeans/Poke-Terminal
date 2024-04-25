import requests as req
import climage
from colorama import Fore, Style

rep = req.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
json = rep.json()
pokedex = json.get('results')

while True:
    
    query = input("Hello, fellow pokemon trainer! Enter a pokemon name, or enter 's' to search through our directory: ").lower().strip()


    if query == 's' or query == 'search':
        query = input("\nEnter search query for pokemon names: ").lower().strip()
        
        
        search_results = [pokemon.get('name') for pokemon in pokedex if query in pokemon.get('name')]
        # print(search_results)
        # if there are no results, let the user know and restart the loop
        if not search_results:
            print(f'\n{Fore.RED}No search results found for "{query}"')
            print(Style.RESET_ALL)
            continue
       
        search_str = f'\n{Fore.RED}Search Results:\n\n'
        counter = 0
        for result in search_results:
            search_str += f"{Fore.YELLOW}{result}\n"
            counter += 1
            if counter >= 3:
                counter = 0
                # search_str = search_str.rstrip()
                search_str += '\n'
        search_str = search_str.rstrip()
        search_str += f'\n'
        print(search_str)
        print(Style.RESET_ALL)
    
    else:
        try:
            rep = req.get(f'https://pokeapi.co/api/v2/pokemon/{query}')
            poke1 = rep.json()
       
        except:
            print(f'\n{Fore.RED}Invalid Pokemon Name')
            print(Style.RESET_ALL)
            continue
       
        else:
            print(Style.RESET_ALL)
           
            poke_url1 = poke1.get('sprites').get('front_default')
            img_data = req.get(poke_url1).content
            with open('sprite1.jpg', 'wb') as handler:
                handler.write(img_data)
            poke_sprite1 = climage.convert('sprite1.jpg', width=64, is_unicode=True, is_256color=False, is_truecolor=True)

           #ensures the names are upper case/capitalized
            poke_name1 = poke1.get('species').get('name').capitalize()

           
            poke_types1 = [type.get('type').get('name') for type in poke1.get('types')]
            poke_types1_str = ''
            for type in poke_types1:
                poke_types1_str += f'{type} \t'

            
            poke_stats1 = {stat.get('stat').get('name'): stat.get('base_stat') for stat in poke1.get('stats')}
            poke_stat1_str = f"{Fore.RED}HP: {Fore.YELLOW}{poke_stats1.get('hp')}\t\t{Fore.RED}Att: {Fore.YELLOW}{poke_stats1.get('attack')}  \t{Fore.RED}Def: {Fore.YELLOW}{poke_stats1.get('defense')}\n{Fore.RED}Sp-Att: {Fore.YELLOW}{poke_stats1.get('special-attack')}\t{Fore.RED}Sp-Def: {Fore.YELLOW}{poke_stats1.get('special-defense')}\t{Fore.RED}Speed: {Fore.YELLOW}{poke_stats1.get('speed')}"

            
            poke_weight1 = poke1.get('weight')
            poke_height1 = poke1.get('height')

            print(f'\n{Fore.YELLOW}{poke_name1}:\n')
            print(poke_sprite1)
            print(f"{Fore.RED}Type: \t{Fore.YELLOW}{poke_types1_str}\n\n{Fore.RED}Height: {Fore.YELLOW}{poke_height1} \t {Fore.RED}Weight: {Fore.YELLOW}{poke_weight1}\n\n{poke_stat1_str}\n")
            print(Style.RESET_ALL)

            
            is_repeat = True
            while True:
               
                repeat = input('Would you like to search for another Pokemon (Y / N): ').lower().strip()
                
                if repeat == 'y' or repeat == 'yes':
                    break
                
                elif repeat == 'n' or repeat == 'no':
                    is_repeat = False
                    print(Style.RESET_ALL)
                    break
                
                else:
                    print (f'\n{Fore.RED}Invalid Response, please answer "yes" or "no" (Y / N)')
                    print(Style.RESET_ALL)
                    continue
           
            if is_repeat:
                continue
          
            else: 
                print(Style.RESET_ALL)
                break
# goodbye message moved outside of loop so if we get here unexpectedly, it will always play
print (f'\n{Fore.RED}Off to fight Team Rocket? Come back soon!')
print(Style.RESET_ALL)