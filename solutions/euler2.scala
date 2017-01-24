object Solution {
  case class Memo[A, B](f: A => B) {
    import scala.collection.mutable.Map
    private val cache = Map.empty[A, B]
    def apply(x: A) = cache getOrElseUpdate (x, f(x))
  }
  def main(args:Array[String]) {
      var max = 4000000;
      euler2(max);
      return
  }
  def euler2(max:Int) : Long = {
    var sum = 0l
    var i = 2
    while(fib(i) <= max) {
      if (fib(i) % 2 == 0) sum += fib(i)
      i += 1
    }
    println(sum);
    sum
  }
  val fib: Memo[Long, Long] = Memo {
    case 1l => 1l
    case 2l => 2l
    case n => fib(n - 1) + fib(n - 2)
  }
}
