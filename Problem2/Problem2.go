/*
James Woo
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four 
million, find the sum of the even-valued terms.

Written in golang

October 4 2014
*/

package main

import "fmt"

func main() {
	previous1 := 1
	previous2 := 2
	next := previous1 + previous2
	sum := 0
	
	for i := 1; next <= 4000000; i++ {
		if(next % 2 == 0){
			sum += next
		}
		previous1 = previous2
		previous2 = next
		
		next = previous1 + previous2
	}
	fmt.Println(sum + 2)
}