public class Runner {
    public void Run() {
        var sum = 0;
        var x = 3;
        var y = 5;

        try {
            for (int i = 0; i < 5; i++) {
                if (x > y) {
                    sum = sum + x;
                } else if (x == y) {
                    switch (x)
                    {
                        case 1:
                            sum = sum + 1;
                            break;
                        case 2:
                            sum = sum + 2;
                            break;
                        default:
                            sum = sum + 10;
                    }
                } else {
                    sum = sum + y;
                }
                x = x + 1;
            }
        } catch (Exception e) {
            sum = -1;
        } finally {
            sum = sum + 100;
        }

        return sum;
    }
}
