from flask import Flask, render_template, url_for

app = Flask(__name__)

def primes(n):
	prime_nums = []
	## Algorithm is Sieve of Eratosthenes
	prime = [True] * (n+1) 
	p = 2
	while (p * p <= n): 
	      
	    # If prime[p] is not changed, then it is a prime 
	    if (prime[p] == True): 
	          
	        # Update all multiples of p 
	        for i in range(p * p, n+1, p): 
	            prime[i] = False
	    p += 1
	  
	# Print all prime numbers 
	for p in range(2, n+1): 
		if prime[p]: 
			prime_nums.append(p)
	return prime_nums

def getOddsOrEvens(n, mod):
	return [i for i in range(1, n+1) if i % 2 == mod]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<number>')
def number(number):
	try:
		num = int(number)
	except:
		return render_template('error.html')

	nums = [i for i in range(1, num+1)]
	return render_template('number.html', title="Numbers", nums=nums)


@app.route('/<number>/odd')
def odd(number):
	try:
		num = int(number)
	except:
		return render_template('error.html')

	nums = getOddsOrEvens(num, 1)
	return render_template('number.html', title="Odds", nums=nums)

@app.route('/<number>/even')
def even(number):
	try:
		num = int(number)
	except:
		return render_template('error.html')

	nums = getOddsOrEvens(num, 0)
	return render_template('number.html', title="Evens", nums=nums)

@app.route('/<number>/prime')
def prime(number):
	try:
		num = int(number)
	except:
		return render_template('error.html')

	nums = primes(num)
	return render_template('number.html', title="Primes", nums=nums)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')