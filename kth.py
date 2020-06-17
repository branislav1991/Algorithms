def kthGrammar(N: int, K: int) -> int:
    string = ["0"]
    for n in range(N):
        new_str = ""
        for s in string:
            new_str = new_str + ("01" if s == "0" else "10")
        string = new_str
        
    return string[K-1]

print(kthGrammar(2, 1))