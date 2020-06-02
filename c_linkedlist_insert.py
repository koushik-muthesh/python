'''def search(root,key):
    if root is None or root.val=key:
        return root
    if root.val<key:
        return search(root.right,key)
    else:
        return search(root.left,key)'''

#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *left;
    struct node *right;
};
struct node * insert(struct node *p,int n)
{
 
 struct node *nn=(struct node *)malloc(sizeof(struct node));
 nn->data=n;
 nn->right=NULL;
 nn->left=NULL;
 
 if(p == NULL)
 {
     p = nn;
 }
 else
 {
     struct node *t=p;
     if(n > t->data)
     {
         t->right = insert(t->right,n);
     }
     else
     {
         t->left = insert(t->left,n);
     }
 }
 return p;
}

void inorder(struct node *p)
{
    if (p!=NULL)
    {
        inorder(p->left);
        printf("%d ",p->data);
        inorder(p->right);
    }
}
int main()
{
    struct node *p=NULL;
    int n,i,k;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
      scanf("%d",&k);
      p=insert(p,k);
    }
    inorder(p);
}

