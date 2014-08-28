// Cubic maximum subsequence sum
public static in maxSubSum1(int[] a)
{
	int maxSum = 0;

	for (int i = 0; i < a.length; i++)
		for (int j=i; j < a.length; j++)
		{
			int thisSum = 0;

			for (int k = i; k <= j; k++)
				thisSum += a[k];

			if (thisSum > maxSum)
				maxSum = thisSum;
		}	

	return maxSum;
}