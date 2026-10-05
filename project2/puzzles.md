## Puzzle 1

Cipher: `GZKoGZKoGZKnGZHuGZHoGZHnGZKuGZHuGHKnGZKuGZKuGHKnGZKuGHHuGZHnGZHuGZHoGZHnGZKuGZHoGZKnGZHuGZHoGZHnGZKuGZKoGHHnGZKuGZHoGZKnGZKuGHHoGHHnGZHuGZHoGZHnGZKuGZKuGHKnGZKuGZHuGHHnGZHuGZHoGZHnGZKuGZHuGZHnGZKuGZKoGZKnGZKuGHHoGHHnGZKuGHHuGZH`

Operations:

1. Vigenere cipher with key 'dirt'
2. Substitution cipher that maps QUERTY keyboard letters to alphabetical order
3. Base64 decode
4. Binary to ASCII

Plaintext: `I got a jar of dirt`

## Puzzle 2

Operations:

Ciphertext: `S NSSR NRE RRF URN U NSNU RNSS UNR URR EU NN S   UI NS RUN RU  SE CN ISCNR ICN CRUNERUCFS R  CIS N  I  S R  ER  FSURNS I SNU`

1. Substitution using table in image, which maps `CYBERISFUN` -> `0123456789` letter to number
2. Use a ceaser cipher box cipher with a width of 5, you must preserve spacing in the tool
3. Decode with multi-tap phone keypad
4. Use an atbash cipher to decode the message, with reverse on

Plaintext: `NOT ALL TREASURES SILVER AND GOLD`