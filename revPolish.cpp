#include <bits/stdc++.h>
#include <stack>
using namespace std;	
int main(){
	stack<char> op;
	string input,output;
	int cases;
	string operators = "+-*/^";
	cin>>cases;
	op.push('N');
	while(cases--){
		cin >> input;
		for(int i=0;i<input.length();i++){
			char c =input[i];
			if(isalpha(c)){
				output=output+c;
			}
			else if (c=='('){
				op.push('(');
			}
			else if (c==')'){
				while(op.top()!='('&&!op.empty()){
					output=output+op.top();
					op.pop();
				}
			}
			else if (operators.find(c)!=string::npos){
				if(!op.empty()&&operators.find(op.top())!=string::npos){
					while((operators.find(c)<operators.find(op.top()))&&!op.empty()/*&&operators.find(op.top())!=string::npos*/){
						output=output+op.top();
						op.pop();

					}
				}
				else {
					op.push(c);		
				}

				
			}
			else{
				output=output+c;
			}
		}
		while(op.top!='N'){
			output=output+op.top();
			op.pop();

		}
		cout<<output;
	}


	return 0;
}
	