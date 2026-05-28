# List of questions
questions = [
    {
        "question": "Ce este hardware?",
        "options": ["a) Programe", "b) Componente fizice", "c) Date", "d) Internet"],
        "answer": "b"
    },
    {
        "question": "Ce este un sistem de operare?",
        "options": ["a) Joc", "b) Browser", "c) Software care gestioneaza hardware-ul", "d) Antivirus"],
        "answer": "c"
    },
    {
        "question": "Cati biti are un octet?",
        "options": ["a) 4", "b) 8", "c) 16", "d) 32"],
        "answer": "b"
    },
    {
        "question": "Care este baza sistemului binar?",
        "options": ["a) 2", "b) 8", "c) 10", "d) 16"],
        "answer": "a"
    },
    {
        "question": "Ce tip de date este 3.14?",
        "options": ["a) int", "b) string", "c) float", "d) bool"],
        "answer": "c"
    },
    {
        "question": "Ce este o variabila?",
        "options": ["a) O functie", "b) Un spatiu de stocare pentru date", "c) Un program", "d) Un loop"],
        "answer": "b"
    },
    {
        "question": "Ce face instructiunea if?",
        "options": ["a) Repeta cod", "b) Verifica o conditie", "c) Afiseaza text", "d) Creeaza variabile"],
        "answer": "b"
    },
    {
        "question": "Ce este o functie?",
        "options": ["a) O bucla", "b) Un bloc de cod reutilizabil", "c) O variabila", "d) Un tip de date"],
        "answer": "b"
    },
    {
        "question": "Ce face un for loop?",
        "options": ["a) Verifica conditii", "b) Ruleaza cod o singura data", "c) Itereaza printr-o colectie", "d) Opreste programul"],
        "answer": "c"
    },
    {
        "question": "Ce face while loop?",
        "options": ["a) Ruleaza cat timp conditia e adevarata", "b) Ruleaza o data", "c) Creeaza functii", "d) Nu face nimic"],
        "answer": "a"
    }
]

# Function to ask a question
def ask_question(q):
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Raspunsul tau (a/b/c/d): ").lower()
    
    if answer == q["answer"]:
        print("Corect!")
        return 1
    else:
        print(f"Gresit! Raspuns corect: {q['answer']}")
        return 0

# Function to display final score
def show_score(score, total):
    print("\n--- REZULTAT FINAL ---")
    print(f"Ai raspuns corect la {score} din {total} intrebari.")
    
    if score == total:
        print("Perfect! Esti geniu 🧠")
    elif score >= total // 2:
        print("Decent, dar poti mai bine ")
    else:
        print("Bro... mai invata ")

# Main program
score = 0

for q in questions:
    score += ask_question(q)

show_score(score, len(questions))