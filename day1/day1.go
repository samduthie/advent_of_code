package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
	"strconv"
)

func moreFuel(fuel int) int {
	if fuel <= 0 {
		return 0
	}
	var total_fuel = moreFuel(fuel/3 -2)
	return fuel + total_fuel
}

func main() {
	var total_fuel = 0
	
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

        var fuel = mass/3-2
        total_fuel += moreFuel(fuel)
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    // var recFuel = moreFuel(total_fuel)
    fmt.Println(total_fuel)
}

