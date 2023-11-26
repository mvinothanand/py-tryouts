# REFERENCE: https://realpython.com/python-pathlib/
from pathlib import Path

def main():
  # get current working dir
  print(Path.cwd())
  # get the user home path
  print(Path.home())
  # join and create a new path
  print(Path.home() / "class_schedule" / "xyz.txt")
  # an alternate way to join and create a new path
  print(Path.home().joinpath("class-schedule", "xyz.txt"))

  #Path properties
  new_file = Path.cwd().joinpath("class-schedule", "abc.txt")
  # get the file name - returns a string
  print(f"File name: {new_file.name}")
  # get the filename without extension - returns a string
  print(f"file stem: {new_file.stem}")
  # get the file suffix - returns a string
  print(f"file suffix: {new_file.suffix}")
  # get the anchor - returns a string
  print(f"file anchor: {Path.cwd().anchor}")
  # get the parent directory - returns a new path object
  print(f"Parent directory: {new_file.parent}")
  print(f"Parent directory: {Path.cwd()}")

  # Reading and writing files
  sample_file = Path.cwd() / "test.py"
  # read file contents as string
  print(sample_file.read_text(encoding="utf-8"))
  sample_file_write = Path.cwd() / "testwrite.txt"
  # write text as a string to file
  sample_file_write.write_text("abcd\nefgh\nijkl", encoding="utf-8")
  # NOTE: use read_bytes() and write_bytes() for reading and writing as bytes
  # by default the write_text() method overwrites the file
  # path.open(mode="r", encoding="utf-8") shall be used to open a file in a specified mode 
  #   and then perform the traditional read/write operation

  # Renaming files
  sample_file = Path.cwd() / "colored-text.py"
  # change the filename stem - returns a new path object
  print(sample_file.with_stem("color-text"))
  # change the filename suffix - returns a new path object
  print(sample_file.with_suffix(".txt"))
  # change the filename entirely - returns a new path object
  print(sample_file.with_name("color-text.java"))
  # to actually move the file to a new name use .replace()
  new_file = sample_file.with_stem("color")
  sample_file.replace(new_file) # changes the original colored-text.py to color.py
  sample_file = new_file.with_name("colored-text.py")
  new_file.replace(sample_file)

  # Copying files
  # NOTE: pathlib doesn't have a copy methof
  # but using a combination of renaming methods, read_bytes() and write_bytes copying can be achieved
  # consider using shutil module alng with Path objects to copy files 

  # Create an empty file
  new_empty_file = Path.cwd() / "dummy.txt"
  new_empty_file.touch()
  # Check if path exists
  print(new_empty_file.exists())

  # create a dir
  new_dir = Path.cwd() / "dummy" / "empty_folder"
  if not new_dir.exists():
    new_dir.mkdir(parents=True)

if __name__ == "__main__":
  main()