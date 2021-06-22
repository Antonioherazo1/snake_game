from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:/Users/Anton/OneDrive/OneHundredDaysOfCodePython/data/data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_high_score(self):
        with open("C:/Users/Anton/OneDrive/OneHundredDaysOfCodePython/data/data.txt", mode="w") as file:
            file.write(f'{self.high_score}')

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.update_high_score()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
