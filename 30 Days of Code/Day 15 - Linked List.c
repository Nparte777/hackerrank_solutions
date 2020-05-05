#include <stdlib.h>
#include <stdio.h>
typedef struct Node
{
    int data;
    struct Node* next;
}Node;

Node* insert(Node *head,int data)
{
    Node *q=malloc(sizeof(Node));
    Node *t=malloc(sizeof(Node));
    q->data=data;
    q->next=NULL;
    if(head==NULL)
    {
        head=q;
        return head;
    }
    else
    {
        for(t=head;t->next!=NULL;t=t->next);
        t->next=q;
        return head;
    }
}

void display(Node *head)
{
	Node *start=head;
	while(start)
	{
		printf("%d ",start->data);
		start=start->next;
	}
}
int main()
{
	int T,data;
    scanf("%d",&T);
    Node *head=NULL;
    while(T-->0){
        scanf("%d",&data);
        head=insert(head,data);
    }
  display(head);

}
