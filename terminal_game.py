# Mini Pokemon Game
import random
print("Available round format to chose from are best of 3 and best of 5"+ "\n To choose best of 3 enter 3 and to choose best of 5 enter 5")
round = int(input("Enter the round format you want to play: "))
user_win = 0
ai_win = 0
if round == 3 or round == 5 :
    for i in range(round):
        print("List of Pokemon available: Pikachu, Charmander, Bulbasaur, Squrtle, Jigglypuff")
        pokemon = input("Enter your pokemon: ")
        ai = random.choice(["Pikachu", "Charmander", "Bulbasaur", "Squrtle", "Jigglyypuff"])
        print("You chose ", pokemon)
        print("Opponent chooses ", ai)
        if(pokemon == ai):
            print("It's a tie!")
            break
        else :
            if pokemon == "Pikachu":
                print("Attacks available for selection are: Thunderbolt, Quick Attack, Iron Tail, Electro Ball")
                attack = input("Enter your attack: ")
                if ai == "Charmander":
                    print("Charmander used Ember")
                    print("It's very effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                elif ai == "Jigglypuff" :
                    print("Jigglypuff used Sing")
                    print("It's super effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                else :
                    print('Pikachu used ', attack)
                    print("It's super effective!")
                    print("You win!")
                    user_win += 1
                    break
            elif pokemon == "Charmander" :
                print("Attacks available for selection are: Ember, Quick Attack, Iron Tail, Dragon Claw")
                attack = input("Enter your attack: ")
                if ai == "Squrtle":
                    print("Squrtle used Water Gun")
                    print("It's very effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                elif ai == "Jigglypuff" :
                    print("Jigglypuff used Sing")
                    print("It's super effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                elif ai == "Pikachu" :
                    print("Pikachu used Thunderbolt!")
                    print("It's super effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                else :
                    print('Charmender used ', attack)
                    print("It's super effective!")
                    print("You win!")
                    user_win += 1
                    break
            elif pokemon == "Bulbasaur" :
                print("Attacks available for selection are: Vine Whip, Tackle, Razor Leaf, Seed Bomb")
                attack = input("Enter your attack: ")
                if ai == "Charmender":
                    print("Charmender used Ember")
                    print("It's very effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                elif ai == "Jigglypuff" :
                    print("Jigglypuff used Sing")
                    print("It's super effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                elif ai == "Pikachu" :
                    print("Pikachu used Thunderbolt!")
                    print("It's super effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                else :
                    print('Bulbasaur used ', attack)
                    print("It's super effective!")
                    print("You win!")
                    user_win += 1
                    break
            elif pokemon == "Squrtle" :
                print("Attacks available for selection are: Water Gun, Tackle, Bite, Hydro Pump")
                attack = input("Enter your attack: ")
                if ai == "Pikachu":
                    print("Pikachu used Thunderbolt")
                    print("It's very effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                elif ai == "Jigglypuff" :
                    print("Jigglypuff used Sing")
                    print("It's super effective!")
                    print("You lose!")
                    ai_win += 1
                    break
                elif ai == "Bulbasaur" :
                    print("Bulbasaur used Vine Whip!")
                    print("It's super effective!")
                    print("You Lose!")
                    ai_win += 1
                    break
                else :
                    print('Squrtle used ', attack)
                    print("It's super effective!")
                    print("You win!")
                    user_win += 1
                    break
            elif pokemon == "Jigglypuff" :
                print("Attacks available for selection are: Sing, Pound, Rest, Hyper Voice")
                attack = input("Enter your attack: ")
                print('Jigglypuff used ', attack)
                print("It's super effective!")
                print("You win!")
                user_win += 1;
                break
            else :
                pokemon = input("Enter a valid pokemon: ")