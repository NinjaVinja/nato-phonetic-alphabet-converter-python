import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for index,row in data.iterrows()}

user = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in user]
print(output_list)
