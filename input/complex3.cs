class TestClass
{
    void ComplexMethod()
    {
        const int limit = 3;
        int sum = 0;
        int i = 0;

        while(i < limit)
        {
            sum = sum +i;
            i = i + 1;
        }

        do
        {
            i = i - 1;
        } while (i > 0);

        for (int j = 0; j < 5; j++)
        {
            if (j % 2 == 0)
            {
                sum = sum + j;
            }
            else
            {
                sum = sum - j;
            }
        }

        return;
    }
}
