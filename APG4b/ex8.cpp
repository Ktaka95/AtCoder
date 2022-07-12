#include <bits/stdc++.h>
using namespace std;

int main() {
	int p;
	cin >> p;

	string text;
	int price;
	int N;

	if (p == 1) {
		cin >> price;
		cin >> N;
		cout << price * N << endl;
	}

	else if (p == 2) {
		cin >> text >> price >> N;
		cout << text << "!" << endl;
		cout << price * N << endl;
	}
}
