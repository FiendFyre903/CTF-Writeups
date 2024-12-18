# BackTrack

Kenji is a nice guy who lives in Tokyo. He is in a dilemma. In 2017, he was late to an important meeting and is now facing repercussions. To defend himself, he needs to prove that it was not his fault. His evidence? The train he boarded that day, traveling between Omotesando and Suitengumae, was delayed. However, his boss is not providing the specific details of the accusation. Kenji vividly remembers one key fact: the train was around 61 minutes late.

Help him uncover the exact date of the incident and the start time of the delay. Justice for Kenji!

#### Flag Format: nite{time_date} <br>Example: nite{13:00_3January}

# About the challenge

The challenge wants us to find the exact start time and date of an event(Train Delay) that matches the clues given.

# How to Solve

There is one line connecting Omotesando and Suitengumae and it is the Hanzomon Line.

The [tokyo metro website](https://www.tokyometro.jp/lang_en/delay/history/hanzomon.html) tracked delays but it only showed the details of the last 35 days

Using the wayback machine(link [here](https://web.archive.org/web/20170326043929/https://www.tokyometro.jp/lang_en/delay/history/hanzomon.html)), I looked at old snapshots of the website in 2017 (There were multiple).

Going chronologically, the first match that I found was on 20th Feb at 17:00 

I tried `nite{17:00_20February}` and it worked!

```
nite{17:00_20February}
```




