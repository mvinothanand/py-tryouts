class Person:
  def __init__(self, initialAge: int):
    if initialAge < 0:
      print('Age is not valid. Setting age to 0.')
      self.age = 0
    else:
      self.age = initialAge
    print(f'initial age set to: {self.age}')

  def yearPasses(self):
    self.age += 1
    print(f'Year passed. age is now: {self.age}')

  def amIOld(self):
    if self.age < 13:
      print('You are young.')
    elif self.age < 18:
      print('You are a teenager.')
    else:
      print('You are old.')

def main():
  initialAge = int(input('Initial Age: '))
  person = Person(initialAge)
  person.yearPasses()
  person.amIOld()


if __name__ == '__main__':
  main()