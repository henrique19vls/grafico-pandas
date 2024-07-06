import panda as pd

data = {
        'Nome' : ['Grylo', 'Bob', 'Wanderson', 'Jo soares'],
        'Idade': [55, 10, 70, 70],
        'Cidade': ['Brazilandia','Valinhos','Barao Geraldo','Sao Paulo']

  
}

df = pd.DataFrame(data)
print(df)