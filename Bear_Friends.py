import pickle

def Bear_Friends():
    f=open("Bear_Friends_final.txt","w")
    
    s="""One day, two best friends were walking on a lonely and dangerous path through a jungle. As the sun began to set, they grew afraid but held on to each other.

Suddenly, they saw a bear in their path. One of the boys ran to the nearest tree and climbed it soon. The other boy did not know how to climb the tree by himself,

so he lay on the ground, pretending to be dead. The bear approached the boy on the ground and sniffed around his head. After appearing to whisper something in the

boy's ear, the bear went on its way.The boy on the tree climbed down and asked his friend what the bear had whispered in his ear. He replied, "Do not trust friends

who do not care for you." """
    
    f.write(s)
    f.close()

    f=open("Bear_Friends.txt","w")
    
    s="""One day, two _ _ _ _(1.Verb) friends were walking on a lonely and _ _ _ _ _ _ _ _ _ (2.Adjective) path through a jungle. As the sun _ _ _ _ _ (3.Verb) to

set, they grew _ _ _ _ _ _ (4.Adjective) but held on to each other. Suddenly, they saw a bear in their _ _ _ _(5.Noun). One of the boys ran to the

_ _ _ _ _ _ _(6.Adjective) tree and climbed it soon. The other boy did not know how to _ _ _ _ _ (7.Verb) the tree by himself,so he lay on the ground,

_ _ _ _ _ _ _ _ _ _ (8.Verb) to be dead. The bear _ _ _ _ _ _ _ _ _ _(9.Verb) the boy on the ground and sniffed _ _ _ _ _ _(10.Adverb) his head. After appearing to

_ _ _ _ _ _ _ (11.Verb) something in the boy's ear,the _ _ _ _ (12.Noun) went on its way. The boy on the tree climbed down and _ _ _ _ _ (13.Verb)his friend what

the bear had whispered in his _ _ _(14.Noun). He replied, "Do not _ _ _ _ _(15.Noun) friends who do not care for you." """

    
    f.write(s)
    f.close()

    f=open("Bear_Friends_ans.dat","wb")
    ans={1:"best",2:"dangerous",3:"began",4:"afraid",5:"path",6:"nearest",7:"climb",8:"pretending",9:"approached",10:"around",11:"whisper",12:"bear",13:"asked",
         14:"ear",15:"trust"}
    pickle.dump(ans,f)
    f.close()
Bear_Friends()
