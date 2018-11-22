import winspeech
text = "Hello"
#winspeech.say("99 bottles of beer on the wall")

count = 99
while count > 0:

    phrase1 = count, "bottles of beer on the wall,", count, "bottles of beer, you take one down, you pass it around,"
    count -=1
    print(phrase1)
    winspeech.say(phrase1)
    phrase2 = count, "bottles of beer on the wall, bottles of beer... "
    print(phrase2)
    winspeech.say(phrase2)
