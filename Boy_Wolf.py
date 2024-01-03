import pickle

def Boy_Wolf():
    f=open("Boy_Wolf_final.txt","w")
    
    s="""In a village, lived a carefree boy with his father. The boy's father told him that he was old enough to watch over the sheep while they graze in the fields.

Every day, he had to take the sheep to the grassy fields and watch them as they graze. However, the boy was unhappy and didn't want to take the sheep to the fields.

He wanted to run and play, not watch the boring sheep graze in the field. So, he decided to have some fun. He cried, "Wolf! Wolf!" until the entire village came

running with stones to chase away the wolf before it could eat any of the sheep. When the villagers saw that there was no wolf, they left muttering under their breath

about how the boy had wasted their time. The next day, the boy cried once more, "Wolf! Wolf!" and, again, the villagers rushed there to chase the wolf away.

The boy laughed at the fright he had caused. This time, the villagers left angrily. The third day, as the boy went up the small hill, he suddenly saw a wolf attacking

his sheep. He cried as hard as he could, "Wolf! Wolf! Wolf!", but not a single villager came to help him. The villagers thought that he was trying to fool them again

and did not come to rescue him or his sheep. The little boy lost many sheep that day, all because of his foolishness. """
    
    f.write(s)
    f.close()

    f=open("Boy_Wolf.txt","w")
    
    s="""In a village, lived a _ _ _ _ _ _ _ _(1.Adjective) boy with his father. The boy's father told him that he was old _ _ _ _ _ _(2.Deteminer) to watch over the

sheep while they graze in the fields. Every day, he had to take the sheep to the _ _ _ _ _ _(3.Adjective) fields and watch them as they graze. However,

the boy was  _ _ _ _ _ _ _ (4.Adjective) and didn't want to take the sheep to the fields. He _ _ _ _ _ _(5.Verb) to run and play. So, he decided to have some fun.

He cried, "Wolf! Wolf!" until the entire _ _ _ _ _ _ _(6.Noun) came running with stones to _ _ _ _ _(7.Verb) away the wolf before it could eat any of the sheep.

When the villagers saw that there was no wolf, they left _ _ _ _ _ _ _ _ _ (8.Noun) under their breath about how the boy had _ _ _ _ _ _(9.Adjective) their time.

The next day, the boy cried once more, "Wolf! Wolf!" and, again, the villagers _ _ _ _ _ _(10.Adjective) there to chase the wolf away.The boy laughed at the

_ _ _ _ _ _ (11.Noun) he had caused. This time, the villagers left _ _ _ _ _ _ _(12.Adverb). The third day, as the boy went up the small hill, he suddenly saw a wolf

_ _ _ _ _ _ _ _ _(13.Adjective)his sheep. He cried as hard as he could, "Wolf! Wolf! Wolf!", but not a single villager came to help him. The villagers thought that he was trying to fool them again

and did not come to _ _ _ _ _ _(14.Verb) him or his sheep. The little boy lost many sheep that day, all because of his _ _ _ _ _ _ _ _ _ _ _(15.adjective)."""

    
    f.write(s)
    f.close()

    f=open("Boy_Wolf_ans.dat","wb")
    ans={1:"carefree",2:"enough",3:"grassy",4:"unhappy",5:"wanted",6:"village",7:"chase",8:"muttering",9:"wasted",10:"rushed",11:"fright",12:"angrily",
         13:"attacking",14:"rescue",15:"foolishness"}
    pickle.dump(ans,f)
    f.close()
Boy_Wolf()
