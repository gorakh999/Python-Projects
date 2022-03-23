from turtle import Turtle
DIMENSION_X = 0
DIMENSION_Y = 245

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')

class Score(Turtle):

    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color('white')
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(DIMENSION_X, DIMENSION_Y)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def bye_user(self, name):
    #     self.goto(0, -50)
    #     self.write(f"Thank you for Playing {name}", move=False, align=ALIGNMENT, font=FONT)
    #     self.goto(0, -100)
    #     self.write(f"You Score is {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def set_high_score(self):
        with open("high_score.txt", 'w') as f:
            f.write(str(self.high_score))

    def get_high_score(self):
        
        try:
            with open("high_score.txt", 'r') as f:
                content = f.read()
        except Exception as e:
            content = 0
        return int(content)
        


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        # print(f"Score : {self.score} High score is {self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        

    # def high_score(self):
    #     self.clear()
    #     self.write(f"High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        



