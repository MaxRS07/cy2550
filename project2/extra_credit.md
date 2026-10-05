
## Extra Credit

Ciphertext: `A̯ǎa̮A̯a̯a̮A̯a̮a̯A̯a̯a̮A̮ǎa̮Ǎa̯a̯A̮a̮ǎǍa̯a̮...`

Observation:
1. 27 lines and 10580 characters
2. there are 3 different kinds of accesnt marks (u below, n below, v above).
3. capital A every 3 characters

Approach:

1. First I split the ciphertext into groups of three characters split by the capital A. I extracted the accent marks and tried to convert them to base-3 integers (0..26) and mapped it to the alphabet. I assigned values 0..2 to each caron/breve type and tested the output in cyberchef, but the entropy was too high for any of them to be useful. I couldn't think of any other 3 character languages so I took a break from the idea.

2. I then tried to work backwards from the clue. I assumed it was going to be a reference to either Rick and Morty or Rick Astley's _Never Gonna Give You Up_. I knew the ladder was a safer bet so I extracted the unicode accent marks into a file and asked Claude to map the accent marks to the lyrics of _Never Gonna Give You Up_. It used frequency analysis to discover a morse code mapping where 

a caron `ǎ` = "."
upside-down breve `a̯` = "-"
breve `a̮` = " " (space)

(Looking back, I should have guessed that mapping since it uses 3 characters as well.)

This produces a very clean cipher text:

`NMTO EW UDIIPQVZU DF TQFV GQE BVQG KPG BLTGC RVF CF LQ S...`

At this point the mapping becomes pretty transparent, when you pass it through the Vignere ciper with key "RICK" from the hint it produces the lyrics:

`WERE NO STRANGERS TO LOVE YOU KNOW THE RULES AND SO DO I A FULL COMMITMENTS WHAT IM THINKING OF YOU WOULDNT GET THIS FROM ANY OTHER GUY I JUST WANNA TELL YOU HOW IM FEELING GOTTA MAKE YOU UNDERSTAND NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN NEVER GONNA RUN AROUND AND DESERT YOU NEVER GONNA MAKE YOU CRY NEVER GONNA SAY GOODBYE NEVER GONNA TELL A LIE AND HURT YOU WEVE KNOWN EACH OTHER FOR SO LONG YOUR HEARTS BEEN ACHING BUT YOURE TOO SHY TO SAY IT INSIDE WE BOTH KNOW WHATS BEEN GOING ON WE KNOW THE GAME AND WERE GONNA PLAY IT ANNNNND IFYOU ASK ME HOW IM FEELING DONT TELL ME YOURE TOO BLIND TO SEE NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN NEVER GONNA RUN AROUND AND DESERT YOU NEVER GONNA MAKE YOU CRY NEVER GONNA SAY GOODBYE NEVER GONNA TELL A LIE AND HURT YOU NEVER GONNA GIVE YOU UP NEVER GONNA LETYOU DOWN NEVER GONNA RUN AROUND AND DESERT YOU NEVER GONNA MAKE YOU CRY NEVER GONNA SAY GOODBYE NEVER GONNA TELL A LIE AND HURT YOU GIVEYOU UP GIVE YOU UP GIVE YOU UP GIVE YOU UP NEVER GONNA GIVE NEVER GONNA GIVE GIVE YOU UP NEVER GONNA GIVE NEVER GONNA GIVE GIVE YOU UP WEVE KNOWN EACH OTHER FOR SO LONG YOUR HEARTS BEEN ACHING BUT YOURE TOO SHY TO SAY IT INSIDE WE BOTH KNOW WHATS BEEN GOING ON WE KNOW THE GAME AND WERE GONNA PLAY IT I JUST WANNA TELL YOU HOW IM FEELING GOTTA MAKE YOU UNDERSTAND NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN NEVER GONNA RUN AROUND AND DESERT YOU NEVER GONNA MAKE YOU CRY NEVER GONNA SAY GOODBYE NEVER GONNA TELL A LIE AND HURT YOU NEVER GONNAGIVE YOU UP NEVER GONNA LET YOU DOWN NEVER GONNA RUN AROUND AND DESERT YOU NEVER GONNA MAKE YOU CRY NEVER GONNA SAY GOODBYE NEVER GONNA TELL A LIE AND HURT YOU NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN NEVER GONNA RUN AROUND AND DESERT YOU NEVER GONNA MAKE YOU CRY NEVER GONNA SAY GOODBYE NEVER GONNA TELL A LIE AND HURT YOU`