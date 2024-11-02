# Графы

## Компонента связности + Сама реализация графа

```cpp
#include <algorithm>
#include <bits/stdc++.h>
#include <map>
#include <vector>
using namespace std;
typedef long long lg;
typedef vector<int> iv;
typedef vector<lg> lv;
#define range(i, n) for (lg i = 0; i < n; i++)
#define rpt(i, a, b) for (lg i = a; i < b; i++)
#define all(v) begin(v), end(v)
#define ГООООЛ(v, d) auto v = d
#define РУСЫ*ДАЮ*ВАМ_ДОБРО \
ios::sync_with_stdio(0); \
cin.tie(0); \
cin.exceptions(cin.failbit); // Throws an exception, if you have an input
// error. Variable
#define ПРАВОСЛАВИЕ \
int t; \
cin >> t; \
while (t--)
void solve();
int main() {

РУСЫ*ДАЮ*ВАМ_ДОБРО
// int t; cin >> t; while(t--)
// solve2();
solve();
return 0;
}
bool isBipartite(map<int, vector<int>> &graph) {
map<int, int> colors; // цвет для каждой вершины: 0, 1 или -1 (не посещён)

for (const auto &node : graph) {
int start = node.first;

    // Если вершина уже была окрашена, пропускаем её
    if (colors.count(start))
      continue;

    // Инициализируем BFS с текущей вершины
    queue<int> q;
    q.push(start);
    colors[start] = 0; // Начинаем с цвета 0

    while (!q.empty()) {
      int current = q.front();
      q.pop();

      // Проверяем всех соседей
      for (int neighbor : graph.at(current)) {
        // Если сосед ещё не окрашен, окрашиваем в противоположный цвет
        if (!colors.count(neighbor)) {
          colors[neighbor] = 1 - colors[current];
          q.push(neighbor);
        }
        // Если сосед уже окрашен и имеет тот же цвет, что и текущая вершина
        else if (colors[neighbor] == colors[current]) {
          return false; // Граф не является двудольным
        }
      }
    }

}
return true;
}
void PrintGraph(map<int, vector<int>> gr) {
for (auto var : gr) {
cout << var.first << " : ";
for (auto val : var.second) {
cout << val << " ";
}
cout << '\n';
}
}
map<int, vector<int>> g;
const int maxn = 1e5;
vector<int> component(maxn, 0); // тут будут номера компонент
int component2[maxn];

void dfs(int v, int num) {
component[v] = num;
for (int u : g[v])
if (!component[u]) // если номер не присвоен, то мы там ещё не были
dfs(u, num);
}
map<int, vector<int>> computateGraph(map<int, vector<int>> graph1,
map<int, vector<int>> graph2, int n) {
range(i, n) {
vector<int> firstgraph = graph1[i];
vector<int> &secondgraph = graph2[i];
for (auto var : firstgraph) {
if (binary_search(all(secondgraph), var))
secondgraph.erase(lower_bound(all(secondgraph), var));
}
}

return graph2;
}
int n;
bool used[maxn];
vector<int> comp;

void dfs(int v, vector<bool> &used, vector<int> &comp) {
used[v] = true;
comp.push_back(v);
for (size_t i = 0; i < g[v].size(); ++i) {
int to = g[v][i];
if (!used[to])
dfs(to, used, comp);
}
}

vector<vector<int>> find_comps(vector<bool> &used, vector<int> &comp, int n) {
// cout << "------------------";
vector<vector<int>> ans;
for (int i = 0; i < n; ++i)
used[i] = false;
for (int i = 0; i < n; ++i)
if (!used[i]) {
comp.clear();
dfs(i, used, comp);

      // cout << "Component:";
      ans.push_back(comp);
      // for (size_t j = 0; j < comp.size(); ++j)
      //   cout << ' ' << comp[j];
      // cout << endl;
    }

return ans;
}
bool isBipartite(unordered_map<int, unordered_set<int>> &graph, int start,
unordered_map<int, int> &color) {
stack<int> s;
s.push(start);
color[start] = 0; // Начинаем с окраски в 0

while (!s.empty()) {
int node = s.top();
s.pop();

    for (int neighbor : graph[node]) {
      if (color.find(neighbor) == color.end()) { // Если не окрашен
        color[neighbor] = 1 - color[node]; // Окрашиваем в противоположный цвет
        s.push(neighbor);
      } else if (color[neighbor] ==
                color[node]) { // Если сосед имеет тот же цвет
        return false;           // Граф не двудолен
      }
    }

}
return true;
}

string canDivideComponents(const vector<vector<int>> &components) {
unordered_map<int, unordered_set<int>> graph;

// Создаем граф
for (const auto &component : components) {
for (int number : component) {
if (graph.find(number) == graph.end()) {
graph[number] = unordered_set<int>();
}
for (int other : component) {
if (number != other) {
graph[number].insert(other);
}
}
}
}

// Проверка двудольности графа
unordered*map<int, int> color; // -1 означает, что узел еще не окрашен
for (const auto &[node, *] : graph) {
if (color.find(node) == color.end()) { // Если узел не окрашен
if (!isBipartite(graph, node, color)) {
return "Impossible";
}
}
}

return "Possible";
}
void PrintAns(vector<vector<int>> mas) {
for (auto var : mas) {
for (auto v : var) {
cout << v << " ";
}
cout << '\n';
}
}

bool isBipartite(unordered_map<int, vector<int>> &graph, int start,
unordered_map<int, int> &colors) {
queue<int> q;
q.push(start);
colors[start] = 0; // Начинаем с цвета 0 (герои)

while (!q.empty()) {
int node = q.front();
q.pop();

    for (int neighbor : graph[node]) {
      if (colors.find(neighbor) == colors.end()) {
        // Красим соседа в противоположный цвет
        colors[neighbor] = 1 - colors[node];
        q.push(neighbor);
      } else if (colors[neighbor] == colors[node]) {
        // Если сосед имеет тот же цвет, граф не двудольный
        return false;
      }
    }

}
return true;
}

string canDivideIntoHeroesAndVillains(const vector<vector<int>> &components) {
unordered_map<int, vector<int>> graph;

// Строим граф из компонентов
for (const auto &component : components) {
for (size_t i = 0; i < component.size(); ++i) {
for (size_t j = i + 1; j < component.size(); ++j) {
int a = component[i];
int b = component[j];
graph[a].push_back(b);
graph[b].push_back(a);
}
}
}

unordered_map<int, int> colors;

// Проверяем каждый компонент связности на двудольность
for (const auto &node : graph) {
if (colors.find(node.first) == colors.end()) {
if (!isBipartite(graph, node.first, colors)) {
return "Impossible";
}
}
}

return "Possible";
}
void solve() {
ГООООЛ(v, 2LL);
int n, m, q;
cin >> n >> m >> q;
map<int, vector<int>> graph;
range(i, n + 1) { graph[n]; }
vector<map<int, vector<int>>> graphs;
range(i, m) {
int buf1, buf2;
cin >> buf1 >> buf2;
graph[buf1].push_back(buf2);
graph[buf2].push_back(buf1);
range(i, n) { sort(all(graph[i])); }
graphs.push_back(graph);
}

range(i, q) {
int l, r;
cin >> l >> r;
vector<bool> used(maxn);
vector<int> comp;
g = computateGraph(graphs[l - 1], graphs[r - 1], n + 1);

    // int num = 0;
    // for (int v = 0; v < n + 10; v++)
    //   if (!component[v])
    //     dfs(v, ++num);
    //
    // range(i, n + 10) { cout << component[i] << " "; }
    // cout << '\n';
    auto ans = find_comps(used, comp, n + 1);
    ans.erase(ans.begin());
    g.erase(g.find(0));
    // cout << ans.size() << '\n';
    // if ((ans.size() - 1) % 2 == 0) {
    //   cout << "Possible\n";
    // } else {
    //   cout << "Impossible\n";
    // }
    if (isBipartite(g)) {
      cout << "Possible" << endl;
    } else {
      cout << "Impossible" << endl;
    }
    // PrintGraph(g);
    // cout << canDivideIntoHeroesAndVillains(ans) << endl;
    // PrintAns(ans);
    // cout << canDivideComponents(ans) << endl;

}
}
```
