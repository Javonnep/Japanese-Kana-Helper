import random

higarana = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
]

ひらがな = [
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の"
]


def KanaTest(list, numOfWords, numOfKanaPerWord):
    for i in range(numOfWords):
        print("")
        for j in range(numOfKanaPerWord):
            print(list[random.randint(0, len(list)-1)], end="")
        # print("")


KanaTest(higarana, 2, 4)
print("")
KanaTest(ひらがな, 2, 3)
print("")
print("")
