class Solution {
    public List<String> fizzBuzz(int n) {

 /*
        1. create string array answer (Fizzbuzz, Fizz, Buzz, i)
        2. switch statement for each scenario
 */
    
   ArrayList<String> answer = new ArrayList<String>(); 
 
    for (int i = 1; i <= n; i++)
    {
        if (i % 3 == 0 && i % 5 == 0) {
            answer.add("FizzBuzz");
        } else if (i % 3 == 0) {
            answer.add("Fizz");
        } else if (i % 5 == 0) {
            answer.add("Buzz");
        } else {
            answer.add("" + i);
        }
    }
    System.out.print(answer);
    
    return answer;
}
}