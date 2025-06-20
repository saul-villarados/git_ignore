def g():
  try:
    with open('PROJECT/config/secrets.txt') as f:
      d = f.read()
      return print(d + 'lo lograste')  
  except Exception as e:
    return print(e)
g()
