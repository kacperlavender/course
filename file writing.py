import json, csv

# a = append
# w = write
# x = create if doesnt exist => if exist = error

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

employees = [["name", "age", "job"],
             ["spongebob", 30, "cook"],
             ["patrick", 37, "unemployed"],
             ["sandy", 27, "scientist"]]

txt_data = "bmw"

file_path1 = "file writingf.json"
file_path2 = "file writingf.csv"
file_path3 = "file writingf.txt"


#JSON
try:
    with open(file_path1, "w") as file1:
        json.dump(employee, file1, indent=4)
        print(f"json file '{file_path1}' was created")
except FileExistsError:
    print("that file already exists")


#CSV
try:
    with open(file_path2, "w", newline="") as file2:
        writer = csv.writer(file2)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path2}' was created")
except FileExistsError:
    print("that file already exists")


#TXT
try:
    with open(file_path3, "x") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path3} was created")
except Exception as e:
    print(f"an error occurred: {e}")