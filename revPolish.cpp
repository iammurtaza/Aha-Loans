#include <bits/stdc++.h>
<<<<<<< HEAD
#include <stack>
using namespace std;	
int main(){
	stack<char> op;
	string input,output;
	int cases;
	string operators = "+-*/^";
	//freopen("input.txt", "r", stdin);
	cin>>cases;
	op.push('N');
	while(cases--){
		cin >> input;
		output="";
		for(int i=0;i<input.length();i++){
			char c =input[i];
			if(isalpha(c)){
				//cout<<"alpha ";
				output=output+c;
			}
			else if (c=='('){
				//cout<<"open ";
				op.push('(');
			}
			else if (c==')'){
				//cout<<"close ";
				while(op.top()!='('){
					output=output+op.top();
					op.pop();
				}
				op.pop();
			}
			else if (operators.find(c)!=-1){ 
				
				if(!op.empty() && operators.find(op.top()) != -1){
					//cout<<"op1 ";
					while( operators.find(c)<operators.find(op.top()) && !op.empty() ){
						output=output+op.top();
						op.pop();
					}
				}
				else {
					//cout<<"op2 ";
					op.push(c);		
				}
			}
			else{
				//cout<<"spc ";
				output=output+c;
			}
		}
		while(op.size()>2){
			output=output+op.top();
			op.pop();

#include<bits/stdc++.h>
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
	



