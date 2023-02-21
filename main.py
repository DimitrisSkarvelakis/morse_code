morse_list = {"A": '.-', "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
              "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
              "Q": ".--.", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--.."}

morse_swap = {v: k for k, v in morse_list.items()}

what = input("please tell me what would you like to convert? morse or text?").lower()
text = input("please tell me the text").upper()

answer = ""

if what == "text":
    for i in text:
        answer = answer + morse_list[i] + " "
    print(answer)
elif what == "morse":
    final_text = text.split()
    for i in final_text:
        for n in morse_swap:
            if i == n:
                answer += morse_swap[n]
    print(answer)
else:
    print("please choose one or another, text or morse?")
