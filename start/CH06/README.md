# Hacking linux passwords
Linux passwords are stored in the file /etc/shadow, which is only readable by root. This restriction is added because if you can read the passwords, you can hack the passwords.
These arent the passwords, but hashes of the passwords. Hashing is similar to encryption, but is a one-way process and can't be unencrypted. This means the actual password cant be retrieved from the hash
We can however **guess** at the contents, and then hash them to see if they match

# Breakdown of /etc/shadow
Sample line from /etc/shadow. Username **justincase**, password **Password01**
`justincase:$6$G.DTW7g9s5U7KYf5$xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p.:18617:0:99999:7:::`

The password hash is between 1st and 2nd colons (`$6$G.DTW7g9s5U7KYf5$xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p.` in the example above)
The password hash is made up of:
 1. the first few characters define the hashing algorithm: (`$6` in the example above)
   - $1=MD5
   - $2=Blowfish
   - $2a=eksblowfish
   - $5=SHA-256
   - $6=SHA-512
 2. A SALT which is between the 2 dollar signs (`G.DTW7g9s5U7KYf5` in the example above)
   - Note: the SALT is random and is used to complicate the HASH
   - This ensures if 2 passwords are the same, the HASH is different
 3. The hash of the salted password (`xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p.`)

# Creating password hashes
Uses **crypt** module. NOTE: this is a Linux module and may not work on other operating systems. There are similar modules for Windows, search Google for the best option.
Possibly start in interactive mode. Show without / with SALT
```
import crypt
print(crypt.crypt("Password01")
print(crypt.crypt("Password01", "$6$G.DTW7g9s5U7KYf5$")
```
Use **passHasher.py** to show different encryption methods (not all are available)
Demonstrate how the SALT changes the HASH
If same password and salt are used, resultant HASH is the same -- this is how passwords work

# Guessing passwords
Create script that prompts for:
1. Hashed password from /etc/shadow
2. The SALT to use
3. Plaintext password

Create a function called **testPass** that hashes the plaintext password with the salt and compares with the hashedPass
If the hashes match, return **True**, else return **False**

# Dictionary attack
Extend guessing script to include
- Reading plaintext password from a file
- 1 at a time, tries the passwords
- When a match is found, program quits and reports the correct password

**NOTE:** For testing you may want to limit the dictionary file to ~10 passwords and use #5 as the hashed password
Most common passwords pulled from https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

# Brute Force attack
Example of how a brute force attack works. See image of bike combo lock with 4 numbers, each ranging 0-9
![](https://thebestbikelock.com/wp-content/uploads/2019/10/combination-lock.jpg)

To brute force this, you start at `0000`, then `0001`, and so on until you reach `9999` or the correct answer
If you dont know the length of the password, you start at `0` and keep going until `9999999999999`

This example is similar to the Dictionary attack and uses same **testPass** function.Instead of reading from a file, we do a `for i in range(100000)`
This example is simplified to only numbers. Use debugger if needed to highlight how each number in turn is being tested.

More complex brute forcing includes larger character sets such as those shown below. This obviously complicates and slows the process, explaining why this may be the last choice in an attack
- abcdefghijklmnopqrstuvwxyz
- ABCDEFGHIJKLMNOPQRSTUVWXYZ
- 0123456789
- 0123456789abcdef
- 0123456789ABCDEF
- «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
- ?l?u?d?s
- 0x00 - 0xff


# Other suggestions
Have students create process that separates hashed password into SALT and HASH so that it is no longer prompted
Have students create script that opens a shadow file and pulls out the hashes for attacking
