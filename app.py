from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return jsonify([
        ("What is the correct file extension for Python files?", [".python", ".py", ".pt", ".pyt"], 1),
        ("How do you create a function in Python?", ["def function_name():", "function function_name():", "create function_name():", "func function_name():"], 0),
        ("Which of the following is used to output text in Python?", ["echo", "print()", "write()", "printf()"], 1),
        ("What is the correct syntax to create a variable in Python?", ["var x = 5", "int x = 5", "x = 5", "declare x = 5"], 2),
        ("Which keyword is used to create a class in Python?", ["class", "define", "object", "struct"], 0),
        ("How do you create a comment in Python?", ["// This is a comment", "# This is a comment", "<!-- This is a comment -->", "/* This is a comment */"], 1),
        ("How do you start a for loop in Python?", ["for i in range(10)", "for (i = 0; i < 10; i++)", "loop i in 10", "foreach i in 10"], 0),
        ("Which of the following is a correct list in Python?", ["my_list = [1, 2, 3]", "my_list = {1, 2, 3}", "my_list = (1, 2, 3)", "my_list = <1, 2, 3>"], 0),
        ("Which of the following is a valid way to import a module?", ["import module_name", "use module_name", "load module_name", "require module_name"], 0),
        ("How do you check the length of a list in Python?", ["len(list_name)", "list_name.size()", "length(list_name)", "list_name.length()"], 0),
        ("What data type is used to store multiple items in a single variable in Python?", ["List", "Dictionary", "Set", "Tuple"], 0),
        ("How do you handle exceptions in Python?", ["try...catch", "try...except", "catch...except", "try...handle"], 1),
        ("What is the output of: print(2 ** 3)?", ["5", "6", "7", "8"], 3),
        ("How do you convert a string into an integer in Python?", ["str()", "int()", "float()", "string()"], 1),
        ("Which of the following methods removes the last item from a list?", ["remove()", "pop()", "delete()", "clear()"], 1),
        ("Which operator is used for exponentiation in Python?", ["^", "**", "//", "exp"], 1),
        ("What will the following code output: print(bool(0))?", ["True", "False", "0", "None"], 1),
        ("How do you write an inline if statement in Python?", ["if x > 5 then:", "if x > 5 do:", "x = 5 if x > 5 else 0", "x > 5 ? 5 : 0"], 2),
        ("Which of the following is a tuple?", ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "<1, 2, 3>"], 0),
        ("Which keyword is used to define a lambda function?", ["def", "lambda", "func", "method"], 1),
        ("How do you define a dictionary in Python?", ["{key: value}", "[key: value]", "(key: value)", "<key: value>"], 0),
    ])

if __name__ == '__main__':
    app.run(debug=True)
