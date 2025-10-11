from logic import *

"""
Dans cet exercice nous allons passer trois phrases dans notre base de connaissance, chacune de ces phrases répresente
une information que notre agent(IA) va checker pour conclure s'il a pleut ou pas."""

# If it didn't rain, Harry visited hagrid today.
# Harry visited hagrid or dumbledore today, but not both.
# Harry visited dumbledore.

rain = Symbol("rain") # reprensents the sentence (it rained)
hagrid = Symbol("hagrid") # -||- (Harry visited hagrid)
dumbledore = Symbol("dumbledore") # -||- (Harry visited dumbledore)

knowledge = And(
    Implication(Not(rain), hagrid), # if it didn't rain, then Harry visited hagrid today.
    Or(hagrid, dumbledore), # Harry visited hagrid or dumbledore
    Not(And(hagrid, dumbledore)), # but not both
    dumbledore # Harry visited dumbledore
)

print(knowledge.symbols())
print(knowledge.formula())
if model_check(knowledge, Not(rain)):
    print("It rained today\nHarry did not visited Hagrid today") # inferences 
else:
    print("It didn't rain today\nHarry visited Hagrid") # inferences
 
