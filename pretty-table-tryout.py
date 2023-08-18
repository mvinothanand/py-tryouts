# pip install prettytable
from prettytable import PrettyTable, MSWORD_FRIENDLY, DEFAULT, PLAIN_COLUMNS, MARKDOWN,ORGMODE, SINGLE_BORDER, DOUBLE_BORDER

# To print table in color
from prettytable.colortable import ColorTable, Themes

x = PrettyTable()
y = ColorTable(theme=Themes.OCEAN)

# Add each row individually
x.field_names = ["Day", "1", "2", "3", "4", "5", "6", "8"]
x.add_row (["Mon", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])
x.add_row (["Tue", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])
x.add_row (["Wed", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])
x.add_row (["Thu", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])
x.add_row (["Fri", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])


y.field_names = ["Day", "1", "2", "3", "4", "5", "6", "8"]
y.add_row (["Mon", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])
y.add_row (["Tue", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])
y.add_row (["Wed", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])
y.add_row (["Thu", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])
y.add_row (["Fri", "SUB-1", "SUB-2", "subject 3", "subject ten", "mechanical engineering lab", "c programming lab", "communication skills"])

# Set the table style to make it print MS WORD friendly
#x.set_style(MSWORD_FRIENDLY)

# Set the table style to default
x.set_style(DEFAULT)

# Set the table style to PLAIN_COLUMNS - without any border lines
#x.set_style(PLAIN_COLUMNS)

# MARKDOWN style
#x.set_style(MARKDOWN)

#ORGMODE syntax
#x.set_style(ORGMODE)

# Single border
#x.set_style(SINGLE_BORDER)

# Double border
#x.set_style(DOUBLE_BORDER)

# print the table in ASCII
print(x)

# print the color table in ASCII 
print(y)

# Write the table to a file
with open("pretty-table.txt", "w") as fp:
  fp.write(x.get_string())



