import random

higarana = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",

    "ra", "ri", "ru", "re", "ro"
]

ひらがな = [
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の",
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",

    "ら", "り", "る", "れ", "ろ"

]

mini = [
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",

    "ra", "ri", "ru", "re", "ro"
]
mini1 = [
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",

    "ら", "り", "る", "れ", "ろ"
]

def KanaTest(list, numOfWords, numOfKanaPerWord):
    for i in range(numOfWords):
        print("")
        for j in range(numOfKanaPerWord):
            print(list[random.randint(0, len(list)-1)], end="")
        # print("")


KanaTest(mini, 5, 4)
print("")
KanaTest(mini1, 5, 4)
print("")
print("")
