import pickle

def The_Lion_Mouse():
    f=open("The_Lion_Mouse_final.txt","w")
    
    s="""A lion was once sleeping in the jungle when a mouse started running up and down his body just for fun.This disturbed the lion's sleep, and he woke up quite

angry.He was about to eat the mouse when the mouse desperately requested the lion to set him free."I promise you, I will be of great help to you someday if you save

me." The lion laughed at the mouse's confidence and let him go.One day, a few hunters came into the forest and took the lion with them. They tied him up against a

tree. The lion was struggling to get out and started to whimper.Soon, the mouse walked past and noticed the lion in trouble.Quickly, he ran and chewed on the ropes

to set the lion free. Both of them sped off into the jungle."""
    
    f.write(s)
    f.close()

    f=open("The_Lion_Mouse.txt","w")
    
    s="""A lion was once sleeping in the _ _ _ _ _ _(1.Noun) when a mouse started running up and down his _ _ _ _(2.Noun) just for fun.

This _ _ _ _ _ _ _ _ _(3.Adjective) the lion's sleep, and he woke up quite _ _ _ _ _(4.Adjective).He was about to eat the mouse when the mouse desperately

_ _ _ _ _ _ _ _ _ (5.Verb) the lion to set him  _ _ _ _(6.Adverb)."I _ _ _ _ _ _ _ (7.Noun)you, I will be of great help to you_ _ _ _ _ _ _(8.Adverb) if you save me."

The lion laughed at the mouse's _ _ _ _ _ _ _ _ _ _ (9.Noun) and let him go.One day, a few _ _ _ _ _ _  _(10.Noun)came into the forest and took the _ _ _  _(11.Noun)

with them. They tied him up _ _ _ _ _ _ _ (12.Preposition) a tree.The lion was _ _ _ _ _ _ _ _ _ _(13.Adjective) to get out and started to whimper.Soon, the mouse

walked past and noticed the lion in _ _ _ _ _ _ _(14.Noun).Quickly, he ran and _ _ _ _  _ _(15.Verb)  on the ropes to set the lion free. Both of them sped off into

the jungle."""
    
    
    f.write(s)
    f.close()

    f=open("The_Lion_Mouse_ans.dat","wb")
    ans={1:"jungle",2:"body",3:"disturbed",4:"angry",5:"requested",6:"free",7:"promise",8:"someday",9:"confidence",10:"hunters",11:"lion",12:"against",13:"struggling",
         14:"trouble",15:"chewed"}
    pickle.dump(ans,f)
    f.close()
The_Lion_Mouse()
