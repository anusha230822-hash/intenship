number = 5
analysis = {
	"positive": number > 0,
	"even": number % 2 == 0,
	"divisible by 5": number % 5 == 0,
	"in range 1 to 100": 1 <= number <= 100,
}
print("Number analysis:", analysis)