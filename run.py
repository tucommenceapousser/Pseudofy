from app import Create_Apps

app = Create_Apps()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port="80")
