#include <stdio.h>

int count=0;
void swap(int *a,int *b){
	int c=*a;
	*a=*b;
	*b=c;
}


int partition(int a[],int l, int h, int pivot){
		int x=pivot;
		int i = l ;  // Index of smaller element
    int j;
    for ( j = l+1; j <= h- 1; j++)
    {
        // If current element is smaller than or equal to pivot 
        if (a[j] <= x)
        {
	    //count++;
             swap(&a[i], &a[j]);  // Swap current element with index
             i++;    // increment index of smaller element
        }
	count++;
    }
    swap(&a[i + 1], &a[h]);  
    return (i + 1);
}





int main(void) {
	// your code goes here
	int n,i,j;
	scanf("%d",&n);
	int a[i];
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}

	int rank,ans,pivot,l,h,flag=1;
	l=0;
	h=n-1;
	pivot=a[l];
	rank=partition(a,l,h,a[l]);
while(flag){
	if(rank==(n)/2) {
		flag=0;
		ans=pivot;
	}
	else if(rank<(n)/2){
		l=rank;
		pivot=a[l];
		if(l<h)
		rank=partition(a,l,h,a[l]);
	}
	else if(rank>(n)/2){
		h=rank;
		pivot=a[l];
		if(l<h)
		rank=partition(a,l,h,a[l]);
	}
}	

	printf("%d\n%d\n",ans,count);	
	return 0;
}

