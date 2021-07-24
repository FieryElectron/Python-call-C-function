#include<stdio.h>

void my_add(int num){
	long int result = 0;

	for (long int i=1; i<=num; i++){
		// printf("num: %ld\n",i);
	    result += i;
	}

	printf("C from 1 to %d accumulation => %ld\n",num,result);
}
