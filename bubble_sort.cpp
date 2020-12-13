#include <iostream>
static const int arraySize = 10;
int array[10];

void bubbleSort(int *array)
{
	for (short i = 0; i < arraySize; i++)
	{
		for (short j = 0; j < arraySize - 1; j++)
		{
			if (array[j] > array[j + 1])
			{
				short temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}
}

void bubbleSortOptimized(int* array)
{
	bool hasSwapped = true;
	short iterCount = 0;
	while (hasSwapped)
	{
		hasSwapped = false;
		for (short j = 0; j < arraySize - 1 - iterCount; j++)
		{
			if (array[j] > array[j + 1])
			{
				short temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
				hasSwapped = true;
			}
		}
		iterCount++;
	} 
}

int main()
{
	std::cout << "Please input 10 integers to be sorted" << "\n";

	for (short i = 0; i < arraySize; i++)
	{ 
		std::cin >> array[i];
	}
	std::cout << "Sorting your array" << "\n";

	bubbleSortOptimized(array);

	std::cout << "===================" << "\n";

	for (short i = 0; i < arraySize; i++)
	{
		std::cout << array[i] << "\n";
	}
	system("pause");

}