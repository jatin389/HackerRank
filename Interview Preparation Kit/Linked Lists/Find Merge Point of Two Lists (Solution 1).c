// https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists

/* 
BASIC IDEA:
1. Take two pointers (one for each list).
2. if pointer of any list reaches to the last node(or NULL) then connect it to the beginning of next list.
   (connecting the ends of each list to the beginning of the next list)
*/ 
 
int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
	SinglyLinkedListNode* p1=head1;
	SinglyLinkedListNode* p2=head2;

	while(1)
	{
		if(p1==p2)
			return (p1->data);

		if(p1==NULL)
			p1=head2;
		else
			p1=p1->next;

			
		if(p2==NULL)
			p2=head1;
		else
			p2=p2->next;
			
	}
}