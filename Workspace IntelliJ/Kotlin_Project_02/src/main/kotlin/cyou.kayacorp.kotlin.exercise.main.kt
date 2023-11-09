package cyou.kayacorp.kotlin.exercise

fun main(args: Array<String>) {

    val input1 = 1
    val input2 = 105
    // divisibility is by 3, 5, both
    fizzbuzz(input1, input2)

}

fun fizzbuzz(param1: Int, param2: Int) {
    println("Input Numbers range from $param1 to $param2. Let's do the run.....")

    for (item in param1.rangeTo(param2).step(1)){
        print("$item")
        when {
            item % 3 == 0 && item % 5 == 0 -> print(" ) FIZZ-BUZZ ")
            //item % 15 == 0 -> print(" ) FIZZ-BUZZ ")
            item % 3 == 0 -> print(" ) FIZZ ")
            item % 5 == 0 -> print(" ) BUZZ ")
        }
        println()
    }
}