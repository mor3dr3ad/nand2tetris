// This script works, however there is a performance problem:
// the script ALWAYS paints the screen white whether or not it has been white already. Same for black. 
// So it needs a logic for storing the current status of the screen and comparing it with the desired status.


  @KBD
  D=A // keyboard address to D
  @n
  M=D  // save keyboard address to n
  @SCREEN
  D=A
  @n
  M=M-D // amount of registers to be manipulated between screen and keyboard

(LOOP) // set the break parameter here
  @i
  M=0 // initialize i to 0

  @SCREEN
  D=A
  @pixel
  M=D // use pixel as pointer to the RAM manipulated. initially pixel will equal screen.

  @KBD
  D=M
  @BLACK
  D;JGT // if KBD > 0 a key is pressed. if key is pressed, jump to black branch, otherwise to white branch. 

(WHITE)
  @i
  D=M
  @n
  D=D-M // subtract number of registers to be manipulated from counter i, this will be negative until it isn't
  @LOOP
  D;JEQ // if i==n, break. i.e. go back and re-listen to keyboard and reinitiate. Otherwise, continue

  @pixel
  D=M
  @i
  A=D+M
  M=0 // set Register to 0 (white)
  
  @i
  M=M+1 //i++

  @WHITE
  0;JMP

(BLACK)
  @i
  D=M
  @n
  D=D-M
  @LOOP
  D;JEQ

  @pixel
  D=M
  @i
  A=D+M
  M=-1

  @i
  M=M+1

  @BLACK
  0;JMP

  @LOOP
  0;JMP
