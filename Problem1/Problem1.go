//written in go
//James Woo
//October 4 2014

package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 1000; i++ {
		if (i%3 == 0 || i%5 == 0){
			sum += i
		}
	}
	fmt.Println(sum)
}