# Mumbo Dumbo

> Deep within the void lies the Key, shrouded in secrecy and guarded by the enigmatic Keeper. Created for a single purpose, the Keeper has vowed to protect the Key, its defenses said to be unbreakable.

> But whispers tell of a flaw-a hidden crack in its impenetrable armor. Those who dare to seek the Key must tread lightly, for the Keeper is cunning and relentless, answering only to the most devious of minds.

> Will you uncover the Keeper's secret, or be lost in the void forever?

> `ncat --ssl mumbo-dumbo.chals.nitectf2024.live 1337`

## About the challenge 

The challenge gives us a python file and an ncat link.

The goal is to get the AI (keeper) to give us the flag by entering the correct phrase/command.

## How to Solve

The first task after connecting to the server is a proof of work that requires us to download and run the python file with a given input.

![alt text](images/image.png)

After this the conversation with the AI begins.

After chatting with it for a few minutes I noticed that it kept repeating a certain phrase and it also capitalised for no logical reason. So i simply entered the phrase as is and that gave me the flag.

![alt text](images/end.png)

```
nite{C@TCHME!FY0UCAN}
```
