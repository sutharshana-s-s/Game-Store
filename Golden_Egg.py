import pickle

def Golden_Egg():
    f=open("Golden_Egg_final.txt","w")
    
    s="""Once upon a time, a farmer had a goose that laid a golden egg every day. The egg provided enough money for the farmer and his wife for their day-to-day needs.

The farmer and his wife were happy for a long time. But one day, the farmer got an idea and thought, "Why should I take just one egg a day? Why can't I take all of

them at once and make a lot of money?" The foolish farmer's wife also agreed and decided to cut the goose's stomach for the eggs. As soon as they killed the bird and

opened the goose's stomach, to find nothing but guts and blood. The farmer, realizing his foolish mistake, cries over the lost resource!"""
    
    f.write(s)
    f.close()

    f=open("Golden_Egg.txt","w")
    
    s="""Once upon a time, a farmer had a goose that laid a _ _ _ _ _ _ (1.Colour) egg every day. The egg _ _ _ _ _ _ _ _(2.Conjunction) enough money for the farmer

and his wife for their day-to-day _ _ _ _ _ (3.Adverb).The farmer and his wife were _ _ _ _ _(4.Adjective) for a long time. But one day, the farmer got an idea and

_ _ _ _ _ _ _(5.Noun), "Why should I take just one egg a _ _ _(6.Noun) ? Why can't I take all of them at once and make a lot of _ _ _ _ _(7.Noun)?" The

_ _ _ _ _ _ _(8.Adjective) farmer's wife also agreed and _ _ _ _ _ _ _ (9.Adjective) to cut the goose's _ _ _ _ _ _ _ (10.Noun) for the eggs. As soon as they

_ _ _ _ _ _(11.Verb) the bird and opened the goose's stomach, to find _ _ _ _ _ _ _ (12.Pronoun) but guts and _ _ _ _ _ (13.Noun). The farmer, _ _ _ _ _ _ _ _ _

(14.Verb) his foolish mistake, cries over the lost _ _ _ _ _ _ _ _(15.Noun)! """

    
    f.write(s)
    f.close()

    f=open("Golden_Egg_ans.dat","wb")
    ans={1:"golden",2:"provided",3:"needs",4:"happy",5:"thought",6:"day",7:"money",8:"foolish",9:"decided",10:"stomach",11:"killed",12:"nothing",13:"blood",
         14:"realizing",15:"resource"}
    pickle.dump(ans,f)
    f.close()

Golden_Egg()
