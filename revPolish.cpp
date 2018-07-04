#include <bits/stdc++.h>
using namespace std;

int main() {
	int n1,n2,n3;
	freopen("input.txt","r",stdin);
	cin>>n1>>n2>>n3;
	while(n1||n2||n3){
		if(2*n2==n1+n3)
			cout<<"AP "<<n3+(n3-n2)<<"\n";
		else
			cout<<"GP "<<n3*(n3/n2)<<"\n";

		cin>>n1>>n2>>n3;
	}
	return 0;
}