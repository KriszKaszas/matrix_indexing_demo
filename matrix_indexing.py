import os
import time


BLACK = "\u001b[0;30m"
RED = "\u001b[0;31m"
GREEN = "\u001b[0;32m"
YELLOW = "\u001b[0;33m"
BLUE = "\u001b[1;34m"
MAGENTA = "\u001b[1;35m"
CYAN = "\u001b[1;36m"
DARK_CYAN = "\u001b[0;36m"
WHITE = "\u001b[0;37m"
BRIGHT_GREEN = "\u001b[1;32m"
BRIGHT_YELLOW = "\u001b[1;33m"
RED_BACKGROUND_BRIGHT = "\u001b[1;101m"
GREEN_BACKGROUND_BRIGHT = "\u001b[1;102m"
BLUE_BACKGROUND_BRIGHT = "\033[1;104m"
RESET = "\u001b[0m"



def print_matrix_as_code(demo_matrix, current_i_index, current_j_index):
    print("Code representation:")
    print(f"{CYAN}demo_matrix{RESET} = {YELLOW}[{RESET}", end="")
    for i in range(len(demo_matrix)):
        print(f"{MAGENTA}[{RESET}", end="")
        for j in range(len(demo_matrix[i])):
            if i == current_i_index and j == current_j_index:
                print(f"{GREEN_BACKGROUND_BRIGHT}{demo_matrix[i][j]}{RESET}", end="")
            elif i == current_i_index:
                print(f"{BLUE_BACKGROUND_BRIGHT}{demo_matrix[i][j]}{RESET}", end="")
            else:
                print(f"{DARK_CYAN}{demo_matrix[i][j]}{RESET}", end="")
            if j < len(demo_matrix[i])-1 and i == current_i_index:
                print(f"{BLUE_BACKGROUND_BRIGHT}, {RESET}", end="")
            elif j < len(demo_matrix[i])-1:
                print(", ", end="")
        print(f"{MAGENTA}]{RESET}", end="")
        if i != len(demo_matrix)-1:
            print(", ", end="")
    print(f"{YELLOW}]{RESET}")



def print_matrix_as_formatted_code(demo_matrix, current_i_index, current_j_index):
    print("\nFormatted code representation:")
    print(f"{CYAN}demo_matrix{RESET} = {YELLOW}[{RESET}", end="")
    for i in range(len(demo_matrix)):
        if i != 0:
                print("               ", end="")
        print(f"{MAGENTA}[{RESET}", end="")
        for j in range(len(demo_matrix[i])):
            if i == current_i_index and j == current_j_index:
                print(f"{GREEN_BACKGROUND_BRIGHT}{demo_matrix[i][j]}{RESET}", end="")
            elif i == current_i_index:
                print(f"{BLUE_BACKGROUND_BRIGHT}{demo_matrix[i][j]}{RESET}", end="")
            else:
                print(f"{DARK_CYAN}{demo_matrix[i][j]}{RESET}", end="")
            if j < len(demo_matrix[i])-1 and i == current_i_index:
                print(f"{BLUE_BACKGROUND_BRIGHT}, {RESET}", end="")
            elif j < len(demo_matrix[i])-1:
                print(", ", end="")
        print(f"{MAGENTA}]{RESET}", end="")
        if i != len(demo_matrix)-1:
            print(", " )
    print(f"{YELLOW}]{RESET}\n")



