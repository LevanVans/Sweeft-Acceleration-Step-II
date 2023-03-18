

grid_input = ["..0.","..0.",".0..",]

grid = "".join(grid_input)

print(grid)

c = len(grid_input[0])
r = len(grid_input)


bombs = [[i//4, i%4] for i in range(len(grid)) if grid[i] == "0"]



print(bombs)

destroyed = []

while len(bombs) > 0:
    
    for i in bombs:
    
        r_index = i[0]
        c_index = i[1]
        
        
        if r_index != 0:
            r_up = r_index - 1
        else:
            r_up = r_index
            
        if r_index != r-1:
            r_down = r_index +1
        else:
            r_down = r_index
            
            
        if i[1] != 0:
            c_left = c_index -1 
        else:
            c_left = c_index
        
        if i[1] != c-1:
            c_right = c_index + 1
        else:
            c_right = c_index
            
            
        destroyed.append([r_up,c_index])
        destroyed.append([r_down,c_index])
        destroyed.append([r_index, c_right])
        destroyed.append([r_index, c_left])



        if [r_up,c_index] in bombs:
            bombs.remove([r_up,c_index])
    
            
        if [r_down,c_index] in bombs:
            bombs.remove([r_down,c_index])
            
        
        if [r_index, c_right] in bombs:
            bombs.remove([r_index, c_right])
            
            
        if [r_index, c_left] in bombs:
            bombs.remove([r_index, c_left])
            
     


    
print(destroyed)
    