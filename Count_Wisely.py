import pickle

def Count_Wisely():
    f=open("Count_Wisely_final.txt","w")
    
    s="""One day, king Akbar asked a question in his court that left everyone in the courtroom puzzled.As they all tried to figure out the answer, Birbal walked in and

asked what the matter was. They repeated the question to him. The question was, "How many crows are there in the city?"Birbal immediately smiled and went up to Akbar.

He announced the answer; he said there were twenty-one thousand, five hundred and twenty-three crows in the city. When asked how he knew the answer, Birbal replied,

"Ask your men to count the number of crows. If there are more, then the relatives of the crows must be visiting them from nearby cities. If there are fewer, then the

crows from our city must be visiting their relatives who live outside the city. "Pleased with the answer, Akbar presented Birbal with a ruby and pearl chain."""
    
    f.write(s)
    f.close()

    f=open("Count_Wisely.txt","w")
    
    s="""One day, king Akbar asked a _ _ _ _ _ _ _ _(1.Noun) in his court that left everyone in the _ _ _ _ _ _ _ _ _ (2.Noun) puzzled. As they all tried to figure out

the _ _ _ _ _ _ (3.Noun), Birbal walked in and asked what the _ _ _ _ _ _(4.Verb) was. They _ _ _ _ _ _ _ _ (5.Adjective) the question to him.The question was, "How

many crows are there in the city?"Birbal  _ _ _ _ _ _ _ _ _ _ _(6.Adverb) smiled and went up to Akbar. He _ _ _ _ _ _ _ _ _(7.Verb) the answer; he said there were

twenty-one  _ _ _ _ _ _ _ _(8.Number), five hundred and twenty-three crows in the city. When asked how he knew the answer,  _ _ _ _ _ _(9.Noun) replied, "Ask your men

to  _ _ _ _ _(10.Verb) the number of crows. If there are more, then the _ _ _ _ _ _ _ _ _(11.Noun) of the crows must be  _ _ _ _ _ _ _ _(12.Adjective) them from nearby

cities. If there are _ _ _ _ _ (13.Pronoun), then the crows from our city must be visiting their relatives who live  _ _ _ _ _ _ _(14.Adjective) the city.Pleased with

the answer, Akbar _ _ _ _ _ _ _ _ _(15.Verb)  Birbal with a ruby and pearl chain."""

    
    f.write(s)
    f.close()

    f=open("Count_Wisely_ans.dat","wb")
    ans={1:"question",2:"courtroom",3:"answer",4:"matter",5:"repeated",6:"immediately",7:"announced",8:"thousand",9:"Birbal",10:"count",11:"relatives",12:"visiting",
         13:"fewer",14:"outside",15:"presented"}
    pickle.dump(ans,f)
    f.close()
Count_Wisely()
