import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file")
args = parser.parse_args()


lookup = {}
lookup["januari"] = "01"
lookup["februari"] = "02"
lookup["maart"] = "03"
lookup["april"] = "04"
lookup["mei"] = "05"
lookup["juni"] = "06"
lookup["juli"] = "07"
lookup["augustus"] = "08"
lookup["september"] = "09"
lookup["oktober"] = "10"
lookup["november"] = "11"
lookup["december"] = "12"


regexold = r"^\s*([\w\-&' ]+[a-zA-Z])[ BONUS]*\s+([1-9])\s+([0-9,]+)\s+([0-9,]+)$"
regexnew = r"^\s*([\w\-&' ]+[a-zA-Z])\s+([1-9])\s+([0-9,%]+)\s+([0-9,]+)\s+([0-9,]+)\s+([0-9,]+)$"

datum = r"Datum\s+([0-9]+) ([a-zA-Z]+) ([0-9]+)"

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file) as f:
        file_contents = f.read()
        matches = re.finditer(datum, file_contents, re.MULTILINE)
        datum = ""
        for match in matches:
            groups = match.groups()
            datum = f"{groups[2]}-{lookup[groups[1]]}-{groups[0]}"

        matches = re.finditer(regexold, file_contents, re.MULTILINE)
        for match in matches:
            groups = match.groups()
            amount = float(groups[2].replace(",", "."))
            print(f"{groups[0]}\t{datum}\t{amount:.2f}")
        matches = re.finditer(regexnew, file_contents, re.MULTILINE)
        for match in matches:
            groups = match.groups()
            amount = groups[5].replace(",", ".")
            print(f"{groups[0]}\t{datum}\t{float(amount)/float(groups[1]):.2f}")
