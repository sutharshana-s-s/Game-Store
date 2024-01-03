import pickle


def Proverb_Filling():
    f=open("Proverbs_final.txt","w")
    s="""An apple a day keeps the doctor away.
An empty vessel makes much noise.
An idle brain is the devil’s workshop.
A picture is worth a thousand words.
As you sow, so you shall reap.
Barking dogs seldom bite.
Beauty is in the eye of the beholder.
Better late than never.
Blood is thicker than water.
Cleanliness is next to Godliness.
Cowards die many times before their deaths.
Don’t count your chickens before they hatch.
Don’t judge a book by its cover.
Early bird catches the worm.
Every cloud has a silver lining.
Honesty is the best policy.
Half a loaf is better than none.
Hope for the best, prepare for the worst.
It’s better to be safe than sorry.
Laughter is the best medicine."""
    f.write(s)
    f.close()

    f=open("Proverbs.txt","w")
    s="""An _ _ _ _ _ a day keeps the doctor away.
An empty _ _ _ _ _ _ makes much noise.
An _ _ _ _ brain is the devil’s workshop.
A picture is worth a _ _ _ _ _ _ _ _ words.
As you sow, so you shall _ _ _ _.
Barking dogs _ _ _ _ _ _ bite.
_ _ _ _ _ _ is in the eye of the beholder.
Better _ _ _ _ than never.
_ _ _ _ _ is thicker than water.
Cleanliness is next to _ _ _ _ _ _ _ _ _ .
_ _ _ _ _ _ _ die many times before their deaths.
Don’t count your _ _ _ _ _ _ _ _ before they hatch.
Don’t _ _ _ _ _ a book by its cover.
Early bird catches the _ _ _ _.
Every cloud has a _ _ _ _ _ _ lining.
_ _ _ _ _ _ _ is the best policy.
Half a _ _ _ _ is better than none.
Hope for the best, prepare for the _ _ _ _ _ .
It’s better to be safe than _ _ _ _ _ .
_ _ _ _ _ _ _ _ is the best medicine."""
    f.write(s)
    f.close()

    f=open("Proverbs_ans.dat","wb")
    ans={0:"apple",1:"vessel",2:"idle",3:"thousand",4:"reap",5:"seldom",6:"Beauty",7:"late",8:"Blood",9:"Godliness",10:"Cowards",11:"chickens",12:"judge",13:"worm",14:"silver",15:"Honesty",
         16:"loaf",17:"worst",18:"sorry",19:"Laughter"}
    pickle.dump(ans,f)
    f.close()

Proverb_Filling()
    
