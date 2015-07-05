const int N = 5500;
class Solution {
public:
	int n;
	string str[N];
	vector<int> g[N];
	bool vis[N];
	int can[N];
	int dist[N], res;
	vector<vector<string> > ret;

	bool bfs(int st, int ed) {
		queue<pair<int,int> > Q;
		memset(vis, 0, sizeof(bool) * (n + 1));
		memset(can, -1, sizeof(int) * (n + 1));
		memset(dist, 0x1f, sizeof(int) * (n + 1));
		Q.push(make_pair(st, 0));
		vis[st] = 1;
		dist[st] = 0;
		res = 1<<30;

		while (!Q.empty()) {
			pair<int,int> t = Q.front();
			int u = t.first, step = t.second;
			dist[u] = step;
			if (u == ed) {
				if (step > res) continue;
				res = step;
			}
			Q.pop();
			for (size_t i = 0;i < g[u].size(); ++i) {
				int v = g[u][i];
				if (vis[v]) continue;
				vis[v] = 1;
				Q.push(make_pair(v, step + 1));
			}
		}
		return res != (1<<30);
	}
	bool get(int u) {
		if (u == n - 1) {
			return can[u] = 1;
		}
		if (can[u] != -1) return can[u];
		int ok = 0;
		for (size_t i = 0;i < g[u].size(); ++i) {
			int v = g[u][i];
			if (dist[v] != dist[u] + 1) {
				//can[v] = 0;
				continue;
			}
			if (get(v)) {
				ok = 1;
			}
		}
		return can[u] = ok;
	}
	vector<vector<string> > dfs(int u) {
		vector<vector<string> > res;
		if (u == n - 1) {
			vector<string> tmp;
			tmp.push_back(str[n-1]);
			res.push_back(tmp);
			return res;
		}
		for (size_t i = 0;i < g[u].size(); ++i) {
			int v = g[u][i];
			if (dist[v] == dist[u] + 1 && can[v] == 1) {
				vector<vector<string> > son = dfs(v);
				if (son.empty()) continue;
				for (size_t j = 0;j < son.size(); ++j) {
					vector<string> tmp = son[j];
					tmp.insert(tmp.begin(), str[u]);
					res.push_back(tmp);
				}
			}
		}
		return res;
	}
	vector<vector<string> > findLadders(string start, string end, unordered_set<string> &dict) {
		map<string, int> mapper;
		unordered_set<string>::iterator itr;
		int id = 0, len = start.length();
		for (itr = dict.begin(); itr != dict.end(); ++itr) {
			string word = *itr;
			str[id] = word;
			mapper[word] = id ++;
		}
		mapper[start] = id ++;  mapper[end] = id ++;
		str[id-1] = end;    str[id-2] = start;
		n = id;

		for (int i = 0;i < n; ++i) g[i].clear();

		for (itr = dict.begin(); itr != dict.end(); ++itr) {
			string word = *itr;
			int u = mapper[word], v;
			for (int i = 0;i < len; ++i) {
				for (int j = 0;j < 26; ++j) {
					if (word[i] - 'a' == j) continue;
					string tmp = word;
					tmp[i] = 'a' + j;
					if (dict.find(tmp) == dict.end()) continue;
					v = mapper[tmp];
					g[u].push_back(v);
				}
			}
			int sdiff = 0, ediff = 0;
			for (int i = 0;i < len; ++i) {
				if (word[i] != start[i]) sdiff ++;
				if (word[i] != end[i]) ediff ++;
			}
			if (sdiff == 1) {
				g[n - 2].push_back(u);
				g[u].push_back(n - 2);
			}
			if (ediff == 1) {
				g[n - 1].push_back(u);
				g[u].push_back(n - 1);
			}
		}
		for (int i = 0;i < n; ++i) {
			sort(g[i].begin(), g[i].end());
			vector<int>::iterator itr = unique(g[i].begin(), g[i].end());
			g[i].erase(itr, g[i].end());
		}
	
		if (bfs(n - 2, n - 1)) {
			
			get(n - 2);
		
			return dfs(n - 2);
		} else {
			ret.clear();
			return ret;
		}
	}
};