shema = [
  [
    ["51", 0], ["52", 1], ["53", 1], ["54", 1], ["  ", 0], ["55", 0], ["56", 0], ["57", 0], ["  ", 0], ["58", 1], ["59", 1], ["5A", 1]
  ], 
  [
    ["41", 1], ["42", 1], ["43", 1], ["44", 0], ["  ", 0], ["45", 1], ["46", 1], ["47", 1], ["  ", 0], ["48", 1], ["49", 1], ["4A", 1]
  ],
  [
    ["31", 1], ["32", 1], ["33", 1], ["34", 0], ["  ", 0], ["35", 1], ["36", 0], ["37", 0], ["  ", 0], ["38", 1], ["39", 0], ["3A", 1]
  ],
  [
    ["21", 1], ["22", 1], ["23", 1], ["24", 0], ["  ", 0], ["25", 0], ["26", 0], ["27", 1], ["  ", 0], ["28", 0], ["29", 1], ["2A", 1]
  ],
  [
    ["11", 1], ["12", 1], ["13", 1], ["14", 1], ["  ", 0], ["15", 1], ["16", 1], ["17", 1], ["  ", 0], ["18", 0], ["19", 0], ["1A", 0]
  ],
]


for i in range(5):
  for j in range(12):
    if shema[i][j][1] == 1:
      print(shema[i][j][0], end=" ")
    else:
      print("xx", end=" ")      
  print()    
