// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
// Pseudocode:
// Set R2 to 0  
// Set i to 0
// 
//   While i < R1
//   R2 = R2 + R0   
//   i++


  @R2
  M=0 // set R2 to 0
  @i
  M=0 // set i to 0

(LOOP)
  @i 
  D=M // initialized with 0 
  @R0
  D=D-M // D = i - R0 
  @END
  D;JGE // if i>=n, then end loop 

  @R1
  D=M // save content of R1 to D
  @R2
  M = M + D // add R1 to R2 for as long as the loop runs
  @i
  M = M + 1
  @LOOP
  0;JMP // else continue loop 

(END)
  @END
  0;JMP
