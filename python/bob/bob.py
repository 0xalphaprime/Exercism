def response(hey_bob):
    
    hey_bob = hey_bob.strip()
    answer = "Whatever."

    if len(hey_bob) < 1:
        return "Fine. Be that way!"

    if hey_bob.isupper() == True and hey_bob[-1] != "?":
        answer = "Whoa, chill out!"
    if hey_bob.isupper() == True and hey_bob[-1] == "?":
        answer = "Calm down, I know what I'm doing!"
    if hey_bob.isupper() == False and hey_bob[-1] == "?":
        answer = "Sure."
   

    return answer


