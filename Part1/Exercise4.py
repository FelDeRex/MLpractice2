import random
import pandas as pd

d = [{"Name": "Виктор", "Age": 18},
     {"Name": "Мария", "Age": 21},
     {"Name": "Иван", "Age": 19},
     {"Name": "Иван", "Age": 25},
     {"Name": "Алексей", "Age": 20}]

df = pd.DataFrame(d)

def GeneratePhoneNumber():
     return '+7(' + str(random.randint(100, 999)) + ')' + \
          str(random.randint(100, 999)) + ' ' + \
          str(random.randint(100, 999)) + ' ' + \
          str(random.randint(10, 99)) + ' ' + \
          str(random.randint(10, 99))


for i in range(len(df.index)):
     df.loc[i, "Phone number"] = GeneratePhoneNumber()

print(df)