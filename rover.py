def deplacer_rover(x, y, direction, largeur_plateau, hauteur_plateau, instructions):
    directions_mouvements = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    directions = ['N', 'E', 'S', 'W']
    
    for commande in instructions:
        if commande == 'L':
         
            index_courant = directions.index(direction)
            direction = directions[(index_courant - 1) % 4]
        elif commande == 'R':
           
            index_courant = directions.index(direction)
            direction = directions[(index_courant + 1) % 4]
        elif commande == 'M':
            
            dx, dy = directions_mouvements[direction]
            nouvelle_x = x + dx
            nouvelle_y = y + dy
           
            if 0 <= nouvelle_x <= largeur_plateau and 0 <= nouvelle_y <= hauteur_plateau:
                x, y = nouvelle_x, nouvelle_y
    
    return x, y, direction



if __name__ == "__main__":
    
    x, y, direction = 3, 3, 'E'
    largeur_plateau, hauteur_plateau = 5, 5
    instructions = 'MMRMMRMRRM'
    
    
    x_final, y_final, direction_finale = deplacer_rover(x, y, direction, largeur_plateau, hauteur_plateau, instructions)
    
    print(f"Position finale : {x_final} {y_final} {direction_finale}")