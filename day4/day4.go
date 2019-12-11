package main

import (
	"fmt"
	"strconv"
)

func matchesRules(num int) bool{
	num_as_str := strconv.Itoa(num)

	// go doesnt support backreference in regex
	// r := regexp.MustCompile(`0{2,}|1{2,}|2{2,}|3{2,}|4{2,}|5{2,}|6{2,}|7{2,}|8{2,}|9{2,}`)
	// match := r.FindStringSubmatch(num_as_str) 

	// if len(match) == 0 {
	// 	return false
	// }

	prev_char := ""
	char_counter := 0
	has_chars := false

	highest_digit := 0
	for _, char := range num_as_str {
		// if any number is higher than a number to the left of it 
		// we return false
		n, _ := strconv.Atoi(string(char))
		if n < highest_digit {
			return false
		} else {
			highest_digit = n
		}

		// check for two in a row
		// check against previous character. if diff then we hit 2
		if string(char) == prev_char {
			fmt.Println(string(char), prev_char)
			char_counter = char_counter + 1
		} else if char_counter == 1 {
			has_chars = true
			char_counter = 0
		} else {
			char_counter = 0
		}

		prev_char = string(char)


	}
	if char_counter == 1 {
			has_chars = true
	}

	return has_chars
}
func main() {
	low := 130254
	high := 678275
	matches := 0

	for i := low; i <= high; i++ {
		if matchesRules(i) {
			matches = matches + 1
		}
	}

	fmt.Println(matches)


}