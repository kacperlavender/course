import json, csv

file_path_txt = "file writingf.txt"
file_path_json = "file writingf.json"
file_path_csv = "file writingf.csv"

#txt
try:
    with open(file_path_txt, "r") as filetxt:
        content_txt = filetxt.read()
        print(content_txt)

except Exception as e:
    print(f"a problem: '{e}' occured")


#json
try:
    with open(file_path_json, "r") as filejson:
        content_json = json.load(filejson)
        print(content_json["name"])

except Exception as e:
    print(f"a problem: '{e}' occured")


#csv
try:
    with open(file_path_csv, "r") as filecsv:
        content_csv = csv.reader(filecsv)
        for line in content_csv:
            print(line[0])

except Exception as e:
    print(f"a problem: '{e}' occured")
