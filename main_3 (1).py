from pyscript import document # type: ignore
#included type ignore so no pyscript related errors

def compute_average(event):
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    average = (score1 + score2) / 2 #calculates the average score based on the inputed scores

    if average >= 90:
        result = "Excellent."
    elif average >= 75:
        result = "Passed"
    else:
        result = "Failed"
 #Note: Both tests are out of 100

    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result