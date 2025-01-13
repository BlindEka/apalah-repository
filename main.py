class calculator:
  def __init__(self,number:str) ->None:
    self.number = number
  def calculate(self) ->int:
    tokenizedNumber = self.number.split(' ')
    result = 0
    operator = None
    first = True
    for i in tokenizedNumber:
      if first:
        result += int(i)
        first = False
      elif operator:
        if operator == '+':
          result += int(i)
          operator = None
        elif operator == '-':
          result -= int(i)
          operator = None
        elif operator == '*':
          result *= int(i)
          operator = None
        elif operator == '/':
          result /= int(i)
          operator = None
        elif operator == '**':
          result **= int(i)
          operator == None
        elif operator == '%':
          result %= int(i)
          operator = None
        elif operator == '//':
          result //= int(i)
          operator = None
        elif operator == '^':
          result ^= int(i)
          operator = None
        else:
          raise TypeError(f'unknown operator {operator}')
      else:
        operator = i
    return result

def coba():
  
    return result
    