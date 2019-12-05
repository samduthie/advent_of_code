package main

import (
    "fmt"
    "log"
)


func main() {
    opcodes := []int{1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0}

    var i = 0
    var store = 0
    var no_to_store = 0
    var x = 0
    var y = 0

    opcodes[1] = 12
    opcodes[2] = 2

    var condition = true
    for do := true; do; do = condition {
        var opcode = opcodes[i]

        switch opcode {
        case 1:
            store = opcodes[i+3]
            x = opcodes[i+1]
            y = opcodes[i+2]
            no_to_store = opcodes[x] + opcodes[y]

            opcodes[store] = no_to_store

         case 2:
            store = opcodes[i+3]
            x = opcodes[i+1]
            y = opcodes[i+2]
            no_to_store = opcodes[x] * opcodes[y]
            opcodes[store] = no_to_store

        case 99:
            condition = false
            fmt.Println("solution is: ", opcodes[0])

        default:
            log.Fatal("err: ", i, opcodes[i])
               
        }

        i = i + 4
    }
}