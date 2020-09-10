from flask import Flask, render_template, url_for
app = Flask(__name__)


def primes(n):
    # Algorithm is Sieve of Eratosthenes
    # Taken from https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    prime_nums = []
    prime = [True] * (n+1)
    p = 2
    while (p*p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p]):
            # Update all multiples of p
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    # Add all prime numbers to prime_nums list
    for p in range(2, n+1):
        if prime[p]:
            prime_nums.append(p)
    return prime_nums


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:number>')
def number(number):
    nums = [i for i in range(1, number+1)]
    return render_template('number.html', title="Numbers", nums=nums)


@app.route('/<int:number>/odd')
def odd(number):
    nums = [i for i in range(1, number+1, 2)]
    return render_template('number.html', title="Odds", nums=nums)


@app.route('/<int:number>/even')
def even(number):
    nums = [i for i in range(0, number+1, 2)]
    return render_template('number.html', title="Evens", nums=nums)


@app.route('/<int:number>/prime')
def prime(number):
    nums = primes(number)
    return render_template('number.html', title="Primes", nums=nums)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
