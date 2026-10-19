def login(username, password):
    if username == "admin" and password == "secret":
        return "Login successful"
    return "Invalid credentials"

if __name__ == "__main__":
    print(login("admin", "secret"))
