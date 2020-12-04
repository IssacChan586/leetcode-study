package main

func countPrimes(n int) int {
	if n == 0 || n == 1 {
		return 0
	}
	var primeFlag [5000000]bool
	var primeCont = 0
	for i := 2; i < n; i++ {
		if primeFlag[i] == false {
			primeCont += 1
			if i*i < n {
				for j := i * i; j < n; j += i {
					primeFlag[j] = true
				}
			}
		}
	}
	return primeCont
}

func main() {

}
