# La Casa De Papel

> Word on the street is Bob's about to make a big withdrawal. Too bad you're the one holding his ID. Can you charm Alice into making the transfer before she catches on?

## About the challenge

After looking at `chall.py`  , I learned the following:-

1. Option 1 takes in our input, appends it to a `secret`  (Which we dont know) and performs two encryptions on it. The first is an MD5 hash and the second is BASE64. 

2. Option 2 requires us to give two inputs. The first is `Bob` and the second is the MD5 hash of Bob using the same secret as the Option 1 uses. If we give the correct values, we get a new different secret in return.

3. Option 3 asks for a vault password which is the likely what we get from Option 2 or some encryption of it.


## How to solve

Since MD5 is irreversible under normal circumstances I researches and found about the flaw in MD5 which is length extension attacks. This does not require knowing the secret at all and is a major known issue with MD5. 

I found this video which explained it very well [link](https://www.youtube.com/watch?v=QLSlKxAQD8I)

A good tool to do this is a python module called hashpumpy. However it is not required in this case as the challenge itself provides the encoder in the form of Option 1. 

So the steps for the solution are simple :-

1. Select Option 1 and enter Bob, we will get back the hmac for Bob as a response

    ```
    1. Practice Convo
    2. Let's Fool Alice!
    3. Crack the Vault
    4. Exit
    Choose an option: 1
    Send a message: Bob
    Here is your encrypted message: YjRlMGE4MDI0MjhjYjM1ZjY5YzBlOTUyZDk2MTcyZDY=
    ```

2. Select Option 2 and enter username as Bob and HMAC as BASE64 decoded of the output of option 1. This will give us the vault password.

    ```
    1. Practice Convo
    2. Let's Fool Alice!
    3. Crack the Vault
    4. Exit
    Choose an option: 2

    Bot: Okay, let's see if you're the real deal. What's your name?
    Your name: Bob

    Bot: Please provide your HMAC
    Your HMAC: b4e0a802428cb35f69c0e952d96172d6

    Alice: Oh hey Bob! Here is the vault code you wanted:
    G0t_Th3_G0ld_B3rl1nale
    ```

3. Enter the Vault password obtained in previous step and Voila!

    ```
    1. Practice Convo
    2. Let's Fool Alice!
    3. Crack the Vault
    4. Exit
    Choose an option: 3

    Vault Person: Enter password
    Password: G0t_Th3_G0ld_B3rl1nale

    Vault Unlocked! The flag is: nite{El_Pr0f3_0f_Prec1s10n_Pl4ns}
    ```

```
nite{El_Pr0f3_0f_Prec1s10n_Pl4ns}
```

