//1288/C
//#include "pch.h"
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <limits.h>
#include <string>
#include <deque>
#include <cmath>
#include <bitset>
#include <complex>
#include <time.h>
#include <stdio.h>

using namespace std;
typedef long long ll;
typedef pair<double, double> P;

#define rip(i, n, s) for (int i = (s);i < (int)( n ); i++)
//yoyo
#define mpa make_pair
//yoyo
#define all(a) a.begin(), a.end()
//yoyo

template<typename T>
void vdeb(vector<T> &da) {
int size = da.size();
for (int i = 0;i < size;i++) {
	if (i == size - 1) {
		cout << da[i] << endl;
	}
	else {
		cout << da[i] << ' ';
	}
}
}
//yoyo
template<typename T>
void vvdeb(vector<T> &da) {
int size = da.size();
for (int i = 0;i < size;i++) {
	vdeb(da[i]);
}
}
//yoyo
long long pow(long long n, long long p, long long k) {//n^k(mod p)
if (!k) return 1;
long long a = pow(n,p, k>>1);
a = a * a%p;
if (k & 1) a = a * n%p;
return a;
}
void euclid(long long &a, long long &b, long long p) { // a>=b A*b+B*(a-a/b*b)=1
if (a == 1) {
	a = 1;
}
else {
	long long A = b, B = a % b;
	euclid(A, B, p);
	b = (A - (p + a / b) % p * B % p + p) % p;
	a = B;
}
}
//yoyo
long long rev(long long n, long long p) {//nの逆元 n*x-p*y=1
//long long q = p;
//euclid(p, n, p);
//return n % q;
return pow(n,p,p-2);
}
long long bino(long long n, long long m, long long p) {//nCm(mod p)
long long ans = 1, div = 1;
for(int i = 0;i < m; i++){
	ans = (n - i) * ans % p;
	div = div * (i +1) % p;
}
return ans * rev(div, p) % p;
}
//yoyo
struct modint {
long long num;
long long p;
modint() {
	num = 0;
	p = 1000000007;
}
modint(int x) {
	p = 1000000007;
	num = (long long)x%p;
}
modint(long long x) {
	p = 1000000007;
	num = x % p;
}
modint operator+(const modint &other) {
	modint ret;
	ret.p = p;
	ret.num = (num + other.num) % p;
	return ret;
}
modint operator+(const long long &other) {
	modint ret;
	ret.p = p;
	ret.num = (num + (other%p)) % p;
	return ret;
}
modint operator-(const modint &other) {
	modint ret;
	ret.p = p;
	ret.num = (num - other.num + p) % p;
	return ret;
}
modint operator-(const long long &other) {
	modint ret;
	ret.p = p;
	ret.num = (num - (other%p) + p) % p;
	return ret;
}
modint operator*(const modint &other) {
	modint ret;
	ret.p = p;
	ret.num = (num*other.num) % p;
	return ret;
}
modint operator*(const long long &other) {
	modint ret;
	ret.p = p;
	ret.num = (num*(other%p)) % p;
	return ret;
}
modint operator/(const modint &other) {
	modint ret;
	ret.p = p;
	ret.num = (num*rev(other.num, p)) % p;
	return ret;
}
modint operator/(const long long &other) {
	modint ret;
	ret.p = p;
	ret.num = (num*rev(other%p, p)) % p;
	return ret;
}
void operator+=(const long long &other) {
	num = (num + other) % p;
}
void operator+=(const modint &other) {
	num = (num + other.num) % p;
}
void operator-=(const long long &other) {
	num = (num - other + p) % p;
}
void operator-=(const modint &other) {
	num = (num - other.num + p) % p;
}
void operator*=(const long long &other) {
	num = (num*other) % p;
}
void operator*=(const modint &other) {
	num = (num*other.num) % p;
}
};
//yoyo
modint cal(int m, int x){
modint ret;
ret += bino(x+m-2,m-1,ret.p);
return ret;
}
//yoyo
int main(){
int n, m;cin >> n >> m;
modint ans,gg;
vector<modint> da(n);
rip(i,n,0) da[i] = cal(m, i+1);
rip(i,n,0){
	gg += da[i];
	ans += gg*da[n-i-1];
}
//yoyo

cout << ans.num << endl;
}
