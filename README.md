# NATO Phonetic Alphabet Converter

A simple Python script that converts any word you type into its NATO phonetic alphabet equivalent (e.g., `A` → `Alfa`, `B` → `Bravo`).

## 📌 Features
- Reads the NATO phonetic alphabet from a CSV file (`nato_phonetic_alphabet.csv`)
- Takes user input and converts each letter into its corresponding NATO code word
- Case-insensitive (automatically converts input to uppercase)

## 📂 Project Structure
```
nato-phonetic-alphabet-converter/
│
├── main.py                     # Main script
├── nato_phonetic_alphabet.csv  # NATO alphabet data
└── README.md                   # Project documentation
```

## ⚙️ Requirements
- Python 3.x
- pandas library

Install pandas if you don't have it:
```bash
pip install pandas
```

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/NinjaVinja/nato-phonetic-alphabet-converter.git
   cd nato-phonetic-alphabet-converter
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter a word when prompted:
   ```
   Enter a word: HELLO
   ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
   ```

## 🛠️ Example Code
```python
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]: row["code"] for index, row in data.iterrows()}

user = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in user]
print(output_list)
```

## ✨ Possible Improvements
- Handle spaces and non-alphabet characters gracefully
- Add error handling for invalid input
- Convert into a CLI tool with argument support

## 👤 Author
**Muhammad Taha Ahmad** ([NinjaVinja](https://github.com/NinjaVinja))
*Code Ninja by Night, Student by Day* 🥷

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
