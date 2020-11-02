import random
possible = [ "It is certain.","It is decidedly so.","Without a doubt.","Yes – definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Signs point to yes.","Reply hazy, try again.","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook is not so good","Very doubtful","Yes"]


# input("Ask Away: ")
# print(possible[answer])
for i in range(20):
    answer = random.randint(0,19)
    print(possible[answer])