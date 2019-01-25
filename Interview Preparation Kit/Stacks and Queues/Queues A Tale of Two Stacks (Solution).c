// https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

static int top1=-1,top2=-1;
int ar1[111111],ar2[111111];

void insert(int n)
    {
        top1++;
        ar1[top1]=n;
    }

//------------------------------------------------------
void move2()                // move arr1 to arr2 
{
    while(top1>-1)
    {
        top2++;
        ar2[top2]=ar1[top1];
        top1--;
    }
}

//--------------------------------------------------------
int main() {
    int q;
    
    scanf("%d",&q);
    while(q--)
    {
        int qn , n;
        scanf("%d",&qn);

        if(qn==1)
            {
                scanf("%d",&n);
                insert(n);
            }
        else if(qn==2)
            {
                if(top2==-1)
                    move2();
                top2--;
            }

        else if(qn==3)
            {
                if(top2==-1)
                    move2();
                printf("%d\n",ar2[top2]);
            }
    }
    return 0;
}

