// https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists

/*
BASIC IDEA:
1. Traverse through first list making all the next pointers zero. 
2. Now traverse through second list and whenever the null pointer is encountered, thats the merge point
*/


int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
    SinglyLinkedListNode* p1=head1;
    SinglyLinkedListNode* p2;

    while(p1!=NULL)
    {
        p2=p1;
        p1=p1->next;
        p2->next=NULL;
    }

    while(1)
    {
        if(head2->next==NULL)
            return head2->data;
        head2=head2->next;
    }

}