def print_for_loop_demo(i_index, j_index):
    print("Nested for loop for traversing the matrix:\n"
          f"{MAGENTA}for{RESET}{BLUE_BACKGROUND_BRIGHT} i {RESET}{MAGENTA}in {GREEN}range{YELLOW}({BRIGHT_YELLOW}len{MAGENTA}({CYAN}demo_matrix{MAGENTA}){YELLOW}){RESET}:\n",
          f"    {MAGENTA}for{RESET}{GREEN_BACKGROUND_BRIGHT} j {RESET}{MAGENTA}in {GREEN}range{YELLOW}({BRIGHT_YELLOW}len{MAGENTA}({CYAN}demo_matrix{RESET}{BLUE_BACKGROUND_BRIGHT}[i]{RESET}{MAGENTA}){YELLOW}){RESET}:\n",
          f"        {BRIGHT_YELLOW}print{YELLOW}({CYAN}demo_matrix{RESET}{BLUE_BACKGROUND_BRIGHT}[i]{RESET}{GREEN_BACKGROUND_BRIGHT}[i]{YELLOW}){RESET}"
        )
    print("                      ||")
    print("                      ||")
    print("                     \\  /")
    print("                      \\/")
    print("Nested for loop explained:\n"
          f"{BRIGHT_GREEN}#This line goes through the rows of the matrix from top to bottom.{RESET}\n\n"
          f"{MAGENTA}for{RESET}{BLUE_BACKGROUND_BRIGHT} i {RESET}{MAGENTA}in {GREEN}range{YELLOW}({BRIGHT_YELLOW}len{MAGENTA}({CYAN}demo_matrix{MAGENTA}){YELLOW}){RESET}:\n\n",
          f"    {BRIGHT_GREEN}#In each row of the matrix (the [i]-th row chosen by the outter for loop in the previous line)\n",
          f"    #this line goes through each element in the row{RESET}\n\n",
          f"    {MAGENTA}for{RESET}{GREEN_BACKGROUND_BRIGHT} j {RESET}{MAGENTA}in {GREEN}range{YELLOW}({BRIGHT_YELLOW}len{MAGENTA}({CYAN}demo_matrix{RESET}{BLUE_BACKGROUND_BRIGHT}[i]{RESET}{MAGENTA}){YELLOW}){RESET}:\n\n",
          f"        {BRIGHT_GREEN}#The matrix indexing is composed from the iterator of the outter forloop which\n",
          f"        #selects the matrix row (this iterator is named i) and the iterator\n",
          f"        #of the inner for loop which selects the element in the row (this iterator is named j){RESET}\n\n",
          f"        {BRIGHT_YELLOW}print{YELLOW}({CYAN}demo_matrix{RESET}{BLUE_BACKGROUND_BRIGHT}[i]{RESET}{GREEN_BACKGROUND_BRIGHT}[i]{YELLOW}){RESET}"
        )
    print("                      ||")
    print("                      ||")
    print("                     \\  /")
    print("                      \\/")
    print("Nested for loop demonstrated:\n"
          f"{MAGENTA}for{RESET}{BLUE_BACKGROUND_BRIGHT} {i_index} {RESET}{MAGENTA}in {GREEN}range{YELLOW}({BRIGHT_YELLOW}len{MAGENTA}({CYAN}demo_matrix{MAGENTA}){YELLOW}){RESET}:\n",
          f"    {MAGENTA}for{RESET}{GREEN_BACKGROUND_BRIGHT} {j_index} {RESET}{MAGENTA}in {GREEN}range{YELLOW}({BRIGHT_YELLOW}len{MAGENTA}({CYAN}demo_matrix{RESET}{BLUE_BACKGROUND_BRIGHT}[{i_index}]{RESET}{MAGENTA}){YELLOW}){RESET}:\n",
          f"        {BRIGHT_YELLOW}print{YELLOW}({CYAN}demo_matrix{RESET}{BLUE_BACKGROUND_BRIGHT}[{i_index}]{RESET}{GREEN_BACKGROUND_BRIGHT}[{j_index}]{YELLOW}){RESET}"
        )



def print_matrix_as_grid(demo_matrix, current_i_index, current_j_index):
    print("\nMatrix traversed step by step by the nested for loops:")
    print(f"                {CYAN}demo_matrix{RESET}{BLUE_BACKGROUND_BRIGHT}[{current_i_index}]{GREEN_BACKGROUND_BRIGHT}[{current_j_index}]{RESET}\n")
    for i in range(len(demo_matrix)):
        print("                    ", end="")
        for j in range(len(demo_matrix[i])):
            if i == current_i_index and j == current_j_index:
                print(f"{GREEN_BACKGROUND_BRIGHT}[{demo_matrix[i][j]}]{RESET}", end="")
            elif i == current_i_index:
                print(f"{BLUE_BACKGROUND_BRIGHT}[{demo_matrix[i][j]}]{RESET}", end="")
            else:
                print(f"[{demo_matrix[i][j]}]", end="")
        print()



def print_demo(demo_matrix):
    while True:
        for i in range(len(demo_matrix)):
            for j in range(len(demo_matrix)):
                os.system("cls")
                print_matrix_as_code(demo_matrix, i, j)
                print_matrix_as_formatted_code(demo_matrix, i, j)
                print_for_loop_demo(i, j)
                print_matrix_as_grid(demo_matrix, i, j)
                time.sleep(2)



def main():
    demo_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print_demo(demo_matrix)



if __name__ == "__main__":
    main()