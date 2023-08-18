from tabulate import tabulate

table = [
  ["Day", "1", "2", "3", "4", "5", "6", "7", "8"],
  ["Mon", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills", "communication skills"],
  ["Tue", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills", "communication skills"],
  ["Wed", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills", "communication skills"],
  ["Thu", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills", "communication skills"],
  ["Fri", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills", "communication skills"],
]

# print the table with the first row in the list as header
#print(tabulate(table, headers="firstrow"))

# specify a table format
#print(tabulate(table, headers="firstrow", tablefmt="grid"))
#see https://pypi.org/project/tabulate/ for available format options

# specify a column width to enforce automatic multiline in cells
print(tabulate(table, headers="firstrow", tablefmt="grid", maxcolwidths=[8,15,15,15,15,15,15,15,15]))

# Write the table to a file
with open("tabulate-table.txt", "w") as fp:
  fp.write(tabulate(table, headers="firstrow", tablefmt="grid", maxcolwidths=[8,15,15,15,15,15,15,15,15]))