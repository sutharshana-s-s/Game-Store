import pickle

def Max_Aliens():
    f=open("Max_Aliens_final.txt","w")
    
    s="""It was a dark and stormy night. The town of Greentown was covered by dark clouds.Max was returning home. It started raining cats and dogs. Suddenly he saw

an U.F.O. appearing from the clouds above. In no time it landed on the road. Three aliens came out. Max was astonished as he could understand their language.

Their plan was to take all the trees away from earth. Not wasting a moment, Max called his friends. Those aliens pointed out to a tree """
    
    f.write(s)
    f.close()

    f=open("Max_Aliens.txt","w")
    
    s="""It was a dark and _ _ _ _ _ _(1.Adjective) night. The town of Greentown was _ _ _ _ _ _ _(2.Verb) by dark clouds. Max was _ _ _ _ _ _ _ _ _(3.Verb) home.

It started _ _ _ _ _ _ _ (4.Verb) cats and dogs. _ _ _ _ _ _ _ _(5.Adverb) he saw an U.F.O. _ _ _ _ _ _ _ _ _(6.Verb) from the clouds above. In no time it

_ _ _ _ _ _(7.Adjective) on the road. Three _ _ _ _ _ _ (8.Noun) came out.Max was _ _ _ _ _ _ _ _ _ _(9.Adjective) as he could _ _ _ _ _ _ _ _ _ _(10.Verb) their

language. Their _ _ _ _ (11.Noun) was to take all the trees _ _ _ _ (12.Adverb) from earth. Not _ _ _ _ _ _ _ (13.Adjective) a moment, Max called his

_ _ _ _ _ _ _(14.Noun). The aliens _ _ _ _ _ _ _(15.Adjective) out to a tree """

    
    f.write(s)
    f.close()

    f=open("Max_Aliens_ans.dat","wb")
    ans={1:"stormy",2:"covered",3:"returning",4:"raining",5:"suddenly",6:"appearing",7:"landed",8:"aliens",9:"astonished",10:"understand",11:"plan",12:"away",
         13:"wasting",14:"friends",15:"pointed"}
    pickle.dump(ans,f)
    f.close()

