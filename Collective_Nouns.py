import pickle

def Collective_Nouns():
    f=open("Collective_Nouns_final.txt","w")
    s="""A brood of chickens.
A herd of cattles.
A colony of ants.
A hive of bees.
A flock of sheeps.
A flight of birds.
A pack of wolves.
A litter of puppies.
A pride of lions.
A muster of peacocks.
A shoal of fishes.
A string of camels.
A team of horses.
A bevy of quails.
A troop of kangaroos.
A nest of rabbits.
A hust of hares.
A pod of whales.
A sloth of bears.
A punnet of strawberries."""
    f.write(s)
    f.close()

    f=open("Collective_Nouns.txt","w")
    s="""A _ _ _ _ _  of chickens.
A _ _ _ _  of cattles.
A _ _ _ _ _ _  of ants.
A _ _ _ _  of bees.
A _ _ _ _ _  of sheeps.
A _ _ _ _ _ _  of birds.
A _ _ _ _  of wolves.
A _ _ _ _ _ _  of puppies.
A _ _ _ _ _  of lions.
A _ _ _ _ _ _ of peacocks.
A _ _ _ _ _ of fishes.
A _ _ _ _ _ _ of camels.
A _ _ _ _ of horses.
A _ _ _ _ of quails.
A _ _ _ _ _ of kangaroos.
A _ _ _ _ of rabbits.
A _ _ _ _ of hares.
A _ _ _ of whales.
A _ _ _ _ _ of bears.
A _ _ _ _ _ _ of strawberries."""
    f.write(s)
    f.close()

    f=open("Collective_Nouns_ans.dat","wb")
    ans={0:"brood",1:"herd",2:"colony",3:"hive",4:"flock",5:"flight",6:"pack",7:"litter",8:"pride",9:"muster",10:"shoal",11:"string",12:"team",13:"bevy",14:"troop",15:"nest",
         16:"hust",17:"pod",18:"sloth",19:"punnet"}
    pickle.dump(ans,f)
    f.close()

Collective_Nouns()
    







