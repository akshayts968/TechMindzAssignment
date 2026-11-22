from random import choice



movies = [
    # Malayalam Movies (2020 - 2026)
    "Ayyappanum Koshiyum",
    "Anjaam Pathiraa",
    "Kappela",
    "Forensic",
    "Trance",
    "Joji",
    "The Great Indian Kitchen",
    "Nayattu",
    "Malik",
    "Minnal Murali",
    "Churuli",
    "Thinkalazhcha Nishchayam",
    "Home",
    "Kala",
    "Operation Java",
    "Jana Gana Mana",
    "Hridayam",
    "Bheeshma Parvam",
    "Jaya Jaya Jaya Jaya Hey",
    "Thallumaala",
    "Nna Thaan Case Kodu",
    "Pada",
    "Rorschach",
    "Puzhu",
    "Mukundan Unni Associates",
    "Romancham",
    "Kannur Squad",
    "Kaathal",
    "Nanpakal Nerathu Mayakkam",
    "Neru",
    "Iratta",
    "Falimy",
    "Garudan",
    "Bramayugam",
    "Manjummel Boys",
    "Premalu",
    "Aavesham",
    "Aadujeevitham",
    "Kishkindha Kaandam",
    "Aattam",
    "Ullozhukku",
    "All We Imagine As Light",
    "Anweshippin Kandethum",
    "Ajayante Randam Moshanam",
    "Thalavan",
    "Guruvayoorambala Nadayil",
    "Bougainvillea",
    "Pani",
    "Sookshmadarshini",
    "Marco",
    "Rekhachithram",
    "Ponman",
    "Thudarum",
    "Lokah",
    "Dies Irae",
    "Eko",
    "Sarvam Maya",
    "Kalamkaval",
    "Officer on Duty",
    "Alappuzha Gymkhana",
    "Patriot",
    "Bethlehem Kudumba Unit",
    "Athiradi",
    "Balan",
    "Pennum Porattum",

    # Tamil Movies (2020 - 2026)
    "Soorarai Pottru",
    "Kannum Kannum Kollaiyadithaal",
    "Psycho",
    "Oh My Kadavule",
    "Jai Bhim",
    "Sarpatta Parambarai",
    "Maanaadu",
    "Karnan",
    "Mandela",
    "Doctor",
    "Master",
    "Kadaisi Vivasayi",
    "Vikram",
    "Ponniyin Selvan",
    "Love Today",
    "Thiruchitrambalam",
    "Gargi",
    "Rocky",
    "Taanakkaran",
    "Vendhu Thanindhathu Kaadu",
    "Por Thozhil",
    "Maaveeran",
    "Jigarthanda DoubleX",
    "Chithha",
    "Good Night",
    "Jailer",
    "Leo",
    "Dada",
    "Ayothi",
    "Irugapatru",
    "Maharaja",
    "Amaran",
    "Meiyazhagan",
    "Lubber Pandhu",
    "Vaazhai",
    "Kottukkaali",
    "Thangalaan",
    "Vettaiyan",
    "The Greatest of All Time",
    "Dragon",
    "Kudumbasthan",
    "Bison Kaalamaadan",
    "Thalaivan Thalaivii",
    "Paranthu Po",
    "Kuberaa",
    "Parasakthi",
    "Jana Nayagan",
    "Karuppu",
    "Thaai Kizhavi",
    "Vaa Vaathiyaar",
]




selected_movie = choice(movies)
selected_movie = selected_movie.lower()
#selected_movie = "Don".lower()
# print(selected_movie)
mov_len = len(selected_movie)


chanceCount = 6
guessDirect = 2
chance = -1
correctGuessCount = 0
guessedLetter=""
answer = []
directname = ""
print("\n\n\n")
for i in selected_movie:
    if i == " ":
        print(end="\t")
        answer.append(" ")
    else:
        print(end='_ ')
        answer.append("_")

print("\n\n")

print("You have Total 6 Chance to Guess letter of the movie")
print("You have Total 2 Chance to Guess movie directly")
while chanceCount:
    print(f"\nTotal Letter Guess Chance remaining {chanceCount}")
    print(f"\nTotal Movie name Guess Chance remaining {guessDirect}")
    if guessDirect:
        chance = input('\nEnter the number to select guess option\n1.Guess Letter\n2.Guess Directly\n3.Exit\n')
    else:
        chance = input('Enter the number to select  option\n1.Guess Letter \n2.Exit\n')
    alpha = ""
    if chance == '1':
        while len(alpha) != 1: 
            alpha = input("Enter single character: ").lower()
        # print(alpha)
        if alpha not in guessedLetter:
            guessedLetter += alpha

            if alpha in selected_movie:

                for i in range(mov_len):
                    if alpha == selected_movie[i]:
                        print(alpha,end=" ")
                        answer[i] = alpha
                    elif answer[i] not in "_ ":
                        print(answer[i],end=" ")
                    elif answer[i] ==" ":
                        print(end="\t")
                    else:
                        print(end="_ ")
            else:
                chanceCount -= 1
                print(f"You selected wrong letter {alpha} and your chance left {chanceCount}")
                print(" ".join(answer))
        else:
            print("You selected the same letter you typed")
    elif chance == '2' and guessDirect:
        directname = input("\nEnter the direct movie name: ").lower()
        if directname == selected_movie:
            print(f"\nYou Found the Movie {selected_movie}")
            break
        else:
            guessDirect -= 1
            print(f"Your Direct Guess {directname} is Wrong")
            print(" ".join(answer))
            continue
    elif chance == '2' or chance == '3':
        print("Exit")
        break
    else:
        print("Error")
        continue


    if "".join(answer) == selected_movie:
        print(f"\nYou Found the Movie {selected_movie}")
        break
else:
    print(f"Game Over! You ran out of chances. The movie was: {selected_movie.title()}")