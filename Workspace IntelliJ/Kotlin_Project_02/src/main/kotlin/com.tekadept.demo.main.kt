package com.tekadept.demo

fun main(args: Array<String>){
    println("Hello, World")

    val aSentence = "I am a string"
    val myPi = 3.14
    val myAnswer = 42

    var aString: String
    val aDouble: Double
    val aInt: Int

    var myDouble = 1.999
    var myFloat = 1.9F
    var myLong = 12345678L
    var myInt = 999
    var myShort: Short = 12
    var myByte: Byte = 127

    val aLongNumber = 123_456_789
    val theSameNumber = 123456789

    val anInt: Int = 1
    val aLong: Long = anInt.toLong()

    //java expression. it won't run in kotlin though.
    // int lowest = (a , b) ? a : b;
    // Just like the above, here is the kotlin expression

    val lowest = if( myInt < anInt ) myInt else anInt;
    println("The lowest value is $lowest")

    val temp = 80
    val isAirConditionerOn = if(temp >= 80){
        println("It is warm")
        true;
    } else {
        println("It is not so warm")
        false;
    }
    println("Is the air conditioner on: $isAirConditionerOn")

    val burgersOrdered = 9

    when(burgersOrdered) {
        0 -> println("Not hungry")
        1, 2 -> println("Hungry")
        3 -> println("Very hungry")
        else -> {
            println("Are you sure?")
        }
    }

    when(burgersOrdered) {
        Math.abs(burgersOrdered) -> println("ordered 0 or more burgers")
        else -> {
            println("ordered less than 0")
        }
    }

    when(burgersOrdered) {
        0 -> println("we need orders")
        in 1..4 -> println("got some orders")
        in 5..9 -> println("business is up")
        else -> {
            println("not sure")
        }
    }

    when {
        burgersOrdered <= 0 -> println("none ordered")
        burgersOrdered % 2 == 1 -> println("odd number ordered")
        burgersOrdered % 2 == 0 -> println("even number ordered")
    }

    var x = 0

    while (x < 10) {
        println("x = $x")
        x += 3
    }

    do {
        println("x = $x")
        x -= 3
    } while (x > 0)

    for (item in 1..10) {
        print("$item, ")
    }

    for (ch in "biscuit") {
        println(ch)
    }

    println();
    var ndx = 0
    for (item in 10.rangeTo(20).step(2)){
        print("${++ndx}) $item, ")
    }
    println();

    for((index, item) in 10.rangeTo(25).step(2).withIndex()) {
        print("${index + 1}) $item, ")
    }
    println();

    val myArray = arrayOf(10, 20, 30, 40, 50)
    for(item in myArray.indices) {
        println(" At index $item is ${myArray[item]}.")
    }
    println();

    println("10 + 20 = ${myFunction(10, 20)}")
    println("10 + 20 = ${myFunction1(10, 20)}")
    println("10 + 20 = ${myFunction2(10, 20)}")

    myDefaults(10, 20)
    myDefaults(10, 20, "Hi")
    myDefaults(message = "Greetings")

}


fun myFunction(param1: Int, param2: Int): Int {
    return param1 + param2
}

fun myFunction1(param1: Int, param2: Int): Int = param1 + param2

fun myFunction2(param1: Int, param2: Int) = param1 + param2

fun myDefaults(param1: Int = 1, param2: Int = 5, message: String = "Hello"): Int {
    val results = param1 + param2
    println(message)
    return results
}




// I am a end-of-line comment
/*
I am a block comment
 */

/* inner and outer block comment.
fun meaninglessFunc(){
    /*
    i am a comment
     */
}

 */


