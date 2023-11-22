import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import font
import pyttsx3

#The main application
class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.title("Pop Quiz Game")
        self.master.geometry("550x600")
        self.master.config(bg="#115ABE")

        self.categories = ["Games", "Technology", "Entertainment", "Sports", "Math", "Surprise Me"]  # Defining Categories
        self.selected_category = tk.StringVar(value=self.categories[0])

        self.create_home_screen()

        # creating the home screen
    def create_home_screen(self):
              # Creating "pop quiz" title
          label = tk.Label(self.master,text="POP QUIZ", font=('OpenDyslexic-Bold.otf',45,'bold'), fg="white", bg="#115ABE")
          label.pack()
          label.place(x=120, y=220)

          #'GAME' big letters
          label = tk.Label(self.master,text="GAME", font=('OpenDyslexic-Bold.otf',80,'bold'),fg='white', bg='#115ABE')
          label.pack()
          label.place(x=110, y=280)

          #takes you to category screen
          start_button = tk.Button(self.master, text="Start Quiz", command=self.create_category_screen, font=("Helvetica", 16, "bold"))
          start_button.pack(pady=10)
          start_button.config(fg= "white", bg="#0B154E")
          start_button.place(x=205 ,y=430)


  #shows the category screen
    def create_category_screen(self):

        self.category_frame = tk.Frame(self.master, bg="#115ABE", padx= 100, pady=100)
        self.category_frame.pack()

        #select a category titld
        category_label = tk.Label(self.category_frame, text="Select a Category:", font=("Arial", 25), fg= "white", bg="#115ABE")
        category_label.pack(pady=10)

        for category in self.categories:
            category_radio = tk.Radiobutton(self.category_frame, text=category, variable=self.selected_category, value=category, font=("arial", 18)) 
            category_radio.pack()

        start_button = tk.Button(self.category_frame, text="Start Quiz", command=self.start_quiz, fg="white", bg= "#0B154E", font=("arial", 18))
        start_button.pack(pady=10)

    def show_category_screen(self):
      if hasattr(self, 'category_frame') and self.category_frame:
        for widget in self.category_frame.winfo_children():
            widget.destroy()

      else:
        self.create_category_screen()

    def start_quiz(self):
        selected_category = self.selected_category.get()
        if selected_category:
            self.category_screen_destroy()
            self.load_questions(selected_category)
            self.create_quiz_screen()
        else:
            messagebox.showinfo("Error", "Please select a category.")

    def category_screen_destroy(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def load_questions(self, category):
        # Loads questions based on the selected category
        if category == "Games":
            self.questions = [
                {"question": "The best-selling game console of all time?", "options": ["PS2", "Xbox One", "Nintendo Switch", "GameCube"], "correct": "PS2"},

                {"question": "The original intent of The Sims?", "options": ["Be a fun game", "City builder/architectural simulator", "For a cash grab", "A life simulator"], "correct": "City builder/architectural simulator"},

                {"question": "How long was the longest Mario Kart marathon?", "options": ["36 hours", "24 hours", "40 hours", "50 hours"],"correct": "40 hours"},

                {"question": "What classic arcade game was developed and published by Namco in 1980??", "options": ["Galactica", "Pac Man", "Tetris", "Mario 64"], "correct": "Pac Man"},

                {"question": "The first video game to be played in space?", "options": ["Tic Tac Toe", "Tetris", "Galatica", "Pac-Man"],"correct": "Tetris"}
            ]

        elif category == "Technology":
            self.questions = [

                {"question": "Example of an 'incorrect' algorithm?", "options": ["It's a series of steps", "It's not specific", "It reaches the desired outcome", "The measurements are accurate"], "correct": "It's not specific"},

                {"question": "What's an example of software?", "options": ["Microchips", "Monitors", "Photo Editors", "Keyboards"], "correct": "Photo Editors"},

                {"question": "What programming language is taught in CS125?", "options": ["JavaScript", "Python", "Html", "C++"], "correct": "Python"},

                {"question": "What data type is a truth variable?", "options": ["Float", "String", "Integer", "Boolean"], "correct": "Boolean"},

                {"question": "What does 'GUI' stand for?", "options": ["Graphical User Interface", "Graphic Unit Interface", "Graph Unit Interface", "Graphical Unit Information"], "correct": "Graphical User Interface"},
            ]

        elif category == "Entertainment":
            self.questions = [

                {"question": "Who helps Dory find her parents?", "options": ["Nemo", "Marlin", "Bruce", "Gill"], "correct": "Nemo"},

                {"question": "What is a movie where a rat loves to cook?", "options": ["Toy Story", "Ratatouille", "Winnie the Pooh", "Shrek"], "correct": "Ratatouille"},

                {"question": "How many Toy Story movies are there?", "options": ["3", "4", "6", "5"], "correct": "4"},

                {"question": "What movie did we hear 'Kiss the Girl'?", "options": ["The Little Mermaid", "Moana", "Tangled", "Shrek"], "correct": "The Little Mermaid"},

                {"question": "Baymax is a character in this movie?", "options": ["Big Hero Six", "The Incredibles", "Toy Story", "Star Wars" ], "correct": "Big Hero Six"}

            ]

        elif category == "Math":
          self.questions = [

                {"question": "What is the most popular lucky number?", "options": ["6", "8", "7", "10"], "correct": "7"},

                {"question": "What does the roman numeral 'X' equal?", "options": ["12", "10", "6", "8"], "correct": "10"},

                {"question": "What prime number comes after 3?","options": ["5", "8", "9", "12"],"correct": "5"},

                {"question": "How may lives are cats said to have?", "options": ["10", "5", "9", "4"], "correct": "9"},

                {"question": "The only temperature that is the same F and C?", "options": ["60", "40", "30", "70"],"correct": "40"},
      ]

        elif category == "Sports":
          self.questions = [

          {"question": "What sport is known as the 'king of sports'?", "options": ["Football", "Soccer", "Volleyball", "Basketball"], "correct": "Soccer"},

          {"question": "What color flag do you see in motor racing?", "options": ["Red", "Checkered", "Striped", "Yellow"], "correct": "Checkered"},

          {"question": "How many medals did China win at the Beijing Olympics?","options": ["75", "100", "120", "80"], "correct": "100"},

          {"question": "Name for when a bowler makes three strikes in a row?","options": ["Turkey", "Mega Strike", "Ostrich", "Chicken"],"correct": "Turkey"},

          {"question": "What's the national sport of Canada?", "options": ["Tennis", "Lacrosse", "Soccer", "Snowboarding"], "correct": "Lacrosse"},
      ]

        elif category == "Surprise Me":
          self.questions = [

          {"question": "The first President of the USA  was:", "options": ["George Washington", "John Adams", "Thomas Jefferson", "James Madison"], "correct": "George Washington"},

          {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid", "Rome"], "correct": "Paris"},

          {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "correct": "Mars"},

          {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"], "correct": "Canberra"},

          {"question": "Where is the Great Wall of China located?", "options": ["China", "Japan", "India", "Australia"], "correct": "China"},
      ]
      
        self.current_question = 0
        self.score = 0

    #creates the quiz screen
    def create_quiz_screen(self):
        self.question_label = tk.Label(self.master, text="", fg="white", bg="#115ABE", font=("Arial", 16))
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        self.radio_buttons = []
        for i in range(4):
            option = tk.Radiobutton(self.master, text="", variable=self.radio_var, value=i, font= ("arial", 18))
            option.pack()
            self.radio_buttons.append(option)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, fg= "white", bg="#0B154E", font=("arial", 18))
        self.submit_button.pack(pady=10)

        self.next_question()

         #Add a button for text-to-speech
        self.tts_button = tk.Button(self.master, text="Text-to-Speech", command=self.speak_question)
        self.tts_button.pack(pady=10)

      # Text to speech function
    def speak_question(self):
      # Use pyttsx3 to speak the current question
      current_question_data = self.questions[self.current_question - 1]["question"]
      self.engine = pyttsx3.init()
      self.engine.say(current_question_data)
      self.engine.runAndWait()

  
    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for i in range(4):
                self.radio_buttons[i].config(text=question_data["options"][i])

            self.current_question += 1
        else:
            self.show_result()

    #checks the answer
    def check_answer(self):
        if self.radio_var.get() is not None:
            selected_option = self.questions[self.current_question - 1]["options"][int(self.radio_var.get())]
            correct_option = self.questions[self.current_question - 1]["correct"]

            if selected_option == correct_option:
                self.score += 1
                messagebox.showinfo("Result", "Correct! You're doing great!")
            else:
                messagebox.showinfo("Result", f"Sorry, the correct answer is: {correct_option}")

            self.radio_var.set(None)
            self.next_question()
        else:
            messagebox.showinfo("Error", "Please select an option.")

    def show_result(self):
        self.score_check = tk.Label(self.master, text=f"You scored {self.score} out of {len(self.questions)}. Rock on Superstar! ★ ★ ★", fg="white", bg="#115ABE", font=("Arial", 13))
        self.score_check.pack()
        self.score_check.place(x=40, y=400)

        back_button = tk.Button(self.master, text="Back to Categories", command=self.show_category_screen, fg="white", bg="#0B154E", font=("arial", 16))
        back_button.pack(pady=10)
        back_button.place(x=180, y=500)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
