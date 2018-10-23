from pydub import AudioSegment

choice = 0
#Initialize finalSong as a blank audio file
finalSong = AudioSegment.silent(duration=1000)

print("Welcome to Vusa's Song Maker 3000!\n")
print("To begin, please select from the following: \n")

#You can replace these file locations here with local files on your device!
trumpets = AudioSegment.from_wav("\\Users\\vusaj\\PycharmProjects\\Day1Python\Trumpets_2.wav")
violins = AudioSegment.from_wav("\\Users\\vusaj\\PycharmProjects\\Day1Python\Violins.wav")
whew= AudioSegment.from_wav("\\Users\\vusaj\\PycharmProjects\\Day1Python\Whew.wav")
whew2= AudioSegment.from_wav("\\Users\\vusaj\\PycharmProjects\\Day1Python\Whew_2.wav")
birds= AudioSegment.from_wav("\\Users\\vusaj\\PycharmProjects\\Day1Python\Birds.wav")
fish= AudioSegment.from_wav("\\Users\\vusaj\\PycharmProjects\\Day1Python\Fish.wav")
dawn = AudioSegment.from_wav("\\Users\\vusaj\\PycharmProjects\\Day1Python\Dawn.wav")
feeling = AudioSegment.from_wav("\\Users\\vusaj\\PycharmProjects\\Day1Python\Feeling_Good.wav")

#originalSong = birds + whew + trumpets + fish + dawn + feeling
#mySong = OuLive.whewIntro() + OuLive.whewTOtrumpets() + (trumpets *2) + (violins * 2) + (dawn * 2 ) + feeling

class OuLive:

    def whew2Count():
        print('How many times would you like to play whew2?')
        repeat = int(input())
        global finalSong
        finalSong += (whew2 * repeat)
        print('Whew2 will play ',repeat, ' times!')
        return finalSong

    def whewCount():
        print('How many times would you like to play whew?')
        repeat = int(input())
        global finalSong
        finalSong += (whew * repeat)
        print('Whew will play ', repeat, ' times!')
        return finalSong

    def trumpetsCount():
        print('How many times would you like to play trumpets?')
        repeat = int(input())
        global finalSong
        finalSong += (trumpets * repeat)
        print('Trumpets will play ',repeat, ' times!')
        return finalSong

    def violinsCount():
        print('How many times would you like to play violins?')
        repeat = int(input())
        global finalSong
        finalSong += (violins * repeat)
        print('Violins will play ', repeat, ' times!')
        return finalSong

    def birdsCount():
        print('How many times would you like to play birds?')
        repeat = int(input())
        global finalSong
        count = birds * repeat
        print('Whew2 will play ',repeat, ' times!')
        return count

    def fishCount():
        print('How many times would you like to play fish?')
        repeat = int(input())
        global finalSong
        finalSong += (fish * repeat)
        print('Whew will play ', repeat, ' times!')
        return finalSong

    def dawnCount():
        print('How many times would you like to play dawn?')
        repeat = int(input())
        global finalSong
        finalSong += (dawn * repeat)
        print('Whew2 will play ',repeat, ' times!')
        return finalSong

    def feelingCount():
        print('How many times would you like to play feeling?')
        repeat = int(input())
        global finalSong
        finalSong += (feeling * repeat)
        print('Whew will play ', repeat, ' times!')
        return finalSong

    def makeSong():
        print('Your song is now being created!\n')
        global finalSong
        finalSong.export("\\Users\\vusaj\\PycharmProjects\\Day1Python\\OULIVE_Final_2.wav", format="wav")
        print("Song Status: Complete!")
        print("Thank you for using Vusa's Song Maker 3000\n")
        choice = 9
        return choice

while (choice !=9):
    print('''
        1. Trumpets
        2. Violins
        3. Birds
        4. Fish
        5. Whew Long
        6. Whew Short
        7. Dawn
        8. Feeling
        9. Make Song
        ''')
    choice = input("What beat would you like to add? \n")
    if choice=='1':
        OuLive.trumpetsCount()
    elif choice=='2':
        OuLive.violinsCount()
    elif choice=='3':
        OuLive.birdsCount()
    elif choice=='4':
        OuLive.fishCount()
    elif choice=='5':
        OuLive.whewCount()
    elif choice=='6':
        OuLive.whew2Count()
    elif choice=='7':
        OuLive.dawnCount()
    elif choice=='8':
        OuLive.feelingCount()
    elif choice=='9':
        OuLive.makeSong()
        break
    else:
        print("Sorry, ", choice, " was not a valid option. Try Again!")