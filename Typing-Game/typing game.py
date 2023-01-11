import random, time
import sqlite3
con = sqlite3.connect('SQL w Python/Book Excerpts.db')

fin_text = []
def pickText(x):
    cur = con.cursor() 
    rand_ex = cur.execute ("select text from excerpts order by random() limit 1").fetchall()
    rand_ex = [i[0] for i in rand_ex]
    rand_ex = " ".join(rand_ex)
    text = rand_ex.split()
    a = len(text) - x
    a = random.randint(1,a)
    i = 0
    while i < x:
        fin_text.append(text[a-1])
        a += 1
        i += 1

diff = input("Welcome to Cow's Typing Game! Choose your difficulty. Short, Med, or Long? ")
if diff.lower() == "short":
    ex_length = random.randint(10,15)
elif diff.lower() == "med" or "medium":
    ex_length = random.randint(20,25)
elif diff.lower() == "long":
    ex_length = random.randint(30,40)
else:
    print("Could not read input, please run again.")
    exit()
pickText(ex_length)

fin_text = " ".join(fin_text)
print("Your text to type is:\n" + fin_text)

timer = 3
while timer > 0:
    print(timer)
    timer -= 1
    time.sleep(1)

start = time.time()
player_text = input("Start typing! \n")
end = time.time()
seconds = round((end - start),2)

player_text = player_text.split()
fin_text = fin_text.split()
score = 0

for i in range(0, len(player_text)):
    if player_text[i] == fin_text[i]:
        score += 1
score = 100 * (score/len(fin_text))
score = str(round(score,2))
print("You took %s seconds and you had %s percent accuracy!" % (seconds, score))

con.close