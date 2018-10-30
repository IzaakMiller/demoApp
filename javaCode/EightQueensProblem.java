/** Izaak Miller
*  Eight Queens Problem
* */

import java.util.Scanner;

public class EightQueensProblem{
  static int[][] board;
  static Scanner scan = new Scanner(System.in);
  static int rowSize, colSize;

  public static void main(String args[]){
    takeInput();
    placeQueen(0);
  } //main

  public static void takeInput() {
    System.out.println("Do you want to use an 8x8 of the problem? (Yes/No)");
    String input = scan.next();

    if(input.equalsIgnoreCase("Yes")){
      rowSize = colSize = 8;
    } else if(input.equalsIgnoreCase("No")){
      System.out.println("How many rows and columns do you want?");
      rowSize = scan.nextInt();
      colSize = rowSize;
    } else{ //else-if
      System.out.println("Wrong input");
    } //else

    createBoard(rowSize, colSize);
  }

  public static void createBoard(int row, int col){
    board = new int[row][col];
    for(int i = 0; i < row; i++){
      for(int j = 0; j < col; j++){
        board[i][j] = 0;
      } //for
    } //for
  }

  public static void placeQueen(int row){
    for (int col = 0; col < colSize; col++) {
      if (isLegalPlacement(row,col)){
        addQueen(row, col);
        if (row == rowSize - 1) {
          printSolutionAndExit();
        } else {
          placeQueen(row+1);
        } //else
        board[row][col] = 0;
      } //if
    } //for
  } //placeQueen

  public static boolean isLegalPlacement(int row, int col){
    int x = col, y = col;
    if (row == 0) {
      return true;
    } //if
    else{
      for(int i = row-1; i >= 0; i--){
        if(board[i][col] == 1){
          return false;
        } //if
        if(x > 0){
          if (board[i][--x] == 1)
          {
            return false;
          } //if
        } //if
        if(y < rowSize-1) {
          if (board[i][++y] == 1){
            return false;
          } //if
        } //if
      } //for
      return true;
    } //else
  } //isLegalPlacement

  public static void addQueen(int row, int col){
    board[row][col] = 1;
  } //addQueen

  public static void printSolutionAndExit(){
    for(int i = 0; i < rowSize; i++){
      System.out.print("\n");
      for(int j = 0; j < colSize; j++){
        if(board[i][j] == 0){
          System.out.print("-");
          System.out.print(" ");
        } //if
        if(board[i][j] == 1){
          System.out.print("Q");
          System.out.print(" ");
        } //if
      } //for
    } //for
    System.out.println("\n");

  } //printSolutionAndExit

} //EightQueens
