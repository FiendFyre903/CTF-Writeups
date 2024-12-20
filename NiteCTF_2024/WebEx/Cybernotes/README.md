# Cybernotes

> I created the world's most secure notes app, but might have uploaded and forgotten about some personal files. Whatever,even if they try to look they will go in the wrong place.

## About the Challenge

We are given a link to a notes website https://cyber-notes.chalz.nitectf2024.live/ 

## How to Solve

The challenge desc mentions uploaded files. Inspecting the sources, I found two things of interest 
1. A directory called `uploads` that didnt contain anything useful.
2. Two paths in the javascript, `/uploads` and `/api/notes`.
 
`/api/notes` gave the following error implying that the site is expecting a specific token to be present.

![alt text](images/img1.png)

However `/uploads` was a jackpot with a bunch of log files and one docker file.

The log files contained old chat logs between a few different users with a pretty good storyline. Reading through the chat logs gave me a username and password.

```
Username - D3aDs0ck <br>
Password - bluM#_M@y_N3vr
```

I also got the following from the docker file :-

```
ENV JWT_SECRET_KEY=H6jga21h1
ENV FDRP_JWT_SECRET_KEY=wEdAeLdjae
```

Logging in with the user name i got, i was taken to `https://cyber-notes.chalz.nitectf2024.live/#/notes`. 

There were some notes with recipes on them, and the only pattern I found was that each recipe had exactly 4 numbers somewhere in the text. The numbers were `3745 6237 4536` 

Since my previous try with notes had mentioned a token, I went looking for whether one was generated this time.
I searched for token in the javascript source code and found this

![alt text](images/img2.png)

I went to the local storage and found a token with the value `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ0FBQUFBQm5aUEtTQm9vVGdYRHEtNjhJc1p6Umd3NHNseTNldk42U2VRbUR5bENiZmFGM213WU9BZVJWbUlrLXBuck5ZeUNUd09jTGFBZHNZbEdJZXNTdlNyUVJrYWZ3WkE9PSIsImV4cCI6MTczNDY3MDgwMH0.qAD594oyF1qzeiuxfho5Q5o0pUA75Kbf0fyxWFRo8vs`

The docker file had mentioned JWT, which is a JSON Web Token and this value matched the format.

I found a website to help decode the token (link [here](https://jwt.io/)) and got the output:-

![alt text](images/img3.png)

The user_id looked to be fernet because of the startign gAAAAA however decoding did not give any meaningful result.

The site also mentioned invalid signature so I entered the value i got in the docket file `H6jga21h1`. This modified the JWT. After this I was stuck for a long time and spent a long time trying to decode the token but was unseccesful. Eventually just to try it, i simply plugged the token generated using the docker key and reloaded the webpage. This worked and I got the flag.

![alt text](images/img4.png)

```
nite{7rY_XKcD_S3b_f0R_3xPl4nA7i0n}
```
