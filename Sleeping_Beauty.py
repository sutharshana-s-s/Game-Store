import pickle

def Sleeping_Beauty():
    f=open("Sleeping_Beauty_final.txt","w")
    
    s="""Once there was a princess named Aurora,the much-awaited daughter of the king and queen,who was cursed by an evil witch,to die by the prick from the spindle of a spinning wheel

because her parents did not invite the witch to her Christening.Fortunately,one of the good fairies who had been invited to the Christening was able to help.Though the princess would still

have to be pricked, she would not die,but sleep for a hundred years.She was blessed by the other good fairies,and so grew up to be a beautiful,kind and obedient young girl who was often

called Briar Rose.The people allover the kingdom destroyed all the spinning wheels obeying the order of their king so as to save the princess.As predicted,on her sixteenth birthday,Aurora

was pricked on her finger by a spinning wheel brought by an evil witch dressed up like an old woman and fell into a deep sleep.Along with her every men,women,children and animals in the castle

fell asleep due to the spell casted by the good fairy.Hundred years later,a young prince named Phillip tried to get into the castle,in order to see the famous beauty that had been asleep for

so long.When he found her,he was stunned by her beauty and leaned in for a kiss but unfortunately he had to win the witch in order to wake the princess.He defeated the witch with a magical

sword given by the good fairy and he kissed the princess which broke the curse,and soon everyone in the castle was awaken from their long,hundred years of sleep.The prince and

princess were married,and the kingdom was happy and peaceful once again.\nSleeping beauty teaches us that even though evil can sometimes interrupt our lives,goodness can soften the blow

and eventually,evil will be overcomed."""
    
    f.write(s)
    f.close()

    f=open("Sleeping_Beauty.txt","w")
    
    s="""Once there was a _ _ _ _ _ _ _ _ (1. Noun) named Aurora,the much-awaited daughter of the king and queen,who was _ _ _ _ _ _ (2. Adjective) by an evil witch,to die by the

_ _ _ _ _ (3. Verb) from the spindle of a spinning wheel because her parents did not invite the witch to her Christening.Fortunately,one of the good fairies who had been invited to the

Christening was able to help.Though the princess would still have to be pricked, she would not die,but sleep for a _ _ _ _ _ _ _ (4. Number) years.She was _ _ _ _ _ _ _ (5. Verb) by the

other good fairies,and so grew up to be a beautiful,kind and _ _ _ _ _ _ _ _ (6. Adjective) young girl who was often called Briar Rose.The people allover the kingdom destroyed all the spinning

wheels obeying the order of their king so as to save the princess.As predicted,on her _ _ _ _ _ _ _ _ _ (7. Number) birthday,Aurora was pricked on her finger by a spinning wheel brought by an

evil witch dressed up like an old woman and fell into a deep sleep.Along with her every men,women,children and animals in the castle fell asleep due to the _ _ _ _ _ (8. Noun) casted by the

good fairy.Hundred years later,a young prince named Phillip tried to get into the _ _ _ _ _ _ (9. Noun) ,in order to see the famous beauty that had been asleep for so long.When he found

her,he was _ _ _ _ _ _ _ (10. Adjective) by her beauty and leaned in for a kiss but unfortunately he had to win the witch in order to wake the princess.He _ _ _ _ _ _ _ _ (11. Verb) the witch

with a _ _ _ _ _ _ _ (12. Adjective) sword given by the good fairy and he _ _ _ _ _ _ (13. Verb) the princess which broke the curse,and soon everyone in the castle was awaken from their long,

hundred years of sleep.The prince and princess were married,and the _ _ _ _ _ _ _ (14. Noun) was happy and peaceful once again.\nSleeping beauty teaches us that even though evil can sometimes

_ _ _ _ _ _ _ _ _ (15. Verb) our lives,goodness can soften the blow and eventually,evil will be overcomed."""
    
    f.write(s)
    f.close()

    f=open("Sleeping_Beauty_ans.dat","wb")
    ans={1:"princess",2:"cursed",3:"prick",4:"hundred",5:"blessed",6:"obedient",7:"sixteenth",8:"spell",9:"castle",10:"stunned",11:"defeated",12:"magical",13:"kissed",14:"kingdom",15:"interrupt"}
    pickle.dump(ans,f)
    f.close()
Sleeping_Beauty()
