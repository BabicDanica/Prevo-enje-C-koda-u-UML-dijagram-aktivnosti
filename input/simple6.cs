class ExceptionExample {
    int Handle() {
        try {
            int x = 5 / 0;
            return x;
        } catch (DivideByZeroException e) {
            return -1;
        } finally {
            Console.WriteLine("Done");
        }
    }
}
