# Solutions

## A

```cpp
ll f(ll x,ll a, ll b, ll c){
  ll ab = std::lcm(a,b);
return x/ab -x/std::lcm(ab,c);
}
ll solve(ll n, int a, int b, int c){
  ll low = 0, high = (ll)2e18l;
  while (high -low > 1){
    ll mid = (low +high)/2;
    if (f(mid,a,b,c) + f(mid, a,c,b) + f(mid,b,c,a) >= n){
      high = mid;
    }else{
      low = mid
    }
  }
}
main(){
  int a,b,c;ll n;
  while (std::cin>>a>>b>>c>>n){
    std::cin>>n;
    std::cout << solve(n,a,b,c) <<std::endl;
  }
}
```

## B

```cpp
const int inf = (int)1e9+7;
ll solve(int n, const vi &h) {
  vi left(1+n+1, 1), right(1+n+1, 1);
  for (int i = 1; i <= n; i++)
    if (h[i-1] < h[i])
      left[i] = left[i-1] + 1;
  for (int i = n; i >= 1; i--)
    if (h[i] > h[i+1])
      right[i] = right[i+1] + 1;
  ll answ{};
  for (int i = 1; i <= n; i++)
    answ += (left[i]-1LL) * (right[i] - 1LL);
  return answ;
}
main(){
  int tt; std::cin>>tt;
  while (tt--> 0){
    int n; std::cin>>n;
    vi h(1+n+1,inf);
    for (int i = 1; i<=n;i++)
      std::cin>>h[i];
    std::cout << solve(n,h)<<'\n';

  }
}
```

## C

```cpp
ll solve(std::string s, char ch){
  int pos = 0;
  ll min =0;
  ll max = 0;
  for (int i = 0; i< isz(s); i++){
    if (s[i] == '?')
      s[i] = ch;
    if (s[i] == 'L'){
      pos--;
    }else if (s[i] == 'R'){
      pos++;
    }else{
      assert(false);
    }
    remin(min,pos);
    remax(max,pos);
  }
  return max - min;
}
ll solve(std::string s){
  return std::max<ll>(solve(s,'L'), solve(s,'R'));
}
main(){
  std::string s;
  while (std::cin >> s){
    std::cout << solve(s)<<std::endl;
  }
}
```

## D

```cpp
std::string ask(ll x){
  std::cout << x<< std::endl;
  std::string s; std::cin >> s;
  return s;
}
main(){
  ll maxN = (ll)1e18L;
  ll n = 1;
  while (n<maxN){
    auto s = ask(n);
    if (s=="ok"){
      maxN = n;
    }else {
      assert(s=="wet");
      n = 2*n+1;
    }
  }
  ll low = 0; high = maxN;
  while (high - low >1){
    ll mid = (low + high)/2;
    auto s = ask(mid);
    if (s == "ok")
      high = mid;
    else low = mid;
  }
  std::cout << "! " << high << std::endl;
}
```
