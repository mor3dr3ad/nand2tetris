// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
// Pseudocode:
// Initialize anything?
// (LOOP)
  // read keyboard
  // if 0 
  // check if everything was already white:
  //  yes:keep it
  //  no: change it
  // if not 0 
  // check if screen is black
  //   yes: keep it
  //   no: change it

  // initialization
  @status
  M=-1  // set status to black=0xFFFF

  D=0 // Save 0 to D. Argument - what to set screen bits to
  @SETSCREEN
  0;JMP


(LOOP)
  @KBD
  D=M // D = current KBD input
  @SETSCREEN
  D;JEQ // if no key, go to (SETSCREEN) 
  D=-1 // if a key has been pressed, set screen to all 1 bits (black)


(SETSCREEN)
  @arg
  M=D // set the current status (lines 31 and 39) to arg, 0 to start with 
  @status 
  D=D-M // D = status_of_current_run - status_of_previous_run -> compare status against each other; 0 if equal
  @LOOP
  D;JEQ //if status_of_current_run == status_of_previous_run, start from (LOOP)

  // this only executes if @status != equal
  @arg
  D=M // load current status
  @status
  M=D // save current status 

  @screen
  D=A //D = Screen address
  @8192 // number of registers in screen: 8191
  D=D+A //D=Byte just past last screen address
  @i
  M=D // i = Byte just past last screen address

(SETLOOP)
  @i
  D=M-1
  M=D // i = i-1
  @LOOP
  D;JLT // if i<0 goto LOOP

  @status
  D=M
  @i
  A=M //indirect
  M=D // M[current screen address]=status
  @SETLOOP
  0;JMP



