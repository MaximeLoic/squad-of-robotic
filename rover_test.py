import unittest
from rover import deplacer_rover

class TestRover(unittest.TestCase):
    
    def test_deplacer_rover_avancer(self):
        
        x, y, direction = 1, 2, 'N'
        largeur_plateau, hauteur_plateau = 5, 5
        instructions = 'M'
        
        
        x_final, y_final, direction_finale = deplacer_rover(x, y, direction, largeur_plateau, hauteur_plateau, instructions)
        
        
        self.assertEqual((x_final, y_final, direction_finale), (1, 3, 'N'))

    def test_deplacer_rover_gauche(self):
       
        x, y, direction = 1, 2, 'N'
        largeur_plateau, hauteur_plateau = 5, 5
        instructions = 'L'
        
    
        x_final, y_final, direction_finale = deplacer_rover(x, y, direction, largeur_plateau, hauteur_plateau, instructions)
        
       
        self.assertEqual((x_final, y_final, direction_finale), (1, 2, 'W'))

    def test_deplacer_rover_droite(self):
      
        x, y, direction = 1, 2, 'N'
        largeur_plateau, hauteur_plateau = 5, 5
        instructions = 'R'
        
        
        x_final, y_final, direction_finale = deplacer_rover(x, y, direction, largeur_plateau, hauteur_plateau, instructions)
        
       
        self.assertEqual((x_final, y_final, direction_finale), (1, 2, 'E'))

    def test_deplacer_rover_multiple_instructions(self):
        
        x, y, direction = 1, 2, 'N'
        largeur_plateau, hauteur_plateau = 5, 5
        instructions = 'LMLMLMLMM' 
        
    
        x_final, y_final, direction_finale = deplacer_rover(x, y, direction, largeur_plateau, hauteur_plateau, instructions)
        
        
        self.assertEqual((x_final, y_final, direction_finale), (1, 3, 'N'))

    def test_deplacer_rover_bord_plateau(self):
        
        x, y, direction = 0, 0, 'N'
        largeur_plateau, hauteur_plateau = 5, 5
        instructions = 'M' 
        
        
        x_final, y_final, direction_finale = deplacer_rover(x, y, direction, largeur_plateau, hauteur_plateau, instructions)
        

        self.assertEqual((x_final, y_final, direction_finale), (0, 1, 'N'))

if __name__ == "__main__":
    unittest.main()