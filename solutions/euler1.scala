object Solution {
    def main(args:Array[String]) {
        var n = 1000;
        euler1(n);
        return;
    }
    def euler1(n:Int) : Int = {
        val r = (1 until n).view.filter(n => n % 3 == 0 || n % 5 == 0).sum
        println(r);
        return r
    }
}
