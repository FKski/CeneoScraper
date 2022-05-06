import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
productId = input("Please, pass the product id: ")

opinions = pd.read_json("opinions/" + productId + ".json")
print(opinions)