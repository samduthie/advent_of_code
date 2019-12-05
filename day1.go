package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
	"strconv"
)

func main() {
	var total_fuel_needed = 0
	
	file, err := os.Open("day1.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        var mass_as_str = scanner.Text()
        var mass, err = strconv.Atoi(mass_as_str)

        if err != nil {
        	log.Fatal(err)
        }

        total_fuel_needed += mass/3 -2
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    fmt.Println(total_fuel_needed)
}