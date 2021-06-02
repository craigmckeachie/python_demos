# start
def greeting(name):
    print(f"Hello! {name}")

greeting('John')

greeting('John' + ' ' + 'Doe')

# default parameters
def greeting(name, greeting_text="Hello!"):
    print(f"{greeting_text}! {name}")

greeting('John', 'Hi!')

# named arguments
def greeting(name, greeting_text="Hello!", repeat_greeting=1):
    for _ in range(repeat_greeting):
        print(f"{greeting_text}! {name}")

greeting('John', 'Hi!', 6)
greeting('John', repeat_greeting=6)