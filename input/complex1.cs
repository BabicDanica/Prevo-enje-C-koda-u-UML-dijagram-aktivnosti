class Test {
    void Run() {
        int x = 3;
        try {
            switch (x) {
                case 1:
                    x = 10;
                    break;
                case 3:
                    x = 30;
                    break;
                default:
                    x = 0;
            }
        } catch (int ex) {
            x = -1;
        } finally {
            x = x + 1;
        }
    }
}
