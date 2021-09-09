

Chess
=====

Code up a chess system where the input are chess notations and the output would be the current board conditions

* The notations and board representation are up to the candidates
* A consistent and logical representation should be printed




#### My attempt

Sample
```
> e5
[
"RNBKQBNR",
"PPPP PPP",
"        ",
"    P   ",
"        ",
"        ",
"pppppppp",
"rnbkqbnr"
]
```



#### After 4 hours

I was able to create a fairly successful attempt with the following feature

##### Pieces

* Pawn
  * able to move 2 if unmoved (row 2 and 7)
  * able to capture diagonally
* Knight
  * Able to calculate its available moves
* Rook/Bishop/Queen
  * Will be stopped if something is blocking
 * King

 ##### Other feature

 * Use long notation like this `Ra1a5` or `Ng1h3` or `e2e4`
 * Note: pawn's piece notation can be omitted (can also use `p` instead)
 * Will not be able to eat ally pieces
 * Will ensure that players take turns

 TODO: 
 * Make a winning scenario (i.e. checkmate)
 * Resolve pinning
 * Castleing + En passant


 You can try it out by running the file by:
 ```
 python3 run.py
 ```

 Example run:
 ```
RNBQKBNR
PPPPPPPP
  

 

pppppppp
rnbqkbnr
Move: e2e4
[e3, e4]
RNBQKBNR
PPPPPPPP


     p

pppp ppp
rnbqkbnr
Move: e7e5
[e6, e5]
RNBQKBNR
PPPP PPP

     P
     p

pppp ppp
rnbqkbnr
Move: ng1f3
[h3, f3, e2]
RNBQKBNR
PPPP PPP

     P
     p
      n
pppp ppp
rnbqkb r
Move: ng1f3
[a6, c6, d7]
R BQKBNR
PPPP PPP
   N
     P
     p
      n
pppp ppp
rnbqkb r
Move: 
```
