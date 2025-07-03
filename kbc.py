import random
import time

# Define questions with options and correct answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B",
        "prize": 1_000
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B",
        "prize": 2_000
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B",
        "prize": 5_000
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "C",
        "prize": 10_000
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A. Go", "B. Gd", "C. Au", "D. Ag"],
        "answer": "C",
        "prize": 20_000
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["A. China", "B. Brazil", "C. Russia", "D. UK"],
        "answer": "B",
        "prize": 50_000
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"],
        "answer": "B",
        "prize": 1_00_000
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A. 1942", "B. 1947", "C. 1950", "D. 1935"],
        "answer": "B",
        "prize": 5_00_000
    },
    {
        "question": "Who is known as the 'Father of the Indian Constitution'?",
        "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. B.R. Ambedkar", "D. Sardar Patel"],
        "answer": "C",
        "prize": 10_00_000
    },
    {
        "question": "Which of these is not a prime number?",
        "options": ["A. 2", "B. 3", "C. 5", "D. 9"],
        "answer": "D",
        "prize": 50_00_000
    },
    {
        "question": "What is the national currency of Japan?",
        "options": ["A. Dollar", "B. Euro", "C. Yen", "D. Won"],
        "answer": "C",
        "prize": 1_00_00_000
    }
]
 
# Lifelines
def fifty_fifty(options, correct_answer):
    incorrect_options = [opt for opt in ['A', 'B', 'C', 'D'] if opt != correct_answer]
    remove = random.sample(incorrect_options, 2)
    return [opt for opt in options if opt[0] not in remove]

def audience_poll(correct_answer):
    percentages = [0] * 4
    correct_index = ord(correct_answer) - ord('A')
    percentages[correct_index] = random.randint(50, 80)
    
    remaining = 100 - percentages[correct_index]
    for i in range(4):
        if i != correct_index:
            percentages[i] = random.randint(0, remaining)
            remaining -= percentages[i]
    
    # Normalize to ensure sum is 100
    if sum(percentages) != 100:
        percentages[correct_index] += (100 - sum(percentages))
    
    return percentages

# Game logic
def play_kbc():
    print("\n" + "="*50)
    print("WELCOME TO KAUN BANEGA CROREPATI!")
    print("="*50 + "\n")
    
    name = input("Enter your name: ")
    print(f"\nHello {name}! Let's begin the game...\n")
    
    total_prize = 0
    lifelines = ["50-50", "Audience Poll"]
    
    for i, q in enumerate(questions[:10]):  # Play first 10 questions
        print(f"\nQuestion for ₹{q['prize']:,}")
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        # Lifeline display
        if lifelines:
            print("\nAvailable lifelines:", ", ".join(lifelines))
        
        while True:
            answer = input("\nYour answer (A/B/C/D) or 'L' for lifeline: ").upper()
            
            if answer == 'L' and lifelines:
                if not lifelines:
                    print("No lifelines left!")
                    continue
                
                print("\nAvailable lifelines:")
                for idx, lifeline in enumerate(lifelines, 1):
                    print(f"{idx}. {lifeline}")
                
                lifeline_choice = input("Choose lifeline (1/2): ")
                
                if lifeline_choice == '1' and "50-50" in lifelines:
                    print("\nApplying 50-50 lifeline...")
                    new_options = fifty_fifty(q["options"], q["answer"])
                    for option in new_options:
                        print(option)
                    lifelines.remove("50-50")
                elif lifeline_choice == '2' and "Audience Poll" in lifelines:
                    print("\nApplying Audience Poll lifeline...")
                    percentages = audience_poll(q["answer"])
                    for idx, percent in enumerate(percentages):
                        print(f"{chr(65 + idx)}: {percent}%")
                    lifelines.remove("Audience Poll")
                else:
                    print("Invalid lifeline choice or lifeline already used!")
                continue
            
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input! Please enter A, B, C, or D.")
        
        if answer == q["answer"]:
            total_prize = q["prize"]
            print("\n" + "="*50)
            print(f"Correct answer! You've won ₹{total_prize:,}")
            print("="*50)
            
            if i < len(questions) - 1:
                next_prize = questions[i+1]["prize"]
                print(f"\nNext question for ₹{next_prize:,}")
                choice = input("Do you want to continue? (Y/N): ").upper()
                if choice == 'N':
                    print(f"\nCongratulations! You take home ₹{total_prize:,}")
                    return
        else:
            print("\n" + "="*50)
            print(f"Wrong answer! The correct answer was {q['answer']}.")
            if i > 0:
                print(f"You take home ₹{questions[i-1]['prize']:,}")
            else:
                print("You win nothing!")
            print("="*50)
            return
        
        time.sleep(1)
    
    print("\n" + "="*50)
    print(f"CONGRATULATIONS {name.upper()}! YOU'VE WON ₹1 CRORE!")
    print("="*50)

# Start the game
if __name__ == "__main__":
    play_kbc()